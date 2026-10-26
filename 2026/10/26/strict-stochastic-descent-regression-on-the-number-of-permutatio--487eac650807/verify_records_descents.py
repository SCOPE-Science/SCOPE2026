#!/usr/bin/env python3
"""Exact arithmetic tests for conditional descent/record ordering in uniform permutations."""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial


def counts_by_insertion(limit):
    joint = {(0, 1): 1}
    for n in range(1, limit + 1):
        if n > 1:
            nxt = defaultdict(int)
            for (d, r), c in joint.items():
                nxt[(d, r + 1)] += c
                nxt[(d, r)] += d * c
                nxt[(d + 1, r)] += (n - 1 - d) * c
            joint = {key: value for key, value in nxt.items() if value}
        yield n, joint


def direct_joint(n):
    out = defaultdict(int)
    for p in permutations(range(1, n + 1)):
        d = sum(a > b for a, b in zip(p, p[1:]))
        current, r = 0, 0
        for x in p:
            if x > current:
                current, r = x, r + 1
        out[d, r] += 1
    return dict(out)


def run():
    comparisons = 0
    for n, joint in counts_by_insertion(48):
        assert sum(joint.values()) == factorial(n)
        if n <= 8:
            assert direct_joint(n) == joint
        totals = {r: sum(c for (d, s), c in joint.items() if s == r) for r in range(1, n + 1)}
        assert all(totals.values())
        for r in range(1, n):
            a, b = totals[r], totals[r + 1]
            strict = False
            for h in range(n):
                upper = Fraction(sum(c for (d, s), c in joint.items() if s == r and d >= h), a)
                lower = Fraction(sum(c for (d, s), c in joint.items() if s == r + 1 and d >= h), b)
                assert upper >= lower, (n, r, h, upper, lower)
                strict |= upper > lower
                comparisons += 1
            assert strict
        eD = Fraction(sum(d * c for (d, r), c in joint.items()), factorial(n))
        eR = Fraction(sum(r * c for (d, r), c in joint.items()), factorial(n))
        edr = Fraction(sum(d * r * c for (d, r), c in joint.items()), factorial(n))
        assert edr - eD * eR == -Fraction(n - 1, 2 * n)
        assert eD == Fraction(n - 1, 2)
    print('PASS: exact insertion recurrence, exhaustive permutation comparisons n<=8,')
    print(f'  {comparisons} exact stochastic tail inequalities for n<=48,')
    print('  strict adjacent conditioned orders and closed covariance formula n<=48.')


if __name__ == '__main__':
    run()
