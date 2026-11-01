#!/usr/bin/env python3
"""Reproducible tests of the alpha-harmonic radial Poisson multiplier theorem.
All comparisons test finite numerical instances; the accompanying proof covers all parameters.
Requires scipy >=1.8.
"""
import math
from scipy.special import betainc, gammaincc
from scipy.optimize import brentq

checks = 0

def verify(cond, explanation):
    global checks
    if not cond:
        raise AssertionError(explanation)
    checks += 1

def multiplier(alpha, radius, k):
    if k == 0:
        return 1.0
    return math.exp(-k * math.log(radius)) * betainc(k, alpha+1, radius*radius)

def q1(radius, k):
    return radius**k * (1+k*(1-radius*radius))

def scalar_profile(alpha,t):
    return math.exp(t) * gammaincc(alpha+1,2*t)

def critical(alpha):
    b=alpha+1
    def hazard(x):
        return math.exp((b-1)*math.log(x)-x-math.lgamma(b)) / gammaincc(b,x)
    x=brentq(lambda x:hazard(x)-0.5,1e-8,max(10.,10*b))
    return x/2, scalar_profile(alpha,x/2)

# Exact alpha=1 radial multiplier agrees with its beta-function expression.
for r in (.12,.33,.50,(math.sqrt(5)-1)/2,.63,.71,.83,.91,.98):
    for k in range(1,60):
        verify(abs(multiplier(1,r,k)-q1(r,k))<2e-11, f'alpha=1 multiplier r={r},k={k}')

# Exact modal staircases and equality at the transition radii.
for k in range(0,20):
    rho=(math.sqrt(1+4*(k+1)**2)-1)/(2*(k+1))
    arr=[q1(rho,j) for j in range(max(100,5*k+20))]
    verify(abs(arr[k]-arr[k+1])<3e-12, f'modal tie k={k}')
    verify(max(arr) - arr[k]<3e-12, f'optimal tie k={k}')
for r in (.01,.3,.6,.62,.66,.72,.79,.88,.93,.97,.99):
    t=(r*r+r-1)/(1-r*r)
    best=0 if t<0 else math.floor(t)+1
    qs=[q1(r,k) for k in range(1+max(120,best+75))]
    verify(max(qs)-qs[best]<2e-12, f'fixed radius argmax {r}')

# Sign-of-weight contractivity contrast in representative examples.
for alpha in (-.95,-.5,-.05,0.):
    for r in (.2,.55,.8,.94):
        for k in range(1,90):
            verify(multiplier(alpha,r,k)<1+1e-10, f'contractivity alpha={alpha},r={r},k={k}')

# Unique gamma-hazard optimizer and boundary-limit agreement.
for alpha in (.2,.5,1.,2.,4.):
    t, peak=critical(alpha)
    verify(t>0 and peak>1, f'nontrivial gain alpha={alpha}')
    for u in (t/5,t/2,t*.95,t*1.05,2*t,4*t):
        verify(scalar_profile(alpha,u)<peak+1e-10, f'unimodal gamma profile {alpha}')
    for r in (.95,.98,.992):
        vals=[multiplier(alpha,r,k) for k in range(1,max(200,int(15/(1-r))))]
        km=max(range(1,len(vals)+1),key=lambda i:vals[i-1])
        verify(abs(km*(1-r)-t)<max(.35,2.5*(1-r)**.5), f'scaling {alpha},{r},{km},{t}')
        verify(abs(vals[km-1]-peak)<.15*peak, f'norm gain {alpha},{r}')

print('PASS:',checks,'finite assertions; exact alpha=1 threshold, weighted contraction contrast, and Gamma-profile scaling.')
print('alpha=1 boundary norm:',2/math.sqrt(math.e))
for alpha in (.5,1.,2.):
    t,v=critical(alpha)
    print('alpha=',alpha,'t_alpha=',format(t,'.10f'),'M_alpha=',format(v,'.10f'))

# Alpha-dependent sharp threshold and discrete strict logarithmic concavity.
for alpha in (.2,.5,1.,2.,4.):
    def threshold_equation(r):
        return alpha * math.log1p(-r) + (alpha+1) * math.log1p(r)
    rc=brentq(threshold_equation,1/(2*alpha+1),1-1e-12)
    verify(abs(threshold_equation(rc))<1e-9, f'threshold zero {alpha}')
    verify(abs(multiplier(alpha,rc,1)-1)<1e-9,f'threshold first mode {alpha}')
    verify(multiplier(alpha,rc*.98,1)<1,f'contractive below threshold {alpha}')
    verify(multiplier(alpha,(1+rc)/2,1)>1,f'expansive above threshold {alpha}')
    for rad in (.55,.75,.90,.97):
        modes=[multiplier(alpha,rad,k) for k in range(0,55)]
        ratios=[modes[k+1]/modes[k] for k in range(0,53)]
        for j in range(0,52):
            verify(ratios[j+1]<ratios[j]+3e-9, f'strict logconcavity alpha={alpha} r={rad} k={j}')
print('PASS: additional alpha thresholds and discrete modal log-concavity checks',checks)
