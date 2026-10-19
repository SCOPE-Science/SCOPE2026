#!/usr/bin/env python3
"""Independent numerical probes of a kurtosis envelope for a reset telegraph trap.

Uses standard-library arithmetic, a renewal-path simulator, direct generator
balances, and global one-dimensional optimization on finite test grids.
Simulation is supplementary; exact inequalities have separate analytic proofs.
"""
import math
import random

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def close(a,b,tol=1e-10):
    return abs(a-b) <= tol * max(1.0,abs(a),abs(b))

def qc(g):
    return (1-g+math.sqrt((g+1)**2+12))/2

def v0(q,g):
    return 2/((q+2)*(q+g+1))

def variance(q,g,x):
    return (2/(q+g+1)+q*x)/(q+2)

def fourth(q,g,x,y):
    return (12*variance(q,g,x)/(q+g+3)+q*y)/(q+4)

def lower_k(q,g,x):
    return fourth(q,g,x,x*x)/variance(q,g,x)**2

def kinfty(q):
    return (q+2)**2/(q*(q+4))

def xopt(q,g):
    delta=3-(q-1)*(q+g)
    return 3/delta if q<qc(g) else math.inf

def kopt(q,g):
    if q>=qc(g): return kinfty(q)
    delta=3-(q-1)*(q+g)
    return kinfty(q)-4*delta**2/(q*(q+4)*(q+g+3)**2)

def sample_regenerative(q,g,x,n=90000,seed=2023):
    rng=random.Random(seed)
    rate=q; flip=g/2
    second=fourth_=0.0
    a=math.sqrt(x)
    for _ in range(n):
        age=rng.expovariate(rate)
        z=math.exp(-age)*(a if rng.getrandbits(1) else -a)
        t=0.0
        spin=1 if rng.getrandbits(1) else -1
        while t<age:
            nxt=age if flip==0 else min(age,t+rng.expovariate(flip))
            z+=spin*(math.exp(t-age)*(-1)+math.exp(nxt-age))
            spin=-spin
            t=nxt
        zz=z*z
        second+=zz
        fourth_+=zz*zz
    return second/n,fourth_/n

# Algebraically independent generator residuals for n=2 and n=4.
for q in [0.05,0.2,0.8,1.0,1.8,2.5,5.0]:
  for g in [0.01,0.2,1.0,2.0,8.0]:
    for x in [0.,0.05,0.5,1.,2.,20.]:
        V=variance(q,g,x)
        for y in [x*x, x*x+0.15, 4*x*x+1.]:
            F=fourth(q,g,x,y)
            check(close((q+2)*V, 2/(q+g+1)+q*x), 'second generator')
            check(close((q+4)*F, 12*V/(q+g+3)+q*y), 'fourth generator')
            check(F>=V*V-1e-12,'admissible moment pair')

# The exact minimizer and criticality: derivative sign and a global x-grid.
for g in [0.,0.01,.2,1.,3.,10.,100.]:
    edge=qc(g)
    check(edge>1 and close((edge-1)*(edge+g),3), 'critical root')
    for ratio in [.05,.2,.5,.8,.98,1.,1.02,1.2,2.,4.]:
        q=edge*ratio
        xo=xopt(q,g)
        K=kopt(q,g)
        if q<edge:
            check(xo>0 and math.isfinite(xo), 'interior radius')
            check(close(lower_k(q,g,xo),K,4e-10),'interior value')
            left=lower_k(q,g,max(0,xo*.91))
            right=lower_k(q,g,xo*1.09)
            check(left>K and right>K, 'strict local min')
        else:
            check(math.isinf(xo),'nonattainment marker')
        for xx in [0.,.001,.01,.1,.3,1.,3.,10.,100.,1e4,1e8]:
            check(lower_k(q,g,xx)>=K-2e-10,'global lower envelope')
        check(lower_k(q,g,1e9)>=K-1e-9,'large-spread regime')

# Check universal extremizers at fixed second moment (Pearson/Jensen).
for q,g,x in [(0.6,.1,.7),(1.,1.,3.),(2.,4.,.5),(.1,8.,100.)]:
    for p in [.1,.2,.4,.7,.9]:
        # Three-point reset with equal mass at +/-radius and mass 1-p at 0;
        # this has variance x and fourth x*x/p.
        y=x*x/p
        check(fourth(q,g,x,y)>=fourth(q,g,x,x*x),'binary extremizes')
        check(close(variance(q,g,x),variance(q,g,x)), 'finite variance')

# A pathwise regenerative simulation independent of moment closure.
for q,g,x in [(0.8,.2,1.0), (1.4,2.0,0.8), (2.8,1.5,4.)]:
    a,b=sample_regenerative(q,g,x,n=110000,seed=int(10000*q+100*g))
    v=variance(q,g,x); f=fourth(q,g,x,x*x)
    check(abs(a-v)/v<.04,f'regenerative second, q={q}, {a} versus {v}')
    check(abs(b-f)/f<.085,f'regenerative fourth, q={q}, {b} versus {f}')
    print(f'pathwise q={q:.2f} g={g:.2f}: variance {a:.7f}/{v:.7f}; fourth {b:.7f}/{f:.7f}')

# Boundary: divergent optimal radius with exponent -1/2.
for g in [.1,1.,4.]:
    e=qc(g); slope=2*e+g-1
    for eps in [1e-2,1e-3,1e-4]:
        estimate=xopt(e-eps,g)*eps
        check(abs(estimate-3/slope)/(3/slope)<.03,'critical radius law')

print(f'PASS: {checks} numerical assertions; regeneratively sampled paths and stationary moment envelope.')
