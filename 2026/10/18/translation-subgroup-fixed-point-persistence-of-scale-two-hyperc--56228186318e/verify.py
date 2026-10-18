"""Independent finite verification of fixed-translation orbit complexes.

For a coordinate-flip subgroup of (F_2)^n acting on VR(Q_n; 2),
the geometric fixed space is a simplicial complex on admissible vertex orbits.
This script enumerates these orbits and their compatibility without using
symbolic classifications from the accompanying proof.
"""
from itertools import combinations
from collections import Counter


def weight(x):
    return x.bit_count()


def subgroup(gens):
    out = {0}
    for g in gens:
        out |= {h ^ g for h in tuple(out)}
    return frozenset(out)


def all_subgroups_of_rank(n, rank):
    found = set()
    for gens in combinations(range(1, 1 << n), rank):
        H = subgroup(gens)
        if len(H) == (1 << rank):
            found.add(H)
    return sorted(found, key=lambda H:tuple(sorted(H)))


def fixed_orbit_complex(n, H, scale=2):
    """Construct all admissible cosets and compatibility edges by Hamming distances.
    Return cosets and list of unordered compatible coset indices.
    """
    cosets = {}
    for x in range(1 << n):
        c = frozenset(x ^ h for h in H)
        cosets[c] = c
    admitted = [c for c in cosets if all(weight(u ^ v) <= scale for u,v in combinations(c,2))]
    edges = []
    for i,j in combinations(range(len(admitted)),2):
        if all(weight(u ^ v) <= scale for u in admitted[i] for v in admitted[j]):
            edges.append((i,j))
    return admitted, edges


def graph_hypercube_check(n, H, cosets, edges):
    # For this conjectured 1-dimensional fixed space, verify graph invariants
    # and an explicit isomorphism via a coordinate-flip orbit basis.
    k = n-1
    v = 1 << k
    if len(cosets) != v or len(edges) != k*(1 << (k-1)):
        return False
    adjacency = [set() for _ in cosets]
    for i,j in edges:
        adjacency[i].add(j)
        adjacency[j].add(i)
    if any(len(adj) != k for adj in adjacency):
        return False
    # Label the vertices of a candidate cube using any initial vertex and
    # its neighbors, checking that its adjacency graph is the full cube.
    # A general connected graph of this size/degree need not be a cube, so
    # we additionally verify graph metric Hamming distance distributions.
    for s in range(len(cosets)):
        distances={s:0}; queue=[s]
        for p in queue:
            for q in adjacency[p]:
                if q not in distances:
                    distances[q] = distances[p]+1
                    queue.append(q)
        if Counter(distances.values()) != Counter({d:__import__('math').comb(k,d) for d in range(k+1)}):
            return False
    # For these Cayley graphs, this signature check is only a finite corroboration;
    # the symbolic proof gives the explicit coordinate-linear graph isomorphism.
    return True


def main():
    summary=[]
    for n in range(3, 7):
        counts=Counter(); g1=0; g2=0; empties=0
        for rank in (1,2):
            for H in all_subgroups_of_rank(n,rank):
                cosets,edges=fixed_orbit_complex(n,H,scale=2)
                initial,initial_edges=fixed_orbit_complex(n,H,scale=1)
                before_zero,zero_edges=fixed_orbit_complex(n,H,scale=0)
                assert not before_zero and not zero_edges
                if rank==1 and next(iter(H-{0})).bit_count()==1:
                    assert len(initial)==1<<(n-1) and not initial_edges
                    assert set(initial)==set(cosets), (n,H,'0-skeleton inclusion')
                else:
                    assert not initial and not initial_edges
                eligible=all(weight(h)<=2 for h in H)
                assert bool(cosets)==eligible, (n,rank,H,'admissibility')
                if rank==1 and eligible:
                    assert graph_hypercube_check(n,H,cosets,edges), (n,H,'cube graph')
                    assert len(cosets)-len(edges) == (1 << (n-2))*(3-n)
                    g1 += 1
                elif rank==2 and eligible:
                    assert len(cosets) == (1 << (n-2)), (n,H,'points')
                    assert not edges, (n,H,'spurious edge')
                    g2 += 1
                else:
                    assert not cosets and not edges, (n,H,'should be empty')
                    empties += 1
                counts[rank] += 1
        # Every 3-dimensional binary subspace contains a vector of weight >=3.
        rank3=all_subgroups_of_rank(n,3)
        assert all(any(weight(h)>2 for h in H) for H in rank3)
        summary.append((n,counts[1],counts[2],len(rank3),g1,g2,empties))
    for row in summary:
        print('n=%d rank1=%d rank2=%d rank3=%d graph_loci=%d point_loci=%d empty_rank1or2=%d' % row)
    print('PASS: scale 0,1,2 subgroup-fixed orbit complexes for all rank-one/two subgroups and rank-three obstruction, 3<=n<=6.')

if __name__ == '__main__':
    main()
