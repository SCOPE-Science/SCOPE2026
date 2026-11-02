#!/usr/bin/env python3
"""Self-contained finite verification of Kneser convexity shattering formulas.

The universal assertions are proved in RESULT.md; this script independently
checks small graphs from graph distances and exhaustively enumerates all
hypotheses and traces for the two exceptional orders.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb, factorial


def graph_data(n):
    vertices = list(combinations(range(n), 2))
    N = len(vertices)
    edges = [set(pair) for pair in vertices]
    adjacent = [[int(not edges[i].intersection(edges[j])) for j in range(N)]
                for i in range(N)]
    for i in range(N):
        adjacent[i][i] = 0
    distances = []
    for root in range(N):
        dist = [-1] * N
        dist[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for v in range(N):
                if adjacent[u][v] and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        assert min(dist) >= 0
        distances.append(dist)
    # Geodesic intervals are reconstructed independently of special formulas.
    intervals = {}
    for a, b in combinations(range(N), 2):
        intervals[a, b] = sum(
            1 << z for z in range(N)
            if distances[a][z] + distances[z][b] == distances[a][b]
        )
    return vertices, edges, distances, intervals


def closure(seed, intervals, N):
    S = seed
    while True:
        next_S = S
        for (a, b), req in intervals.items():
            if S & (1 << a) and S & (1 << b):
                next_S |= req
        if next_S == S:
            return S
        S = next_S


def convex_masks(intervals, N):
    full = (1 << N) - 1
    return [S for S in range(1 << N) if all(
        not(S & (1 << a) and S & (1 << b)) or not(req & (full ^ S))
        for (a, b), req in intervals.items()
    )]


def is_matching(S, edges):
    selected = [i for i in range(len(edges)) if (S >> i) & 1]
    return all(not(edges[a] & edges[b]) for a, b in combinations(selected, 2))


def is_partition_hypothesis(S, edges):
    n = len(set.union(*edges))
    assert n == 6
    for A in combinations(range(n), 3):
        A = set(A)
        expected = sum(1 << i for i, e in enumerate(edges)
                       if e.issubset(A) or e.isdisjoint(A))
        if S == expected:
            return True
    return False


def support_profile(hypotheses, N):
    max_k = len(hypotheses).bit_length() - 1
    result = Counter()
    shattered = {}
    for k in range(max_k + 1):
        for indices in combinations(range(N), k):
            S = sum(1 << i for i in indices)
            traces = {h & S for h in hypotheses}
            if len(traces) == 1 << k:
                result[k] += 1
                shattered.setdefault(k, []).append(indices)
    return result, shattered


def run():
    expected = {
        5: ({0: 1, 1: 10, 2: 45, 3: 90, 4: 15}, 79),
        6: ({0: 1, 1: 15, 2: 105, 3: 255}, 87),
    }
    for n in (5, 6):
        vertices, edges, distances, intervals = graph_data(n)
        N = len(vertices)
        assert set(d for row in distances for d in row) == {0, 1, 2}
        C = convex_masks(intervals, N)
        assert len(C) == expected[n][1]
        profile, sets = support_profile(C, N)
        assert dict(profile) == expected[n][0], (n, profile)
        # A second implementation of intervals uses the Kneser diameter-two rule.
        for (a, b), I in intervals.items():
            direct = (1 << a) | (1 << b)
            if edges[a] & edges[b]:
                direct |= sum(1 << z for z in range(N)
                              if not(edges[a] & edges[z])
                              and not(edges[b] & edges[z]))
            assert direct == I
        if n == 5:
            # Exactly the four-edge cycles on four of the five ground points.
            all_four_cycles = set()
            for omit in range(5):
                four = set(range(5)) - {omit}
                for diagonal in combinations(sorted(four), 2):
                    other = tuple(sorted(four - set(diagonal)))
                    diag = {frozenset(diagonal), frozenset(other)}
                    cycle = frozenset(i for i, e in enumerate(edges)
                                      if e.issubset(four) and frozenset(e) not in diag)
                    all_four_cycles.add(cycle)
            actual = set(frozenset(s) for s in sets[4])
            assert len(actual) == len(all_four_cycles) == 15
            assert actual == all_four_cycles
        if n == 6:
            all_mask = (1 << N) - 1
            predicted = {s for s in range(1 << N)
                         if is_matching(s, edges) or
                         is_partition_hypothesis(s, edges) or s == all_mask}
            assert set(C) == predicted
            expected_bad_triples = set()
            for A in combinations(range(6), 3):
                A = set(A)
                tube = tuple(i for i,e in enumerate(edges)
                             if e.issubset(A) or e.isdisjoint(A))
                expected_bad_triples.update(combinations(tube, 3))
            actual_bad = set(combinations(range(N), 3)) - set(sets[3])
            assert len(actual_bad) == 200
            assert actual_bad == expected_bad_triples
        print('EXCEPTIONAL_ORDER_PASS n=%d vertices=%d convex=%d shattering=%s' %
              (n, N, len(C), dict(sorted(profile.items()))))
    for n in (7, 8, 9):
        vertices, edges, distances, intervals = graph_data(n)
        N = len(vertices)
        full = (1 << N) - 1
        for (a, b) in intervals:
            if edges[a] & edges[b]:
                assert closure((1 << a) | (1 << b), intervals, N) == full
        match_counts = [factorial(n) // (2**k * factorial(k) * factorial(n - 2*k))
                        for k in range(n//2 + 1)]
        assert match_counts[1] == comb(n, 2)
        print('STABLE_PAIR_HULL_PASS n=%d pairs=%d matchings=%d' %
              (n, sum(bool(edges[a]&edges[b]) for a,b in intervals), sum(match_counts)))
    print('ALL_RANK_TWO_KNESER_SHATTERING_CHECKS_PASS')


if __name__ == '__main__':
    run()
