#!/usr/bin/env python3
"""Exact Pappus perfect-matching hexagon/octagon flip verification.

No external dependencies; Python 3.9+. Coordinates are modulo three.
"""
from collections import Counter, deque
from itertools import combinations, product

points = list(product(range(3), repeat=2))
lines = list(product(range(3), range(3)))

def incident(point, line):
    x, y = point
    direction, c = line
    return (x if direction == 0 else y if direction == 1 else (x + y) % 3) == c

allowed = [tuple(j for j, line in enumerate(lines) if incident(p, line)) for p in points]
assert len(points) == len(lines) == 9 and all(len(a) == 3 for a in allowed)
matchings = []
def walk(i, occupied, assignment):
    if i == 9:
        matchings.append(tuple(assignment))
        return
    for j in allowed[i]:
        if not occupied & (1 << j):
            walk(i + 1, occupied | (1 << j), assignment + [j])
walk(0, 0, [])
assert len(matchings) == len(set(matchings)) == 42

def change_length(left, right):
    inverse = {col: row for row, col in enumerate(right)}
    unseen = set(range(9))
    nontrivial = []
    while unseen:
        i = next(iter(unseen)); j = i; size = 0
        while j in unseen:
            unseen.remove(j); size += 1; j = inverse[left[j]]
        if size > 1:
            nontrivial.append(size)
    return 2 * nontrivial[0] if len(nontrivial) == 1 else None

def parity(p):
    return sum(p[i] > p[j] for i in range(9) for j in range(i + 1, 9)) % 2

N = len(matchings)
adj = {6: [set() for _ in range(N)], 8: [set() for _ in range(N)]}
for i, j in combinations(range(N), 2):
    size = change_length(matchings[i], matchings[j])
    if size in adj:
        adj[size][i].add(j)
        adj[size][j].add(i)
assert sum(map(len, adj[6])) // 2 == 72
assert sum(map(len, adj[8])) // 2 == 108
assert Counter(parity(m) for m in matchings) == {0: 21, 1: 21}
assert all(parity(matchings[i]) == parity(matchings[j]) for i in range(N) for j in adj[6][i])
assert all(parity(matchings[i]) != parity(matchings[j]) for i in range(N) for j in adj[8][i])

def components(graph):
    remaining = set(range(len(graph))); result = []
    while remaining:
        root = min(remaining); remaining.remove(root); comp = {root}; queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v in remaining:
                    remaining.remove(v); comp.add(v); queue.append(v)
        result.append(comp)
    return result

def distances(graph, root):
    queue = deque([root]); dist = {root: 0}
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1; queue.append(v)
    return dist

six_comps = components(adj[6])
assert sorted(map(len, six_comps)) == [21, 21]
assert {frozenset(c) for c in six_comps} == {frozenset(i for i in range(N) if parity(matchings[i]) == p) for p in (0, 1)}
assert Counter(len(x) for x in components(adj[8])) == {1: 6, 36: 1}
assert Counter(len(neighbors) for neighbors in adj[6]) == {3: 36, 6: 6}
assert Counter(len(neighbors) for neighbors in adj[8]) == {0: 6, 6: 36}

# Each parity-sector graph has three valency-six hubs and three alternating
# six-cycles. Each residual vertex belongs to one cycle and one hub spoke.
for comp in six_comps:
    hubs = sorted(v for v in comp if len(adj[6][v]) == 6)
    assert len(hubs) == 3
    others = comp - set(hubs)
    assert len(others) == 18
    assert all(len(adj[6][u] & set(hubs)) == 1 for u in others)
    assert all(len(adj[6][u] & others) == 2 for u in others)
    rem = set(others); seen_pairs = set()
    while rem:
        first = min(rem); rem.remove(first); cycle = [first]; previous = None; current = first
        while True:
            nxts = sorted(v for v in adj[6][current] & others if v != previous)
            nxt = nxts[0]
            if nxt == first:
                break
            assert nxt in rem
            rem.remove(nxt); cycle.append(nxt); previous, current = current, nxt
        assert len(cycle) == 6
        labels = [next(h for h in hubs if h in adj[6][u]) for u in cycle]
        assert labels[0] == labels[2] == labels[4]
        assert labels[1] == labels[3] == labels[5]
        assert labels[0] != labels[1]
        seen_pairs.add(frozenset(labels))
    assert seen_pairs == {frozenset(pair) for pair in combinations(hubs, 2)}
    assert max(max(distances(adj[6], v).values()) for v in comp) == 4

combined = [adj[6][i] | adj[8][i] for i in range(N)]
assert Counter(len(x) for x in combined) == {6: 6, 9: 36}
assert len(components(combined)) == 1
assert Counter(tuple(Counter(distances(combined, i).values()).get(d, 0) for d in range(4)) for i in range(N)) == {(1, 6, 24, 11): 6, (1, 9, 24, 8): 36}
pair_hist = Counter(distances(combined, i)[j] for i, j in combinations(range(N), 2))
assert pair_hist == {1: 180, 2: 504, 3: 177}
assert sum(pair_hist.values()) == 861
print('AFFINE_PAPPUS_HEXAGON_OCTAGON_EXHAUSTIVE_PASS')
print('MATCHINGS=42; HEXAGON_PARITY_COMPONENTS=21+21; OCTAGON_THRESHOLD=8; COMBINED_DIAMETER=3')
