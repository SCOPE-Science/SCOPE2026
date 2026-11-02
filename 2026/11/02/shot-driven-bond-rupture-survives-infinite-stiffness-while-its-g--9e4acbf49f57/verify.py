#!/usr/bin/env python3
"""Reproducibility checks for exact shot-rupture theorem.

Checks symbolic reductions and Gaussian first-exit formula; finite Monte Carlo is
illustrative only and is not a proof of a limiting assertion.
"""
from __future__ import annotations
import math
import random
import sympy as sp
import mpmath as mp

checks = 0

def check(flag, reason):
    global checks
    assert bool(flag), reason
    checks += 1

k, lam, D, om, sigma, z = sp.symbols('k lam D om sigma z', real=True, positive=True)
A = sp.Matrix([[-(lam+k),k],[k,-(lam+k)]])
v = sp.Matrix([[-1,1]])
check(sp.simplify(v*A+(lam+2*k)*v) == sp.zeros(1,2), 'relative drift eigenvector')
check(sp.simplify((v*v.T)[0]) == 2, 'thermal noise quadratic variation')
check(sp.simplify((v*sp.eye(2)*v.T)[0]*om*sigma**2) == 2*om*sigma**2,'total jump QV')
rate = lam+2*k
Theta=2*D+om*sigma**2
check(sp.simplify((4*D+2*om*sigma**2)/(2*rate)-Theta/rate)==0,'stationary variance')
check(sp.simplify((2*om*3*sigma**4)/(4*rate)-3*om*sigma**4/(2*rate))==0,'fourth cumulant')
check(sp.simplify((3*om*sigma**4/(2*rate))/(Theta/rate)**2 - 3*om*sigma**4*rate/(2*Theta**2))==0, 'fourth standardized cumulant')

# Verify the double-integral mean exit formula through the backward equation.
x,a,T=sp.symbols('x a T', positive=True, real=True)
I=sp.Function('I')(x)
Uprime= -sp.exp(a*x*x/(2*T))*I/T
# I' = exp(-a*x^2/(2*T)), I(0)=0; verify ODE by eliminating I'.
check(sp.simplify(T*sp.diff(Uprime,x)-a*x*Uprime + sp.exp(a*x*x/(2*T))*sp.diff(I,x)) == 0,
      'mean first passage derivative identity')
check(sp.simplify(sp.exp(a*x*x/(2*T))*sp.exp(-a*x*x/(2*T))-1)==0, 'ODE forcing')

mp.mp.dps=50

def exact_gaussian_mfpt(aa, th=1, L=1):
    aa=mp.mpf(aa); th=mp.mpf(th); L=mp.mpf(L)
    coeff=mp.sqrt(mp.pi*th/(2*aa))
    return mp.quad(lambda xx: mp.exp(aa*xx*xx/(2*th))*coeff*mp.erf(xx*mp.sqrt(aa/(2*th)))/th,
                   [0,L])

def asymp(aa, th=1,L=1):
    aa=mp.mpf(aa); th=mp.mpf(th); L=mp.mpf(L)
    return mp.sqrt(mp.pi*th/2)/(aa**mp.mpf('1.5')*L)*mp.exp(aa*L*L/(2*th))

numerical=[]
for aa in [20,40,80,120]:
    val=exact_gaussian_mfpt(aa)
    appr=asymp(aa)
    ratio=val/appr
    numerical.append((aa,mp.nstr(val,15),mp.nstr(ratio,12)))
    check(val>0, f'positive Gaussian MFPT {aa}')
check(abs(mp.mpf(numerical[-1][2])-1)<mp.mpf('0.04'), 'Laplace leading constant')
check(mp.mpf(numerical[3][2])<mp.mpf(numerical[2][2]), 'asymptotic sequence improving')

# Bounded-each-path by first mark exceeding 2L; event simulation uses D=0 only.
rng = random.Random(807196)
nsamples=10000
ages=[2.0,12.0,60.0,240.0]
agree=[0]*len(ages)
mean_t=[0.0]*len(ages)
all_limit=0.0
for _ in range(nsamples):
    shots=[]
    time=0.0
    first_big=None
    first_huge=None
    # Stopping at first |>2L guarantees all ages have ruptured, including paths
    # that had cancellations before a first |>L mark.
    while first_huge is None:
        time += rng.expovariate(2.0)
        amp = rng.gauss(0,1)
        shots.append((time,amp))
        if first_big is None and abs(amp)>1.0:
            first_big=time
        if abs(amp)>2.0:
            first_huge=time
    all_limit += first_big
    for j, aa in enumerate(ages):
        X=0.0
        last=0.0
        exit_t=None
        for t,y in shots:
            X=math.exp(-aa*(t-last))*X+y
            if abs(X)>=1.0:
                exit_t=t
                break
            last=t
        check(exit_t is not None,'oversized jump must exit')
        check(exit_t<=first_huge,'uniform exponential domination')
        mean_t[j]+=exit_t
        if exit_t==first_big:
            agree[j]+=1

p=math.erfc(1/math.sqrt(2))
q=2.0*p
check(abs(all_limit/nsamples - 1/q)<0.055, 'limiting exp mean simulation')
for j in range(len(ages)):
    check(mean_t[j]>0, 'positive finite sample mean')
check(agree[-1]/nsamples > 0.985, 'high-drift sample path equality frequency')
check(agree[-1]>=agree[0], 'larger drift agrees at least as often as low-drift')

print('PASS', checks, 'checks')
print('Gaussian MFPT asymptotics [a, exact, ratio to leading]:', numerical)
print('Gaussian-mark event limit rate=',q,'limiting mean=',1/q,'MC mean=',all_limit/nsamples)
print('Pathwise eventual equality sample frequencies:', [(a0,agree[j]/nsamples) for j,a0 in enumerate(ages)])
print('Sample mean rupture times:', [(a0, mean_t[j]/nsamples) for j,a0 in enumerate(ages)])
print('Finite simulations support but do not establish the almost-sure theorem.')
