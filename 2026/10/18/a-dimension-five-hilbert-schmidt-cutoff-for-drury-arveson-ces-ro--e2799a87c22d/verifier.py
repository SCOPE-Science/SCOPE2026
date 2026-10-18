#!/usr/bin/env python3
"""Finite exact-arithmetic checks for a Drury--Arveson Cesaro commutator identity.

This is supporting arithmetic only; the infinite-dimensional theorem requires
its separate analytic proof.
"""
from fractions import Fraction
from math import factorial, comb
from itertools import product


def compositions(total, d):
    if d == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for b in compositions(total - a, d - 1):
            yield (a,) + b


def squared_monomial_ratio(alpha, k, ell):
    m = sum(alpha)
    top = list(alpha)
    top[0] += k
    top[1] += ell
    return Fraction(factorial(m), factorial(m+k+ell)) * Fraction(
        factorial(top[0]) * factorial(top[1]),
        factorial(alpha[0]) * factorial(alpha[1]),
    )


def summed_ratio_formula(d,m,k,ell):
    r=k+ell
    num=1
    den=1
    for s in range(1,d):
        num *= m+r+s
        den *= r+s
    return Fraction(num,den*comb(r,k))


def commutator_coefficient(m,k,ell):
    return Fraction(k-ell,(m+k+1)*(m+ell+1)*(m+k+ell+1))


def verify():
    cases=0
    for d in range(2,6):
        for m in range(0,6):
            for k in range(0,5):
                for ell in range(0,5):
                    actual=sum((squared_monomial_ratio(alpha,k,ell)
                              for alpha in compositions(m,d)),Fraction(0))
                    assert actual==summed_ratio_formula(d,m,k,ell),(d,m,k,ell,actual)
                    c1=Fraction(1,(m+ell+1)*(m+k+ell+1))
                    c2=Fraction(1,(m+k+1)*(m+k+ell+1))
                    assert c1-c2==commutator_coefficient(m,k,ell)
                    cases+=1
    assert commutator_coefficient(0,1,0)==Fraction(1,4)
    # Fixed (k,ell)=(1,0) gives an exact nonnegative subsum.
    # Its mth term is asymptotic to a positive multiple of m^(d-7),
    # separating dimensions <=5 from >=6.
    for d in range(2,9):
        for m in range(1,8):
            term=commutator_coefficient(m,1,0)**2*summed_ratio_formula(d,m,1,0)
            assert term>0
    print(f'DRURY_CESARO_COMMUTATOR_EXACT_IDENTITIES_OK cases={cases}')

if __name__=='__main__':
    verify()
