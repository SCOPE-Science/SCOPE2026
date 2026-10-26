#!/usr/bin/env python3
"""Standalone deterministic checks for a one-step LCD3 objective frontier.

All universal conclusions are proved in RESULT.md; these tests are supplementary.
"""
import math
import random

PHI=(1.0+math.sqrt(5.0))/2.0
KCRIT=(11.0+5.0*math.sqrt(5.0))/2.0
COEFF=(5.0*math.sqrt(5.0)-11.0)/2.0

def analytic(k):
    u=min(1.0/PHI, math.sqrt(1.0-1.0/k))
    return k*u*u*(1.0-u)/(1.0+u)

def step_ratio(lambdas,weights):
    assert all(z>=1.0 for z in lambdas)
    assert abs(sum(weights)-1.0)<1e-12
    m1=sum(w*l for w,l in zip(weights,lambdas))
    m2=sum(w*l*l for w,l in zip(weights,lambdas))
    alpha=1.0-math.sqrt(max(0.0,1.0-1.0/m1))
    r1=1.0-2.0*alpha*m1+alpha*alpha*m2
    r2=sum(w*(1.0-alpha*l)**2 for w,l in zip(weights,lambdas))
    assert math.isclose(r1,r2,rel_tol=1e-11,abs_tol=1e-11)
    return r1

def witness(k):
    if k==1.0: return step_ratio([1.0,1.0],[0.5,0.5])
    if k<=PHI: return step_ratio([1.0,k],[0.0,1.0])
    p=(PHI-1.0)/(k-1.0)
    return step_ratio([1.0,k],[1.0-p,p])

for k in [1.0,1.01,1.1,1.5,PHI,2.0,5.0,10.0,KCRIT,12.0,100.0,1000.0]:
    bound=analytic(k)
    assert math.isclose(witness(k),bound,rel_tol=2e-12,abs_tol=2e-12),(k,bound,witness(k))
    if k>=PHI: assert math.isclose(bound,COEFF*k,rel_tol=1e-12,abs_tol=1e-12)
    else: assert math.isclose(bound,(1.0-k+math.sqrt(k*(k-1)))**2,rel_tol=1e-12,abs_tol=1e-12)
    if k<KCRIT-1e-9: assert bound<1.0
    if k>KCRIT+1e-9: assert bound>1.0

# All two-endpoint weights, all allowed means; no numerical optimization oracle.
for k in [1.001,1.2,2.0,5.0,12.0,100.0]:
    for j in range(1001):
        p=j/1000.0
        r=step_ratio([1.0,k],[1-p,p])
        assert r<=analytic(k)+2e-11,(k,p,r)

# Intermediate spectra and random higher-dimensional directions.
rng=random.Random(20241023)
for k in [1.2,2.0,12.0,100.0]:
    for d in [2,3,7,30]:
        lambdas=[1.0,k]+[1.0+(k-1.0)*rng.random() for _ in range(d-2)]
        for _ in range(200):
            weights=[rng.random()**2 for _ in range(d)]
            total=sum(weights);weights=[w/total for w in weights]
            r=step_ratio(lambdas,weights)
            assert r<=analytic(k)+2e-11
print('VERIFY_OK: exact branches, sharp two-eigenvector witnesses, 6006 endpoint-grid and 3200 higher-dimensional checks')
