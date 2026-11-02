#!/usr/bin/env python3
"""Exact finite checks for rational motivic-density identities.

No scientific claim of exhaustive verification for unbounded exponents is made.
"""
from fractions import Fraction
from math import gcd, lcm

def theta(a, m, L):
    prefactor = (1 - 1/L) / (1 - L**(-a))
    return prefactor * L**(m - a * ((m+a-1)//a))

def formula(a,b,L):
    d=gcd(a,b)
    return Fraction(d,a*b)*(L-1)/(L+1)*(L**d+1)/(L**d-1)

def run():
    tests=0
    for ell in (2,3,5,11):
        L=Fraction(ell)
        for a in range(2,15):
            solo=sum((theta(a,m,L) for m in range(a)),Fraction(0))/a
            assert solo==Fraction(1,a),(ell,a,solo)
            for b in range(2,15):
                period=lcm(a,b)
                direct=sum((theta(a,m,L)*theta(b,m,L)
                            for m in range(period)),Fraction(0))/period
                assert direct==formula(a,b,L),(ell,a,b,direct,formula(a,b,L))
                tests+=1
        cusp=formula(2,2,L)
        assert cusp==(L**2+1)/(2*(L+1)**2)
        assert cusp-Fraction(1,4)==(L-1)**2/(4*(L+1)**2)
    assert tests==676
    print("VERIFY_OK 676 exact period averages; 52 single-factor means; 4 two-cusp defects")
if __name__=='__main__':run()
