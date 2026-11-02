#!/usr/bin/env python3
"""Reproducible finite checks for an exact two-coordinate random-splitting theorem.

Only Python 3 standard-library modules are required. Numerical checks corroborate,
but do not replace, the analytic monotonicity and limit arguments in RESULT.md.
"""
import math
import itertools
from fractions import Fraction

N = 0

def close(x, y, rtol=1e-11, atol=1e-13):
    global N
    N += 1
    assert math.isfinite(x) and math.isfinite(y), (x, y)
    assert abs(x-y) <= atol + rtol*max(abs(x), abs(y)), (x, y)

def gt(x, y, tol=0.0):
    global N
    N += 1
    assert x > y + tol, (x, y)

def f(rate, h, prob):
    if prob == 0.0: return 0.0
    return -prob*math.expm1(-2.0*rate*h/prob)

def q1(a, h, p): return 1.0-f(a, h, p)
def q2(b, h, p): return 1.0-f(b, h, 1.0-p)
def qworst(a, b, h, p): return max(q1(a,h,p), q2(b,h,p))

def opt(a,b,h):
    lo,hi=0.0,1.0
    for _ in range(100):
        p=(lo+hi)/2.0
        if q1(a,h,p)>q2(b,h,p): lo=p
        else: hi=p
    return (lo+hi)/2.0

def kap(a,b):
    lo,hi=0.0,max(2*b,2*a)
    def g(k): return k*(-math.expm1(-2*a/k)) if k>0 else 0.0
    while g(hi)<=2*b: hi*=2
    for _ in range(100):
        x=(hi+lo)/2
        if g(x)<2*b:lo=x
        else:hi=x
    return (lo+hi)/2

# Independently enumerate all 2^n switching words and compute stepwise state
# multipliers. Check diagonal moment formula and worst-case objective.
for a,b in [(2.0,1.0),(10.0,1.0),(1.2,1.0)]:
    for h in [0.03125, 0.2, 1.4]:
        for p in [0.125,0.37,0.81]:
            for n in range(1,8):
                e1=e2=0.0
                for seq in itertools.product((0,1),repeat=n):
                    k=seq.count(0)
                    pr=p**k*(1-p)**(n-k)
                    mult1=math.exp(-a*h*k/p)
                    mult2=math.exp(-b*h*(n-k)/(1-p))
                    e1+=pr*mult1**2
                    e2+=pr*mult2**2
                close(e1,q1(a,h,p)**n,rtol=2e-11)
                close(e2,q2(b,h,p)**n,rtol=2e-11)

# Find the unique crossing and verify it strictly beats distinct probabilities
# and the variance-proxy optimizer. The latter lies on the opposite side of 1/2.
for a,b in [(1.0001,1),(1.1,1),(2,1),(3,1),(10,1),(100,1)]:
    for h in [0.0001,0.003,0.1,0.5,1.,2.]:
        p=opt(a,b,h)
        close(q1(a,h,p),q2(b,h,p),rtol=3e-11)
        gt(0.5,p)
        for pp in [p/4,p/2,(p+0.5)/2,0.5,(p+1)/2,0.9,0.99]:
            if abs(p-pp)>1e-12:
                gt(qworst(a,b,h,pp),qworst(a,b,h,p),-1e-13)
        pvar=a/(a+b)
        gt(pvar,0.5)
        gt(qworst(a,b,h,pvar),qworst(a,b,h,p),-1e-13)

# Small-h rare-event limit, numerically at shrinking h for separated rates.
for a,b in [(2.0,1.0),(3.0,1.0),(10.,1.)]:
    kappa=kap(a,b)
    close(kappa*(-math.expm1(-2*a/kappa)),2*b)
    for h in [1e-3,1e-4,1e-5]:
        p=opt(a,b,h)
        close(p/h,kappa,rtol=max(0.015,12*h),atol=0.)
        close((1-qworst(a,b,h,p))/h,2*b,rtol=0.006)
        gt(p,0.)

# Large-h asymptotic, not a claim of numerical accuracy after underflow.
for a,b in [(3.,1.),(10.,1.)]:
    for h in [1.,1.5,2.]:
        p=opt(a,b,h)
        approx=math.exp(-4*b*h)/4
        close(0.5-p,approx,rtol=0.25,atol=1e-12)
    close(a/(a+b)/(0.5),2*a/(a+b))

# Verify the positive rare-event nonconsistency limit against finite-n
# binomial transforms, with n=round(T/h). The Poisson nonzero variance is
# independently evaluated from its exponential generating function.
a,b,T=3.0,1.0,1.0
k=kap(a,b)
mu=math.exp(-k*T*(1-math.exp(-a/k)))
sec=math.exp(-k*T*(1-math.exp(-2*a/k)))
target=math.exp(-a*T)
limerr=sec-2*target*mu+target**2
gt(limerr,0.0)
for n in [500,2000,10000]:
    h=T/n
    p=opt(a,b,h)
    first=q1(a,h,p)**n
    mean=(1-p+p*math.exp(-a*h/p))**n
    err=first-2*target*mean+target**2
    close(err,limerr,rtol=max(0.02,6/n))
    # A fixed positive sampling probability is consistent in mean square.
    p0=0.5
    f1=q1(a,h,p0)**n
    m1=(1-p0+p0*math.exp(-a*h/p0))**n
    e0=f1-2*target*m1+target**2
    gt(1/n,e0,-1e-13)

print(f'PASS: {N} independent finite comparisons; no external dependencies')
print(f'Example a=10,b=1,h=1: p_opt={opt(10,1,1):.12f}, p_variance={10/11:.12f}, '
      f'q_opt={qworst(10,1,1,opt(10,1,1)):.12f}, q_variance={qworst(10,1,1,10/11):.12f}')
print(f'Example a=3,b=1: kappa={kap(3,1):.12f}, limiting error at T=1={limerr:.12f}')
