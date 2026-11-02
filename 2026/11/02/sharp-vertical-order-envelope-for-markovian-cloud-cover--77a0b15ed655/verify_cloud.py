#!/usr/bin/env python3
"""Exact checks for sharp Markov cloud-cover arrangement bounds.

Run with Python 3 standard library only: python3 verify_cloud.py
Finite enumeration confirms examples and computations; the proof for all n
is combinatorial and is given separately in RESULT.md.
"""
from fractions import Fraction as F
from itertools import permutations
from functools import reduce
from operator import mul


def product(items):
    return reduce(mul, items, F(1))


def overlap(a, b, alpha):
    return alpha * min(a, b) + (1 - alpha) * a * b


def markov_clear(seq, alpha):
    # Evaluate clear-column probability via conditional probabilities,
    # without using the odds-factorization being checked.
    clear = 1 - seq[0]
    for prev, now in zip(seq, seq[1:]):
        joint_clear = 1 - prev - now + overlap(prev, now, alpha)
        assert F(0) <= joint_clear <= min(1 - prev, 1 - now)
        clear *= joint_clear / (1 - prev)
    return clear


def factor_clear(seq, alpha):
    odds = [a / (1 - a) for a in seq]
    return product(1 - a for a in seq) * product(
        1 + alpha * min(x, y) for x, y in zip(odds, odds[1:])
    )


def sharp_bounds(seq, alpha):
    a = sorted(x / (1 - x) for x in seq)
    baseline = product(1 - x for x in seq)
    smallest = baseline * product(1 + alpha * a[k // 2] for k in range(len(seq) - 1))
    largest = baseline * product(1 + alpha * a[k] for k in range(len(seq) - 1))
    return smallest, largest


def alternating_order(seq):
    # Small fractions are interleaved among larger fractions, with the
    # largest sequence elements serving as separators.
    x = sorted(seq)
    n = len(x)
    m = n // 2 if n % 2 == 0 else (n - 1) // 2
    hi = x[m:]
    lo = x[:m]
    order = []
    for j in range(m):
        order.extend([hi[j], lo[j]])
    if len(hi) > m:
        order.append(hi[-1])
    assert sorted(order) == x
    return order


def run():
    checks = 0
    alphas = (F(0), F(1, 4), F(1, 2), F(1))
    for n in range(2, 9):
        # Strictly ordered exact rational profiles.
        profile = [F(i, n + 3) for i in range(1, n + 1)]
        for alpha in alphas:
            lo, hi = sharp_bounds(profile, alpha)
            sorted_profile = sorted(profile)
            alternating_profile = alternating_order(profile)
            assert markov_clear(sorted_profile, alpha) == hi
            assert markov_clear(alternating_profile, alpha) == lo
            checks += 2
            if alpha == 1:
                assert hi == 1 - max(profile)
                checks += 1
            for seq in permutations(profile):
                actual = markov_clear(seq, alpha)
                factored = factor_clear(seq, alpha)
                assert actual == factored
                assert lo <= actual <= hi
                checks += 2
    # The width of the sharp interval grows strictly with overlap weight
    # for strictly increasing profiles with at least three layers.
    for n in range(3, 9):
        profile = [F(i, n + 3) for i in range(1, n + 1)]
        widths = []
        for alpha in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            lo, hi = sharp_bounds(profile, alpha)
            widths.append(hi - lo)
        assert widths[0] == 0
        assert all(x < y for x, y in zip(widths, widths[1:]))
        checks += 5
    # Tie cases: exact bounds remain sharp without distinct cloud fractions.
    for profile in (
        [F(1, 5), F(1, 5), F(3, 5)],
        [F(1, 6), F(2, 6), F(2, 6), F(5, 6)],
        [F(1, 8)] * 5,
        [F(1, 10), F(1, 4), F(1, 4), F(3, 5), F(4, 5)],
    ):
        for alpha in alphas:
            lo, hi = sharp_bounds(profile, alpha)
            vals = {markov_clear(seq, alpha) for seq in set(permutations(profile))}
            assert min(vals) == lo and max(vals) == hi
            checks += 2
    # Independent four-layer example and exact 5.7 percentage-point gap.
    p = [F(1, 10), F(1, 5), F(2, 5), F(3, 5)]
    lo, hi = sharp_bounds(p, F(1, 2))
    assert hi == F(171, 625)
    assert lo == F(1083, 5000)
    assert 1 - hi == F(454, 625)
    assert 1 - lo == F(3917, 5000)
    assert hi - lo == F(57, 1000)
    checks += 5
    print(f'CHECKS_PASSED={checks}')
    print('CLOUD_MIN=454/625 CLOUD_MAX=3917/5000 GAP=57/1000')

if __name__ == '__main__':
    run()
