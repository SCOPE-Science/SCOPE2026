#!/usr/bin/env python3
"""Numerical checks of two-patch Poisson source-sink formulas.
All principal assertions in the accompanying result are analytically proved;
iteration here checks finite-precision instances, not universal quantifiers.
"""
from math import exp, log, sqrt, isclose

def q_root(r):
    lo,hi=0.,1.-1.e-10
    for _ in range(180):
        mid=(lo+hi)/2
        if exp(r*(mid-1))>mid:lo=mid
        else:hi=mid
    return (lo+hi)/2

def rho(r,s,d):
    return ((r+s)*(1-d)+sqrt((r-s)**2*(1-d)**2+4*r*s*d*d))/2

def surviving(r,s,d):
    if rho(r,s,d)<=1: return 0.0
    x=y=0.0
    for _ in range(200000):
        xx=exp(r*((1-d)*x+d*y-1))
        yy=exp(s*(d*x+(1-d)*y-1))
        if max(abs(x-xx),abs(y-yy))<3e-15:
            return (2-xx-yy)/2
        x,y=xx,yy
    raise RuntimeError('no numerical convergence')

r=4*log(4)/3
s=.5
q=q_root(r)
assert abs(q-.25)<1e-12
assert r*q<s<1/r
critical=(r-1)*(1-s)/(r+s-2*r*s)
assert abs(critical-(r-1))<1e-12
slope=(1-q)*(s-r*q)/(2*(1-s)*(1-r*q))
assert slope>0
s0=surviving(r,s,0)
s01=surviving(r,s,.01)
assert abs(s0-3/8)<1e-12
assert s01>s0
assert abs((surviving(r,s,1e-5)-s0)/1e-5-slope)<1e-4
assert rho(r,s,.9)<1
assert surviving(r,s,.9)==0
for rr in (1.1,1.25,1.5,2.,3.,6.,12.):
    qq=q_root(rr)
    assert qq<1/rr**2
    ss=(rr*qq+1/rr)/2
    assert rr*qq<ss<1/rr
    dd=(rr-1)*(1-ss)/(rr+ss-2*rr*ss)
    assert 0<dd<1
    samples=[rho(rr,ss,j/200.) for j in range(201)]
    assert all(a>b for a,b in zip(samples,samples[1:]))
    assert rho(rr,ss,dd-1e-6)>1>rho(rr,ss,dd+1e-6)
print('PASS: q, sharp low-dispersal derivative, full growth decline, terminal extinction, seven nonempty parameter bands')
print('r=',repr(r),'s=',s,'q=',q,'cutoff=',critical,'S0=',s0,'S(0.01)=',s01,'Sprime0=',slope)
