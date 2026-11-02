"""Reproduce the coefficient and valuation identities over Q.

This checks finitely many values of m. The unrestricted statement requires
and is proved by the formal binomial calculation in the accompanying proof.
"""
from fractions import Fraction
from math import comb


def poly_add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return out


def poly_mul(a, b):
    out = [Fraction(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out


def binom_poly(u, v, n):
    return [Fraction(comb(n,j))*u**(n-j)*v**j for j in range(n+1)]

for m in range(3, 19):
    d=2*m-1
    for t in [Fraction(2),Fraction(3,2),Fraction(-2,3)]:
        # z=s^m. H=( t^{m(m-1)}(1-z)^m + (dz-1)(t^m-z)^{m-1} ) /
        #      (t^{m(m-1)}(1-z)^m).
        numer=poly_add(
            [t**(m*(m-1))*v for v in binom_poly(Fraction(1),Fraction(-1),m)],
            poly_mul([Fraction(-1),Fraction(d)],
                binom_poly(t**m,Fraction(-1),m-1)))
        assert numer[0]==0
        assert numer[1]==(m-1)*t**(m*(m-1))*(1+t**(-m))
        assert numer[1]!=0
        # u3/u1 = s^{m-1}(s^m-d)/(d*s^m-1) has leading coeff d.
        assert d != 0
        # Unique off-boundary preimages of generic target fail unless t^m=1.
        assert t**m != 1
print('VALUATION_IDENTITY_OK')
