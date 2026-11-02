#!/usr/bin/env python3
"""Finite-arithmetic checks and reproducible simulations for geometric occupancy norms.
Scientific statements and assumptions are in RESULT.md. No finite experiment proves a limit theorem.
"""
from fractions import Fraction as F
from math import log, sqrt
import numpy as np

assertions=0

def check(x):
    global assertions
    assert x
    assertions+=1

# Exact norm identity in finite test cases with geometric masses 1/2,1/4,...
# Count the unobserved infinite tail exactly as sum p_j = 2^-J.
for n in (1,2,3,4,5,8,11,17):
    for x1 in range(n+1):
        for x2 in range(n-x1+1):
            x3=n-x1-x2
            counts=[x1,x2,x3]
            masses=[F(1,2),F(1,4),F(1,8)]
            for r in (2,3,4):
                direct=sum(p*abs(F(k,n)/p-1)**r for k,p in zip(counts,masses))+F(1,8)
                through=sum(abs(F(k)-n*p)**r/(n**r*p**(r-1)) for k,p in zip(counts,masses))+F(1,8)
                check(direct==through)
                if r==2:
                    check(direct>=0)

# Exact binomial expectation E[(N-np)^2/(np)] = 1-p.
from math import comb
for n in (1,2,3,5,9,13):
    for p in (F(1,2),F(1,4),F(1,8),F(3,7)):
        val=sum(F(comb(n,k))*p**k*(1-p)**(n-k) * (F(k)-n*p)**2/(n*p) for k in range(n+1))
        check(val==1-p)

# geometric phase endpoint: tau=1/rho shifts all bi-infinite intensities by 1 index.
for rho in (F(1,2),F(2,3),F(3,4)):
    for k in range(-8,9):
        check(rho**(k-1)==(1/rho)*rho**k)

# Simulation checks: stationary phase n=2^k for p_j=2^-j.
rng=np.random.default_rng(20261026)
prob=np.array([2.0**(-j) for j in range(1,61)],float)
probs=np.r_[prob,2.0**-60]
check(abs(probs.sum()-1)<1e-15)
print('simulation: nominal critical constant 1/log(2)=%.10f' % (1/log(2)))
for n in (2**12,2**16):
    sample=rng.multinomial(n,probs,size=3000)
    check(np.all(sample[:,-1]==0))
    mu=n*prob[None,:]
    diff=np.abs(sample[:,:60]-mu)
    chi=np.sum(diff**2/mu,axis=1)+n*(2.0**-60)
    cubic=np.sum(diff**3/mu**2,axis=1)+n*(2.0**-60)
    chi_scaled=chi/log(n)
    print('n=%d: critical n*Delta_2^2/log(n) median=%.6f, p10=%.6f, p90=%.6f' % (n,*np.quantile(chi_scaled,[.5,.1,.9])))
    print('n=%d: cubic n*Delta_{3/2}^3 median=%.6f, p10=%.6f, p90=%.6f' % (n,*np.quantile(cubic,[.5,.1,.9])))
    check(np.isfinite(np.median(chi_scaled)))
    check(np.isfinite(np.median(cubic)))
print('FINITE_CHECKS_PASSED=%d' % assertions)
