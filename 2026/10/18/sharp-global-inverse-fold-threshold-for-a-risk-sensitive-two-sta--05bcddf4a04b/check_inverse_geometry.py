#!/usr/bin/env python3
"""Numerical and symbolic spot checks for a two-state MWU inverse-geometry theorem.

This is a finite diagnostic only; the global statements follow from monotonicity
and exact elimination in the accompanying mathematical proof.
"""
from math import exp, log, sqrt, atanh
import random
import sympy as sp
from scipy.optimize import brentq


def sigmoid(t):
    return 1/(1+exp(-t)) if t>=0 else exp(t)/(1+exp(t))


def logit(x):
    return log(x/(1-x))


def map_logit(t,q,a,b,c,p0,p1,k):
    x=sigmoid(t)
    return t-a*(x-b+c*q),(1-k)*q+k*(p0+p1*x)


def reduced(t,B):
    return t-B*sigmoid(t)


def crossings(B):
    assert B>4
    d=sqrt(1-4/B)
    u=log((1+d)/(1-d))
    return -u,u,reduced(u,B),reduced(-u,B)


def targets(T,Q,a,b,c,p0,k):
    return T-a*b+a*c*(Q-k*p0)/(1-k)


def roots(z,B):
    if B>4:
        t1,t2,low,high=crossings(B)
        if low<z<high:
            return [brentq(lambda t:reduced(t,B)-z,-100,t1),
                    brentq(lambda t:reduced(t,B)-z,t1,t2),
                    brentq(lambda t:reduced(t,B)-z,t2,100)]
    return [brentq(lambda t:reduced(t,B)-z,-100,100)]


def test():
    t,q,a,b,c,p0,p1,k=sp.symbols('t q a b c p0 p1 k',real=True)
    x=sp.symbols('x',real=True)
    J=sp.Matrix([[1-a*x*(1-x),-a*c],
                 [k*p1*x*(1-x),1-k]])
    expected=(1-k)*(1-a*(1-c*k*p1/(1-k))*x*(1-x))
    assert sp.simplify(J.det()-expected)==0
    z=sp.symbols('z',real=True)
    S=1/(1+sp.exp(-z))
    assert sp.series(z-4*S,z,0,6).removeO().expand()==-2+z**3/12-z**5/120
    checks=0
    rng=random.Random(137)
    for i in range(400):
        a=rng.uniform(0.1,60)
        k=rng.uniform(0.05,0.95)
        c=rng.uniform(0.02,5)
        p1=rng.uniform(0.002,0.2)
        b=rng.uniform(0.1,0.9)
        p0=rng.uniform(0,0.1)
        ti=rng.uniform(-7,7)
        qi=rng.uniform(0,1)
        T,Q=map_logit(ti,qi,a,b,c,p0,p1,k)
        B=a*(1-c*k*p1/(1-k))
        zvalue=targets(T,Q,a,b,c,p0,k)
        assert abs(reduced(ti,B)-zvalue)<2e-12
        found=False
        if B<=4:
            sol=roots(zvalue,B)
            found=abs(sol[0]-ti)<2e-9
        else:
            # In the three-root strip, recover all real branches; elsewhere one branch.
            tminus,tplus,lo,hi=crossings(B)
            if lo+1e-10 < zvalue < hi-1e-10:
                sol=roots(zvalue,B)
                found=any(abs(s-ti)<2e-9 for s in sol)
            else:
                found=abs(reduced(ti,B)-zvalue)<2e-12
        assert found,(i,B,ti,zvalue)
        checks+=1
    # Explicitly demonstrate two distinct admissible preimages near a fold.
    a,b,c,p0,p1,k=20,.3,.5,.01,.2,.1
    B=a*(1-c*k*p1/(1-k))
    assert B>4
    tminus,tplus,lo,hi=crossings(B)
    q0=.5
    T0,Q0=map_logit(tminus,q0,a,b,c,p0,p1,k)
    z0=targets(T0,Q0,a,b,c,p0,k)
    zz=z0-1e-5
    rr=roots(zz,B)
    assert len(rr)==3
    close=sorted(rr,key=lambda t:abs(t-tminus))[:2]
    assert close[0]!=close[1]
    qvals=[(Q0-k*p0-k*p1*sigmoid(t))/(1-k) for t in close]
    assert all(0<q<1 for q in qvals)
    obs=[map_logit(t,q,a,b,c,p0,p1,k) for t,q in zip(close,qvals)]
    assert abs(obs[0][0]-obs[1][0])<1e-9 and abs(obs[0][1]-obs[1][1])<1e-12
    checks+=1
    # Universal three-to-one image strip and opening coefficient.
    for B in [4.01,4.1,4.5,5,9,30,100]:
        tminus,tplus,lo,hi=crossings(B)
        assert hi>lo and len(roots((lo+hi)/2,B))==3
        checks+=1
    for eps in [1e-2,1e-3,1e-4]:
        _,_,lo,hi=crossings(4+eps)
        assert abs((hi-lo)/eps**1.5-1/3)<0.002
        checks+=1
    # The published example has no fold at any positive learning intensity.
    c,p1,k=500,.001,.865
    assert c*k*p1>1-k
    for a in [.1,4,20,100,1000]:
        B=a*(1-c*k*p1/(1-k))
        assert B<0
        for xx in [.01,.25,.5,.8,.99]:
            assert (1-k)*(1-B*xx*(1-xx))>0
            checks+=1
    print('PASS symbolic Jacobian and critical cubic series; finite numerical assertions:',checks)

if __name__=='__main__':
    test()
