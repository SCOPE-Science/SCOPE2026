#!/usr/bin/env python3
"""Independent finite diagnostics for stationary spectral design under partial resetting.

Only Python's standard library is needed. Finite numerical tests supplement,
but do not establish, the analytic all-parameter theorem.
"""
import math
import random
from fractions import Fraction

N = 0

def verify(condition, msg):
    global N
    N += 1
    if not condition:
        raise AssertionError(msg)


def spectrum(a, w, D=1.0, r=1.0):
    return 4.0 * D / ((1.0 + a) * (r*r*(1.0-a)**2 + w*w))


def fden(a, w, r=1.0):
    return (1.0+a)*(r*r*(1.0-a)**2+w*w)


def a_low(w, r=1.0):
    return (1.0-math.sqrt(4.0-3.0*(w/r)**2))/3.0


def finite_time_var(a, T, D=1.0, r=1.0):
    lam=r*(1-a)
    sig2=2*D/(r*(1-a*a))
    return 2*sig2*(T/lam+math.expm1(-lam*T)/(lam*lam))/(T*T)


# Exact identities with fractions: moment formula, integrated CLT variance,
# spectral endpoint comparison, and sharp average-noise improvement.
for an, ad in [(-9,10),(-1,3),(0,1),(1,7),(7,8)]:
    a=Fraction(an,ad)
    r=Fraction(7,5)
    D=Fraction(11,13)
    s2=2*D/(r*(1-a*a))
    verify(2*D+r*(a*a-1)*s2 == 0,"stationary second moment")
    lam=r*(1-a)
    bracket=2*D+r*(1-a)**2*s2
    verify(bracket/lam**2 == 4*D/(r*r*(1-a)**2*(1+a)),"CLT bracket")
    for k in (0,1,3,5):
        w=Fraction(k,3)*r
        f=(1+a)*(r*r*(1-a)**2+w*w)
        verify(f-2*w*w == (1-a)*(r*r*(1-a*a)-w*w),"endpoint comparison")

verify(Fraction(27,32) == (Fraction(1,1)/((1-Fraction(-1,3))**2*(1+Fraction(-1,3)))), "sharp gain")

# Numerical full-interval maximization diagnostics for the denominator.
for r,D in [(0.5,2.5),(1.0,1.0),(2.7,0.3)]:
    for z in [0,.01,.08,.2,.4,.7,.95,.999,1.0,1.001,1.03,1.1,1.3,2.0,4.0]:
        w=z*r
        if z<1:
            a_star=a_low(w,r)
            v_star=fden(a_star,w,r)
            verify(-1/3-1e-12<=a_star<=1e-12,"low frequency location")
            verify(abs(r*r*(1-a_star)*(1+3*a_star)-w*w)<1e-11*(1+r*r),"stationarity")
            verify(v_star>=2*w*w-1e-10,"beats boundary")
        elif z==1:
            a_star=0.0
            v_star=fden(0.0,w,r)
        else:
            v_star=2*w*w
        for j in range(800):
            a=-0.9999+1.9998*j/799
            verify(fden(a,w,r)<=v_star+1e-10*(1+r*r),"global optimum")
            if z>=1:
                verify(spectrum(a,w,D,r) >= 2*D/(w*w)-1e-10,"high frequency infimum")
        if z<1:
            q=math.sqrt(4-3*z*z)
            closed=54*D/(r*r*(2+q)*(4-q)**2)
            verify(abs(closed-spectrum(a_star,w,D,r))<1e-10*(1+closed),"sharp spectrum value")

# Exact stationary covariance is exponential; a time-domain integration must
# agree with the independent Fourier expression and finite-horizon law.
for a in (-.8,-.3,0.,.33,.85):
    for r in (.7,1.9):
        D=1.3
        sig2=2*D/(r*(1-a*a))
        lam=r*(1-a)
        for w in (0,.1*r,.9*r,r,2*r):
            upper=60/lam
            h=upper/20000
            s=0.5*sig2+0.5*sig2*math.exp(-lam*upper)*math.cos(w*upper)
            for j in range(1,20000):
                t=j*h
                s+=sig2*math.exp(-lam*t)*math.cos(w*t)
            num=2*h*s
            truth=spectrum(a,w,D,r)
            verify(abs(num-truth) < 1.5e-4*(1+truth),"Fourier integration")
        for T in (.1,1,5,25):
            # Closed integral of the exact covariance, checked by midpoint sum.
            h=T/10000
            num=0.
            for j in range(10000):
                t=(j+.5)*h
                num+=(T-t)*sig2*math.exp(-lam*t)
            num=2*h*num/(T*T)
            truth=finite_time_var(a,T,D,r)
            verify(abs(num-truth)<8e-7*(1+truth),"finite-time averaging")

# Monte Carlo independent path construction: stationary diffusion as a
# backwards sum of Gaussian free-motion pieces separated by exponential
# reset intervals; forward evolution then uses exact jump epochs.
rng=random.Random(240608387)
D,r=1.2,1.5
for a,t in [(-1/3,.5),(.55,.7)]:
    acc=0.
    n=16000
    for _ in range(n):
        x0=0.
        c=1.
        # Truncation of the stationary backwards series is negligible here.
        for j in range(65):
            if abs(c)<1e-14:
                break
            e=rng.expovariate(r)
            x0+=c*math.sqrt(2*D*e)*rng.gauss(0,1)
            c*=a
        x=x0
        time=0.
        while True:
            e=rng.expovariate(r)
            if time+e>=t:
                x+=math.sqrt(2*D*(t-time))*rng.gauss(0,1)
                break
            x+=math.sqrt(2*D*e)*rng.gauss(0,1)
            x*=a
            time+=e
        acc+=x*x0
    empirical=acc/n
    expected=(2*D/(r*(1-a*a)))*math.exp(-r*(1-a)*t)
    verify(abs(empirical-expected)<0.08*expected,"stationary two-time simulation")

print(f"PASS: {N} finite assertions; exact rational identities, continuum-grid design checks, independent Fourier quadrature, finite-horizon integration, and seeded path simulation")
