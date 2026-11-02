#!/usr/bin/env python3
"""Standalone arithmetic checks for finite-tumble trapped persistent-motion threshold theorem.
No assertions here certify an infinite-time limit; see the analytic argument in RESULT.md.
"""
from fractions import Fraction as F
from math import gamma, pi, isclose
import random

def poch(q,k):
    x=F(1)
    for j in range(k): x*=q+j
    return x

def even_plus(k,a,b):
    pi_plus=b/F(2*(a+b))
    return pi_plus*poch(F(1,2),k)*poch(1+b/2,k)/(poch(1+(a+b)/2,k)*poch((1+a)/2,k))

def even_zero(k,a,b):
    pi_zero=a/(a+b)
    return pi_zero*poch(F(1,2),k)*poch(b/2,k)/(poch(1+(a+b)/2,k)*poch((1+a)/2,k))

def negative_moment_constant(a,b):
    return gamma(1+(a+b)/2)/(gamma(1+a/2)*gamma(1+b/2))

def intensity(a,b):
    return a*b/(2*(a+b))*negative_moment_constant(a,b)

checks=0
for aa,bb in [(F(1),F(1)),(F(2),F(1)),(F(1,2),F(3,2)),(F(3,2),F(1,3)),(F(3),F(2))]:
    mplus={0:bb/(2*(aa+bb))}
    mzero={0:aa/(aa+bb)}
    for n in range(1,41):
        if n%2:
            mp=n*mplus[n-1]/(n+aa)
            mplus[n]=mp
        else:
            # Three-state stationary-generator linear equations for even moments.
            mp=n*mplus[n-1]*(n+bb)/(n*(n+aa+bb))
            mplus[n]=mp
            mz=2*aa*mp/(n+bb)
            mzero[n]=mz
            assert (n+aa)*mp == n*mplus[n-1]+bb*mz/2
            assert (n+bb)*mz == 2*aa*mp
            checks+=2
            assert mp==even_plus(n//2,aa,bb)
            assert mz==even_zero(n//2,aa,bb)
            checks+=2
    a,b=float(aa),float(bb)
    H=negative_moment_constant(a,b)
    assert H>0
    # The series of the stationarity-derived negative moment is a Gauss hypergeometric sum.
    import mpmath as mp
    mp.mp.dps=45
    H_mp=mp.hyper([mp.mpf(str(a/2)),mp.mpf(str(b/2))],[1+mp.mpf(str((a+b)/2))],1)
    assert abs(float(H_mp)-H)<1e-10
    checks+=1

# Exact landmarks, independent of any floating-density approximation.
assert isclose(intensity(1,1),1/pi,rel_tol=1e-13)
assert isclose(intensity(2,1),1/2,rel_tol=1e-13)
checks+=2

# Simulated marked run-start chain: explicit random switching, not stationary-density sampling.
# Run starts +; each + run of duration Exp(a) followed by 0 and zero or more - runs.
# Check rare-event probabilities and approximate exponential event count for moderate delta.
random.seed(41242)
a=b=1.0
N=20000
delta=0.025
x=0.0
counts=[]
succ=0
success_lengths=[]
for j in range(N):
    t=0
    while True:
        s=random.expovariate(a)
        boundary_time=max(0.0,__import__('math').log((1-x)/delta))
        if s>=boundary_time:
            counts.append(t+1)
            success_lengths.append(boundary_time)
            break
        x=1+(x-1)*__import__('math').exp(-s)
        t+=1
        x=x*__import__('math').exp(-random.expovariate(b))
        if random.random()<.5:
            continue
        while True:
            tm=random.expovariate(a)
            x=-1+(x+1)*__import__('math').exp(-tm)
            x=x*__import__('math').exp(-random.expovariate(b))
            if random.random()<.5:
                break
        # then next + run
    # after a successful + run, restart at x=0 to generate another trial; this block is
    # diagnostic of rare-event cycle cost, not a stationary test.
    x=0.0
p0=delta*negative_moment_constant(a,b)
mean=sum(counts)/len(counts)
assert mean>1 and mean<5/p0
checks+=1
# One concrete full simulated stationary + entry test of the moment-product distribution.
rng=random.Random(71)
M=80000
ss=0.0
for _ in range(M):
    U=rng.betavariate(.5,a/2)
    V=rng.betavariate(b/2,1+a/2)
    X=(1 if rng.random()<.5 else -1)*(U*V)**.5
    ss+=min(1,(delta/(1-X))**a)
p_emp=ss/M
assert abs(p_emp/p0-1)<.10  # first correction at delta=.025 is nonzero
checks+=1
print('VERIFIER PASS',checks,'exact/analytic/test assertions','alpha=beta=1 rate=',intensity(1,1),'delta=',delta,'empirical run-start success=',p_emp,'asymptotic=',p0,'trial mean runs=',mean)
