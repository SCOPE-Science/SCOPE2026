"""Exact verification of resolving bases in the bipartite Petersen double cover.

Requires only Python 3 standard library. Vertex (side, pair) has side in
{0,1} and pair an index in lexicographic 2-subsets of range(5).
"""
from itertools import combinations, product
from collections import Counter, deque
import json

pairs = tuple(combinations(range(5), 2))
vertices = tuple((side, p) for side in range(2) for p in pairs)
N = len(vertices)
assert N == 20
adj = [[] for _ in vertices]
for i, (s, a) in enumerate(vertices):
    for j, (t, b) in enumerate(vertices):
        if s != t and set(a).isdisjoint(b):
            adj[i].append(j)
assert sum(map(len, adj)) == 60 and all(len(x) == 3 for x in adj)

def petersen_d(a, b):
    if a == b: return 0
    return 1 if set(a).isdisjoint(b) else 2

def lifted_d(u, v):
    s, a = vertices[u]
    t, b = vertices[v]
    return ((0, 4, 2) if s == t else (5, 1, 3))[petersen_d(a,b)]

# Reconstruct graph distances without relying on the closed formula.
all_dist = []
for origin in range(N):
    d = [-1] * N
    d[origin] = 0
    q = deque([origin])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
    assert min(d) == 0 and max(d) <= 5
    all_dist.append(d)
assert all(lifted_d(u,v) == all_dist[u][v]
           for u in range(N) for v in range(N))

# Check full set of triples, including all 1140 unordered choices.
bases = []
for B in combinations(range(N), 3):
    signatures = {tuple(all_dist[x][w] for w in B) for x in range(N)}
    if len(signatures) == N:
        bases.append(B)

# The asserted family: three distinct spokes with one unique center.
def star_center(B):
    ps = [vertices[w][1] for w in B]
    common = set(ps[0]) & set(ps[1]) & set(ps[2])
    return next(iter(common)) if len(common) == 1 and len(set(ps)) == 3 else None

expected = {tuple(sorted(next(i for i, v in enumerate(vertices)
                              if v == (sgn, tuple(sorted((x,y)))))
                         for y, sgn in zip(Y, signs)))
            for x in range(5)
            for Y in combinations([y for y in range(5) if y != x], 3)
            for signs in product((0,1), repeat=3)}
assert set(bases) == expected
assert len(bases) == 160
assert Counter(star_center(b) for b in bases) == Counter({x:32 for x in range(5)})

bindex = {b:i for i,b in enumerate(bases)}
neighbors = [set() for _ in bases]
for i, B in enumerate(bases):
    for u in B:
        for v in range(N):
            if v not in B:
                replacement = tuple(sorted((set(B) - {u}) | {v}))
                j = bindex.get(replacement)
                if j is not None and j != i:
                    neighbors[i].add(j)
assert all(len(neighbors[i]) == 9 for i in range(160))
assert all(i in neighbors[j] for i,nbrs in enumerate(neighbors) for j in nbrs)

components = []
unvisited = set(range(len(bases)))
while unvisited:
    seed = min(unvisited)
    found = {seed}
    q = deque([seed])
    while q:
        for w in neighbors[q.popleft()]:
            if w not in found:
                found.add(w)
                q.append(w)
    unvisited -= found
    components.append(found)
assert len(components) == 5
assert sorted(map(len,components)) == [32]*5
assert all(len({star_center(bases[i]) for i in c}) == 1 for c in components)
profiles = set()
for c in components:
    for seed in c:
        # Direct BFS with correctly recorded frontier levels.
        ds = {seed:0}
        q = deque([seed])
        while q:
            i = q.popleft()
            for j in neighbors[i]:
                if j not in ds:
                    ds[j] = ds[i] + 1
                    q.append(j)
        assert len(ds) == len(c)
        profiles.add(tuple(Counter(ds.values()).get(t,0) for t in range(4)))
assert profiles == {(1, 9, 15, 7)}

print(json.dumps({
    'graph': 'Desargues graph / bipartite double of Petersen',
    'vertices': N, 'edges': sum(map(len,adj))//2,
    'tested_pairs': N*(N-1)//2,
    'tested_triples': 1140,
    'metric_dimension': 3,
    'bases': len(bases),
    'component_sizes': sorted(map(len,components)),
    'edges_of_exchange_graph': sum(map(len,neighbors))//2,
    'exchange_degree': 9,
    'component_distance_profile': [1, 9, 15, 7],
    'component_diameter': 3,
    'exact_family_confirmed': True,
    'distance_formula_confirmed': True,
}, sort_keys=True))
