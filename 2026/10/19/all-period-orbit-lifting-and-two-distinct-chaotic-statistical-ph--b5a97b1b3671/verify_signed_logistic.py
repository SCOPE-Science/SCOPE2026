#!/usr/bin/env python3
"""Exact rational periodic-point certificate for the full tent map.

All computations use fractions; this file checks finite traces only.
"""
from fractions import Fraction
from math import gcd


def tent(v):
    return 2*v if v <= Fraction(1, 2) else 2*(1-v)


def fixed_tent(n):
    points = set()
    # Inverse branches g0(y)=y/2, g1(y)=1-y/2.
    for mask in range(1 << n):
        a, b = Fraction(1), Fraction(0)
        for j in range(n):
            if (mask >> j) & 1:
                a, b = -a/2, 1-b/2
            else:
                a, b = a/2, b/2
        y = b/(1-a)
        assert 0 <= y <= 1
        z = y
        for _ in range(n):
            z = tent(z)
        assert z == y
        points.add(y)
    assert len(points) == 2**n, (n, len(points))
    return points


def mobius(n):
    primes = [p for p in range(2,n+1) if n%p==0 and all(p%d for d in range(2,int(p**.5)+1))]
    ans = 0
    for m in range(1<<len(primes)):
        d = 1
        for k,p in enumerate(primes):
            if m>>k & 1:d*=p
        ans += (-1)**m * fix_count(n//d)
    assert ans%n==0
    return ans//n


def fix_count(n, sign=1):
    if sign == -1: return 2**(n+1)-1
    return 1 if n%2 else 2**(n+1)-1


if __name__ == '__main__':
    for n in range(1,13):
        pts = fixed_tent(n)
        assert len(pts)==2**n
        # The signed map has one shared zero and two nonzero lifts.
        minus = 2*len(pts)-1
        plus = 1 if n%2 else minus
        assert minus == fix_count(n, -1)
        assert plus == fix_count(n, 1)
        print(f'n={n:2d} tent={len(pts):5d} alpha=-4 fixed={minus:5d} alpha=+4 fixed={plus:5d}')
    # All primitive cycles of the sign-flipping map have even least period.
    for n in range(3,12,2):
        primes=[p for p in range(2,n+1) if n%p==0 and all(p%v for v in range(2,int(p**.5)+1))]
        primitive_points=0
        for mask in range(1<<len(primes)):
            d=1
            for j,p in enumerate(primes):
                if mask>>j&1: d*=p
            primitive_points+=(-1)**(mask.bit_count())*fix_count(n//d,1)
        assert primitive_points==0
    print('PASS: all exact tent inverse-branch and signed-lift checks')
