#!/usr/bin/env python3
"""Finite checks for colored equal-size equivalence-class probability formulas.

The infinite first-order convergence theorem uses a mathematical EF proof;
these checks verify only its finite probability and profile enumerations.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, exp


def exact_probability(s, c, j):
    p = Fraction(comb(s,j), 2**s) if j <= s else Fraction(0)
    return 1 - (1 - p)**c


def enumerate_probability(s, c, j):
    success = 0
    total = 2**(s*c)
    profiles = Counter()
    for bits in product((0,1), repeat=s*c):
        red = [sum(bits[k*s:(k+1)*s]) for k in range(c)]
        success += j in red
        profiles[tuple(Counter(red).get(t,0) for t in range(s+1))] += 1
    assert sum(profiles.values()) == total
    return Fraction(success, total)


def multinomial_class_profile(s,c):
    # Independent blocks' generating polynomial, exact rational counts.
    dp = {tuple(0 for _ in range(s+1)): 1}
    for _ in range(c):
        next_dp = Counter()
        for counts,weight in dp.items():
            for j in range(s+1):
                arr = list(counts); arr[j] += 1
                next_dp[tuple(arr)] += weight*comb(s,j)
        dp = next_dp
    assert sum(dp.values()) == 2**(s*c)
    return dp


def verify():
    for s,c in ((1,1),(2,2),(3,2),(3,3),(4,2)):
        for j in range(s+1):
            assert enumerate_probability(s,c,j) == exact_probability(s,c,j)
        direct = Counter()
        for bits in product((0,1), repeat=s*c):
            red = [sum(bits[k*s:(k+1)*s]) for k in range(c)]
            direct[tuple(Counter(red).get(t,0) for t in range(s+1))] += 1
        assert dict(direct) == dict(multinomial_class_profile(s,c))
    # Critical example: j=0 and c=2**s gives expected count 1.
    for s in (8,12,16):
        c = 2**s
        prob = float(exact_probability(s,c,0))
        assert abs(prob - (1-exp(-1))) < 0.003
        assert c * Fraction(comb(s,0),2**s) == 1
    # Adjacent rare-profile means diverge by (s-j)/(j+1).
    for s in range(3,22):
        for j in range(s):
            for c in (1,3,100):
                x = Fraction(c*comb(s,j),2**s)
                y = Fraction(c*comb(s,j+1),2**s)
                assert y / x == Fraction(s-j,j+1)
    print('EQUIVALENCE_COLOR_LIMIT_LAW_VERIFY_OK')

if __name__ == '__main__':
    verify()
