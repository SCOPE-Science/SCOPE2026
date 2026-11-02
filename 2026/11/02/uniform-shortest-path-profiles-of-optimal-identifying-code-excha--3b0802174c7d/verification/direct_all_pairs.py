#!/usr/bin/env python3
"""Complete, explicit census of the optimal closed-neighborhood identifying codes of Q4.
Run: python3 verification/direct_all_pairs.py. No dependencies beyond Python 3.
"""
from collections import Counter, deque

N = 16
closed = []
for x in range(N):
    mask = 1 << x
    for i in range(4):
        mask |= 1 << (x ^ (1 << i))
    closed.append(mask)

def identifies(code):
    signatures = [code & ball for ball in closed]
    return all(signatures) and len(set(signatures)) == N

# Each one of the 2**16 possible sensor layouts is tested.
all_codes = [mask for mask in range(1 << N) if identifies(mask)]
hist = Counter(mask.bit_count() for mask in all_codes)
assert not any(hist.get(i, 0) for i in range(7))
assert hist[7] == 960
states = [mask for mask in all_codes if mask.bit_count() == 7]
index = {mask: i for i, mask in enumerate(states)}
adj = []
for state in states:
    nbrs = set()
    for old in range(N):
        if state & (1 << old):
            for new in range(N):
                if not state & (1 << new):
                    nxt = state ^ (1 << old) ^ (1 << new)
                    if nxt in index:
                        nbrs.add(index[nxt])
    adj.append(nbrs)
assert len(adj) == 960
assert all(len(neighbors) == 9 for neighbors in adj)
assert all(i in adj[j] for i, ns in enumerate(adj) for j in ns)
assert sum(map(len, adj)) // 2 == 4320
shell = (1, 9, 35, 132, 300, 338, 130, 15)
distance_counts = Counter()
for start in range(len(states)):
    distances = [-1] * len(states)
    distances[start] = 0
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for other in adj[current]:
            if distances[other] < 0:
                distances[other] = distances[current] + 1
                queue.append(other)
    assert -1 not in distances
    counts = Counter(distances)
    assert tuple(counts[d] for d in range(8)) == shell
    distance_counts.update(distances)
assert all(distance_counts[d] == 960 * shell[d] for d in range(8))
assert sum(distance_counts[d] // 2 for d in range(1, 8)) == 960 * 959 // 2
print('DIRECT_ALL_PAIRS_PASS')
print('minimum=7, codes=960, edges=4320, degree=9, radius=7, diameter=7')
print('all_source_shells=', shell)
print('unordered_distance_counts=', tuple(distance_counts[d] // 2 for d in range(1, 8)))
