#!/usr/bin/env python3
"""Reproduce exact finite checks for a sharp radial modulus-square inverse theorem.

The infinite-degree assertion is proved algebraically in RESULT.md.
This script gives independently executable finite exact checks only.
"""
from fractions import Fraction as Q
from itertools import product
from math import ceil, sqrt

def coeffs(a):
    d = len(a) - 1
    return [sum((Q(a[j+k]*a[j], 2*j+k+1)
                 for j in range(d-k+1)), Q(0)) for k in range(d+1)]

def bound_sq(k, d):
    assert 1 <= k <= d
    return Q(1,4)*(1-Q(k*k,(2*d-k+1)**2))

def interior_check():
    a = [1,1,-2]
    c = coeffs(a)
    assert c[1] == 0 and c[2] != 0
    assert abs(c[2]/c[0])**2 < bound_sq(2,2)
    return (str(c[0]),str(c[2]/c[0]))

def scan():
    checked = 0
    exact_harmonic_cases = 0
    strict_below = 0
    for d in range(1,8):
        for a in product((-1,0,1),repeat=d+1):
            if not any(a) or a[-1] == 0 and d>0:
                continue
            c = coeffs(a)
            checked += 1
            nz = [j for j in range(1,d+1) if c[j] != 0]
            if len(nz) != 1:
                continue
            k = nz[0]
            support = [j for j,x in enumerate(a) if x]
            assert max(support)-min(support)==k
            ratio_sq = (c[k]/c[0])**2
            assert ratio_sq <= bound_sq(k,d)
            if ratio_sq < bound_sq(k,d):
                strict_below += 1
            exact_harmonic_cases += 1
    return checked,exact_harmonic_cases,strict_below

def symbolic_check():
    import sympy as s
    m,k=s.symbols('m k',integer=True,nonnegative=True)
    expr=(2*m+1)*(2*m+2*k+1)/(4*(2*m+k+1)**2)
    simpler=(1-k*k/(2*m+k+1)**2)/4
    assert s.factor(expr-simpler)==0
    assert s.simplify(s.Rational(1,2)*(s.Rational(1,2)))==s.Rational(1,4)
    # First several d,k at exact sharp amplitudes: A^2=(2m+1)/2,B^2=(2m+2k+1)/2.
    for kk in range(1,11):
        for dd in range(kk,kk+12):
            mm=dd-kk
            A2=Q(2*mm+1,2)
            B2=Q(2*mm+2*kk+1,2)
            h0=A2/Q(2*mm+1)+B2/Q(2*mm+2*kk+1)
            hk_sq=A2*B2/Q((2*mm+kk+1)**2)
            assert h0==1 and hk_sq==bound_sq(kk,dd)
    return 110

def construction_check():
    # Stable real-valued construction, including near-positivity boundary.
    import cmath
    cases=0
    for k in range(1,8):
        for epsilon in (.05,.22,.32,.41,.48,.499):
            v=1-4*epsilon**2
            d=max(k,ceil((k/sqrt(v)+k-1)/2-1e-12))
            assert d>=k
            m=d-k
            c=sqrt((2*m+1)*(2*m+2*k+1))/(2*m+k+1)
            assert epsilon<=c/2+1e-13
            s=2*epsilon/c
            x=sqrt((1+sqrt(max(0.0,1-s*s)))/2)
            y=sqrt((1-sqrt(max(0.0,1-s*s)))/2)
            # Avoid subtractive cancellation by taking y=s/(2x).
            y=s/(2*x)
            A=sqrt(2*m+1)*x
            B=sqrt(2*m+2*k+1)*y*1j
            h0=(A*A/(2*m+1)+(B*B.conjugate()).real/(2*m+2*k+1))
            hk=B*A/(2*m+k+1)
            assert abs(h0-1)<3e-12 and abs(hk-1j*epsilon)<3e-12
            if d>k:
                assert epsilon>0.5*sqrt(float(1-Q(k*k,(2*(d-1)-k+1)**2))) - 1e-12
            cases+=1
    return cases



def weighted_check():
    # Exact rational power weights t^beta, including beta close to -1.
    cases=0
    for beta in (Q(-1,2),Q(0),Q(3,2),Q(5)):
        for d in range(1,7):
            for a in product((-1,0,1),repeat=d+1):
                if not a[-1]:
                    continue
                hs=[sum((Q(a[j+k]*a[j]) / (Q(2*j+k+1)+beta)
                    for j in range(d-k+1)),Q(0)) for k in range(d+1)]
                nz=[k for k in range(1,d+1) if hs[k]]
                if len(nz)!=1:
                    continue
                k=nz[0]
                nonzero=[j for j in range(d+1) if a[j]]
                assert nonzero[-1]-nonzero[0]==k
                sharp=(Q(1)-Q(k*k)/(Q(2*d-k+1)+beta)**2)/4
                assert (hs[k]/hs[0])**2 <= sharp
                cases+=1
            for k in range(1,d+1):
                m=d-k
                A2=(Q(2*m+1)+beta)/2
                B2=(Q(2*d+1)+beta)/2
                h0=A2/(Q(2*m+1)+beta)+B2/(Q(2*d+1)+beta)
                hk2=A2*B2/(Q(2*m+k+1)+beta)**2
                sharp=(Q(1)-Q(k*k)/(Q(2*d-k+1)+beta)**2)/4
                assert h0==1 and hk2==sharp
    return cases

if __name__=='__main__':
    assert interior_check()==('32/15','-5/16')
    a,b,c=scan()
    s=symbolic_check()
    q=construction_check()
    z=weighted_check()
    print('exact exhaustive integer-coefficient polynomial tests:',a)
    print('exact one-harmonic instances:',b)
    print('instances strictly below sharp bound:',c)
    print('sharp rational-power algebra instances:',s)
    print('phase-resolved target constructions:',q)
    print('exact power-weight one-harmonic cases:',z)
    print('non-binomial inverse example: R[1+z-2z^2](theta)=32/15-(4/3)cos(2theta)')
    print('All finite checks passed; no finite scan is an infinite proof.')
