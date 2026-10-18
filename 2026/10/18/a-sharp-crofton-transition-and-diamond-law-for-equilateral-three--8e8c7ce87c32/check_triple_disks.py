#!/usr/bin/env python3
"""Independent quadrature and sampling checks for equilateral three-disk line section law."""
import math
import numpy as np
from scipy.integrate import quad

q0=math.sqrt(3)/2
centers=np.array([(0.,0.),(1.,0.),(.5,math.sqrt(3)/2)])

def pair(q):
    return 2*(q*math.asin(q)+math.sqrt(1-q*q)-1)

def triple(q):
    if q<=q0: return 0.
    return 6*(q*(math.pi/6-math.acos(q)) + math.sqrt(1-q*q)-.5)

def formula(q):
    b,t=pair(q),triple(q)
    z=3*math.pi*q-3*b+t
    assert z>0
    return np.array([(3*math.pi*q-6*b+3*t)/z, (3*b-3*t)/z,t/z]), z, b, t

def profile(theta,q):
    n=np.array([math.cos(theta),math.sin(theta)])
    p=sorted(centers @ n)
    # independent interval union by breakpoints
    intervals=[(x-q/2,x+q/2) for x in p]
    breaks=sorted({a for it in intervals for a in it})
    v=[0.,0.,0.]
    for a,b in zip(breaks,breaks[1:]):
        x=(a+b)/2
        k=sum(a0<x<b0 for a0,b0 in intervals)
        if k:v[k-1]+=(b-a)
    return np.array(v)

# Piecewise smooth angular integrals (avoid discontinuity surprises)
for q in (.02,.2,.55,.8,q0-1e-5,q0+1e-4,.9,.95,.999):
    p,z,b,t=formula(q)
    numerical=np.array([sum(quad(lambda th:profile(th,q)[j], lo,hi,epsabs=1e-10,epsrel=1e-10,limit=200)[0]
                           for lo,hi in zip(np.linspace(0,math.pi,19)[:-1],np.linspace(0,math.pi,19)[1:]))
                        for j in range(3)])
    err=np.max(np.abs(numerical-z*p))
    print('q',q,'z',z,'prob',p,'error',err)
    assert err<2e-7
    if q>q0: assert abs(z-(3+math.pi*q))<1e-12

# Monte Carlo: independent line orientation and offset covering all possible intervals.
rng=np.random.default_rng(253721)
for q in (.3,.88,.96):
    n=500000
    theta=rng.uniform(0,math.pi,n)
    offset=rng.uniform(-1.5,1.5,n)
    x=centers[:,0,None]*np.cos(theta)[None,:]+centers[:,1,None]*np.sin(theta)[None,:]
    k=(np.abs(x-offset[None,:])<q/2).sum(axis=0)
    conditional=np.array([(k==i).sum() for i in (1,2,3)],dtype=float)
    conditional/=conditional.sum()
    exact,_,_,_=formula(q)
    diff=np.max(abs(conditional-exact))
    print('MC',q,conditional,exact,'maxerr',diff)
    assert diff<.006

# Critical coefficient via high-precision mpmath (avoid cancellation).
import mpmath as mp
mp.mp.dps=90
q00=mp.sqrt(3)/2
for eps in (mp.mpf('1e-2'),mp.mpf('1e-3'),mp.mpf('1e-4'),mp.mpf('1e-5')):
    qq=q00+2*eps
    tt=6*(qq*(mp.pi/6-mp.acos(qq))+mp.sqrt(1-qq*qq)-mp.mpf('.5'))
    ratio=tt/(eps**2)
    print('onset eps',mp.nstr(eps,5),'ratio',mp.nstr(ratio,18))
    assert abs(ratio-24)<5

# Limit at externally tangent radius.
P,z,b,t=formula(1.)
assert np.max(abs(P-np.array([3,3,math.pi-3])/(math.pi+3)))<2e-14
print('TRIPLE_DISK_TRANSVERSAL_OK quadrature_cases=9 monte_carlo=3 critical_tests=4')
