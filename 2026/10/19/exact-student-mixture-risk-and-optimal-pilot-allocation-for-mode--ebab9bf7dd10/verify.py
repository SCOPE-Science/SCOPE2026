#!/usr/bin/env python3
"""Reproducible checks for a two-stage Gaussian OLS difference-estimator theorem.
Checks are finite diagnostic tests; the theorem requires its analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt, isclose, gamma, pi
import random

checks=0

def check(x):
    global checks
    assert x
    checks += 1

# Enumerate actual residual-stage subsets with a fixed, deterministic pilot model.
# Conditional mean and finite-population variance are exact rational identities.
for N in range(5, 13):
    for a in range(1, N-2):
        vals=[F((i*i+3*i+7)%13-6,5) for i in range(N)]
        preds=[F((4*i+5)%9-4,7) for i in range(N)]
        errs=[x-z for x,z in zip(vals,preds)]
        L=N-a
        target=sum(vals,F(0))/N
        for b in range(1,min(L,5)):
            results=[]
            for S in combinations(range(a,N),b):
                estimate=(sum(vals[:a],F(0))+sum(preds[a:],F(0))+
                          F(L,b)*sum((errs[i] for i in S),F(0)))/N
                results.append(estimate)
            mu=sum(results,F(0))/len(results)
            var=sum(((z-mu)**2 for z in results),F(0))/len(results)
            ebar=sum(errs[a:],F(0))/L
            S2=sum(((z-ebar)**2 for z in errs[a:]),F(0))/(L-1)
            expected=F(L*(L-b),N*N*b)*S2
            check(mu==target)
            check(var==expected)

# Exact integer minimization and positivity of the unique derivative root.
for p in range(1,12):
    for B in range(p+3,p+35):
        for N in [B+1,B+2,2*B,20*B]:
            L=N-1; c=B-1
            t=p*c*L/(p*c+sqrt(p*c*(L-c)*(L-p)))
            check(p<t<c)
            def risk(a):
                return F((N-a)*(a-1),(B-a)*(a-p-1))
            domain=range(p+2,B)
            best=min(risk(a) for a in domain)
            near={max(p+2,min(B-1, int(1+t))), max(p+2,min(B-1, int(1+t)+1))}
            check(min(risk(a) for a in near)==best)
            cmin=F(B,N)*best
            check(cmin>1)

# Independent formulas for moments via a beta variable and the q=2 simplification.
for p in range(1,9):
    for a in range(p+2,p+20):
        nu=a-p+1
        # E[(1+V/U)] for independent chi-square V,U
        beta_ratio=gamma((nu-2)/2)*gamma((nu+p)/2)/(gamma(nu/2)*gamma((nu+p-2)/2))
        check(isclose(beta_ratio, (a-1)/(a-p-1), rel_tol=3e-13))

# Gaussian pilot OLS plus a random residual sample: observed mean squared error
# agrees with the unconditional finite-N analytic prediction.
try:
    import numpy as np
    rng=np.random.default_rng(13071)
    for (N,p,B,a) in [(31,2,12,7),(37,1,14,8),(55,3,22,11)]:
        b=B-a; rep=70000
        errs=np.empty(rep)
        for j in range(rep):
            X=rng.standard_normal((N,p))
            eps=rng.standard_normal(N)
            g=eps+X@np.arange(1,p+1)
            fit=np.linalg.lstsq(X[:a],g[:a],rcond=None)[0]
            pred=X@fit
            S=rng.choice(N-a,b,replace=False)+a
            est=(g[:a].sum()+pred[a:].sum()+((N-a)/b)*(g[S]-pred[S]).sum())/N
            errs[j]=est-g.mean()
        theory=(N-a)*(N-B)/(N*N*b)*(a-1)/(a-p-1)
        sample=(errs**2).mean()
        check(abs(sample/theory-1)<.09)
        print('Monte Carlo p,N,B,a',p,N,B,a,'observed/theory',round(sample/theory,5))
except ImportError:
    print('NumPy unavailable; analytic/rational checks completed')
print('PASS',checks,'checks')
