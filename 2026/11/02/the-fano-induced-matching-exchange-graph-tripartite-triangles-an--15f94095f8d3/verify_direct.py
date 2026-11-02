#!/usr/bin/env python3
"""Independent direct flag-subset verifier for Fano incidence induced matchings."""
from itertools import combinations
from collections import Counter, deque

points = tuple(range(1, 8))
lines = tuple(sorted({tuple(sorted((a, b, a ^ b))) for a in points for b in points if a != b}))
assert len(lines) == 7
flags = tuple((p, i) for i, line in enumerate(lines) for p in line)
assert len(flags) == 21

def compatible(a, b):
    p, i = flags[a]
    q, j = flags[b]
    return p != q and i != j and p not in lines[j] and q not in lines[i]

compatible_pairs = {frozenset(pair) for pair in combinations(range(21), 2) if compatible(*pair)}
assert len(compatible_pairs) == 84

def is_induced_matching(c):
    return all(frozenset(pair) in compatible_pairs for pair in combinations(c, 2))

maxima = tuple(c for c in combinations(range(21), 3) if is_induced_matching(c))
assert len(maxima) == 84
assert not any(is_induced_matching(c) for c in combinations(range(21), 4))
lookup = {frozenset(c): i for i, c in enumerate(maxima)}
assert len(lookup) == 84

adj = [set() for _ in maxima]
for i, a in enumerate(maxima):
    for removed in a:
        for inserted in range(21):
            if inserted in a:
                continue
            b = frozenset(set(a) - {removed} | {inserted})
            if b in lookup:
                adj[i].add(lookup[b])
assert all(len(nbrs) == 6 for nbrs in adj)
assert sum(map(len, adj)) == 504
assert all(i in adj[j] for i, ns in enumerate(adj) for j in ns)

def geometry(c):
    pp = {flags[e][0] for e in c}
    ii = {flags[e][1] for e in c}
    point_collinear = any(pp.issubset(line) for line in lines)
    line_concurrent = any(all(p in lines[j] for j in ii) for p in points)
    if not point_collinear:
        assert line_concurrent
        return 'A'
    return 'C' if line_concurrent else 'B'

types = tuple(geometry(c) for c in maxima)
assert Counter(types) == {'A': 28, 'B': 28, 'C': 28}
assert all(types[i] != types[j] for i, ns in enumerate(adj) for j in ns)
assert all(Counter(types[j] for j in ns) == Counter({t: 3 for t in 'ABC' if t != types[i]})
           for i, ns in enumerate(adj))
assert Counter(len(adj[i] & adj[j]) for i, ns in enumerate(adj) for j in ns if i < j) == {1: 252}
assert sum(1 for i in range(84) for j in adj[i] if j > i
           for k in (adj[i] & adj[j]) if k > j) == 84

pair_distances = Counter()
detours = Counter()
ecc = Counter()
profiles = {t: set() for t in 'ABC'}
diametrical_types = Counter()
for s in range(84):
    d = {s: 0}
    queue = deque([s])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in d:
                d[w] = d[v] + 1
                queue.append(w)
    assert len(d) == 84
    ecc[(types[s], max(d.values()))] += 1
    profiles[types[s]].add(tuple(Counter(d.values())[k] for k in range(6)))
    for t in range(s + 1, 84):
        dist = d[t]
        pair_distances[dist] += 1
        lower = 3 - len(set(maxima[s]) & set(maxima[t]))
        detours[dist - lower] += 1
        if dist == 5:
            diametrical_types[''.join(sorted((types[s], types[t])))] += 1
assert pair_distances == {1: 252, 2: 840, 3: 1442, 4: 840, 5: 112}
assert detours == {0: 2492, 1: 882, 2: 112}
assert ecc == {('A', 5): 28, ('B', 5): 28, ('C', 4): 28}
assert profiles == {'A': {(1, 6, 21, 34, 18, 4)},
                    'B': {(1, 6, 21, 34, 18, 4)},
                    'C': {(1, 6, 18, 35, 24, 0)}}
assert diametrical_types == {'AA': 42, 'AB': 28, 'BB': 42}
print('DIRECT_FANO_FLAG_EXCHANGE_PASS')
print('maxima=84 edges=252 triangles=84 classes=28+28+28 center=28 radius=4 diameter=5')
print('distance_pairs=', sorted(pair_distances.items()))
print('detours=', sorted(detours.items()))
