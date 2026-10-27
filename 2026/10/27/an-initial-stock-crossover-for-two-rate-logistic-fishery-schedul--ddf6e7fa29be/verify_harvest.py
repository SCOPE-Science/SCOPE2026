#!/usr/bin/env python3
"""Reproducible checks of two-block logistic fishing calculations.
Standalone reproducibility checks; requires Python's standard library only.
These finite tests are not a proof of uniqueness for all parameters.
"""
import math
import random


def pulse(z, effort, duration):
    rate=1.0-effort
    E=math.exp(rate*duration)
    J=math.expm1(rate*duration)/rate if abs(rate)>1e-12 else duration
    terminal=z*E/(1.0+J*z)
    catch=effort*math.log1p(J*z)
    return terminal, catch, E, J


def compare(z,H,L,U,V):
    a,ya,eh,p=pulse(z,H,U)
    b,yb,_,_=pulse(a,L,V)
    c,yc,el,q=pulse(z,L,V)
    d,yd,_,_=pulse(c,H,U)
    m=p+eh*q
    n=q+el*p
    D=(H-L)*math.log((1+p*z)*(1+q*z)/(1+n*z))+L*math.log((1+m*z)/(1+n*z))
    return (ya+yb)-(yc+yd),D,b,d,(p,q,m,n)

rng=random.Random(486340)
for j in range(2000):
    H=rng.uniform(.05,2.6)
    L=rng.uniform(0.001,H*.99)
    U=rng.uniform(.12,2.5)
    V=rng.uniform(.12,2.5)
    if j%11==0:L=0.0
    z=rng.uniform(.05,5)
    measured,formula,term_HL,term_LH,par=compare(z,H,L,U,V)
    assert abs(measured-formula)<2e-12*(1+abs(measured)),(j,measured,formula)
    assert term_HL>term_LH,(j,term_HL,term_LH)
    low=compare(.8,H,L,U,V)[0]
    assert low<0,('below K',j,low)
    if L==0:
        assert abs(compare(1,H,L,U,V)[0])<2e-12
    else:
        assert compare(1,H,L,U,V)[0]<0,('at K',j)
        a=1.;b=16.
        while compare(b,H,L,U,V)[0]<=0:
            b*=2
            assert b<1e14
        for _ in range(60):
            m=(a+b)/2
            if compare(m,H,L,U,V)[0]>0:b=m
            else:a=m
        root=(a+b)/2
        assert root>1
        assert compare(root*.9,H,L,U,V)[0]<0
        assert compare(root*1.1,H,L,U,V)[0]>0

H,L,U,V=.9,.1,1.,1.
a,b=1.,3.
for _ in range(70):
 m=(a+b)/2
 if compare(m,H,L,U,V)[0]>0:b=m
 else:a=m
root=(a+b)/2
print('2000 deterministic parameter checks passed')
print('example H=0.9 L=0.1 U=V=1: threshold=',format(root,'.14f'))
for z in (.6,1,root,2):
 delta,_,xHL,xLH,_=compare(z,H,L,U,V)
 print('z=%0.10f yield(HL)-yield(LH)=%+.12f; terminal(HL)=%0.12f; terminal(LH)=%0.12f'%(z,delta,xHL,xLH))
