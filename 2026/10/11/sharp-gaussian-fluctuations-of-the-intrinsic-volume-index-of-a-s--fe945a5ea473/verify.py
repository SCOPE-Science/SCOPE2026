#!/usr/bin/env python3
"""Numerical, finite-case checks of the stated geometric cone calculation."""
import numpy as np
from scipy.special import ndtr
from scipy.optimize import brentq, nnls
from scipy.stats import norm

rng=np.random.default_rng(718283)

def h(t):
    return norm.pdf(t)-t*norm.sf(t)

def threshold(m):
    return brentq(lambda t:m*h(t)-t,0.,max(10.,np.sqrt(2*np.log(m))+5.),xtol=1.e-12)

def face_count(z,g0):
    ordered=np.sort(z)[::-1]
    sums=np.cumsum(ordered)
    k=np.arange(1,len(z)+1)
    scores=(sums-g0)/(k+1)
    valid=ordered>scores
    return int(np.sum(valid))

def bisection_root(z,g0):
    lo=min(float(np.min(z))-abs(g0)-5.,-abs(g0)-5.)
    hi=max(float(np.max(z))+abs(g0)+5.,abs(g0)+5.)
    return brentq(lambda s: np.sum(np.maximum(0.,z-s))-g0-s,lo,hi,xtol=1.e-12)

checks=0
for m in [1,2,3,5,13,70]:
    for _ in range(80):
        z=rng.standard_normal(m)
        g0=float(rng.standard_normal())
        s=bisection_root(z,g0)
        k=face_count(z,g0)
        assert k==np.sum(z>s), (m,k,s)
        a=np.maximum(z-s,0.)
        assert abs(float(np.sum(a))-g0-s)<2.e-9
        # Projection is optimal if active ray normal products vanish and inactive are nonnegative.
        grad=s-z+a
        if np.any(a>1.e-9):
            assert np.max(np.abs(grad[a>1.e-9])) <2.e-8
        if np.any(a<=1.e-9):
            assert np.min(grad[a<=1.e-9])>=-2.e-8
        checks+=1

# Compare face dimension with an independent nonnegative least-squares solution.
for m in [2,3,5]:
    mat=np.zeros((m+1,m))
    mat[0,:]=1.
    for i in range(m):mat[i+1,i]=-1.
    for _ in range(20):
        g=rng.standard_normal(m+1)
        coef,_=nnls(mat,g)
        count_nnls=int(np.sum(coef>1.e-7))
        count_root=face_count(-g[1:],g[0])
        assert count_nnls==count_root
        checks+=1

for m in [20,200,2000]:
    t=threshold(m)
    lam=m*norm.sf(t)
    assert abs(m*h(t)-t)<2.e-8
    assert t>0 and lam>0
    for _ in range(12):
        z=rng.standard_normal(m)
        g0=float(rng.standard_normal())
        s=bisection_root(z,g0)
        assert np.sum(z>s)==face_count(z,g0)
        checks+=1
    print(f'm={m}: threshold={t:.8f}; lambda={lam:.8f}; 2log(m)={2*np.log(m):.8f}')

# Finite Monte Carlo moments are diagnostics, not proofs of the asymptotic law.
for m,samples in [(200,1800),(2000,1000),(10000,240)]:
    j=np.empty(samples,dtype=np.int32)
    for i in range(samples):
        zz=rng.standard_normal(m)
        gg=float(rng.standard_normal())
        j[i]=face_count(zz,gg)
    t=threshold(m)
    print(f'finite MC m={m}: mean={j.mean():.5f}, var={j.var():.5f}, '+
          f'lambda={m*norm.sf(t):.5f}, 2t^2={2*t*t:.5f}')
    checks+=samples

# The exact truncated normal identity must agree with numerical quadrature.
from scipy.integrate import quad
for t in [0.,.5,2.,4.]:
    numerical=quad(lambda x:(x-t)*norm.pdf(x),t,np.inf,epsabs=1.e-12)[0]
    assert abs(numerical-h(t))<2.e-12
    checks+=1
print('VERIFY_OK',checks)
