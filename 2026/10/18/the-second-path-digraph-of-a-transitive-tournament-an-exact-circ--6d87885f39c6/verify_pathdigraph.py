"""Reproduce the directed-face-incidence construction for transitive tournaments.
No third-party dependencies. Finite checks only; the all-n proof is mathematical.
"""
from itertools import combinations
from collections import defaultdict, deque
from math import comb


def choose(n, r):
    return comb(n, r) if n >= r >= 0 else 0


def check(n):
    triangles_of_input = list(combinations(range(n), 3))
    idx = {t: i for i, t in enumerate(triangles_of_input)}
    deleting = [defaultdict(list) for _ in range(3)]
    for i, t in enumerate(triangles_of_input):
        for p in range(3):
            deleting[p][t[:p] + t[p+1:]].append(i)
    arcs = set()
    for p in range(3):
        for q in range(p+1, 3):
            for face in deleting[p].keys() & deleting[q].keys():
                for source in deleting[p][face]:
                    for target in deleting[q][face]:
                        if source != target:
                            arcs.add((source, target))
    assert not any((v, u) in arcs for u, v in arcs)
    successors = [set() for _ in triangles_of_input]
    neighbors = [set() for _ in triangles_of_input]
    for u, v in arcs:
        successors[u].add(v)
        neighbors[u].add(v)
        neighbors[v].add(u)
    face3 = set()
    for u, v in arcs:
        for w in successors[v] & successors[u]:
            face3.add(tuple(sorted((u, v, w))))
    # No directed 4-clique is expected. Verify directly from oriented 3-cliques.
    for f in face3:
        common = neighbors[f[0]] & neighbors[f[1]] & neighbors[f[2]]
        assert not (common - set(f)), (n, f, common)
    n0 = len(triangles_of_input)
    n1 = len(arcs)
    n2 = len(face3)
    assert (n0, n1, n2) == (choose(n, 3), 3*choose(n, 4), choose(n, 5))
    expected_face3 = set()
    for a, b, c, d, e in combinations(range(n), 5):
        expected_face3.add(tuple(sorted((idx[(a,b,d)], idx[(b,c,d)], idx[(b,d,e)]))))
    assert face3 == expected_face3
    # Independent reconstruction of edges by 2-subset block and three interval parts.
    expected_edges = set()
    for u, v in combinations(range(n), 2):
        parts = [[idx[tuple(sorted((u, v, w)))] for w in region]
                 for region in (range(0, u), range(u+1, v), range(v+1, n))]
        for a, b in combinations(range(3), 2):
            for i in parts[a]:
                for j in parts[b]:
                    expected_edges.add((min(i,j), max(i,j)))
    underlying_edges = {(min(a,b),max(a,b)) for a,b in arcs}
    assert underlying_edges == expected_edges
    # Connectivity of the one-skeleton.
    seen = {0}
    q = deque([0])
    while q:
        x = q.popleft()
        for y in neighbors[x] - seen:
            seen.add(y); q.append(y)
    assert len(seen) == n0
    # Sparse exact rank of the F_2 boundary from ordered 2-faces to 1-faces.
    eidx = {edge: j for j, edge in enumerate(sorted(underlying_edges))}
    pivots = {}
    for f in sorted(face3):
        bits = 0
        for a, b in combinations(f, 2):
            bits ^= 1 << eidx[(min(a,b),max(a,b))]
        while bits:
            lead = bits.bit_length()-1
            if lead in pivots:
                bits ^= pivots[lead]
            else:
                pivots[lead] = bits
                break
    rank2 = len(pivots)
    beta2 = n2 - rank2
    beta1 = n1 - n0 + 1 - rank2
    assert (beta1, beta2) == (5*choose(n-2,3), choose(n-3,5))
    # Verify the integral second-homology rank identity as a separate calculation.
    direct_h2 = 0
    for u,v in combinations(range(n), 2):
        l,m,r = u,v-u-1,n-v-1
        direct_h2 += max(0,l-1)*max(0,m-1)*max(0,r-1)
    assert direct_h2 == beta2
    return {'n': n, 'vertices': n0, 'edges': n1, 'triangles': n2,
            'rank_boundary2_F2': rank2, 'beta1_F2': beta1, 'beta2_F2': beta2}


if __name__ == '__main__':
    for n in range(3, 12):
        print(check(n))
    print('PATH_DIGRAPH_TOURNAMENT_2_FLAG_FINITE_CHECKS_OK')
