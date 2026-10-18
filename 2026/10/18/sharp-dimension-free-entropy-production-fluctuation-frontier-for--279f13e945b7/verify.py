#!/usr/bin/env python3
"""Reproduce independent tests of the Gaussian relative-information variance frontier."""
import math
import numpy as np
from scipy.optimize import brentq

checks = 0

def check(condition, label):
    global checks
    assert bool(condition), label
    checks += 1

def h(u):
    return u - 1.0 - math.log(u)

def endpoints(k):
    assert k>0
    lo = brentq(lambda u: h(u)-2*k, math.exp(-2*k-2), 1.0-1e-14, xtol=1e-15)
    upper = 2.0
    while h(upper) <= 2*k:
        upper *= 2.0
    hi = brentq(lambda u: h(u)-2*k, 1+1e-14, upper, xtol=1e-13)
    return lo, hi

def frontier(k):
    a,b = endpoints(k)
    return .5*(1-a)**2, .5*(b-1)**2

rng=np.random.default_rng(19429)
for d in (1,2,3,5,10):
    for trial in range(100):
        # Independent covariance, vector and log likelihood expansion.
        U=rng.normal(size=(d,d)) / math.sqrt(d)
        C=U@U.T+np.eye(d)*0.7
        H=np.linalg.inv(C)
        m=rng.normal(size=d)
        eigen=np.linalg.eigvalsh(H)
        K=0.5*(np.trace(H)-d-np.linalg.slogdet(H)[1]+m@H@m)
        V=0.5*np.trace((H-np.eye(d))@(H-np.eye(d)))+m@(H@H)@m
        lower,upper=frontier(K)
        check(lower-1e-9<=V<=upper+1e-9, f'Gaussian pair outside frontier d={d}, test={trial}')
        check(abs(K-(.5*sum(float(h(u)) for u in eigen)+.5*m@H@m))<1e-9, 'KL spectral decomposition')
        check(abs(V-(.5*sum((float(u)-1)**2 for u in eigen)+m@(H@H)@m))<1e-9, 'variance spectral decomposition')
for k in (0.02,0.1,0.5,1,3,8):
    low,high=endpoints(k)
    for u in (low, low+.25*(high-low),low+.5*(high-low),low+.75*(high-low),high):
        q=max(0.0,2*k-h(u)); m=math.sqrt(q/u)
        kk=.5*(h(u)+u*m*m)
        vv=.5*(u-1)**2+u*u*m*m
        fminus,fplus=frontier(k)
        check(abs(kk-k)<1e-9,'fixed-K one-mode parametrization')
        check(fminus-1e-10<=vv<=fplus+1e-10,'every interpolant in interval')
    check(abs(frontier(k)[0]-.5*(1-low)**2)<1e-12,'lower endpoint')
    check(abs(frontier(k)[1]-.5*(high-1)**2)<1e-12,'upper endpoint')
for k in (0.1,0.3,1,2,5):
    a,b=frontier(k)
    check(a<2*k<b,'strict separation from translation-only information variance')

# Direct sample test: independently evaluate log density ratio for two general covariance matrices.
for d in (1,2,3,4):
    A=rng.normal(size=(d,d))
    C=A@A.T+np.eye(d)
    B=rng.normal(size=(d,d))
    G=B@B.T+np.eye(d)
    m=rng.normal(size=d)
    invC=np.linalg.inv(C); invG=np.linalg.inv(G)
    _,lc=np.linalg.slogdet(C);_,lg=np.linalg.slogdet(G)
    t=rng.multivariate_normal(np.zeros(d),C,size=120000)
    dif=t-m
    ln=-0.5*(lc-lg)-0.5*np.sum((t@invC)*t,axis=1)+0.5*np.sum((dif@invG)*dif,axis=1)
    H=np.linalg.solve(np.linalg.cholesky(C), G)
    W=np.linalg.solve(np.linalg.cholesky(C), H.T).T  # transformed covariance
    # Use direct trace for reference independent of the whitening calculation.
    M=invG@C
    k=.5*(np.trace(M)-d+lc*0-lg*0+lg-lc+m@invG@m)
    v=.5*np.trace((M-np.eye(d))@(M-np.eye(d)))+m@invG@C@invG@m
    check(abs(np.mean(ln)-k)<0.05+0.025*k,'sampled mean log-likelihood')
    check(abs(np.var(ln)-v)<0.07+0.05*v,'sampled log-likelihood variance')

if __name__=='__main__':
    for K in (0.1,1,8):
        a,b=endpoints(K)
        lo,hi=frontier(K)
        print('K=',K,'u_minus=',a,'u_plus=',b,'V_interval=',(lo,hi))
    print('PASS',checks,'independent tests')
