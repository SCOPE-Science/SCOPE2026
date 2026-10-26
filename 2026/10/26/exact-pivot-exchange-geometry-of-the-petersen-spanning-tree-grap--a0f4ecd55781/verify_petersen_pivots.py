#!/usr/bin/env python3
"""Reproduce the exact pivot-exchange geometry of Petersen spanning trees.

Python >=3.9, standard library only. No external data files.
"""
import itertools
from collections import Counter, deque

# KG(5,2): vertex labels are lexicographically ordered two-subsets.
V = list(itertools.combinations(range(5), 2))
E = [(u, v) for u in range(10) for v in range(u+1, 10)
     if set(V[u]).isdisjoint(V[v])]
assert len(E) == 15
FULL = (1 << len(E)) - 1
EDGE_ID = {frozenset(pair): i for i, pair in enumerate(E)}


def connected_tree(mask):
    """DSU certificate: 9 chosen edges connect all 10 vertices."""
    if mask.bit_count() != 9:
        return False
    parent = list(range(10))
    def find(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for i, (u, v) in enumerate(E):
        if (mask >> i) & 1:
            a, b = find(u), find(v)
            if a == b:
                return False
            parent[b] = a
    return len({find(v) for v in range(10)}) == 1


def det_bareiss(M):
    """Fraction-free exact integer determinant; no libraries."""
    a = [list(row) for row in M]
    n = len(a)
    last = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            i = next((j for j in range(k + 1, n) if a[j][k]), None)
            if i is None:
                return 0
            a[k], a[i] = a[i], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                nmr = a[i][j] * pivot - a[i][k] * a[k][j]
                assert nmr % last == 0
                a[i][j] = nmr // last
        for i in range(k+1, n):
            a[i][k] = 0
        last = pivot
    return sign * a[n-1][n-1]


def matrix_tree_count():
    L = [[0] * 10 for _ in range(10)]
    for u, v in E:
        L[u][u] += 1
        L[v][v] += 1
        L[u][v] -= 1
        L[v][u] -= 1
    return det_bareiss([row[:-1] for row in L[:-1]])


TREES = [sum(1 << i for i in c)
         for c in itertools.combinations(range(15), 9)
         if connected_tree(sum(1 << i for i in c))]
LOOKUP = {t: i for i, t in enumerate(TREES)}
assert len(TREES) == len(LOOKUP) == matrix_tree_count() == 2000


def exchange_neighbors(t):
    """Method A: test all incident-edge exchanges against full tree list."""
    out = set()
    for i, old in enumerate(E):
        if not ((t >> i) & 1):
            continue
        for j, new in enumerate(E):
            if (t >> j) & 1:
                continue
            if not (set(old) & set(new)):
                continue
            k = LOOKUP.get(t ^ (1 << i) ^ (1 << j))
            if k is not None:
                out.add(k)
    return out


def path_neighbors(t):
    """Method B: each omitted chord pivots around its two cycle ends."""
    g = [[] for _ in range(10)]
    for i, (u, v) in enumerate(E):
        if (t >> i) & 1:
            g[u].append((v, i))
            g[v].append((u, i))
    out = set()
    for j, (src, dst) in enumerate(E):
        if (t >> j) & 1:
            continue
        parent = {src: (-1, -1)}
        q = deque([src])
        while q and dst not in parent:
            u = q.popleft()
            for v, eid in g[u]:
                if v not in parent:
                    parent[v] = (u, eid)
                    q.append(v)
        assert dst in parent
        cur = dst
        backwards = []
        while cur != src:
            par, eid = parent[cur]
            backwards.append(eid)
            cur = par
        assert len(backwards) >= 2
        for eid in (backwards[0], backwards[-1]):
            out.add(LOOKUP[t ^ (1 << j) ^ (1 << eid)])
    return out


A = [sorted(exchange_neighbors(t)) for t in TREES]
B = [sorted(path_neighbors(t)) for t in TREES]
assert A == B
assert all(len(nbs) == 12 for nbs in A)
assert all(i in A[j] for i, nbs in enumerate(A) for j in nbs)


def bfs(adjacency, root):
    d = [-1] * len(adjacency)
    d[root] = 0
    q = deque([root])
    while q:
        u = q.popleft()
        for v in adjacency[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
    assert -1 not in d
    return d


# Method A: exhaustive all-source/all-target distances.
DISTRIBUTION = Counter()
ECCENTRICITIES = Counter()
EXCESS = Counter()
DIAMETER_PAIRS = set()
EXTREME_PAIRS = set()
for i, t in enumerate(TREES):
    distance = bfs(A, i)
    ECCENTRICITIES[max(distance)] += 1
    for j in range(i+1, len(TREES)):
        d = distance[j]
        lower = ((t ^ TREES[j]).bit_count()) // 2
        excess = d - lower
        assert excess >= 0
        DISTRIBUTION[d] += 1
        EXCESS[excess] += 1
        if d == 8:
            DIAMETER_PAIRS.add((i, j))
        if excess == 4:
            EXTREME_PAIRS.add((i, j))
assert DISTRIBUTION == {1:12000,2:72000,3:266940,4:588060,5:678350,
                        6:327080,7:52500,8:2070}
assert ECCENTRICITIES == {7:1040, 8:960}
assert EXCESS == {0:565010, 1:1045740, 2:363290, 3:24810, 4:150}
assert sum(DISTRIBUTION.values()) == 2000*1999//2
assert len(DIAMETER_PAIRS) == 2070 and len(EXTREME_PAIRS) == 150
assert EXTREME_PAIRS.issubset(DIAMETER_PAIRS)

# Full graph automorphism group: permutations of the 5 symbols of KG(5,2).
AUTOMORPHISMS = []
for p in itertools.permutations(range(5)):
    vmap = [V.index(tuple(sorted((p[x], p[y])))) for x,y in V]
    emap = tuple(EDGE_ID[frozenset((vmap[u],vmap[v]))] for u,v in E)
    AUTOMORPHISMS.append(emap)
assert len(set(AUTOMORPHISMS)) == 120

def transform(t, a):
    return sum(1 << a[i] for i in range(15) if (t >> i) & 1)

TREE_ORBIT_REP = {}
for i,t in enumerate(TREES):
    TREE_ORBIT_REP[i] = min(LOOKUP[transform(t, a)] for a in AUTOMORPHISMS)
ORBIT_SIZES = Counter(TREE_ORBIT_REP.values())
assert len(ORBIT_SIZES) == 21

# Method B: orbit-weighted independent BFS checks every source up to symmetry,
# using the independently generated path-pivot adjacency.
SECOND_DIST = Counter()
SECOND_EXCESS = Counter()
SECOND_ECC = Counter()
for root, size in ORBIT_SIZES.items():
    dist = bfs(B, root)
    SECOND_ECC[max(dist)] += size
    for j, d in enumerate(dist):
        if j == root:
            continue
        SECOND_DIST[d] += size
        lower = ((TREES[root] ^ TREES[j]).bit_count()) // 2
        SECOND_EXCESS[d - lower] += size
assert all(v % 2 == 0 for v in SECOND_DIST.values())
assert all(v % 2 == 0 for v in SECOND_EXCESS.values())
assert Counter({d:v//2 for d,v in SECOND_DIST.items()}) == DISTRIBUTION
assert Counter({d:v//2 for d,v in SECOND_EXCESS.items()}) == EXCESS
assert SECOND_ECC == ECCENTRICITIES

# The maximal four-step overhead consists of two symmetry orbits.
def transform_pair(pair,a):
    i, j = pair
    return tuple(sorted((LOOKUP[transform(TREES[i],a)],
                         LOOKUP[transform(TREES[j],a)])))
remaining = set(EXTREME_PAIRS)
PAIR_ORBIT_SIZES = []
while remaining:
    first = min(remaining)
    orbit = {transform_pair(first,a) for a in AUTOMORPHISMS}
    assert orbit <= remaining
    PAIR_ORBIT_SIZES.append(len(orbit))
    remaining -= orbit
assert sorted(PAIR_ORBIT_SIZES) == [30, 120]
ENDPOINTS = {i for pair in EXTREME_PAIRS for i in pair}
assert len(ENDPOINTS) == 60
assert len({TREE_ORBIT_REP[x] for x in ENDPOINTS}) == 1
assert ORBIT_SIZES[TREE_ORBIT_REP[next(iter(ENDPOINTS))]] == 60

print('VERIFY_OK')
print('spanning_trees=2000, pivot_graph_edges=12000, tree_orbits=21')
print('distance_pairs=', sorted(DISTRIBUTION.items()))
print('eccentricities=', sorted(ECCENTRICITIES.items()))
print('excess_counts=', sorted(EXCESS.items()))
print('maximum_excess_pair_orbits=', sorted(PAIR_ORBIT_SIZES))
