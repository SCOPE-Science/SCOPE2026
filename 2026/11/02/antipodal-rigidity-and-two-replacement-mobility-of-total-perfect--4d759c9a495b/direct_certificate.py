"""Exhaustive open-neighborhood verification for total perfect codes of Q_4.

Standard library only. Run with: python direct_certificate.py
"""
from collections import Counter, deque
from itertools import combinations

V = range(16)
NEIGHBORS = [frozenset(v ^ (1 << j) for j in range(4)) for v in V]


def valid(code):
    return all(sum(int(w in code) for w in NEIGHBORS[v]) == 1 for v in V)


codes = [frozenset(x) for x in combinations(V, 4) if valid(x)]
assert len(codes) == 16, len(codes)
assert len({x for x in codes}) == 16
assert all(any((a ^ 15) in c for a in c) for c in codes)
assert all(all((a ^ 15) in c for a in c) for c in codes)

# Every possible 4-vertex candidate was checked, and size four is forced
# by the degree-sum equation for an exact open-neighborhood covering.
counts = Counter(len(a - b) for i, a in enumerate(codes) for b in codes[:i])
assert counts == {2: 48, 4: 72}, counts

# Build exact-two-replacements reconfiguration and independently inspect all
# breadth-first-search distance profiles.
adj = [set() for _ in codes]
for i, a in enumerate(codes):
    for j in range(i):
        if len(a - codes[j]) == 2:
            adj[i].add(j)
            adj[j].add(i)
assert set(map(len, adj)) == {6}
assert sum(map(len, adj)) // 2 == 48
assert sum(sum(v in adj[u] for v in adj[u]) for u in range(16)) == 96
for i in range(len(codes)):
    q = deque([i]); distances = {i: 0}
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w not in distances:
                distances[w] = distances[v] + 1
                q.append(w)
    assert Counter(distances.values()) == {0: 1, 1: 6, 2: 9}
    for j, b in enumerate(codes):
        assert distances[j] == len(codes[i] - b) // 2
        if distances[j] == 2:
            assert len(adj[i] & adj[j]) == 2
        if distances[j] == 1:
            assert len(adj[i] & adj[j]) == 2
assert all(len(a - b) != 1 for i, a in enumerate(codes) for b in codes[:i])
partitions = [quad for quad in combinations(range(len(codes)), 4)
              if len(set().union(*(codes[i] for i in quad))) == 16]
assert len(partitions) == 24, len(partitions)
assert Counter(i for quad in partitions for i in quad) == Counter({i: 6 for i in range(16)})
print('DIRECT_Q4_OPEN_NEIGHBORHOOD_PASS', len(codes), sum(map(len, adj)) // 2, counts)
