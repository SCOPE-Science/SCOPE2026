#!/usr/bin/env python3
"""Independent Dyck-word/allowed-chord reconstruction of the same graph.
Run: python3 verify_dyck_dp.py
No third-party packages or input data needed.
"""
from collections import Counter, deque
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from math import comb

K = 9
N = 2 * K

def from_dyck(open_positions):
    stack = []
    pairs = []
    for pos in range(N):
        if pos in open_positions:
            stack.append(pos)
        else:
            if not stack:
                return None
            pairs.append((stack.pop(), pos))
    if stack:
        return None
    return tuple(sorted(pairs))

vertices = []
for opens in combinations(range(N), K):
    m = from_dyck(set(opens))
    if m is not None:
        vertices.append(m)
vertices.sort()
assert len(vertices) == 4862 and len(vertices) == len(set(vertices))
vid = {m: i for i, m in enumerate(vertices)}

def crosses(one, two):
    a, b = one
    c, d = two
    return (a < c < b < d) or (c < a < d < b)

# For each matching, list all alternative noncrossing perfect matchings
# made entirely from chords disjoint and noncrossing with the original.
adj = [[] for _ in vertices]
for i, original in enumerate(vertices):
    allowed = set()
    for a in range(N):
        for b in range(a + 1, N, 2):
            e = (a, b)
            if e not in original and all(not crosses(e, f) for f in original):
                allowed.add(e)

    @lru_cache(None)
    def augment(left, right):
        if left > right:
            return ((),)
        results = []
        for j in range(left + 1, right + 1, 2):
            if (left, j) not in allowed:
                continue
            for middle in augment(left + 1, j - 1):
                for suffix in augment(j + 1, right):
                    results.append(((left, j),) + middle + suffix)
        return tuple(results)

    neighbors = []
    for match in augment(0, N - 1):
        match = tuple(sorted(match))
        assert match in vid
        neighbors.append(vid[match])
    adj[i] = sorted(neighbors)
    assert len(adj[i]) == len(set(adj[i]))

assert all(i in adj[j] for i in range(len(vertices)) for j in adj[i])
edge_hash = sha256()
for i in range(len(vertices)):
    for j in adj[i]:
        if i < j:
            edge_hash.update(f'{i},{j}\n'.encode('ascii'))
assert sum(map(len, adj)) // 2 == 8677

remaining = set(range(len(vertices)))
components = []
while remaining:
    root = min(remaining)
    remaining.remove(root)
    layer = [root]
    collection = []
    for x in layer:
        collection.append(x)
        for y in adj[x]:
            if y in remaining:
                remaining.remove(y)
                layer.append(y)
    components.append(collection)
assert Counter(map(len, components)) == {1: 612, 5: 36, 4070: 1}
assert all(Counter(len(adj[v]) for v in comp) == {1: 4, 4: 1}
           for comp in components if len(comp) == 5)
big = max(components, key=len)
ecc = Counter()
centers = []
max_distance = 0
for source in big:
    dist = {source: 0}
    frontier = [source]
    while frontier:
        next_frontier = []
        for x in frontier:
            for y in adj[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    next_frontier.append(y)
        frontier = next_frontier
    assert len(dist) == 4070
    d = max(dist.values())
    ecc[d] += 1
    if d == 10:
        centers.append(source)
    max_distance = max(max_distance, d)
assert ecc == {10: 2, 11: 480, 12: 483, 13: 1377, 14: 1368, 15: 360}
assert max_distance == 15
assert {vertices[i] for i in centers} == {
    tuple((2*i, 2*i+1) for i in range(K)),
    tuple([(0, N-1)] + [(i, i+1) for i in range(1, N-1, 2)])
}
print('VERTICES', len(vertices))
print('EDGES', sum(map(len, adj)) // 2)
print('COMPONENTS', sorted(Counter(map(len, components)).items()))
print('BIG_RADIUS', min(ecc))
print('BIG_DIAMETER', max_distance)
print('BIG_ECCENTRICITIES', sorted(ecc.items()))
print('BIG_CENTER', sorted(vertices[i] for i in centers))
print('EDGE_SHA256', edge_hash.hexdigest())
print('VERIFY_OK')
