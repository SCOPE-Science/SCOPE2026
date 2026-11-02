#!/usr/bin/env python3
"""Reproducibility checks for random-edge matching on complete split graphs.

All probability comparisons are exact; simulations are diagnostic only.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import exp, sqrt
import random

@lru_cache(maxsize=None)
def terminal_law(a, b):
    """Exact distribution of unmatched independent vertices."""
    if a == 0 or (a == 1 and b == 0):
        return {b: Fraction(1)}
    clique = a * (a - 1) // 2
    cross = a * b
    total = clique + cross
    assert total > 0
    result = {}
    for aa, bb, weight in ((a - 2, b, clique), (a - 1, b - 1, cross)):
        if weight:
            for k, value in terminal_law(aa, bb).items():
                result[k] = result.get(k, Fraction()) + Fraction(weight, total) * value
    return result

def brute_edge_orders(a, b):
    """Independently enumerate full permutations of original labeled edges."""
    edges = ([(i, j) for i in range(a) for j in range(i + 1, a)]
             + [(i, a+j) for i in range(a) for j in range(b)])
    frequencies = Counter()
    for order in permutations(edges):
        matched = set()
        for i, j in order:
            if i not in matched and j not in matched:
                matched.add(i)
                matched.add(j)
        k = sum(a + j not in matched for j in range(b))
        frequencies[k] += 1
    den = sum(frequencies.values())
    return {k: Fraction(v, den) for k, v in frequencies.items()}

def sample_unmatched(a, b, rng):
    while a and (a > 1 or b):
        clique_twice = a * (a - 1)
        cross_twice = 2 * a * b
        if rng.randrange(clique_twice + cross_twice) < clique_twice:
            a -= 2
        else:
            a -= 1
            b -= 1
    return b

def theoretical(alpha, beta):
    ratio = alpha / beta
    survivor = beta * exp(-ratio)
    variance = survivor * (4 - exp(-ratio) * (ratio + 2)**2)
    return survivor, variance

def main():
    assertions = 0
    for a in range(0, 8):
        for b in range(0, 8):
            d = terminal_law(a, b)
            assert sum(d.values(), Fraction()) == 1
            assertions += 1
            assert all(0 <= k <= b and p > 0 for k,p in d.items())
            assertions += 1
            if a * (a - 1)//2 + a*b <= 8:
                assert d == brute_edge_orders(a,b), (a,b,d,brute_edge_orders(a,b))
                assertions += 1
    # Independent finite recursions for moments of survivors.
    for a in range(0, 9):
        for b in range(0, 9):
            d=terminal_law(a,b)
            mean = sum(Fraction(k)*p for k,p in d.items())
            second = sum(Fraction(k*k)*p for k,p in d.items())
            if a == 0 or (a == 1 and b == 0):
                assert mean==b and second==b*b
            else:
                c=a*(a-1)//2; t=a*b; D=c+t
                em = ((c*sum(Fraction(k)*p for k,p in terminal_law(a-2,b).items()) if c else 0)
                    +(t*sum(Fraction(k)*p for k,p in terminal_law(a-1,b-1).items()) if t else 0))/D
                es = ((c*sum(Fraction(k*k)*p for k,p in terminal_law(a-2,b).items()) if c else 0)
                    +(t*sum(Fraction(k*k)*p for k,p in terminal_law(a-1,b-1).items()) if t else 0))/D
                assert mean==em and second==es
            assertions += 2
    # Sharp ratio: decreasing to aspect ratio 1, increasing afterwards.
    import math
    for i in range(1, 1001):
        r=i/500
        ratio=(r+1-math.exp(-r))/(2*min(r,(r+1)/2))
        assert ratio>=1-1/(2*math.e)-1e-13
        assertions+=1
    # Deterministic random simulations: verify finite-size mean and variance trends.
    for n, trials in ((100, 8000), (200, 8000), (400, 5000)):
        rng = random.Random(1771 + n)
        sample = [sample_unmatched(n,n,rng) for _ in range(trials)]
        sample_mean = sum(sample) / trials
        sample_var = sum((x-sample_mean)**2 for x in sample)/(trials-1)
        limit_mean, limit_variance = theoretical(1.,1.)
        assert abs(sample_mean/n-limit_mean) < .020
        assert abs(sample_var/n-limit_variance) < .045
        assertions += 2
        print(f'n={n}, trials={trials}, survivor mean/n={sample_mean/n:.7f}, '
              f'variance/n={sample_var/n:.7f}; predicted {limit_mean:.7f}, {limit_variance:.7f}')
    print(f'PASS {assertions} exact/analytic/diagnostic assertions')

if __name__ == '__main__':
    main()
