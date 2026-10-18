#!/usr/bin/env python3
"""Exhaustive chord-mask certificate for convex noncrossing 9-matchings.
Run: python3 verify_chord_masks.py
No third-party packages or input data needed.
"""
from collections import Counter, deque
from functools import lru_cache
from hashlib import sha256
from math import comb

N = 18
K = N // 2

@lru_cache(None)
def all_matchings(a, b):
    if a > b:
        return ((),)
    answer = []
    for j in range(a + 1, b + 1, 2):
        for inside in all_matchings(a + 1, j - 1):
            for outside in all_matchings(j + 1, b):
                answer.append(((a, j),) + inside + outside)
    return tuple(answer)

vertices = sorted(tuple(sorted(m)) for m in all_matchings(0, N - 1))
assert len(vertices) == comb(N, K) // (K + 1) == 4862
assert len(vertices) == len(set(vertices))
chords = [(i, j) for i in range(N) for j in range(i + 1, N)
           if (j - i) % 2 == 1]
index = {edge: r for r, edge in enumerate(chords)}

def crossing(a, b, c, d):
    return (a < c < b < d) or (c < a < d < b)

prohibited = []
for a, b in chords:
    bitmap = 0
    for r, (c, d) in enumerate(chords):
        if (a, b) == (c, d) or crossing(a, b, c, d):
            bitmap |= 1 << r
    prohibited.append(bitmap)

bits = []
ban = []
for match in vertices:
    mbit = 0
    forbidden = 0
    for edge in match:
        r = index[edge]
        mbit |= 1 << r
        forbidden |= prohibited[r]
    bits.append(mbit)
    ban.append(forbidden)

adj = [[] for _ in vertices]
edge_hash = sha256()
for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        if not (bits[j] & ban[i]):
            assert not (bits[i] & ban[j])
            adj[i].append(j)
            adj[j].append(i)
            edge_hash.update(f'{i},{j}\n'.encode('ascii'))

components = []
seen = set()
for root in range(len(vertices)):
    if root in seen:
        continue
    seen.add(root)
    queue = deque([root])
    group = []
    while queue:
        x = queue.popleft()
        group.append(x)
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                queue.append(y)
    components.append(group)

big = max(components, key=len)
assert len(big) == 4070
assert Counter(len(c) for c in components) == {1: 612, 5: 36, 4070: 1}
assert sum(map(len, adj)) // 2 == 8677
assert all(Counter(len(adj[v]) for v in comp) == {1: 4, 4: 1}
           for comp in components if len(comp) == 5)

hist = Counter()
center = []
diameter = 0
witness = None
for root in big:
    distances = [-1] * len(vertices)
    distances[root] = 0
    queue = deque([root])
    while queue:
        x = queue.popleft()
        for y in adj[x]:
            if distances[y] < 0:
                distances[y] = distances[x] + 1
                queue.append(y)
    d = max(distances)
    assert sum(t >= 0 for t in distances) == len(big)
    hist[d] += 1
    if d == 10:
        center.append(root)
    if d > diameter:
        diameter = d
        witness = (root, distances.index(d))
assert hist == {10: 2, 11: 480, 12: 483, 13: 1377, 14: 1368, 15: 360}
assert diameter == 15
center_matchings = [vertices[i] for i in center]
ring_a = tuple((i, i + 1) for i in range(0, N, 2))
ring_b = tuple([(0, N - 1)] + [(i, i + 1) for i in range(1, N - 1, 2)])
assert set(center_matchings) == {ring_a, ring_b}
assert all(len(adj[i]) == 232 for i in center)
print('VERTICES', len(vertices))
print('EDGES', sum(map(len, adj)) // 2)
print('COMPONENTS', sorted(Counter(len(c) for c in components).items()))
print('BIG_RADIUS', min(hist))
print('BIG_DIAMETER', diameter)
print('BIG_ECCENTRICITIES', sorted(hist.items()))
print('BIG_CENTER', sorted(center_matchings))
print('DIAMETER_WITNESS', vertices[witness[0]], vertices[witness[1]])
print('EDGE_SHA256', edge_hash.hexdigest())
print('VERIFY_OK')
