"""Numerical and algebraic crosschecks for triangular boundary diameter crossover.
Requires NumPy and SciPy. Run: python verify.py
"""
from fractions import Fraction
import math
import numpy as np
from scipy.stats import qmc


def rates(c):
    a=1-c*c/2
    P=2+c
    ka=(1+1/a)/P
    kb=(1+2/c)/P
    assert abs(kb-1/c)<1e-12
    assert abs(ka-(2-c)/(2-c*c))<1e-12
    return a,P,ka,kb


def cdf_unique(t,ka,kb):
    if t<=0:return 0.0
    return 1-(kb*math.exp(-ka*t)-ka*math.exp(-kb*t))/(kb-ka)


def limit_samples(c,lam,m=19,seed=2026):
    a,P,ka,kb=rates(c)
    x=qmc.Sobol(d=4,scramble=True,seed=seed).random_base2(m)
    X=-P*np.log1p(-x[:,0]);Y=-P*np.log1p(-x[:,1])
    B=-np.log1p(-x[:,2])/kb;C=-np.log1p(-x[:,3])/kb
    return np.minimum(np.minimum(X,a*Y)+B,lam+np.minimum(Y,a*X)+C),X,Y


def finite_diameter(c,lam,n,reps=8000,seed=991):
    rng=np.random.default_rng(seed)
    AC=1-lam/n
    assert c>lam/n and AC>0
    xx=(1+AC**2-c*c)/2
    cc=np.array([xx,math.sqrt(AC*AC-xx*xx)])
    vertices=np.array([[0.,0.],[1.,0.],cc])
    edges=np.array([[0,1],[1,2],[2,0]])
    L=np.array([1.,c,AC]);per=L.sum();cum=np.cumsum(L)
    out=np.empty(reps)
    for j in range(reps):
        arc=rng.random(n)*per
        typ=np.searchsorted(cum,arc,side='right')
        ts=np.array([arc[typ==k]-(cum[k-1] if k else 0) for k in range(3)],dtype=object)
        pts=[]
        for k in range(3):
            if len(ts[k]):
                v0=vertices[edges[k,0]];v1=vertices[edges[k,1]]
                for t in (np.min(ts[k]),np.max(ts[k])):
                    pts.append(v0+(v1-v0)*t/L[k])
        v=np.array(pts)
        dist=np.sqrt(np.max(np.sum((v[:,None,:]-v[None,:,:])**2,axis=-1)))
        out[j]=n*(1-dist)
    return out


def check():
    for c in (0.25,0.5,0.85):
        a,P,ka,kb=rates(c)
        assert 0<a<1 and kb>ka
        # Joint-survival formula and exact correlation: a(2-a).
        rng=np.random.default_rng(110)
        X=rng.exponential(P,350000);Y=rng.exponential(P,350000)
        U=np.minimum(X,a*Y);V=np.minimum(Y,a*X)
        assert abs(np.mean(U)-1/ka)<.018
        assert abs(np.corrcoef(U,V)[0,1]-a*(2-a))<.008
        for u,v in ((0.2,0.6),(0.8,0.4)):
            surv=math.exp(-(max(u,v/a)+max(v,u/a))/P)
            assert abs(np.mean((U>u)&(V>v))-surv)<.004
    c=.5;lam=.7;a,P,ka,kb=rates(c)
    ws,X,Y=limit_samples(c,lam,m=20)
    for t in (.2,.5,.7):
        assert abs(np.mean(ws<=t)-cdf_unique(t,ka,kb))<.003
    # Sharp quadratic channel onset using conditional integration of B and C.
    U=np.minimum(X,a*Y);V=np.minimum(Y,a*X)
    lead=ka*kb*math.exp(-kb*lam)/2
    values=[]
    for h in (.1,.05,.025):
        d=np.mean((-np.expm1(-kb*np.maximum(h-V,0)))*np.exp(-kb*np.maximum(lam+h-U,0)))
        values.append(d/(h*h))
    assert abs(values[-1]-lead)<.025,(values,lead)
    assert values[0]<values[1]<values[2]<lead
    for lam,n in ((0.0,350),(0.7,350),(0.7,900)):
        finite=finite_diameter(.5,lam,n,reps=8000,seed=123+n+int(lam*10))
        limit,_,_=limit_samples(.5,lam,m=19,seed=334)
        for t in (.6,1.2,2.0):
            err=abs(np.mean(finite<=t)-np.mean(limit<=t))
            assert err<.035,(lam,n,t,err)
    print('VERIFY_OK rate_identities=6 joint_law=6 correlation=3 onset=3 finite_sample_comparisons=9')

if __name__=='__main__':
    check()
