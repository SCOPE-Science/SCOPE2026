#!/usr/bin/env python3
"""Finite numerical consistency diagnostics for a finite weighted-triangle theorem.
Not a proof of an infinite-dimensional assertion. Python standard library only.
"""
from fractions import Fraction
from itertools import product
from math import sqrt, isclose


def numerical_radius3(a,b,c):
    # largest positive eigenvalue of the nonnegative 3x3 weighted adjacency,
    # divided by two. Bisection uses its cubic: L^3-p L-2abc=0.
    a,b,c=map(float,(a,b,c))
    p=a*a+b*b+c*c
    lo=sqrt(p); hi=max(a+b,a+c,b+c)+1.0
    for _ in range(110):
        mid=(lo+hi)/2
        if mid**3-p*mid-2*a*b*c < 0: lo=mid
        else: hi=mid
    return (lo+hi)/4


def envelope(a,b,c):
    s=a+b+c
    q=3*(a*a+b*b+c*c)/(s*s)-1
    if q<=Fraction(1,2):
        u=sqrt(float(q)/2)
        f=(1-2*u+sqrt(9+12*u+12*u*u))/12
    else:
        f=0.5*sqrt(float((1+q)/3))
    return float(s)*f, float(q)


def main():
    cases=0
    min_gap=1e50
    k=1/sqrt(2)-2/3
    for a,b,c in product(range(0,17),repeat=3):
        if a+b+c==0: continue
        s=Fraction(a+b+c)
        aa,bb,cc=Fraction(a),Fraction(b),Fraction(c)
        qx=(aa-bb)**2+(bb-cc)**2+(cc-aa)**2
        assert qx==3*(aa**2+bb**2+cc**2)-s**2
        f,q=envelope(aa,bb,cc)
        numerical=numerical_radius3(aa,bb,cc)
        # Analytic envelope and sharp quadratic stability (floating round-off only).
        if numerical+2e-11*float(s) < f:
            raise AssertionError((a,b,c,'envelope',numerical,f))
        rhs=float(s)/3+k*float(qx/s)
        if numerical+2e-11*float(s)<rhs:
            raise AssertionError((a,b,c,'linear',numerical,rhs))
        if q>1e-15:
            min_gap=min(min_gap,(numerical-f)/float(s))
        cases+=1
    assert abs(numerical_radius3(1,1,0)/2-(sqrt(2)/4))<1e-12
    for x in [0.0,0.03,0.2,0.49,0.5,0.65,1.1,2.0]:
        if x<=.5:
            u=sqrt(x/2)
            a=b=(1+u)/3
            c=(1-2*u)/3
        else:
            u=sqrt((2*x-1)/3)
            a=(1+u)/2;b=(1-u)/2;c=0.
        f,_=envelope(Fraction(a).limit_denominator(10**9),Fraction(b).limit_denominator(10**9),Fraction(c).limit_denominator(10**9))
        v=numerical_radius3(a,b,c)
        assert abs(v-f)<2e-8,(x,a,b,c,v,f)
    print(f'PASS: {cases} nonzero rational weight triples, exact variance identities,')
    print('sharp-envelope and linear-stability numerical diagnostics, eight boundary checks.')
    print(f'Extremal constant k = {k:.15f}; minimum diagnostic envelope slack {min_gap:.4g}.')

if __name__=='__main__': main()
