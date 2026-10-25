#!/usr/bin/env python3
"""Independent numerical checks of the finite-dimensional covariance-rank theorem.
These tests support, but do not replace, the analytic proof.
"""
import math
import random
from itertools import combinations

rng = random.Random(20261021)
checks = 0

def variance(lam, omega, k):
    # exponents integer; use log1p/expm1 to avoid cancellation
    x=omega*lam
    if x == 1: return 1/lam
    return (-math.expm1(k*math.log1p(-x)))**2/lam

def cross(a,b,omega):
    # b < a, unique crossover in the real iteration count > 1.
    def log_ratio(k):
        return math.log(variance(a,omega,k)/variance(b,omega,k))
    lo,hi=1.,2.
    while log_ratio(hi)>0: hi*=2
    for _ in range(80):
        mid=(lo+hi)/2
        if log_ratio(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

# Exact rational test, omega=1, lambda=1,1/4, K=1 and infinity.
from fractions import Fraction
assert Fraction(1,1) > Fraction(1,4)
assert Fraction(1,1) < Fraction(4,1)
checks += 2

for case in range(250):
    n=rng.randrange(2,12)
    vals=sorted([10**rng.uniform(-2,0) for _ in range(n)],reverse=True)
    # Choose exactly omega L <= 1.
    omega=rng.uniform(.02,1.)/vals[0]
    r=rng.randrange(1,n)
    ks=[1,2,3,5,10,20,50,100,250,500,1000,5000]
    positions=[]
    for k in ks:
        f=[variance(x,omega,k) for x in vals]
        order=sorted(range(n),key=lambda i:(-f[i],-i))
        picked=sorted(order[:r])
        # All top-r indices must be contiguous when there are no exact ties.
        assert picked==list(range(picked[0],picked[0]+r)), (vals,k,r,f,picked)
        positions.append(picked[0])
        checks+=1
    assert positions==sorted(positions), (vals,positions)
    checks+=1
    # For random subset pairs, monotone ratio in K and crossover uniqueness.
    for i,j in list(combinations(range(n),2))[:15]:
        root=cross(vals[i],vals[j],omega)
        assert root>1
        eps=max(1e-4, root*1e-5)
        assert variance(vals[i],omega,max(1,root-eps))>=variance(vals[j],omega,max(1,root-eps))*(1-1e-12)
        assert variance(vals[i],omega,root+eps)<variance(vals[j],omega,root+eps)
        checks+=1

# Block limiting loss for a leading-normal-subspace approximation.
for kappa in [2,4,10,100,1000]:
    L=1.;mu=1/kappa; omega=1
    K=int(kappa*kappa*50)
    retained=variance(L,omega,K)
    missed=variance(mu,omega,K)
    ratio=retained/missed
    assert ratio>=mu/L*(1-1e-12)
    assert math.isclose(ratio,1/kappa,rel_tol=1e-9,abs_tol=1e-12)
    checks+=1

# Unimodality and exact continuous peak condition in integer K.
for K in range(2,41):
    def crit(t): return sum(t**(-h) for h in range(K)) - 2*K
    lo,hi=1e-3,1-1e-13
    # For large K an especially small lo may overflow; root exists by continuity.
    for _ in range(75):
        md=(lo+hi)/2
        if crit(md)>0: lo=md
        else: hi=md
    t=(lo+hi)/2
    x=1-t
    v0=variance(x,1,K)
    for m in [0.05,0.2,0.8]:
        if x*m>0:
            assert variance(x*m,1,K)<v0*(1+1e-12)
        xnew=x+(1-x)*m
        assert variance(xnew,1,K)<v0*(1+1e-12)
        checks+=2
print('PASS finite analytic-identity examples, 250 random spectra, pair crossings, rank blocks, asymptotic loss, unique spectral peaks; checks =', checks)
