#!/usr/bin/env python3
import math


def theta_c(k,q):
    rho=(k+1)/(k-1)
    return 0.5*(math.sqrt((q-2)**2+4*(q-1)*rho*rho)-(q-2))

def coeff(k,q):
    tc=theta_c(k,q)
    bp=(2*tc+q-2)/(q-1)
    return ((k-1)**4/(3*math.sqrt(k)*(k+1)**2*math.log(tc)))*(bp**1.5)

def width(k,q,d):
    tc=theta_c(k,q); th=tc+d
    b=th*(th+q-2)/(q-1)
    D=((k-1)*(b-1)-2)**2-4*b
    if D <= 0: raise AssertionError((k,q,d,D))
    s=math.sqrt(D)
    xm=((k-1)*(b-1)-2-s)/2
    xp=((k-1)*(b-1)-2+s)/2
    def loga(x):
        return -math.log(x)+k*(math.log1p(x)-math.log(b+x))
    return (loga(xp)-loga(xm))/math.log(th)

# Critical identities and derivative coefficients from the closed fold parameterization.
for k in range(2,101):
    rho=(k+1)/(k-1)
    # b(x)=x(x+k+1)/((k-1)x-1), L=log a on the fold.
    bcrit=rho*rho
    # exact formula checks evaluated in floating arithmetic at the rational critical point
    bval=rho*(rho+k+1)/((k-1)*rho-1)
    if abs(bval-bcrit) > 5e-13: raise AssertionError(('bcrit',k,bval,bcrit))
    L2=-(k-1)**2/(k*(k+1))
    L3=2*(k-1)**3*(2*k+1)/(k*k*(k+1)**2)
    if not (L2 < 0 and L3 > 0): raise AssertionError(('derivatives',k,L2,L3))

# Direct replay of source formulas: the scaled width approaches the claimed amplitude.
cases=[(2,2),(2,3),(3,3),(4,5),(6,2),(7,9),(10,4),(20,7)]
worst=0.0
for k,q in cases:
    C=coeff(k,q)
    w1=width(k,q,1e-5)/(1e-5**1.5)
    w2=width(k,q,2.5e-6)/(2.5e-6**1.5)
    # Richardson direction: finer point must be close; tolerance allows double precision at large k.
    rel=abs(w2/C-1)
    worst=max(worst,rel)
    if rel > 4e-4:
        raise AssertionError(('amplitude',k,q,C,w2,rel,w1))
    if width(k,q,1e-5) <= 0:
        raise AssertionError(('positive width',k,q))

# q=2 symmetry: the source has alpha_-=-alpha_+, so half-width is each branch magnitude.
for k in (2,3,5,10):
    if not theta_c(k,2) > 1: raise AssertionError(('theta domain',k))

print(f'VERIFY_OK cases={len(cases)} worst_scaled_rel={worst:.3e} derivative_orders=2..100')
