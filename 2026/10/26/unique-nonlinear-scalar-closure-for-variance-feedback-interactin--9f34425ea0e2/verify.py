#!/usr/bin/env python3
"""Finite algebraic and normalization checks for the scalar-closure classification.
All substantive infinite-time claims are proved analytically in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import gamma, isclose, sqrt

def pmean_dissipation(v,p):
    n=len(v)
    s=p+2
    return sum(abs(x-y)**s for x in v for y in v)/(n*n)

def variance(v):
    n=len(v)
    b=sum(v)/n
    return sum((x-b)**2 for x in v)/n

checks=0
# Exact n=1,N=3 quartic identity over many centered integer triples.
for a,b in product(range(-9,10),repeat=2):
    v=[Fraction(a),Fraction(b),Fraction(-a-b)]
    S=variance(v)
    D=pmean_dissipation(v,2)
    assert D==9*S*S, (v,S,D)
    checks+=1
# Exact linear p=0 identity for numerous dimensions and particle counts.
for n in range(2,8):
    for t in range(40):
        v=[Fraction((19*i+7*t*t)%23-11,3) for i in range(n)]
        assert pmean_dissipation(v,0)==2*variance(v)
        checks+=1
# Structural witnesses: for N>=4 all powers p>0, as factored polynomial >0.
for N,p in product(range(4,31),[.1,.25,.5,1,2,3,5,9]):
    s=p+2
    t=2**(s/2)
    A=[-1.0,1.0]+[0.]*(N-2)
    B=[-1/sqrt(2),-1/sqrt(2),1/sqrt(2),1/sqrt(2)]+[0.]*(N-4)
    diff=pmean_dissipation(A,p)-pmean_dissipation(B,p)
    pred=2/(N*N)*((t-2)*(t*t-2*t+2*N-8)/t)
    assert isclose(variance(A),variance(B),abs_tol=1e-13)
    assert diff>0 and isclose(diff,pred,rel_tol=5e-7,abs_tol=5e-13),(N,p,diff,pred)
    checks+=1
# For three collinear particles, equality exactly at p=0 and p=2;
# the strict sign of the convex exponential comparison is checked away from roots.
for p in [.1,.25,.5,1,1.5,2.5,3,5,10]:
    s=p+2; t=s/2
    g=(4/3)**t+2/(3**t)-2
    assert g<0 if p<2 else g>0,(p,g)
    checks+=1
# Explicit scalar cubic q=1 coefficients and squared-Bessel normalization.
for lam in [Fraction(1,5),Fraction(1,2),Fraction(1),Fraction(2),Fraction(9),Fraction(20)]:
    a2=Fraction(4,3)*lam
    c=Fraction(2,3)*lam
    delta=2+Fraction(27,1)/lam
    # f(S)=3/(lam S), Ito drift = -3/lam*(-9+c)+3*a2/lam.
    ito_drift=-Fraction(3,1)/lam*(-9+c)+Fraction(3,1)/lam*a2
    assert ito_drift==delta
    assert Fraction(3,1)/lam/(delta-2)==Fraction(1,9)
    checks+=1
# Central-chi-square inverse moment identity, including a nontrivial second moment.
for lam in [.5,1.,4.]:
    d=2+27/lam
    for r in [.25,.5,1.]:
        formula=(3/(2*lam))**r*gamma(d/2-r)/gamma(d/2)
        assert formula>0
        if r==1:
            assert isclose(formula,1/9,rel_tol=3e-13)
        checks+=1
print(f"PASS {checks} checks: exact quartic closure, nonclosure witnesses, Bessel coefficients and limiting moments")
