#!/usr/bin/env python3
"""Finite consistency checks for the RSA gap-density inequality.

These checks support, but do not prove, the quantified theorem.
Requires only Python 3 standard library.
"""
from fractions import Fraction
from math import exp, isfinite


def phi(k, s):
    return exp(2.0 * sum((s**j - 1.0)/j for j in range(1, k)))


def simpson(fn, n=8000):
    assert n % 2 == 0
    h = 1.0/n
    total = fn(0.0)+fn(1.0)
    for i in range(1, n):
        total += (4 if i & 1 else 2)*fn(i*h)
    return total*h/3


def check():
    checks=0
    # Reconstruct the crucial finite geometric-sum identity exactly.
    for k in range(2, 51):
        for numerator in range(1, 20):
            z=Fraction(numerator, 20)
            lhs=(1-z)*(-z/(1-z)-1+2*sum((z**j for j in range(1,k)), Fraction()))
            rhs=2*z-1-2*z**k
            assert lhs==rhs,(k,numerator)
            checks+=1
    # Calculate the reciprocal-index reflection derivative.
    for k in (2,3,4,5,8,12,21,30,80,200):
        for y in (0.04,0.1,0.25,0.4,0.49):
            s=y**(1.0/k)
            t=(1-y)**(1.0/k)
            direct=-2+(1-2*y)*sum(s**j-t**j for j in range(k))
            assert direct < -1.99999999999
            x=direct/(k*y*(1-y))
            assert isfinite(x) and x<0
            checks+=2
    # Compare both independent formulas for each strict difference.
    for k in (2,3,4,5,8,10,15,20,21,25,35,50,70):
        g=[2*simpson(lambda s, l=l:(1-s)*s**l*phi(k,s), n=5000)
           for l in range(k)]
        assert g[0]>0
        checks+=1
        for l in range(k-1):
            direct=(l+1)*g[l+1]-l*g[l]
            other=2*simpson(lambda s, l=l:s**l*(1-s)*phi(k,s)*(1-2*s**k), n=5000)
            assert direct>0,(k,l,direct)
            assert abs(direct-other)<2e-8,(k,l,direct,other)
            checks+=2
    print('PASS:', checks, 'exact/algebraic/numerical assertions')
    print('Limit: numerical quadrature does not prove a result for all k.')


if __name__=='__main__':
    check()
