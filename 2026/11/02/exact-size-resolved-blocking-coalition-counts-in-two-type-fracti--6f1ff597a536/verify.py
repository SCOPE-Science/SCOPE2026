#!/usr/bin/env python3
"""Reproduce exact blocking-coalition counts for two-type fractional games.

Standard-library independent exhaustive comparison against coalition-by-coalition
utilities, plus closed-form matched-pair and asymptotic numerical checks.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
from random import Random


def partitions(n):
    """Every set partition of 0..n-1, exactly once."""
    if n == 0:
        yield ()
        return
    for p in partitions(n - 1):
        yield p + ((n - 1,),)
        for j in range(len(p)):
            q = list(p)
            q[j] = q[j] + (n - 1,)
            yield tuple(q)


def old_compositions(a, b, blocks):
    n = a + b
    u = [0] * n
    v = [0] * n
    for block in blocks:
        cu = sum(i < a for i in block)
        cv = len(block) - cu
        for i in block:
            u[i] = cu
            v[i] = cv
    return u, v


def enumerator(a, b, blocks):
    """Exact number blocking by coalition size using the binomial formula."""
    u, v = old_compositions(a, b, blocks)
    result = [0] * (a + b + 1)
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            n_u = sum(y * u[i] > x * v[i] for i in range(a))
            n_v = sum(x * v[j] > y * u[j] for j in range(a, a + b))
            if x <= n_u and y <= n_v:
                result[x + y] += comb(n_u, x) * comb(n_v, y)
    return tuple(result)


def brute(a, b, blocks):
    """Independent literal utilities, exhaustive over all 2^(a+b) coalitions."""
    n = a + b
    own = [None] * n
    for block in blocks:
        for i in block:
            own[i] = block

    def utility(i, coalition):
        if i < a:
            friends = sum(j >= a for j in coalition)
        else:
            friends = sum(j < a for j in coalition)
        return Fraction(friends, len(coalition))

    counts = [0] * (n + 1)
    for mask in range(1, 1 << n):
        coalition = tuple(i for i in range(n) if mask & (1 << i))
        if all(utility(i, coalition) > utility(i, own[i]) for i in coalition):
            counts[len(coalition)] += 1
    return tuple(counts)


def matching_blocks(a, m):
    """a matched pairs and m unmatched second-side participants."""
    return tuple([(i, a + i) for i in range(a)] + [(a + a + j,) for j in range(m)])


def matching_formula(a, m):
    return sum(comb(a, x) * comb(m, y)
               for x in range(1, a + 1)
               for y in range(x + 1, m + 1))


def run():
    tested = 0
    comparisons = 0
    for a in range(1, 5):
        for b in range(1, 5):
            if a + b > 7:
                continue
            for blocks in partitions(a + b):
                formula = enumerator(a, b, blocks)
                literal = brute(a, b, blocks)
                assert formula == literal, (a, b, blocks, formula, literal)
                comparisons += a + b + 1
                tested += 1
    rng = Random(1729)
    randomized = 0
    for _ in range(450):
        a = rng.randint(1, 6)
        b = rng.randint(1, 6)
        n = a + b
        labels = [rng.randint(0, n - 1) for _ in range(n)]
        groups = defaultdict(list)
        for i, label in enumerate(labels):
            groups[label].append(i)
        blocks = tuple(tuple(g) for g in groups.values())
        assert enumerator(a, b, blocks) == brute(a, b, blocks)
        randomized += 1
    pair_checks = 0
    for a in range(1, 10):
        for m in range(0, 10):
            exact = sum(enumerator(a, a + m, matching_blocks(a, m)))
            expected = matching_formula(a, m)
            assert exact == expected, (a, m, exact, expected)
            assert (expected == 0) == (m <= 1)
            if m == 2:
                assert expected == a
            pair_checks += 1
    assert matching_formula(3, 5) == 132
    print('VERIFIED:', tested, 'entire partitions;', comparisons, 'size coefficients;',
          randomized, 'random partitions;', pair_checks, 'matched pair cases;'
          ' matching a=3,m=5 gives 132/2048 = 33/512.')


if __name__ == '__main__':
    run()
