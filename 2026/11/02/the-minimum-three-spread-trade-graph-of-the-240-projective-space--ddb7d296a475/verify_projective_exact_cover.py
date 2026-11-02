"""Independent finite exact-cover verification for projective-space packing trades.

Run: python verify_projective_exact_cover.py
Only Python's standard library is needed.
"""
from itertools import combinations
from collections import Counter, deque

POINTS = range(1, 16)
line_triples = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                             for a, b in combinations(POINTS, 2)}))
assert len(line_triples) == 35
line_masks = tuple(sum(1 << (p - 1) for p in L) for L in line_triples)
assert len(set(line_masks)) == 35
by_point = {p: tuple(i for i, mask in enumerate(line_masks)
                     if mask & (1 << (p - 1))) for p in POINTS}

spreads = set()
def enumerate_spreads(covered, selected):
    if covered == (1 << 15) - 1:
        spreads.add(tuple(sorted(selected)))
        return
    p = next(p for p in POINTS if not covered & (1 << (p - 1)))
    for i in by_point[p]:
        if not covered & line_masks[i]:
            enumerate_spreads(covered | line_masks[i], selected + (i,))
enumerate_spreads(0, ())
spreads = tuple(sorted(spreads))
assert len(spreads) == 56 and all(len(s) == 5 for s in spreads)

by_line = {i: tuple(k for k, s in enumerate(spreads) if i in s)
           for i in range(35)}
spread_line_masks = tuple(sum(1 << i for i in spread) for spread in spreads)
packings = set()
def enumerate_packings(covered, selected):
    if covered == (1 << 35) - 1:
        packings.add(tuple(sorted(selected)))
        return
    i = next(i for i in range(35) if not covered & (1 << i))
    for j in by_line[i]:
        if not covered & spread_line_masks[j]:
            enumerate_packings(covered | spread_line_masks[j], selected + (j,))
enumerate_packings(0, ())
packings = tuple(sorted(packings))
assert len(packings) == 240
assert all(len(p) == 7 for p in packings)

P = [frozenset(x) for x in packings]
intersection = Counter(len(P[i] & P[j]) for i, j in combinations(range(240), 2))
assert intersection == {0:13560, 1:8400, 2:5040, 3:840, 4:840}, intersection
adj = [{j for j in range(240) if j != i and len(P[i] & P[j]) == 4}
       for i in range(240)]
assert all(len(neighbors) == 7 for neighbors in adj)
assert all(i in adj[j] for i in range(240) for j in adj[i])
assert sum(map(len, adj)) // 2 == 840

# Exact all-roots shortest paths and component check.
expected = (1, 7, 42, 105, 77, 8)
for root in range(240):
    dist = {root: 0}
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                queue.append(w)
    assert len(dist) == 240
    assert tuple(Counter(dist.values())[i] for i in range(6)) == expected
    # The breadth-first parity partition proves bipartiteness.
    assert all((dist[u] - dist[v]) % 2 for u in range(240) for v in adj[u])

# The absence of 4-cycles and bipartiteness imply girth at least 6;
# the 42 neighbors at distance two and only 105 at distance three imply a 6-cycle.
assert all(len(adj[i] & adj[j]) <= 1
           for i, j in combinations(range(240), 2))
assert sum(len(adj[i]) * (len(adj[i]) - 1) for i in range(240)) == 240*7*6
print('PROJECTIVE_EXACT_COVER_ALL_240_PACKINGS_PASS')
print('MINIMUM_TRADE_3_DEGREE_7_EDGES_840_GIRTH_6_DIAMETER_5_PASS')
print('ALL_ROOT_DISTANCE_DISTRIBUTION', expected)
