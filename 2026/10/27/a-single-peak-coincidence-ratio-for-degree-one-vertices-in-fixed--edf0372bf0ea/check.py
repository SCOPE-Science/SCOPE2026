#!/usr/bin/env python3
"""Exact integer checks for degree-one coincidence in the fixed-edge graph model.

Requires only Python's standard library. Run: python3 check.py
Finite checks corroborate, but do not replace, the analytic all-order proof.
"""
from fractions import Fraction
from math import comb
from itertools import combinations


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def probabilities(n, m):
    N = n * (n - 1) // 2
    a = (n - 1) * (n - 2) // 2
    b = (n - 2) * (n - 3) // 2
    den = C(N, m)
    p = Fraction((n - 1) * C(a, m - 1), den)
    q = Fraction(C(b, m - 1) + (n - 2)**2 * C(b, m - 2), den)
    return p, q


def ratio(n, m):
    p, q = probabilities(n, m)
    return q / (p * p)


def step(n, m):
    N = n * (n - 1) // 2
    k = n - 2
    t = N - m
    b = Fraction(k*k + k - 4, 2)
    a = k*k - 1
    l = a*m-b
    return (Fraction(m, m+1) * Fraction(t*(t-2*k+1),(t-k)**2)
            * Fraction(l+a,l))


def brute_probabilities(n, m):
    edges = list(combinations(range(n), 2))
    total = both = first = 0
    for subset in combinations(edges, m):
        d0 = sum(0 in edge for edge in subset)
        d1 = sum(1 in edge for edge in subset)
        first += int(d0 == 1)
        both += int(d0 == 1 and d1 == 1)
        total += 1
    return Fraction(first,total),Fraction(both,total)


def run():
    assertions = 0
    for n in range(4, 7):
        N = n*(n-1)//2
        for m in range(N+1):
            assert probabilities(n,m)==brute_probabilities(n,m)
            assertions+=1
    for n in range(6, 33):
        b=(n-2)*(n-3)//2
        peak=(n+1)//2
        values=[ratio(n,m) for m in range(1,b+3)]
        assert max(values)==values[peak-1]
        assert values.count(max(values))==1
        assertions+=2
        for m in range(1,b+2):
            assert values[m]/values[m-1]==step(n,m)
            assertions+=1
            if m < peak:
                assert values[m]>values[m-1]
            else:
                assert values[m]<values[m-1]
            assertions+=1
        for m in range(2,b+2):
            assert values[m-1]**2 > values[m-2]*values[m]
            assertions+=1
    n=8
    for m,expect in [(3,Fraction(-95,21294)),(4,Fraction(29,342225)),(5,Fraction(-113,97344))]:
        p,q=probabilities(n,m)
        assert q-p*p==expect
        assertions+=1
    print(f'PASS: {assertions} exact integer/rational assertions')

if __name__=='__main__':
    run()
