#!/usr/bin/env python3
"""Exact, standalone certificate using the Hamiltonian presentation of the Heawood graph.

Vertices are 0,...,13; edges are the cyclic 14-gon and seven opposite chords.
Every 6-subset and every allowed one-for-one swap are checked; all 448
breadth-first searches are run without quotienting by symmetry.
"""
from collections import Counter
from itertools import combinations

N = 14
CHORDS = [(0, 5), (1, 10), (2, 7), (3, 12), (4, 9), (6, 11), (8, 13)]
EDGES = {tuple(sorted((v, (v+1) % N))) for v in range(N)}
EDGES.update(tuple(sorted(e)) for e in CHORDS)
assert len(EDGES) == 21
adj = [0]*N
for u,v in EDGES:
    adj[u] |= 1 << v
    adj[v] |= 1 << u
assert all(mask.bit_count() == 3 for mask in adj)

def locating_dominating(mask):
    seen = set()
    for vertex in range(N):
        if mask & (1 << vertex):
            continue
        signature = adj[vertex] & mask
        if signature == 0 or signature in seen:
            return False
        seen.add(signature)
    return True

# Examine every subset smaller than 6, establishing the minimum independently.
for size in range(6):
    for subset in combinations(range(N), size):
        mask = sum(1<<v for v in subset)
        assert not locating_dominating(mask)

states = sorted(
    sum(1<<v for v in subset)
    for subset in combinations(range(N), 6)
    if locating_dominating(sum(1<<v for v in subset))
)
assert len(states) == 448
index = {mask:i for i,mask in enumerate(states)}
assert len(index) == 448

neighbors = []
for x in states:
    row = set()
    for removed in range(N):
        if not (x & (1 << removed)):
            continue
        for added in range(N):
            if x & (1 << added):
                continue
            y = x ^ (1 << removed) ^ (1 << added)
            if y in index:
                row.add(index[y])
    neighbors.append(sorted(row))
for i,row in enumerate(neighbors):
    assert all(i in neighbors[j] for j in row)

degree_hist = Counter(map(len, neighbors))
assert degree_hist == {6:28, 12:168, 14:168, 22:84}, degree_hist
assert sum(map(len, neighbors))//2 == 3192

pair_distances = Counter()
pair_detours = Counter()
jump_detour = Counter()
eccentricities = Counter()
for i, source in enumerate(states):
    d = [-1] * len(states)
    d[i] = 0
    queue = [i]
    for u in queue:
        for v in neighbors[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                queue.append(v)
    assert len(queue) == len(states)  # connected
    eccentricities[max(d)] += 1
    for j in range(i+1,len(states)):
        distance = d[j]
        lower = 6 - (source & states[j]).bit_count()
        extra = distance - lower
        assert extra in (0,1)
        pair_distances[distance] += 1
        pair_detours[extra] += 1
        if extra:
            jump_detour[lower] += 1

assert eccentricities == {6:448}
assert pair_distances == {1:3192, 2:15204, 3:32508,
                          4:32298, 5:14868, 6:2058}
assert pair_detours == {0:97188, 1:2940}
assert jump_detour == {2:1008, 3:1428, 4:504}
assert sum(pair_distances.values()) == 448*447//2

print('CYCLIC_HEAWOOD_EXHAUSTIVE_PASS')
print('states=448 edges=3192 degree_hist=',sorted(degree_hist.items()))
print('pair_distances=',sorted(pair_distances.items()))
print('detours=',sorted(pair_detours.items()),'by_lower_bound=',sorted(jump_detour.items()))
print('eccentricities=',sorted(eccentricities.items()))
