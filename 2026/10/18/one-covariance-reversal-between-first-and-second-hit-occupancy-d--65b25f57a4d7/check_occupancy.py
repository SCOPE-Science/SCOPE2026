#!/usr/bin/env python3
"""Independent exact checks for finite uniform-occupancy covariance identities.

The all-parameter zero-count and asymptotic results have analytic proofs
in RESULT.md; finite checks here are consistency tests, not their proof.
"""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import log, exp


def covariance_formula(b, s):
    """Exact Cov(U,V), U=#occupied, V=#bins of occupancy >=2."""
    if b < 3 or s < 2:
        raise ValueError("formula requires b>=3, s>=2")
    q, r = Fraction(b-1, b), Fraction(b-2, b)
    u, v = q**s, Fraction(s,b)*q**(s-1)
    w, t = r**s, Fraction(s,b)*r**(s-1)
    return b*(u*(1-u-v)+(b-1)*(w+t-u*(u+v)))


def covariance_compressed(b,s):
    q,r=Fraction(b-1,b),Fraction(b-2,b)
    return b*(q**s+(b-1)*(r**s+Fraction(s,b)*r**(s-1))
              -b*q**(2*s)-s*q**(2*s-1))


def covariance_enumerated(b,s):
    total=b**s
    su=sv=suv=0
    for outcomes in product(range(b), repeat=s):
        occ=Counter(outcomes).values()
        u=len(occ)
        v=sum(x>=2 for x in occ)
        su+=u;sv+=v;suv+=u*v
    return Fraction(suv,total)-Fraction(su*sv,total**2)


def finite_sign_sequence_test(b, upto):
    signs=[]
    for s in range(2,upto+1):
        c=covariance_formula(b,s)
        signs.append((c>0)-(c<0))
    assert signs[0]==-1
    # Consecutive nonzero signs cannot move from positive back to negative;
    # the analytic theorem is stronger because it covers all later s.
    assert all(x<=y for x,y in zip(signs,signs[1:])), (b,signs)
    return signs.count(-1),signs.count(0),signs.count(1)


def main():
    enum_cases=0
    for b in range(3,7):
        for s in range(2,8):
            a=covariance_formula(b,s)
            assert a==covariance_compressed(b,s)
            assert a==covariance_enumerated(b,s),(b,s)
            enum_cases+=1
    # Two-box boundary direct exact enumeration (not covered by formula).
    for s in range(2,11):
        a=covariance_enumerated(2,s)
        if s==2: assert a==Fraction(-1,4)
        elif s==3: assert a==0
        else:
            expected=Fraction(2,2**s)*(1-Fraction(2*(s+1),2**s))
            assert a==expected>0,(s,a,expected)
    sign_cases=0
    for b in range(3,32):
        counts=finite_sign_sequence_test(b,5*b+5)
        assert counts[0]>0 and counts[-1]>0
        sign_cases+=5*b+4
        q,r=(b-1)/b,(b-2)/b
        d1=q*((b-1)*log(r)-(2*b-1)*log(q))
        assert d1<0
    # Approximate limiting phase brackets; validated by analysis, not numerics.
    f=lambda x:exp(x)-1-x-x*x
    assert f(1.7932)<0<f(1.7934)
    print("PASS independent exhaustive allocations:",enum_cases)
    print("PASS two-bin boundary enumerations: 9")
    print("PASS exact sign-sequence parameters:",sign_cases)
    print("PASS numerical derivative sample b=3..31 and limiting-root bracket")


if __name__=='__main__':
    main()
