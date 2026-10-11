"""Integral matching-complex torsion census; run: python verify_exact.py.

Data: atlas.g6, Graph Atlas simple unlabeled graphs through seven vertices.
Dependencies: SymPy. No computational outputs are assumed.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def parse_graph6(g6):
    b = g6.strip().encode('ascii')
    assert 63 <= b[0] <= 70  # n=0,...,7
    n = b[0] - 63
    bits = []
    for c in b[1:]:
        val = c - 63
        assert 0 <= val < 64
        bits.extend([(val >> i) & 1 for i in (5, 4, 3, 2, 1, 0)])
    assert len(bits) >= n * (n-1) // 2
    assert all(x == 0 for x in bits[n*(n-1)//2:])
    edges = []
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                edges.append((i, j))
            k += 1
    return n, sorted(edges)


def smith_torsion(edges):
    m = len(edges)
    support = [(1 << i) | (1 << j) for i, j in edges]
    # Faces of the edge-set matching complex in dimensions 0, 1, 2.
    pairs = [(i, j) for i in range(m) for j in range(i+1, m)
             if support[i] & support[j] == 0]
    lookup = {face: k for k, face in enumerate(pairs)}
    triples = [(i, j, k) for i, j, k in combinations(range(m), 3)
               if not (support[i] & support[j] or
                       support[i] & support[k] or support[j] & support[k])]
    B = zeros(len(pairs), len(triples))
    for col, (a, b, c) in enumerate(triples):
        B[lookup[(b, c)], col] = 1
        B[lookup[(a, c)], col] = -1
        B[lookup[(a, b)], col] = 1
    S = smith_normal_form(B, domain=ZZ)
    diag = [abs(int(S[k,k])) for k in range(min(S.shape)) if S[k,k] != 0]
    torsion = tuple(a for a in diag if a > 1)
    return torsion, len(diag), (m, len(pairs), len(triples)), diag, pairs


def connected_components(n, pairs):
    if n == 0:
        return 0
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in pairs:
        a, b = root(u), root(v)
        if a != b:
            parent[a] = b
    return len({root(i) for i in range(n)})


def main():
    path = Path(__file__).with_name('atlas.g6')
    records = [line for line in path.read_text(encoding='ascii').splitlines()]
    assert len(records) == 1253
    import json
    certificate = json.loads(Path(__file__).with_name('torsion_certificate.json').read_text(encoding='utf-8'))
    totals = Counter()
    e_dist = Counter()
    torsion_cases = []
    for atlas_index, g6 in enumerate(records):
        n, edges = parse_graph6(g6)
        totals[n] += 1
        torsion, rank2, f, diag, pairs = smith_torsion(edges)
        if torsion:
            assert n == 7 and torsion == (3,), (atlas_index, torsion)
            e_dist[len(edges)] += 1
            torsion_cases.append(atlas_index)
        if atlas_index == 1105:
            expected = [(0,1),(0,5),(0,6),(1,3),(1,4),(2,3),
                        (2,4),(2,5),(2,6),(3,5),(3,6),(4,5),(4,6)]
            assert edges == expected, edges
            assert f == (13,42,30), f
            # Replay a signed integral witness for nonzero 3-torsion.
            assert certificate['graph_atlas_index'] == atlas_index
            assert certificate['graph_edges'] == [list(edge) for edge in expected]
            from sympy import zeros
            z = zeros(len(pairs), 1)
            for k, coeff in certificate['cycle_in_F1_index_basis']:
                z[k] = coeff
            c = zeros(f[2], 1)
            for k, coeff in certificate['chain_in_F2_index_basis']:
                c[k] = coeff
            face_idx = {face:k for k,face in enumerate(pairs)}
            triple_faces = [(i,j,k) for i,j,k in combinations(range(f[0]),3)
                 if not (((1<<expected[i][0])|(1<<expected[i][1])) &
                         ((1<<expected[j][0])|(1<<expected[j][1]))) and
                    not (((1<<expected[i][0])|(1<<expected[i][1])) &
                         ((1<<expected[k][0])|(1<<expected[k][1]))) and
                    not (((1<<expected[j][0])|(1<<expected[j][1])) &
                         ((1<<expected[k][0])|(1<<expected[k][1])))]
            assert len(triple_faces)==f[2]
            B = zeros(len(pairs),f[2])
            for col,(a,b,d) in enumerate(triple_faces):
                B[face_idx[(b,d)],col]=1
                B[face_idx[(a,d)],col]=-1
                B[face_idx[(a,b)],col]=1
            assert B*c == 3*z, 'Integral threefold boundary certificate invalid'
            # Check d1 z = 0; directed boundary e_j - e_i.
            delta = zeros(f[0],1)
            for (a,b), coeff in zip(pairs,z):
                delta[a]-=coeff
                delta[b]+=coeff
            assert delta == zeros(f[0],1), 'Proposed torsion chain is not a cycle'
            assert any(int(t)%3 != 0 for t in c)
            # B is injective over Q (rank f[2] below), hence z cannot
            # be a boundary over Z: its unique rational preimage is c/3.

            assert rank2 == 30 and diag.count(1) == 29 and diag.count(3) == 1
            # rank(d1)=vertices-c_0 of the matching-complex 1-skeleton.
            rank1 = f[0] - connected_components(f[0], pairs)
            assert rank1 == 12
            assert f[1] - rank1 - rank2 == 0  # H1 free rank
            assert f[2] - rank2 == 0             # H2 rank
    assert totals == Counter({0:1,1:1,2:2,3:4,4:11,5:34,6:156,7:1044}), totals
    assert len(torsion_cases) == 40
    assert e_dist == Counter({13:1,14:3,15:9,16:10,17:8,18:5,19:2,20:1,21:1}), e_dist
    assert [i for i in torsion_cases if len(parse_graph6(records[i])[1])==13] == [1105]
    expected_cases = json.loads(Path(__file__).with_name('torsion_cases.json').read_text(encoding='utf-8'))['graph_atlas_indices_with_first_homology_torsion']
    assert torsion_cases == expected_cases, (torsion_cases, expected_cases)
    print('EXACT_OK: 1253 atlas graphs; all n<=6 torsion-free; 40 order-7 Z/3 cases')
    print('EDGE_DISTRIBUTION:', sorted(e_dist.items()))
    print('WITNESS: G1105, 13 edges, f=(13,42,30), SNF(d2)=(1^29,3), H1=Z/3, H2=0')

if __name__ == '__main__':
    main()
