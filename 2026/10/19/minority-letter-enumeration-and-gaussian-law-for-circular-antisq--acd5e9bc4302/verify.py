#!/usr/bin/env python3
"""Finite independent tests of circular antisquare avoidance and its enumerator.

Only standard-library Python is required. These finite tests support, but do not
replace, the mathematical proof for all lengths.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def contains_forbidden_antisquare_cyclic(word):
    """For a word of period n, it is enough to check orders 2..max(n,3)."""
    n = len(word)
    for k in range(2, max(n, 3) + 1):
        for start in range(n):
            if all(word[(start + j) % n] != word[(start + j + k) % n]
                   for j in range(k)):
                return True
    return False


def count_formula(n, k):
    if k == 0:
        return 2
    result = Fraction(0)
    for r in range(k // 2 + 1):
        large = k - r
        spare = n - 4 * k + 2 * r
        if spare < 0:
            continue
        result += Fraction(2 * n * comb(large, r) *
                           comb(spare + large - 1, large - 1), large)
    assert result.denominator == 1
    return result.numerator


def polynomial_coefficients(N):
    # F(z,u)=1-z-u*z^4-u^2*z^6;
    # coefficients of -2*z*F_z/F through z^N.
    a = [[0] * (N // 2 + 1) for _ in range(N + 1)]
    for n in range(1, N + 1):
        for k in range(N // 2 + 1):
            v = 2 if (n, k) == (1, 0) else 0
            if (n, k) == (4, 1):
                v += 8
            if (n, k) == (6, 2):
                v += 12
            if n >= 2:
                v += a[n - 1][k]
            if n >= 4 and k >= 1:
                v += a[n - 4][k - 1]
            if n >= 6 and k >= 2:
                v += a[n - 6][k - 2]
            a[n][k] = v
    return a


def verify():
    N = 19
    a = polynomial_coefficients(N)
    for n in range(1, N + 1):
        for k in range(N // 2 + 1):
            assert a[n][k] == count_formula(n, k), (n, k, a[n][k], count_formula(n, k))
    print('Exact generating-function/closed-sum coefficients agree through n=19')

    for n in range(1, 16):
        count = Counter()
        for bits in product((0, 1), repeat=n):
            if not contains_forbidden_antisquare_cyclic(bits):
                count[min(sum(bits), n - sum(bits))] += 1
        predicted = Counter({k: a[n][k] for k in range(n // 2 + 1) if a[n][k]})
        assert count == predicted, (n, count, predicted)
        if n <= 12:
            print('n=', n, ' counts=', sorted(count.items()))
    print('Independent cyclic antisquare enumeration agrees through n=15')

    # At n=6m, the maximal minority count is 2m and has 12 realizations.
    for m in range(1, 20):
        n = 6 * m
        assert count_formula(n, 2 * m) == 12
        assert count_formula(n, 2 * m + 1) == 0
    print('Maximal-minority rigidity checked for n=6..114')

    # Rigorous interval enclosure for the pole and positive variance rate.
    # Operations below use exact fractions with outward bounds; no floating point.
    from fractions import Fraction as Q
    def add(X, Y): return (X[0]+Y[0], X[1]+Y[1])
    def neg(X): return (-X[1], -X[0])
    def mul(X,Y):
        P = [x*y for x in X for y in Y]
        return (min(P), max(P))
    def inv(X):
        assert X[0]*X[1]>0
        return (1/X[1],1/X[0])
    def div(X,Y): return mul(X,inv(Y))
    def sc(a): return (Q(a),Q(a))
    def pw(X,n):
        assert n>=0
        out=sc(1)
        for _ in range(n):out=mul(out,X)
        return out
    lo,hi=Q(682327803828,10**12),Q(682327803829,10**12)
    F=lambda t:1-t-t**4-t**6
    assert F(lo)>0>F(hi)
    R=(lo,hi)
    A=add(sc(1),add(mul(sc(4),pw(R,3)),mul(sc(6),pw(R,5))))
    rp=neg(div(add(pw(R,4),mul(sc(2),pw(R,6))),A))
    Fzz=neg(add(mul(sc(12),pw(R,2)),mul(sc(30),pw(R,4))))
    Fzu=neg(add(mul(sc(4),pw(R,3)),mul(sc(12),pw(R,5))))
    Fuu=neg(mul(sc(2),pw(R,6)))
    rpp=div(add(add(mul(Fzz,pw(rp,2)),mul(sc(2),mul(Fzu,rp))),Fuu),A)
    mu=neg(div(rp,R))
    sigma2=add(add(mu,pw(mu,2)),neg(div(rpp,R)))
    assert mu[0] > Q(19,100) and mu[1] < Q(20,100)
    assert sigma2[0] > Q(49,1000) and sigma2[1] < Q(51,1000)
    print('Exact rational interval: rho in [0.682327803828,0.682327803829]')
    print('Certified: 0.19 < mean density < 0.20 and 0.049 < variance rate < 0.051')
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    verify()
