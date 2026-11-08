#!/usr/bin/env python3
"""Exact arithmetic checks for vertex-uniform harmonic-polytope covariance.

Run: python3 artifacts/verify.py
Only the accompanying symbolic argument proves the full infinite family.
"""
from fractions import Fraction
from itertools import permutations


def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def closed(n):
    h = harmonic(n)
    v = Fraction(n*n - 1, 12) + 1 + Fraction(2, n) - Fraction(1, n*n) - 2/h
    c = Fraction((3*n - 1)*(n + 2), 2*n*n) - Fraction(n + 11, 4)/h
    return v, c


def enumeration(n):
    # First permutation is a rank-to-label map; sig[j] gives second rank
    # of the label occupying first rank j+1.
    d = 2*n
    count = 0
    moments = [0]*d
    gram = [[0]*d for _ in range(d)]
    for pi in permutations(range(n)):
        for sig in permutations(range(1, n+1)):
            max_right = 0
            for j in reversed(range(n)):
                if sig[j] <= max_right:
                    continue
                max_right = sig[j]
                mark = pi[j]
                r = [0]*n
                s = [0]*n
                for rank, label in enumerate(pi, 1):
                    r[label] = rank
                    s[label] = sig[rank-1]
                vec = r + s
                vec[mark] += 1
                vec[n+mark] += 1
                count += 1
                for a in range(d):
                    moments[a] += vec[a]
                    for b in range(d):
                        gram[a][b] += vec[a]*vec[b]
    return count, moments, gram


def check():
    enumerated = 0
    for n in range(2, 6):
        count, mom, gram = enumeration(n)
        expected = int(sum(Fraction(1, j) for j in range(1, n+1)) * __import__('math').factorial(n)**2)
        assert count == expected, (n, count, expected)
        mu = Fraction(n+1,2) + Fraction(1,n)
        assert all(Fraction(k,count) == mu for k in mom)
        var, cross = closed(n)
        for a in range(2*n):
            for b in range(2*n):
                actual = Fraction(gram[a][b],count)-mu*mu
                rowa, ia = divmod(a,n)
                rowb, ib = divmod(b,n)
                expected_cov = (var if rowa == rowb else cross) * (1 if ia == ib else -Fraction(1,n-1))
                assert actual == expected_cov, (n,a,b,actual,expected_cov)
        enumerated += count
    for n in range(2, 301):
        v,c = closed(n)
        lambdas = [Fraction(n,n-1)*(v+c), Fraction(n,n-1)*(v-c)]
        assert min(lambdas)>0
        assert (c>0 if n<=8 else c<0), (n,c)
    assert closed(8)[1] == Fraction(2395, 48704)
    assert closed(9)[1] == -Fraction(1153,577449)
    print(f'HARMONIC_COVARIANCE_CHECKS_PASSED vertices={enumerated} profiles=299')

if __name__ == '__main__':
    check()
