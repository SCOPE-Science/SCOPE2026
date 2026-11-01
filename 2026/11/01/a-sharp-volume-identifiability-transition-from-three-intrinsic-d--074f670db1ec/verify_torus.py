#!/usr/bin/env python3
"""Independent finite checks of three-dimensional rectangular-torus moment formulas.
Uses exact coordinate integration and synthetic Haar coordinate differences.
No numerical test substitutes for the analytic theorems.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, sqrt, cos, pi
import random

rng=random.Random(27031)
checks=0

def verify(condition, context):
    global checks
    assert condition, context
    checks+=1

def moments_by_integration(x):
    # D^2=sum_i x_i U_i^2, U_i independent uniform[-1/2,1/2].
    out=[]
    for k in (1,2,3):
        total=F(0)
        for inds in product(range(k+1),repeat=3):
            if sum(inds)!=k:continue
            coeff=F(factorial(k),1)
            for i,j in enumerate(inds):
                coeff*=x[i]**j/F(factorial(j))
                coeff*=F(1,(2*j+1)*4**j)
            total+=coeff
        out.append(total)
    return out

for rep in range(400):
    x=[F(rng.randrange(1,41),rng.randrange(1,21)) for _ in range(3)]
    mu,nu,om=moments_by_integration(x)
    S,Q,R=sum(x),sum(v*v for v in x),sum(v**3 for v in x)
    verify(mu==S/12,('mean',rep))
    verify(nu-mu*mu==Q/180,('variance',rep))
    verify(om-3*mu*nu+2*mu**3==R/3780,('cumulant3',rep))
    verify((S**3-3*S*Q+2*R)/6==x[0]*x[1]*x[2],('volume',rep))

for rep in range(400):
    S=rng.uniform(.5,30)
    Q=(S*S)*rng.uniform(1/3,1)
    T=Q-S*S/3
    A=sqrt(2*T/3)
    B=(5*S**3-9*S*Q)/54
    E=T**1.5/(3*sqrt(6))
    maxv=B+E
    minv=max(0.,B-E) if Q<=S*S/2 else 0.
    verify(maxv>=0 and maxv>=minv-1e-7,('bounds',rep))
    # Traverse entire ordered positive-orthant arc.
    seen=[]
    for j in range(121):
        theta=j*pi/360
        x=[S/3 + A*cos(theta+2*pi*i/3) for i in range(3)]
        if min(x)>1e-10:
            vol=x[0]*x[1]*x[2]
            verify(minv-1e-7<=vol<=maxv+1e-7,('fiber',rep,j,vol,minv,maxv))
            seen.append(vol)
    verify(bool(seen),('nonempty',rep))
    verify(abs(max(seen)-maxv)<1e-6*max(1,maxv),('maxattain',rep))

for rep in range(30):
    a=F(rng.randrange(2,20),1)
    delta=F(1,rng.randrange(12,60))
    left=[a+2*delta,a-delta,a-delta]
    right=[a-2*delta,a+delta,a+delta]
    mleft=moments_by_integration(left)
    mright=moments_by_integration(right)
    verify(mleft[:2]==mright[:2],('two-moment collision',rep))
    verify(mleft[2]-mright[2]==delta**3/F(315),('cubic separation',rep))

print(f'VERIFY_OK {checks} exact independent integration, positive-fiber, and cubic-collision checks')
