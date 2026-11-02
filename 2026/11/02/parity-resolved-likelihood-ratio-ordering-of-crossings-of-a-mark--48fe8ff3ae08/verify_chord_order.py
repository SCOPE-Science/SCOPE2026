#!/usr/bin/env python3
"""Exact tests for the parity-resolved chord-crossing likelihood-ratio law.

No external dependencies. Run: python3 chord_lr_verify.py
"""
from collections import Counter
from fractions import Fraction
from math import factorial

checks = 0

def ok(assertion, message):
    global checks
    checks += 1
    if not assertion:
        raise AssertionError(message)


def double_factorial_odd(k):
    if k <= 0:
        return 1
    z = 1
    for j in range(1, k + 1, 2):
        z *= j
    return z


def law(n, a):
    """Exact probability mass on the number of chords crossing a prescribed chord."""
    N = 2*n - 2
    b = N - a
    den = double_factorial_odd(N-1)
    d = {}
    for x in range(a % 2, a + 1, 2):
        if x > b:
            continue
        numerator = factorial(a)*factorial(b)
        denominator = (factorial(x)*2**(n - 1 - x)*
                       factorial((a-x)//2)*factorial((b-x)//2))
        ok(numerator % denominator == 0, ('integral count', n, a, x))
        d[x] = Fraction(numerator // denominator, den)
    ok(sum(d.values()) == 1, ('normalized', n, a, d))
    return d


def matchings(remaining):
    if not remaining:
        yield ()
        return
    u, *tail = remaining
    for i, v in enumerate(tail):
        for rest in matchings(tail[:i] + tail[i+1:]):
            yield ((u, v),) + rest


# Independent matching enumeration with a fixed chord removed.
for n in range(3, 9):
    remaining = list(range(2, 2*n))
    counts = [Counter() for _ in range(n)]
    total = 0
    for matching in matchings(remaining):
        total += 1
        for a in range(n):
            cutoff = a + 2
            x = sum((u < cutoff) != (v < cutoff) for u, v in matching)
            counts[a][x] += 1
    ok(total == double_factorial_odd(2*n-3), ('matching count', n))
    for a, hist in enumerate(counts):
        p = law(n, a)
        ok(set(hist) == set(p), ('support', n, a))
        for x, value in hist.items():
            ok(Fraction(value, total) == p[x], ('count identity', n, a, x))

# Analytic identities and all conditional tail comparisons, exact rational arithmetic.
for n in range(3, 65):
    N = 2*n - 2
    distributions = [law(n, a) for a in range(n)]
    for a in range(n):
        p = distributions[a]
        mean = sum(x*v for x, v in p.items())
        ok(mean == Fraction(a*(N-a), N-1), ('mean', n, a))
        if n >= 4:
            var = sum((x-mean)**2*v for x, v in p.items())
            predicted = Fraction(2*a*(N-a)*(a-1)*(N-a-1), (N-3)*(N-1)**2)
            ok(var == predicted, ('variance', n, a))
    for a in range(n-2):
        b = N-a
        low = distributions[a]
        high = distributions[a+2]
        observed_ratios = []
        for x in sorted(low):
            ratio = high[x]/low[x]
            expected = Fraction((a+2)*(a+1)*(b-x), b*(b-1)*(a+2-x))
            ok(ratio == expected, ('ratio', n, a, x))
            difference_sign = (ratio > 1) - (ratio < 1)
            expected_sign = ((2*n-1)*x > b*(a+2)) - ((2*n-1)*x < b*(a+2))
            ok(difference_sign == expected_sign, ('sign boundary', n, a, x))
            observed_ratios.append(ratio)
        ok(all(u < v for u, v in zip(observed_ratios, observed_ratios[1:])),
           ('strict likelihood-ratio', n, a))
        ok(a+2 in high and a+2 not in low, ('new upper atom', n, a))
        for threshold in range(a % 2 + 1, a+3):
            lt = sum(v for x,v in low.items() if x >= threshold)
            ht = sum(v for x,v in high.items() if x >= threshold)
            ok(ht > lt, ('strict upper-tail dominance', n, a, threshold))

# The smallest nontrivial adjacent-span comparison fails even first-order dominance.
for n in range(3, 25):
    p1 = law(n, 1)
    p2 = law(n, 2)
    ok(p1 == {1: Fraction(1)}, ('length one deterministic', n))
    ok(p2[0] > 0 and p2[2] > 0, ('adjacent-span crossing', n))
print('PASS:', checks, 'independent exact assertions')
