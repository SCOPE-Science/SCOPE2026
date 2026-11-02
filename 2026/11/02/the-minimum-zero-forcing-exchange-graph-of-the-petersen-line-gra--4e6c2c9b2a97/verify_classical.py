"""Independent finite certificate using the usual outer/inner Petersen model.

The program checks all potential smaller forcing sets by individual
one-vertex forces and computes all shortest-path distances directly, without
using the underlying graph's automorphism group or parallel forcing rounds.
"""
from itertools import combinations
from collections import Counter

petersen_edges = []
for i in range(5):
    petersen_edges.append(tuple(sorted((i, (i + 1) % 5))))
    petersen_edges.append(tuple(sorted((5 + i, 5 + (i + 2) % 5))))
    petersen_edges.append((i, 5 + i))
assert len(set(petersen_edges)) == 15
neighbors = []
for e in petersen_edges:
    neighbors.append(tuple(j for j, f in enumerate(petersen_edges)
                           if e != f and set(e).intersection(f)))
assert all(len(x) == 4 for x in neighbors)
FULL = (1 << 15) - 1

# Sequential branching process: can choose each legal force at every state.
# The search is finite and increasing; no heuristic or timeout applies.
def can_force(start):
    frontier = [start]
    visited = {start}
    for colored in frontier:
        if colored == FULL:
            return True
        for u in range(15):
            if colored & (1 << u):
                white = [v for v in neighbors[u] if not (colored & (1 << v))]
                if len(white) == 1:
                    next_state = colored | (1 << white[0])
                    if next_state not in visited:
                        visited.add(next_state)
                        frontier.append(next_state)
    return False

for k in range(7):
    for c in combinations(range(15), k):
        assert not can_force(sum(1 << i for i in c))

states = sorted(sum(1 << i for i in c)
                for c in combinations(range(15), 7)
                if can_force(sum(1 << i for i in c)))
assert len(states) == 2280
adj = {s: [] for s in states}
for i, a in enumerate(states):
    for b in states[i + 1:]:
        if (a ^ b).bit_count() == 2:
            adj[a].append(b)
            adj[b].append(a)
assert sum(len(x) for x in adj.values()) // 2 == 28650
assert Counter(map(len, adj.values())) == {
    22: 180, 23: 480, 24: 240, 25: 240,
    26: 660, 27: 240, 28: 60, 29: 180}

pair_hist = Counter()
ecc_hist = Counter()
defect_hist = Counter()
for source in states:
    dist = {source: 0}
    layer_queue = [source]
    for current in layer_queue:
        for target in adj[current]:
            if target not in dist:
                dist[target] = dist[current] + 1
                layer_queue.append(target)
    assert len(dist) == len(states)
    ecc_hist[max(dist.values())] += 1
    for target, length in dist.items():
        pair_hist[length] += 1
        minimum_possible = (source ^ target).bit_count() // 2
        assert length in (minimum_possible, minimum_possible + 1)
        if length == minimum_possible + 1:
            defect_hist[(minimum_possible, length)] += 1

assert ecc_hist == {6: 600, 7: 1680}
assert dict(pair_hist) == {
    0: 2280, 1: 57300, 2: 468240, 3: 1531140,
    4: 2009280, 5: 966960, 6: 157080, 7: 6120}
assert dict(defect_hist) == {(2, 3): 6360, (3, 4): 23280, (4, 5): 7440}
assert sum(defect_hist.values()) // 2 == 18540
assert sum(pair_hist.values()) == 2280 ** 2
print('CLASSICAL_CERTIFICATE_PASS', len(states),
      sum(len(x) for x in adj.values()) // 2,
      sorted(ecc_hist.items()), 'detour_pairs=18540')
