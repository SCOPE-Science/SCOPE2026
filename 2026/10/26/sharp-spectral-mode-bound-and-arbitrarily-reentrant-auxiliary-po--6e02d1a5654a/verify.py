#!/usr/bin/env python3
"""Exact rational verification of auxiliary-scalar step-size topology."""
from fractions import Fraction as F

def coefficients(lams, roots):
    result=[]
    for i, lam in enumerate(lams):
        value=F(2)
        for root in roots:
            value *= 1+F(1,lam*root)
        for j, other in enumerate(lams):
            if i != j:
                value /= 1-F(other,lam)
        result.append(value)
    return result

def spectral_numerator(lams,c,h):
    return F(2)-sum((v*h*lam/(1+h*lam) for lam,v in zip(lams,c)),F(0))

def interpolation(lams,roots,h):
    result=F(2)
    for root in roots:
        result *= 1-F(h,root)
    for lam in lams:
        result /= 1+h*lam
    return result

def auxiliary_denominator(lams,c,h):
    return 1+F(h,2)*sum((v*v/(1+h*lam) for lam,v in zip(lams,c)),F(0))

for m in range(1,8):
    lams=list(range(1,m+1))
    roots=list(range(1,m+1))
    c=coefficients(lams,roots)
    assert all(v!=0 for v in c)
    for k in range(1,80):
        h=F(k,13)
        assert spectral_numerator(lams,c,h)==interpolation(lams,roots,h)
        assert auxiliary_denominator(lams,c,h)>0
    for k in range(m+1):
        h=F(1,2) if k==0 else (F(m+1) if k==m else F(k,1)+F(1,2))
        assert (spectral_numerator(lams,c,h)>0)==(k%2==0)
    print('dimension',m,'PASS')

lams=[1,4]
roots=[1,2]
c=coefficients(lams,roots)
assert c==[F(-2),F(15,4)]
assert 1-sum(v*v for v in c)/20==F(31,320)
for h, expected in [(F(1,2),F(16,545)),(F(3,2),F(-16,8303)),(F(3),F(8,1715))]:
    # Directly solve x_i^+=(x_i-h*r^+*c_i)/(1+h*lam_i), then
    # r^+=1+sum_i c_i*(x_i^+-1)/2.
    offset=F(1)+sum((c_i*(F(1,1+h*lam)-1)/2 for c_i,lam in zip(c,lams)),F(0))
    slope=sum((c_i*c_i*h/(2*(1+h*lam)) for c_i,lam in zip(c,lams)),F(0))
    direct=offset/(1+slope)
    spectral=spectral_numerator(lams,c,h)/(2*auxiliary_denominator(lams,c,h))
    claimed=16*(h-1)*(h-2)/(609*h*h+449*h+32)
    assert direct==spectral==claimed==expected
print('Exact-rational standalone checks: PASS')
