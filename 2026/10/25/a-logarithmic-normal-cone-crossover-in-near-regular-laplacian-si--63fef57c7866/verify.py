#!/usr/bin/env python3
"""Reproduce finite support identities and numerical crossover diagnostics.
No simulation is treated as proof of a limiting theorem.
"""
import math
import numpy as np
from scipy.special import ndtri, expit

def one_check(p,q,g):
    n=p+q
    adj=np.zeros((n,n),dtype=np.float64)
    adj[:p,p:]=1
    adj[p:,:p]=1
    lap=np.diag(adj.sum(axis=1))-adj
    vals=lap@g
    a=q*g[:p]-g[p:].sum()
    b=p*g[p:]-g[:p].sum()
    assert np.allclose(vals,np.r_[a,b],atol=1e-10)
    g0=g-g.mean()
    assert np.allclose(vals,lap@g0,atol=1e-10)
    sph=np.ptp(vals)/np.linalg.norm(g0)
    assert np.isclose(sph, (max(a.max(),b.max())-min(a.min(),b.min()))/np.linalg.norm(g0))
    return float(sph)

def finite_check():
    rng=np.random.default_rng(20261020)
    cases=0
    for p in range(2,10):
      for q in range(2,10):
       for _ in range(5):
        one_check(p,q,rng.standard_normal(p+q));cases+=1
    return cases

def monte(n,tau_target,trials=3500,seed=42):
    rng=np.random.default_rng(seed)
    b=ndtri(1-2/n)
    d=int(round((tau_target*n/(2*b*b))/2))*2
    p=(n-d)//2; q=(n+d)//2
    tau=2*d*b*b/n
    s=n/(2*b)
    wt=[]; upper=[]; lower=[]
    for i in range(0,trials,50):
        z=rng.standard_normal((min(50,trials-i),n))
        a=q*z[:,:p]-z[:,p:].sum(axis=1,keepdims=True)
        c=p*z[:,p:]-z[:,:p].sum(axis=1,keepdims=True)
        hi_a=a.max(axis=1);hi_c=c.max(axis=1)
        lo_a=a.min(axis=1);lo_c=c.min(axis=1)
        hi=np.maximum(hi_a,hi_c)
        lo=np.minimum(lo_a,lo_c)
        upper.extend(hi_a>hi_c)
        lower.extend(lo_a<lo_c)
        sphere=(hi-lo)/np.sqrt(((z-z.mean(axis=1,keepdims=True))**2).sum(axis=1))
        wt.extend((np.sqrt(n)*sphere-n*b)/s)
    theo_class=expit(tau)
    theo_mean=2*np.euler_gamma+2*np.log(2*np.cosh(tau/2))
    return {'n':n,'p':p,'q':q,'tau_actual':round(tau,5),'class_probability_theory':round(float(theo_class),4),'class_plus_empirical':round(float(np.mean(upper)),4),'class_minus_empirical':round(float(np.mean(lower)),4),'width_centered_mean_theory':round(float(theo_mean),4),'width_centered_mean_empirical':round(float(np.mean(wt)),4)}

if __name__=='__main__':
    print('FINITE_SUPPORT_PASS',finite_check())
    for t in [-1.,0.,1.]: print('CROSSOVER_DIAGNOSTIC',monte(6000,t))
