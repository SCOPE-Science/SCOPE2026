#!/usr/bin/env python3
"""Numerical crosschecks for Shannon entropy vs uniform-spacing exceedance counts.

Requires numpy and scipy. The analytic proof is in RESULT.md; these finite checks
are corroboration, not infinite-dimensional certification.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import exp1

GAMMA = 0.5772156649015328606065120900824

def q(m,x):
    mu = sum(1/j for j in range(1,m+1))-1
    hm=mu-1/m
    h=-(x*math.log(x) if x>0 else 0.)-((1-x)*math.log1p(-x) if x<1 else 0.)
    return h+(1-x)*hm

def covariance(m,t):
    mu=sum(1/j for j in range(1,m+1))-1
    return m*(m-1)*quad(lambda x:(q(m,x)-mu)*(1-x)**(m-2),t,1,epsabs=3e-12,epsrel=3e-12)[0]

def F(c):
    return math.exp(-c)*((2-GAMMA-math.log(c))*(c+1)-2)-exp1(c)

cstar=brentq(F,1,2,xtol=1e-14)
assert abs(cstar-1.700321026132689)<1e-11
check_count=0
for m in (2,3,4,5,8,10,20,30,50,100,200):
    root=brentq(lambda t:covariance(m,t), 0.05/m, min(.98,6/m),xtol=3e-13)
    assert 0<root<1
    assert covariance(m, root*.5)>1e-6
    assert covariance(m, min(root*1.3, .99)) < -1e-9
    for c in (.2,.6,1,1.5,1.7,2.2,3):
        t=c/m
        if t<1:
            v=covariance(m,t)
            assert (v>0)==(t<root) if abs(t-root)>1e-9 else True
            check_count+=1
    print(f'm={m:3d}, t_m={root:.12g}, m*t_m={m*root:.12g}')
assert abs(brentq(lambda t:covariance(2,t),.1,.9)-.5)<1e-9
assert abs(200*brentq(lambda t:covariance(200,t),.001,.03)-cstar)<.02

# Independent representation: simulate Dirichlet spacings from normalized iid Gamma(1).
rng=np.random.default_rng(8901)
for m,t in [(3,.2),(3,.6),(5,.2),(5,.4),(10,.08),(10,.22)]:
    xs=rng.exponential(size=(180000,m)); xs/=xs.sum(axis=1)[:,None]
    h=-(xs*np.log(xs)).sum(axis=1)
    n=(xs>t).sum(axis=1)
    est=np.mean((h-h.mean())*(n-n.mean()))
    exact=covariance(m,t)
    se=np.std((h-h.mean())*(n-n.mean()),ddof=1)/math.sqrt(len(h))
    assert abs(est-exact)<5.5*se+0.0025,(m,t,est,exact,se)
    print(f' MC m={m:2d}, t={t:.2f}, sample_cov={est:+.6f}, formula={exact:+.6f}, SE={se:.6f}')
print('PASS finite integration, signs, asymptotic root, and independent Monte Carlo;',check_count,'threshold evaluations; c*=',cstar)
