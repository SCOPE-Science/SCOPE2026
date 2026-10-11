"""Independent finite-field cross-check via NetworkX clique enumeration.

Run: python verify_modular.py. Requires NetworkX and the atlas.g6 data file.
"""
from collections import Counter
from pathlib import Path
import networkx as nx


def rank_p(rows, p):
    # Sparse row elimination over the prime field, pivot by column.
    pivots = {}
    for row in rows:
        x = dict(row)
        while x:
            col = min(x)
            coeff = x[col] % p
            if coeff == 0:
                del x[col]
                continue
            if col not in pivots:
                inv = pow(coeff, -1, p)
                pivots[col] = {j:(v*inv)%p for j,v in x.items() if (v*inv)%p}
                break
            y = pivots[col]
            x = {j:(x.get(j,0) - coeff*y.get(j,0))%p
                 for j in set(x)|set(y)
                 if (x.get(j,0)-coeff*y.get(j,0))%p}
    return len(pivots)


def boundary_rank(G, p):
    # Uses the disjointness graph and clique enumeration, not direct
    # matching enumeration or the Smith algorithm from verify_exact.py.
    D = nx.complement(nx.line_graph(G))
    D = nx.convert_node_labels_to_integers(D, ordering='sorted')
    triangles = [tuple(sorted(c)) for c in nx.enumerate_all_cliques(D) if len(c)==3]
    m = D.number_of_nodes()
    pairs = sorted(tuple(sorted(e)) for e in D.edges())
    pair_idx = {e:i for i,e in enumerate(pairs)}
    rows = [{} for _ in pairs]
    for j,(a,b,c) in enumerate(triangles):
        for edge,sgn in [((b,c),1),((a,c),-1),((a,b),1)]:
            rows[pair_idx[edge]][j] = sgn
    return rank_p(rows,p), (m,len(pairs),len(triangles))


def main():
    atlas = nx.graph_atlas_g()
    data = Path(__file__).with_name('atlas.g6').read_bytes().splitlines()
    assert len(atlas) == len(data) == 1253
    import json
    expected = json.loads(Path(__file__).with_name('torsion_cases.json').read_text(encoding='utf-8'))['graph_atlas_indices_with_first_homology_torsion']
    torsion_cases = []
    tally = Counter()
    for k,G in enumerate(atlas):
        assert nx.to_graph6_bytes(G,header=False).strip()==data[k], k
        r3,f = boundary_rank(G,3)
        r5,_ = boundary_rank(G,5)
        if r3 != r5:
            assert len(G)==7 and r5-r3 == 1, (k,r3,r5)
            tally[(len(G),G.number_of_edges())] += 1
            torsion_cases.append(k)
        if k==1105:
            assert f==(13,42,30)
            assert (r3,r5)==(29,30)
            for p in (2,7,101):
                rp,_ = boundary_rank(G,p)
                assert rp==30, (p,rp)
    assert torsion_cases == expected
    assert tally == Counter({(7,13):1,(7,14):3,(7,15):9,(7,16):10,
                             (7,17):8,(7,18):5,(7,19):2,(7,20):1,(7,21):1})
    print('MODULAR_OK: independently constructed clique complexes across 1253 atlas graphs')
    print('Exactly 40 torsion candidates; witness rank mod 3=29 vs rank mod 2,5,7,101=30')

if __name__=='__main__':
    main()
