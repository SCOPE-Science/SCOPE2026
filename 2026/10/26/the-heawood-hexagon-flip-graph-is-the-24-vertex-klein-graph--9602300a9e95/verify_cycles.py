"""Independent certificate: generate perfect matchings by incidence DFS;
generate alternating hexagon flips by simple-cycle DFS on 14 vertices.
Uses only Python standard library.
"""
from collections import Counter
from itertools import combinations
from hashlib import sha256
import json

V = range(14)
neighbors = {a: set() for a in V}
for p in range(7):
    for q in range(7):
        if (p-q) % 7 in {0, 1, 3}:
            neighbors[p].add(7+q)
            neighbors[7+q].add(p)
assert all(len(neighbors[v]) == 3 for v in V)

M = []
def fill(point, used, cur):
    if point == 7:
        M.append(tuple(cur))
        return
    for line in sorted(x-7 for x in neighbors[point]):
        if not ((used >> line) & 1):
            fill(point+1, used | (1 << line), cur+[line])
fill(0, 0, [])
assert len(M) == 24
M.sort()
Msets = [frozenset((min(p, 7+m[p]), max(p, 7+m[p])) for p in range(7)) for m in M]
lookup = {match: i for i, match in enumerate(Msets)}
assert len(lookup) == len(M)

# Each 6-cycle is represented uniquely by its six undirected edges.
hexagons = set()
for start in V:
    def extend(path):
        if len(path) == 6:
            if start in neighbors[path[-1]]:
                cyc = path + [start]
                ee = frozenset((min(cyc[i], cyc[i+1]), max(cyc[i], cyc[i+1])) for i in range(6))
                hexagons.add(ee)
            return
        for nxt in sorted(neighbors[path[-1]]):
            if nxt not in path:
                extend(path+[nxt])
    extend([start])
assert len(hexagons) == 28

adj = [set() for _ in M]
for a, match in enumerate(Msets):
    for cyc in hexagons:
        if len(cyc & match) == 3:
            candidate = frozenset(match ^ cyc)
            b = lookup[candidate]
            assert a != b
            adj[a].add(b)
assert all(len(v) == 7 for v in adj)
assert all(a in adj[b] for a in range(24) for b in adj[a])

# Check distance intersection parameters from a completely separate flip generator.
arrays = [dict() for _ in range(24)]
all_dist = []
for a in range(24):
    dist = {a: 0}
    frontier = {a}
    step = 0
    while frontier:
        new = set().union(*(adj[x] for x in frontier)) - set(dist)
        step += 1
        for x in new:
            dist[x] = step
        frontier = new
    assert Counter(dist.values()) == {0: 1, 1: 7, 2: 14, 3: 2}
    all_dist.append(dist)
    for b in range(24):
        level = dist[b]
        arrays[a][b] = tuple(sum(dist[c] == level + j for c in adj[b]) for j in (-1, 0, 1))
        expected = ((0,0,7), (1,2,4), (2,4,1), (7,0,0))[level]
        assert arrays[a][b] == expected

# Characterize complementary two perfect matchings in the 14-cycle complement.
all_edges = frozenset((min(u, v), max(u, v)) for u in V for v in neighbors[u])
factors = set()
for i, j in combinations(range(24), 2):
    if not (Msets[i] & Msets[j]):
        remain = all_edges - Msets[i] - Msets[j]
        k = lookup.get(remain)
        if k is not None:
            factors.add(tuple(sorted((i, j, k))))
assert len(factors) == 8
assert sorted(x for fac in factors for x in fac) == list(range(24))
for fac in factors:
    for i,j in combinations(fac,2):
        assert j not in adj[i]
        assert all_dist[i][j] == 3

edges = sorted((a,b) for a in range(24) for b in adj[a] if a < b)
canonical = json.dumps({'matchings': M, 'edges': edges}, separators=(',', ':'))
print('hexagons=28; matchings=24; flips=84; degree=7; all_points_verified=576')
print('intersection_array=([7,4,1],[1,2,7]); antipodal_fibers=8 triples')
print('canonical_sha256=' + sha256(canonical.encode('utf-8')).hexdigest())
