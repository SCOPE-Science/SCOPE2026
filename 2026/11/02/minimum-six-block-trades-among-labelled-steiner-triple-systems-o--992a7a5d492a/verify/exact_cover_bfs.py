"""Exact-cover census of labelled STS(9) and the six-block trade graph.

Run: python3 verify_exact_cover.py.  Python standard library only.
"""
from collections import Counter, deque
from itertools import combinations

POINTS = range(9)
TRIPLES = list(combinations(POINTS, 3))
PAIRS = list(combinations(POINTS, 2))
PAIR_INDEX = {p: k for k, p in enumerate(PAIRS)}
PAIR_MASK = []
FOR_PAIR = [[] for _ in PAIRS]
for j, triple in enumerate(TRIPLES):
    m = 0
    for pair in combinations(triple, 2):
        i = PAIR_INDEX[pair]
        m |= 1 << i
        FOR_PAIR[i].append(j)
    PAIR_MASK.append(m)
ALL_PAIRS = (1 << 36) - 1
systems = []


def exact_cover(covered, selected, depth):
    if covered == ALL_PAIRS:
        assert depth == 12 and selected.bit_count() == 12
        systems.append(selected)
        return
    assert depth < 12
    chosen = None
    candidates = None
    # Each unfilled pair must be covered by exactly one unused, compatible triple.
    for p in range(36):
        if (covered >> p) & 1:
            continue
        ok = [j for j in FOR_PAIR[p] if not (PAIR_MASK[j] & covered)]
        if not ok:
            return
        if candidates is None or len(ok) < len(candidates):
            chosen, candidates = p, ok
            if len(ok) == 1:
                break
    assert chosen is not None
    for j in candidates:
        exact_cover(covered | PAIR_MASK[j], selected | (1 << j), depth + 1)


exact_cover(0, 0, 0)
assert len(systems) == len(set(systems)) == 840, len(systems)
systems.sort()
assert all(s.bit_count() == 12 for s in systems)

# Enumerate all unordered pairs, not merely candidate swaps.
adj = [[] for _ in systems]
intersection = Counter()
for i, s in enumerate(systems):
    for j in range(i):
        k = (s & systems[j]).bit_count()
        intersection[k] += 1
        if k == 6:
            adj[i].append(j)
            adj[j].append(i)
assert dict(intersection) == {0: 80640, 1: 90720, 2: 90720,
                             3: 63840, 4: 11340, 6: 15120}
assert all(len(neighbors) == 36 for neighbors in adj)
assert sum(map(len, adj)) // 2 == 15120

# Check the full metric, not just the distances from one convenient system.
expected = {12: (0, 1), 6: (1, 36), 4: (2, 27),
            3: (2, 152), 2: (2, 216), 1: (3, 216), 0: (3, 192)}
for root in range(840):
    distances = [-1] * 840
    distances[root] = 0
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if distances[w] == -1:
                distances[w] = distances[v] + 1
                queue.append(w)
    assert -1 not in distances
    assert Counter(distances) == {0: 1, 1: 36, 2: 395, 3: 408}
    intersections_by_k = Counter()
    for i, other in enumerate(systems):
        k = (systems[root] & other).bit_count()
        dist, _ = expected[k]
        assert distances[i] == dist, (root, i, k, distances[i], dist)
        intersections_by_k[k] += 1
    for k, (_, total) in expected.items():
        assert intersections_by_k[k] == total
print('EXACT_COVER_840_DESIGNS_AND_15120_TRADES_PASS')
print('ALL_840_ROOTS_METRIC_AND_INTERSECTION_LAW_PASS')
print('DISTANCES_1_36_395_408_DIAMETER_3_PASS')
