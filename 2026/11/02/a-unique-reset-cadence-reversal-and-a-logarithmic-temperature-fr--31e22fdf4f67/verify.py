#!/usr/bin/env python3
"""Numerical consistency checks for a Gaussian reset-cycle KL comparison.

Only finite calculations are performed; the accompanying proof supplies
universality, the single-crossing theorem, and the asymptotics.
"""
import math


def q(b, t):
    return 1.0 - b * math.expm1(-t)


def g(b, t):
    z = q(b, t)
    return 0.5 * (z - 2.0 + 1.0 / z)


def g_second(b, t):
    z = q(b, t)
    w = 1.0 + b
    return 0.5 * b * math.exp(-t) * (2.0 * w - z - z**3) / (z**3)


def integrate(f, a, b, eps=1e-11, max_depth=35):
    def simpson(a, b, fa, fm, fb):
        return (b-a) * (fa+4*fm+fb) / 6.0
    fa, fb, fm = f(a), f(b), f((a+b)/2.0)
    s = simpson(a, b, fa, fm, fb)
    def rec(a, b, fa, fm, fb, old, tol, depth):
        m = (a+b)/2.0
        fl, fr = f((a+m)/2.0), f((m+b)/2.0)
        s1 = simpson(a, m, fa, fl, fm)
        s2 = simpson(m, b, fm, fr, fb)
        e = s1+s2-old
        if depth <= 0 or abs(e) < 15.0*tol:
            return s1+s2+e/15.0
        return rec(a,m,fa,fl,fm,s1,tol/2,depth-1) + rec(m,b,fm,fr,fb,s2,tol/2,depth-1)
    return rec(a,b,fa,fm,fb,s,eps,max_depth)


def mean_inv(b, x):
    def f(u):
        return math.exp(-u) / q(b, x*u)
    return sum(integrate(f, a, c, eps=3e-12) for a,c in [(0,0.01),(0.01,0.1),(0.1,1),(1,10),(10,45)])


def delta(b, x):
    return 0.5 * (b*(x/(1+x)+math.expm1(-x)) + mean_inv(b,x) - 1/q(b,x))


def root(b):
    lo, hi = 1e-7, 10.0
    assert delta(b, lo) > 0 and delta(b, hi) < 0, (b,delta(b,lo),delta(b,hi))
    for _ in range(57):
        m=(lo+hi)/2
        if delta(b,m)>0:
            lo=m
        else:
            hi=m
    return (lo+hi)/2


def check():
    tests=0
    for b in (0.15, 0.5, 1., 3., 10., 30., 100., 1000.):
        for t in (0.,0.01,0.2,0.8,2.,5.):
            assert math.isclose(g(b,t),.5*(q(b,t)-1.)**2/q(b,t),rel_tol=2e-9,abs_tol=2e-10)
            assert g(b,t)>=0
            tests+=2
        for x in (0.01, 0.04,0.2,0.6,1.,2.,5.):
            direct= sum(integrate(lambda u: math.exp(-u)*g(b,x*u),a,c,eps=1e-9)
                        for a,c in [(0,0.1),(0.1,1),(1,10),(10,45)])-g(b,x)
            assert abs(delta(b,x)-direct)<2e-7*max(1.,b), (b,x,delta(b,x),direct)
            tests+=1
        rt=root(b)
        assert delta(b,rt*.7)>0 and delta(b,rt*1.3)<0
        tests+=2
        last_sign=1
        changes=0
        for j in range(45):
            x=10**(-3.0+4.5*j/44.)
            sign=1 if delta(b,x)>0 else -1
            if sign!=last_sign:
                changes+=1
                last_sign=sign
        assert changes==1,(b,changes)
        tests+=1
        if b>=10:
            print('b=%-7g crossing x=%-14.9g asymptotic ratio=%-8.5f' % (
                b,rt,rt/((2./3.)**(1./3.)*(math.log(b)/b**2)**(1./3.))))
    for v in (0.01,0.1,.2,.6,.99,1.,1.1,2.,5.):
        if v<1.:
            h=math.exp(-v)-1+v
            num=v*v*math.exp(-v)-(1-math.exp(-v))**2
            assert h>0 and num<0
        tests+=1
    # Observe the sign and asymptotic normalization of the logarithmic crossover.
    for b in (1e4,1e5,1e6):
        scale=(math.log(b)/b**2)**(1/3)
        norm=b**(-1/3)*math.log(b)**(2/3)
        for xi in (0.5,0.7,1.1,1.5):
            observed=delta(b,xi*scale)/norm
            limit=-xi*xi/4+1/(6*xi)
            assert observed*limit>0, (b,xi,observed,limit)
            tests+=1
    print('PASS',tests,'bounded numerical and analytic-identity checks')

if __name__=='__main__':
    check()
