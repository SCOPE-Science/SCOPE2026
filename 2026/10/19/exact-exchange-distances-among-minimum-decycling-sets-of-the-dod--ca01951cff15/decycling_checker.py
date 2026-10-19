#!/usr/bin/env python3
"""Exact finite verification of minimum feedback-vertex-set exchange distances.

The dodecahedral graph is the generalized Petersen graph GP(10,2).
Uses the Python standard library only. Run: python3 decycling_checker.py
"""
from collections import Counter, deque
from itertools import combinations
from math import comb

N = 20
OUTER = tuple(range(10))
INNER = tuple(range(10, 20))
EDGES = sorted({tuple(sorted(p)) for i in range(10)
                for p in ((i, (i + 1) % 10), (i, 10 + i),
                          (10 + i, 10 + (i + 2) % 10))})
ADJ = [set() for _ in range(N)]
for x, y in EDGES:
    ADJ[x].add(y)
    ADJ[y].add(x)
assert len(EDGES) == 30 and all(len(a) == 3 for a in ADJ)


def is_forest_union_find(deleted):
    """Acyclicity of GP(10,2) after deletion, by independent edge scans."""
    parent = list(range(N))

    def leader(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for a, b in EDGES:
        if deleted >> a & 1 or deleted >> b & 1:
            continue
        ra, rb = leader(a), leader(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return True


def is_forest_dfs(deleted):
    """Independent cycle test by DFS parent-edge detection."""
    remaining = {v for v in range(N) if not (deleted >> v & 1)}
    seen = set()
    for start in remaining:
        if start in seen:
            continue
        stack = [(start, -1)]
        seen.add(start)
        while stack:
            u, parent = stack.pop()
            for v in ADJ[u]:
                if v not in remaining or v == parent:
                    continue
                if v in seen:
                    return False
                seen.add(v)
                stack.append((v, u))
    return True


def masks(k):
    for c in combinations(range(N), k):
        yield sum(1 << x for x in c)


# Proof that size at most five is impossible: 30-3k+e(S) > 19-k.
assert all(30 - 3 * k > 19 - k for k in range(6))
C = [s for s in masks(6) if is_forest_union_find(s)]
assert len(C) == 2520
assert all(is_forest_dfs(s) for s in C)
assert sum(is_forest_dfs(s) for s in masks(6)) == len(C)

CNT = Counter(sum(int((s >> a & 1) and (s >> b & 1))
                  for a, b in EDGES) for s in C)
assert CNT == {0: 660, 1: 1860}

INDEX = {s: i for i, s in enumerate(C)}
ADJ_RECONF = []
for s in C:
    row = set()
    for a in range(N):
        if not (s >> a & 1):
            continue
        for b in range(N):
            if s >> b & 1:
                continue
            t = s ^ (1 << a) ^ (1 << b)
            if t in INDEX:
                row.add(INDEX[t])
    ADJ_RECONF.append(tuple(sorted(row)))
assert all(i in ADJ_RECONF[j] for i, adj in enumerate(ADJ_RECONF) for j in adj)
assert all(len(set(adj)) == len(adj) for adj in ADJ_RECONF)
assert sum(map(len, ADJ_RECONF)) // 2 == 23940

# Direct graph connectivity, distance/eccentricity, and Hamming-detour census.
counts = Counter()
excess = Counter()
eccentricity = Counter()
for source, a in enumerate(C):
    dist = [-1] * len(C)
    dist[source] = 0
    bfs = deque([source])
    while bfs:
        u = bfs.popleft()
        for v in ADJ_RECONF[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                bfs.append(v)
    assert all(d >= 0 for d in dist)
    eccentricity[max(dist)] += 1
    for j in range(source + 1, len(C)):
        d = dist[j]
        counts[d] += 1
        # Since every solution has six vertices, this equals |S - T|.
        hamming_exchange_bound = (a & ~C[j]).bit_count()
        assert d >= hamming_exchange_bound
        excess[d - hamming_exchange_bound] += 1
assert sum(counts.values()) == comb(len(C), 2)
assert counts == {1: 23940, 2: 162870, 3: 572230,
                  4: 1088390, 5: 993990, 6: 332520}
assert excess == {0: 3124960, 1: 48800, 2: 180}
assert eccentricity == {6: 2520}

print('GRAPH 20 vertices 30 edges; feedback vertex number 6')
print('MINIMUM_SETS', len(C), 'SPLIT_BY_INDUCED_EDGES', sorted(CNT.items()))
print('EXCHANGE_EDGES', sum(map(len, ADJ_RECONF)) // 2)
print('ALL_ECCENTRICITIES', sorted(eccentricity.items()))
print('UNORDERED_PAIR_DISTANCES', sorted(counts.items()))
print('UNORDERED_PAIR_HAMMING_EXCESS', sorted(excess.items()))
print('ALL_CHECKS_PASS')
