#!/usr/bin/env python3
"""Finite numerical consistency checks for sharp unicritical Bloch envelopes.
These tests do not replace the analytical proof.
"""
import math

def finite(n,a,s):
    return 2*n*math.exp(-s)*math.sinh(s/n)*(1-a*a)/(1-a*math.exp(-s))**2

def lim(a,s):
    return 2*s*math.exp(-s)*(1-a*a)/(1-a*math.exp(-s))**2

def sroot(n,a):
    lo,hi=0,.5*n*math.log((n+1)/(n-1))
    for _ in range(80):
        mid=(lo+hi)/2
        t=math.tanh(mid/n)
        aa=math.exp(mid)*(1-n*t)/(1+n*t)
        if aa>a: lo=mid
        else: hi=mid
    return (lo+hi)/2

def slimroot(a):
    lo,hi=0.,1.
    for _ in range(80):
        mid=(lo+hi)/2
        aa=math.exp(mid)*(1-mid)/(1+mid)
        if aa>a:lo=mid
        else:hi=mid
    return (lo+hi)/2

checks=0
for n in [2,3,4,5,7,10,20,100,1000]:
    old=0
    for a in [0,.01,.1,.25,.5,.75,.9,.99]:
        s=sroot(n,a); F=finite(n,a,s)
        assert F>old if a>0 else F>0
        old=F;checks+=1
        assert 0<F<1;checks+=1
        h=(1/n)/math.tanh(s/n)-1-2*a*math.exp(-s)/(1-a*math.exp(-s))
        assert abs(h)<1e-8; checks+=1
        for off in [.2,.6,.95,1.05,1.5,2,3]:
            assert F>=finite(n,a,s*off)-1e-10;checks+=1
        slim=slimroot(a); b=lim(a,slim)
        assert F>b>=2/math.e-1e-12;checks+=1
        bc=2*math.cosh(slim)-(slim+1/slim)*math.sinh(slim)
        assert abs(b-bc)<2e-10;checks+=1
        for off in [.2,.7,1.2,2,3]:
            assert b>=lim(a,slim*off)-1e-11;checks+=1
for a in [0,.05,.2,.7,.97]:
    values=[finite(n,a,sroot(n,a)) for n in [2,3,5,10,25,100]]
    assert all(values[k]>values[k+1] for k in range(len(values)-1));checks+=1
for a in [0,.3,.8]:
    F=finite(100000,a,sroot(100000,a));b=lim(a,slimroot(a))
    assert 0<F-b<1e-9;checks+=1
print('PASS:',checks,'numerical assertions')
