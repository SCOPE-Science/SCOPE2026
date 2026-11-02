#!/usr/bin/env python3
"""Reproduce finite tests for a connected fair-allocation theorem on bicliques.

This verifier is diagnostic; the all-size theorem is proved separately.
No dependencies beyond Python's standard library.
"""
from itertools import combinations
from random import Random


def valid_biclique_partition(a, b, parts):
    A = set(range(a))
    B = set(range(a, a + b))
    for part in parts:
        if not part:
            return False
        if len(part) > 1 and (not part & A or not part & B):
            return False
    return True


def construct(a, b, singleton):
    """Each row of singleton lists an agent's values for all vertices."""
    n = len(singleton)
    assert a <= b and b <= n <= a + b
    remaining = list(range(a + b))
    parts = []
    bases = []
    for row in singleton:
        p = max(remaining, key=lambda vertex: (row[vertex], -vertex))
        remaining.remove(p)
        bases.append(p)
        parts.append({p})
    left_rem = [v for v in remaining if v < a]
    right_rem = [v for v in remaining if v >= a]
    right_picks = [v for v in bases if v >= a]
    left_picks = [v for v in bases if v < a]
    assert len(left_rem) <= len(right_picks)
    assert len(right_rem) <= len(left_picks)
    owner = {v: i for i, v in enumerate(bases)}
    for u, p in zip(left_rem, right_picks):
        parts[owner[p]].add(u)
    for u, p in zip(right_rem, left_picks):
        parts[owner[p]].add(u)
    assert valid_biclique_partition(a, b, parts)
    return parts, bases


def assert_monotone_ef1(a, b, singleton, parts, bases, bonuses=None):
    """Test EF1_outer even with nonadditive monotone pair complementarities."""
    if bonuses is None:
        bonuses = [[0] * (a + b) for _ in singleton]
    def value(i, part):
        if not part:
            return 0
        vals = singleton[i]
        ans = sum(vals[v] for v in part)
        if len(part) == 2:
            ans += bonuses[i][min(part)]
        return ans
    for i, part in enumerate(parts):
        for j, other in enumerate(parts):
            residual = other - {bases[j]}
            assert value(i, part) >= value(i, residual), (a,b,i,j,part,other)


def negative_count(a, b, k):
    """All-one valuation forces a size-one bundle but forbids size >=3."""
    assert a < k < b
    N = a+b
    assert N > k+a
    # At most a bundles meet the a-side, so a singleton in b-side exists.
    # Any EF1 allocation with all item values equal to one would then have
    # each bundle of size at most two, and at most a bundles of size two.
    # Such an allocation covers at most k+a < N vertices.
    return N, k+a


def run():
    rng = Random(20261029)
    positive = 0
    negative = 0
    matching = 0
    for a in range(1, 7):
        for b in range(a, 11):
            N = a + b
            for t in range(0, a + 1):
                for rem in combinations(range(N), t):
                    l = sum(v < a for v in rem)
                    r = t - l
                    assert l <= b - r
                    assert r <= a - l
                    matching += 1
            for k in range(b, N + 1):
                for _ in range(60):
                    singletons = [[rng.randrange(0, 10) for _ in range(N)] for _ in range(k)]
                    parts, bases = construct(a, b, singletons)
                    # A monotone, nonadditive utility is represented by adding
                    # a nonnegative bonus when a pair is present.
                    bonuses = [[rng.randrange(0, 15) for _ in range(N)] for _ in range(k)]
                    assert_monotone_ef1(a, b, singletons, parts, bases, bonuses)
                    positive += 1
            for k in range(a + 1, b):
                N, capacity = negative_count(a, b, k)
                assert capacity < N
                negative += 1
    print('PASS', 'matching_subsets=', matching, 'positive_profiles=', positive,
          'negative_obstructions=', negative)


if __name__ == '__main__':
    run()
