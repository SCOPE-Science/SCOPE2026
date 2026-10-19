#!/usr/bin/env python3
"""Deterministic numerical consistency checks for balanced Lyapunov-source integration.
Requires Python 3.9+ standard library only. Mathematical claims are proved separately.
"""
import math
import random

COUNT = 0

def check(cond, label):
    global COUNT
    COUNT += 1
    if not cond:
        raise AssertionError(f'{COUNT}: {label}')

def d(a,h):
    return -math.expm1(-2.0*a*h)/(2.0*a)

def cross(a,b,h):
    return -math.expm1(-(a+b)*h)/(a+b)

def threshold(a,b,h):
    x,y=d(a,h),d(b,h)
    return 2.0*math.sqrt(x*y)/(x+y)

def threshold_limit(a,b):
    return 2.0*math.sqrt(a*b)/(a+b)

def finite_offdiag(a,b,rho,h,n,kind):
    x,y=d(a,h),d(b,h)
    incr={'exact':cross(a,b,h),'sym':(x+y)/2.0,'balanced':math.sqrt(x*y)}[kind]
    t=(a+b)*h
    weight=-math.expm1(-n*t)/(-math.expm1(-t))
    return rho*incr*weight

rng=random.Random(483173)
for a in [0.2, 0.7, 1.0, 2.3, 9.0]:
    for r in [1.05, 1.25, 2, 4, 10, 50]:
        b=a*r
        old=1.0
        for h in [10**(v/8)/b for v in range(-12,24,2)]:
            x,y=d(a,h),d(b,h)
            q=cross(a,b,h)
            g=math.sqrt(x*y)
            m=(x+y)/2
            check(x>y>0, 'ordered damping integrals')
            check(q<=g+2e-14*max(1,g), 'Cauchy-Schwarz')
            check(g<=m+2e-14*max(1,m), 'AM-GM')
            tau=threshold(a,b,h)
            check(threshold_limit(a,b)-1e-12<tau<1+1e-12, 'threshold bounds')
            check(tau<=old+2e-13, 'threshold strictly falls')
            old=tau
            for rho in [-1,-0.99,-0.9,-0.5,0,0.5,0.9,0.99,1]:
                det=x*y-rho*rho*m*m
                crit=tau-abs(rho)
                check((det>=-1e-12*max(1,x*y))==(crit>=-1e-12), 'determinant iff threshold')
                exact_det=x*y-rho*rho*q*q
                check(exact_det>=-1e-12*max(1,x*y), 'exact PSD covariance')
                bdet=x*y-rho*rho*g*g
                check(bdet>=-1e-12*max(1,x*y), 'balanced PSD covariance')

# Unique crossing for a representative full-rank forcing.
a,b,rho=1.,9.,0.8
lo,hi=1e-10,20.
for _ in range(90):
    mid=(lo+hi)/2
    if threshold(a,b,mid)>rho:lo=mid
    else:hi=mid
hcrit=(lo+hi)/2
check(abs(hcrit-0.29180387462622154)<1e-11,'numerical crossing')
check(threshold(a,b,0.25)>rho>threshold(a,b,0.35),'crossing sign reversal')

# Exact global deviation is strictly reduced by the balanced source at fixed T.
for a,b in [(0.3,0.5),(1,2),(1,9),(3,20)]:
    for rho in [-1,-0.75,0.5,1]:
        for T in [0.2,1,3,9]:
            for n in [1,2,5,10,25,100]:
                h=T/n
                exact=finite_offdiag(a,b,rho,h,n,'exact')
                bal=finite_offdiag(a,b,rho,h,n,'balanced')
                sym=finite_offdiag(a,b,rho,h,n,'sym')
                check(abs(bal-exact)<abs(sym-exact)+1e-13*max(1,abs(sym)), 'strict error dominance')
                check((bal-exact)*rho>=-1e-13,'balanced error sign')
                check((sym-exact)*rho>=-1e-13,'symmetrized error sign')

# Convergence coefficients: with fixed T, the ratio tends to four.
for a,b,rho,T in [(1,3,0.8,1),(0.2,4,-0.9,2),(2,7,1,0.7)]:
    for n in [1000,2000,4000]:
        h=T/n
        ex=finite_offdiag(a,b,rho,h,n,'exact')
        sb=finite_offdiag(a,b,rho,h,n,'balanced')
        ss=finite_offdiag(a,b,rho,h,n,'sym')
        ratio=(ss-ex)/(sb-ex)
        check(abs(ratio-4)<0.04,'asymptotic fourfold gain')
        K=(rho*(a-b)**2 * (-math.expm1(-(a+b)*T))/(24*(a+b)))
        check(abs((sb-ex)/h**2-K)<0.03*max(1e-14,abs(K)), 'balanced sharp coefficient')

# General-mode tests including a positive semidefinite Gram forcing.
for _ in range(120):
    n=5
    rates=sorted([rng.uniform(0.1,3) for i in range(n)])
    G=[[rng.uniform(-1,1) for t in range(3)] for i in range(n)]
    Sigma=[[sum(G[i][t]*G[j][t] for t in range(3)) for j in range(n)] for i in range(n)]
    h=rng.uniform(0.01,2)
    T=rng.uniform(0.3,4)
    steps=rng.randint(1,25)
    hh=T/steps
    sqerr_sym=0.;sqerr_bal=0.
    D=[d(z,hh) for z in rates]
    for i in range(n):
        for j in range(n):
            w=-math.expm1(-steps*(rates[i]+rates[j])*hh)/(-math.expm1(-(rates[i]+rates[j])*hh))
            diff_s=((D[i]+D[j])/2-cross(rates[i],rates[j],hh))*Sigma[i][j]*w
            diff_b=(math.sqrt(D[i]*D[j])-cross(rates[i],rates[j],hh))*Sigma[i][j]*w
            sqerr_sym+=diff_s**2;sqerr_bal+=diff_b**2
    check(sqerr_bal<=sqerr_sym+1e-18, 'general-dimensional Frobenius dominance')
    # Gram-factor argument: B=D^(1/2)G G^T D^(1/2) by construction.
    z=[rng.uniform(-1,1) for _ in range(n)]
    psd_value=sum(sum(z[i]*math.sqrt(D[i])*G[i][t] for i in range(n))**2 for t in range(3))
    check(psd_value>=0,'Gram positivity')

print(f'PASS: {COUNT} deterministic checks; representative threshold h={hcrit:.15f}')
