"""Exact independent finite cross-check for the square-leg counting formulas.

Uses ordinary Euclid parameters and independent quartic parameterizations.
It does not certify the asymptotic or the classical descent theorem.
"""
from math import gcd, isqrt

BOUNDS = (100, 1000, 10000, 100000, 1000000, 10000000)


def via_euclid(limit):
    odd, even = set(), set()
    for m in range(2, isqrt(limit) + 1):
        for n in range(1, m):
            c = m*m + n*n
            if c > limit or gcd(m, n) != 1 or ((m - n) % 2 == 0):
                continue
            a, b = m*m - n*n, 2*m*n
            t = (a, b, c)
            if isqrt(a)**2 == a:
                odd.add(t)
            if isqrt(b)**2 == b:
                even.add(t)
    return odd, even


def via_quartics(limit):
    odd, even = set(), set()
    u = 1
    while u**4 < 2*limit:
        v = u + 2
        while u**4 + v**4 <= 2*limit:
            if gcd(u, v) == 1:
                m = (u*u + v*v)//2
                n = (v*v - u*u)//2
                odd.add((m*m-n*n, 2*m*n, m*m+n*n))
            v += 2
        u += 2

    u = 1
    while 4*u**4 < limit:
        v = 1
        while 4*u**4 + v**4 <= limit:
            if gcd(u, v) == 1:
                m = max(2*u*u, v*v)
                n = min(2*u*u, v*v)
                even.add((m*m-n*n, 2*m*n, m*m+n*n))
            v += 2
        u += 1
    return odd, even


def main():
    for X in BOUNDS:
        a, b = via_euclid(X)
        qa, qb = via_quartics(X)
        assert a == qa, (X, 'odd', a ^ qa)
        assert b == qb, (X, 'even', b ^ qb)
        assert not a.intersection(b), (X, 'overlap')
        for p in a | b:
            x, y, z = p
            assert x*x+y*y == z*z and gcd(x, y) == 1 and z <= X
        print(f'X={X} odd={len(a)} even={len(b)} total={len(a|b)}')
    print('SQUARE_LEG_EXACT_REGRESSION_OK 6 bounds, both parametrizations, independent Euclid classification')

if __name__ == '__main__':
    main()
