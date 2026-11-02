#!/usr/bin/env python3
"""Independent finite arithmetic and numerical checks for a Brownian batch-reset pair.
The universal tail statements require the accompanying analytic proof.
Requires numpy and scipy; deterministic, no remote requests.
"""
from fractions import Fraction as F
import math
import numpy as np
from scipy.special import log_ndtr
from scipy.integrate import cumulative_trapezoid, trapezoid

checks=0

def check(p, msg):
    global checks
    if not p:
        raise AssertionError(msg)
    checks+=1

# Exact marked-Poisson rate identities, resolvent identity, square covariance.
for N in range(2, 31):
    for m in range(1,N+1):
        r,D=F(3),F(2)
        lam=r*F(m,N)
        c=r*F(m*(m-1),N*(N-1))
        e=lam-c
        a=2*lam-c
        beta=a/lam
        check(lam>0 and 0<=c<=lam and e>=0,'rates')
        check(beta==F(2*N-m-1,N-1),'beta')
        check(c/lam==F(m-1,N-1),'co-reset')
        check(e/lam==F(N-m,N-1),'exclusive')
        exactcov=4*D*D*c/(lam*lam*a)
        publishedcov=4*D*D/(r*r)*F(N*N*(m-1),m*m*(2*N-m-1))
        check(exactcov==publishedcov,'stationary square covariance')
        for k1,k2 in ((F(0),F(1)),(F(2),F(3)),(F(1,2),F(4,3))):
            h1=lam/(lam+D*k1*k1);h2=lam/(lam+D*k2*k2)
            mark=(c+e*(h1+h2))/(a+D*(k1*k1+k2*k2))
            paper=(2-beta+(beta-1)*(h1+h2))/(beta+(D/lam)*(k1*k1+k2*k2))
            check(mark==paper,'stationary pair transform')
        if c>0:
            check(0<(c/a)**2<=1,'shared last reset conditional atom')
            check(1/math.sqrt(4.)<1/math.sqrt(float(2*beta))<=1/math.sqrt(2),'eta')
        else:
            check(m==1 and beta==2,'independent case')

# Numerically integrate the exact marked-shock age distribution. Evaluate
# quantities multiplied by exp(x sqrt(2a/D)), avoiding severe underflow.
def rescaled_tail(x,lam,c,D=1.0,laplace_gap=0.0):
    e=lam-c; a=lam+e
    z=x*math.sqrt(2*a/D)
    t=np.linspace(.15*x/math.sqrt(D*lam),1.6*x/math.sqrt(D*lam),30001)
    logq=log_ndtr(-x/np.sqrt(2*D*t))
    if laplace_gap==0:
        diagonal=c*trapezoid(np.exp(-a*t+2*logq+z),t)
    else:
        diagonal=None
    L1=-(e-laplace_gap)*t+logq
    L2=-(lam+laplace_gap)*t+logq
    s1=float(np.max(L1));s2=float(np.max(L2))
    acc=np.r_[0,cumulative_trapezoid(np.exp(L1-s1),t)]
    off=2*e*lam*trapezoid(np.exp(L2-s2)*acc,t)*math.exp(z+s1+s2)
    return diagonal,off,z

for c in (.5,.8):
    beta=2-c
    prev_err=float('inf')
    for x in (100.,300.,1000.):
        diag,off,z=rescaled_tail(x,1.0,c)
        scale=math.sqrt(2*math.pi*z)
        target=beta/c
        err=abs(scale*(diag+off)-target)
        check(err<prev_err,'joint tail ratio approaches predicted coefficient')
        prev_err=err
        check(0<diag/(diag+off)<1,'conditional diagonal fraction')
    x=1000.
    diag,off,z=rescaled_tail(x,1.0,c)
    check(abs(diag/(diag+off)-(c/beta)**2)<0.03,'high-threshold shared-event weight')
    _,off_lap,z2=rescaled_tail(x,1.0,c,laplace_gap=.25)
    check(abs(off_lap/off-c/(c+.5))<.04,'age-gap Laplace transform')
    check(abs((diag+off)*math.sqrt(2*math.pi*z)-beta/c)/target<.06,'sharp prefactor')

# Special independent regime is exactly the product of Laplace tails.
for x in (0.1,1.,10.,100.):
    lam=F(1,3)
    tail=.5*math.exp(-math.sqrt(float(lam))*x)
    joint=.25*math.exp(-2*math.sqrt(float(lam))*x)
    check(abs(tail*tail-joint)<1e-14,'independent regime')

print('PASS',checks,'deterministic exact-rational and quadrature assertions')
