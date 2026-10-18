#!/usr/bin/env python3
"""Reproducible finite consistency checks for annular radial Toeplitz spectra.

Uses only the Python standard library. These finite tests are not proofs of
large-index convergence, uniqueness, or mathematical priority.
"""
import math

SQRT2PI = math.sqrt(2 * math.pi)
COUNT = 0

def check(condition, message):
    global COUNT
    if not condition:
        raise AssertionError(message)
    COUNT += 1

def phi(x):
    return math.exp(-0.5*x*x) / SQRT2PI

def Phi(x):
    return 0.5 * math.erfc(-x / math.sqrt(2))

def acritical(delta):
    lo = delta
    hi = delta + 1.0
    def f(a):
        return math.log((a + delta)/(a - delta)) - 2*a*delta
    while f(hi) > 0:
        hi *= 2
    for _ in range(90):
        mid = 0.5*(lo+hi)
        if f(mid) > 0: lo=mid
        else: hi=mid
    return 0.5*(lo+hi)

def profile(a, delta, x):
    b, c = a-delta, a+delta
    return Phi(c-x)-Phi(b-x)+Phi(-b-x)-Phi(-c-x)

def gd(a, delta, x, order):
    b, c = a-delta, a+delta
    terms = [(c,-1),(b,1),(-b,-1),(-c,1)]
    if order == 1:
        return sum(s*phi(u-x) for u,s in terms)
    if order == 2:
        return sum(s*(u-x)*phi(u-x) for u,s in terms)
    if order == 3:
        return sum(s*((u-x)**2-1)*phi(u-x) for u,s in terms)
    if order == 4:
        return sum(s*((u-x)**3-3*(u-x))*phi(u-x) for u,s in terms)
    raise ValueError(order)

def h(a, delta, x):
    return gd(a, delta, x, 1) + 0.5*x*gd(a, delta, x, 2) + gd(a, delta, x, 3)/3

def eigenvalue(n, k, a, delta):
    if k < 0 or n <= (a+delta)**2:
        raise ValueError('Need nonnegative degree and positive annuli')
    b, c = a-delta, a+delta
    root = math.sqrt(n)
    def density(u):
        t = n + u*root
        return math.exp(0.5*math.log(n) -t + k*math.log(t) - math.lgamma(k+1))
    def simpson(lo,hi,segments=256):
        step = (hi-lo)/segments
        summation = density(lo) + density(hi)
        for j in range(1,segments):
            summation += (4 if j%2 else 2)*density(lo+j*step)
        return summation*step/3
    return simpson(-c,-b) + simpson(b,c)

def positive_root(a,delta):
    b,c=a-delta,a+delta
    def f(x):
        return math.exp(-b*b/2)*math.sinh(b*x)-math.exp(-c*c/2)*math.sinh(c*x)
    lo=1e-10
    hi=a
    check(f(lo)>0 and f(hi)<0, 'supercritical sign bracket')
    for _ in range(90):
        m=(lo+hi)/2
        if f(m)>0:lo=m
        else:hi=m
    return (lo+hi)/2

def run():
    for delta in [0.2,0.6,1.0,2.0]:
        a=acritical(delta)
        b,c=a-delta,a+delta
        q=b*math.exp(-b*b/2)
        gamma=phi(0)*q*a*delta/3
        check(a>delta, 'critical a>delta')
        check(abs(b*math.exp(-b*b/2)-c*math.exp(-c*c/2))<1e-12, 'critical scalar equality')
        check(abs(gd(a,delta,0,2))<1e-12, 'zero quadratic curvature')
        check(abs(gd(a,delta,0,4)+24*gamma)<1e-12, 'quartic coefficient')
        check(abs(h(a,delta,0))<1e-12, 'first odd correction zero at origin')
        for x in [-1.2,-0.4,0.3,0.9]:
            check(abs(profile(a,delta,x)-profile(a,delta,-x))<1e-12,'even limiting profile')
            check(abs(h(a,delta,x)+h(a,delta,-x))<1e-12,'odd skew correction')
            est=(profile(a,delta,x+1e-5)-profile(a,delta,x-1e-5))/(2e-5)
            check(abs(est-gd(a,delta,x,1))<3e-9, 'profile derivative')
        n=100000
        optimal_shift=-2**(1/3)
        k0=round(n+optimal_shift*n**(1/3))
        opt=eigenvalue(n,k0,a,delta)
        for competitor in [0,1,-0.1,-2.5,2]:
            kc=round(n+competitor*n**(1/3))
            check(opt>eigenvalue(n,kc,a,delta), 'critical drift competitor')
        pred=profile(a,delta,0)+6*2**(1/3)*gamma*n**(-2/3)
        check(abs(opt-pred)<0.002, 'critical norm two-thirds expansion')
    for delta,a in [(0.4,1.4),(0.5,2.0),(1.0,1.7)]:
        check(a>acritical(delta),'supercritical choice')
        x=positive_root(a,delta)
        check(x<a,'root within a')
        check(h(a,delta,x)<0,'positive peak has negative h')
        check(abs(gd(a,delta,x,1))<1e-12,'positive peak stationary')
        for n in [100000,300000]:
            k_left=round(n-x*math.sqrt(n))
            k_right=round(n+x*math.sqrt(n))
            check(eigenvalue(n,k_left,a,delta)>eigenvalue(n,k_right,a,delta),'negative peak dominates')
    for delta,a,x in [(0.4,1.4,0.5),(0.5,2.0,-1.2),(0.6,acritical(0.6),-0.4)]:
        for n in [10000,100000]:
            k=round(n+x*math.sqrt(n))
            xx=(k-n)/math.sqrt(n)
            actual=eigenvalue(n,k,a,delta)
            approx=profile(a,delta,xx)+h(a,delta,xx)/math.sqrt(n)
            check(abs(actual-approx)*n<3, 'uniform expansion numerical residual')
    print('PASS: %s finite consistency assertions' % COUNT)
    print('Critical cubic-root target:',-2**(1/3))

if __name__ == '__main__':
    run()
