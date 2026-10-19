#!/usr/bin/env python3
"""Deterministic checks for a commuting-Gaussian semi-unbalanced barycenter theorem.
Run with Python 3.9+; standard library only. Computations supplement the proof.
"""
import math
import random

rng = random.Random(39017)
count = 0

def check(condition, explanation):
    global count
    if not condition:
        raise AssertionError(explanation)
    count += 1

def relaxed_std(b, a, tau):
    c = 2.0 + tau/(a*a)
    return (b + math.sqrt(b*b + tau*c))/c

def relaxed_derivative(b, a, tau):
    c = 2.0 + tau/(a*a)
    return (1.0 + b/math.sqrt(b*b + tau*c))/c

def target(b, inputs, weights, tau):
    return sum(w*relaxed_std(b,a,tau) for w,a in zip(weights,inputs))

def target_derivative(b, inputs, weights, tau):
    return sum(w*relaxed_derivative(b,a,tau) for w,a in zip(weights,inputs))

def global_rate(inputs, weights, tau):
    return sum(w*(2.0/(2.0+tau/(a*a))) for w,a in zip(weights,inputs))

def fixed_point(inputs, weights, tau):
    lo, hi = 0.0, max(1.,max(inputs))
    while target(hi, inputs, weights, tau) > hi:
        hi *= 2
    for _ in range(110):
        mid=(lo+hi)/2
        if target(mid, inputs, weights, tau)>mid:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def minimized_cost(b,a,tau):
    s=relaxed_std(b,a,tau)
    return (s-b)**2 + .5*tau*((s/a)**2-1.-2.*math.log(s/a))

# The exact minimizer quadratic, envelope derivative, and full interval derivative.
for _ in range(1200):
    a=math.exp(rng.uniform(-4,4));tau=math.exp(rng.uniform(-4,4));b=math.exp(rng.uniform(-4,4))
    s=relaxed_std(b,a,tau)
    c=2+tau/(a*a)
    check(abs(c*s*s-2*b*s-tau)<=2e-10*(1+tau+b*s+c*s*s),'stationarity')
    h=max(1e-7,b*1e-5)
    fdp=(relaxed_std(b+h,a,tau)-relaxed_std(b-h,a,tau))/(2*h)
    check(abs(fdp-relaxed_derivative(b,a,tau))<2e-7,'derivative')
    check(0<relaxed_derivative(b,a,tau)<2/c<1,'derivative bounds')
    check(minimized_cost(b,a,tau) <=
          (s*1.1-b)**2+.5*tau*((s*1.1/a)**2-1-2*math.log(s*1.1/a))+1e-11,
          'minimization')

# Exact global rate; contraction in the commuting-Gaussian W2 geometry.
for _ in range(600):
    d=rng.randint(1,7)
    n=rng.randint(2,6)
    tau=math.exp(rng.uniform(-2,3))
    w0=[rng.random()+.05 for _ in range(n)]
    weights=[x/sum(w0) for x in w0]
    inputs=[[math.exp(rng.uniform(-3,4)) for _ in range(d)] for _ in range(n)]
    b=[math.exp(rng.uniform(-2,4)) for _ in range(d)]
    c=[math.exp(rng.uniform(-2,4)) for _ in range(d)]
    q=max(global_rate([inputs[i][j] for i in range(n)],weights,tau) for j in range(d))
    Tb=[target(b[j],[inputs[i][j] for i in range(n)],weights,tau) for j in range(d)]
    Tc=[target(c[j],[inputs[i][j] for i in range(n)],weights,tau) for j in range(d)]
    dist=math.dist(b,c)
    check(0<q<1,'rate')
    check(math.dist(Tb,Tc)<=q*dist+1e-9*(1+dist),'W2 contraction')
    j=rng.randrange(d)
    aa=[inputs[i][j] for i in range(n)]
    large=1e8
    check(abs(target_derivative(large,aa,weights,tau)-global_rate(aa,weights,tau))<1e-10,
          'sharp asymptotic Lipschitz constant')

# Exact identity of one hybrid step with gradient descent (stepsize 1/2).
for _ in range(400):
    a=[math.exp(rng.uniform(-1,2)) for i in range(4)]
    w=[.1,.2,.3,.4]
    tau=math.exp(rng.uniform(-2,2))
    b=math.exp(rng.uniform(-1,2))
    h=1e-5*(1+b)
    obj=lambda x:sum(ww*minimized_cost(x,aa,tau) for aa,ww in zip(a,w))
    finite=(obj(b+h)-obj(b-h))/(2*h)
    check(abs(finite-2*(b-target(b,a,w,tau)))<5e-6*(1+abs(finite)), 'envelope-gradient identity')

# A genuine finite contamination ceiling with a sharp 1/M^2 approach.
a,tau,w=1.,2.,.5
R=lambda b:math.sqrt(b*b+2*tau)
sinf=lambda b:(b+R(b))/2
Tinf=lambda b:(1-w)*relaxed_std(b,a,tau)+w*sinf(b)
lo,hi=0.,10.
for _ in range(110):
    mid=(lo+hi)/2
    if Tinf(mid)>mid:lo=mid
    else:hi=mid
B=(lo+hi)/2
loc=(1-w)*relaxed_derivative(B,a,tau)+w*(1+B/R(B))/2
K=w*tau*sinf(B)**2/(2*R(B)*(1-loc))
check(abs(B-1.7156269037800918)<1e-13,'ceiling value')
check(abs(K-2.2594588405703605)<1e-12,'sharp correction')
for M in [40.,80.,160.,320.,640.]:
    bM=fixed_point([a,M],[1-w,w],tau)
    check(0<bM<B,'monotone contamination ceiling')
    check(abs((B-bM)*M*M-K)<2.0/M, 'asymptotic correction')

# Breakdown occurs only as the clean share vanishes; exponent exactly 1/2.
for eps in [1e-3,1e-4,1e-5,1e-6]:
    ww=1-eps
    def f(b):return (1-ww)*relaxed_std(b,a,tau)+ww*sinf(b)-b
    lo,hi=0.,10/math.sqrt(eps)
    for _ in range(110):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    bw=(lo+hi)/2
    check(abs(bw*math.sqrt(eps)-math.sqrt(a*a+tau/2))<4*math.sqrt(eps),'breakdown exponent')

# The reduced scalar objective is strictly convex (finite-difference).
for _ in range(350):
    a=[math.exp(rng.uniform(-1,2)) for i in range(3)]
    w=[.2,.3,.5]
    tau=math.exp(rng.uniform(-2,2))
    b=math.exp(rng.uniform(-1,2))
    q=global_rate(a,w,tau)
    second=2*(1-target_derivative(b,a,w,tau))
    check(2*(1-q) <= second + 2e-14 and second>0,'strict convexity')

print('PASS: %d deterministic assertions; outlier ceiling=%.15f; correction=%.15f; q=0.75.'%(count,B,K))
