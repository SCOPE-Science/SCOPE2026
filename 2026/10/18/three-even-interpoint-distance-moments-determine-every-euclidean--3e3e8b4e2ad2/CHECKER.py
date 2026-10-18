#!/usr/bin/env python3
"""Exact-arithmetic checks of the triangular pair-distance moment identities.

Requires only Python 3 standard library.  This finite polynomial interpolation
check is a certificate for the displayed identities, not an independent audit
of geometric hypotheses or the analytic inverse-stability argument.
"""
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def simplex_moment(i, j):
    """E[S**i*T**j] for density 2 on the standard triangle."""
    return F(2 * factorial(i) * factorial(j), factorial(i + j + 2))

@lru_cache(None)
def difference_moment(r, s):
    """E[(S-S')**r * (T-T')**s] for independent pairs."""
    return sum(((-1) ** (r - i + s - j) * comb(r, i) * comb(s, j)
                * simplex_moment(i, j) * simplex_moment(r - i, s - j)
                for i in range(r + 1) for j in range(s + 1)), F(0))


def lhs(k, A, B, C):
    """E[(A*U**2+B*V**2+2*C*U*V)**k]."""
    return sum((F(factorial(k), factorial(i) * factorial(j) * factorial(ell))
                * A**i * B**j * (2*C)**ell
                * difference_moment(2*i + ell, 2*j + ell)
                for i in range(k+1) for j in range(k-i+1)
                for ell in [k-i-j]), F(0))


def rhs(k, A, B, C):
    a, b, c = A, B, A + B - 2*C
    s1, s2, s3 = a+b+c, a*b+a*c+b*c, a*b*c
    return [None,
            F(s1, 18),
            F(s1*s1-2*s2, 60),
            F(23*s1**3, 4200)-F(31*s1*s2, 2100)+F(s3, 210)][k]


def moments(a, b, c):
    s1, s2, s3 = a+b+c, a*b+a*c+b*c, a*b*c
    return (F(s1, 18), F(s1*s1-2*s2, 60),
            F(23*s1**3, 4200)-F(31*s1*s2, 2100)+F(s3, 210))


def verify():
    points = 0
    for k in (1, 2, 3):
        # Both sides are polynomials of degree <= k separately in A,B,C.
        # Equality on this tensor grid therefore proves polynomial identity.
        for A in range(k+1):
            for B in range(k+1):
                for C in range(k+1):
                    assert lhs(k, F(A), F(B), F(C)) == rhs(k, F(A), F(B), F(C))
                    points += 1
    a1 = (F(1), F(4), F(4))
    a2 = (F(2), F(2), F(5))
    assert all(4*side[0]*side[1] > (side[0]+side[1]-side[2])**2
               for side in (a1, a2))
    m, n = moments(*a1), moments(*a2)
    assert m[:2] == n[:2] == (F(1, 2), F(11, 20))
    assert n[2]-m[2] == F(2, 105)
    assert F(4*(a1[0]*a1[1]+a1[1]*a1[2]+a1[2]*a1[0])
             -(sum(a1))**2) == F(15)
    # Cubic root sets reconstruct the exact squared sides in both examples.
    for sides in (a1,a2):
        m1,m2,m3=moments(*sides)
        s1=18*m1
        s2=(s1*s1-60*m2)/2
        s3=210*m3-F(23,20)*s1**3+F(31,10)*s1*s2
        assert (s1,s2,s3)==(sum(sides),
                             sides[0]*sides[1]+sides[0]*sides[2]+sides[1]*sides[2],
                             sides[0]*sides[1]*sides[2])
    for eps in (F(1,100), F(1,10)):
        left=(1+eps,1+eps,1-2*eps)
        right=(1-eps,1-eps,1+2*eps)
        denom=1+2*eps
        left=tuple(z/denom for z in left)
        right=tuple(z/denom for z in right)
        p,q=moments(*left),moments(*right)
        assert p[:2]==q[:2]
        assert abs(p[2]-q[2])==F(2,105)*(eps/denom)**3
        assert max(abs(a-b) for a,b in zip(sorted(left),sorted(right)))==2*eps/denom
    print('PASS: %d exact interpolation nodes (degree-1/2/3 identities),' % points)
    print('PASS: two-moment ambiguity, three-moment inversion, and 1/3-exponent family')

if __name__=='__main__':
    verify()
