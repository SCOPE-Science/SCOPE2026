"""Exact rational checks of a B-spline integer-refinement Zak identity.

Run: python3 verify_b_spline_reciprocal_zak.py
This checks finitely many rational fibers and roots; the theorem for all real
parameters follows from the proof, not the finite comparison.
"""
from fractions import Fraction as Q
from math import comb, factorial, floor
from collections import defaultdict
from itertools import product


def bspline(n, x):
    """Centered cardinal B-spline using truncated powers, exact over Q."""
    if x <= -Q(n,2) or x >= Q(n,2):
        return Q(0)
    return sum(Q((-1)**j * comb(n,j), factorial(n-1)) * max(Q(0), x+Q(n,2)-j)**(n-1)
               for j in range(n+1))


def z1(n,x):
    lo=-2*n-3; hi=2*n+4
    return {k:v for k in range(lo,hi) if (v:=bspline(n,x-k))}


def direct(n,m,x):
    lo=-m*n-3; hi=m*n+4
    return {k:v for k in range(lo,hi) if (v:=bspline(n,(x-k)/m))}


def derived(n,m,x):
    h=n*(m-1)
    K=h//2; r=Q(h%2,2)
    # (1+z^(-1)+...+z^(-(m-1)))**n
    coef={0:1}
    for _ in range(n):
        d=defaultdict(int)
        for j,c in coef.items():
            for t in range(m): d[j-t]+=c
        coef=dict(d)
    out=defaultdict(Q)
    for i,c in coef.items():
        for k,v in z1(n,x+r).items():
            out[K+i+k]+=Q(c,m**(n-1))*v
    return {k:v for k,v in out.items() if v}


def evaluate(poly,z):
    return sum(complex(v)*z**k for k,v in poly.items())


def main():
    tests=0
    for n in range(3,9):
        for m in range(2,8):
            for x in [Q(0),Q(1,7),Q(1,3),Q(1,2),Q(5,7),Q(1)]:
                left=direct(n,m,x)
                right=derived(n,m,x)
                assert left==right, (n,m,x,left,right)
                tests+=1
            # Exact vanishing on every nonzero m-th root: the refinement
            # polynomial contains the cyclotomic sum to its nth power.
            for j in range(1,m):
                import cmath
                z=cmath.exp(2j*cmath.pi*j/m)
                assert abs(sum(z**(-k) for k in range(m)))<2e-13
                for x in [Q(1,7),Q(1,2)]:
                    assert abs(evaluate(direct(n,m,x),z))<2e-10
                    tests+=1
    print(f'VERIFY_OK {tests} exact rational polynomial and numerical root checks; n=3..8, m=2..7')

if __name__=='__main__':
    main()
