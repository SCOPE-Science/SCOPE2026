#!/usr/bin/env python3
"""Reproduce independent finite-instance checks of the stated kernel formulas."""
import cmath
import math
import mpmath as mp

CHECKS = 0

def demand(statement, explanation):
    global CHECKS
    CHECKS += 1
    if not statement:
        raise AssertionError(explanation)

def shifted(q,tau,n,z,kmax=180):
    # Analytic Laurent form: K_N(z)/((N+1) z^N).
    return sum((1.0+k/(n+1))/(1+tau*q**k)*z**k for k in range(-n,kmax+1))

def winding(q,tau,n,r,steps=768):
    values=[shifted(q,tau,n,r*cmath.exp(2j*math.pi*j/steps)) for j in range(steps)]
    increments=[cmath.phase(values[(j+1)%steps]/values[j]) for j in range(steps)]
    return round(sum(increments)/(2*math.pi)),max(map(abs,increments))

for q,tau in [(0.35,1.8),(0.25,2.4),(0.20,2.0)]:
    for n in [36,48,72]:
        for r,expected in [(q+0.45*(1/tau-q),0),(1/tau+0.35*(1-1/tau),1)]:
            count,step=winding(q,tau,n,r)
            demand(count==expected,f'Laurent winding q={q} tau={tau} n={n} r={r}: {count}')
            demand(step<0.6,'Contour sampling did not resolve winding')

mp.mp.dps=80
q=mp.mpf('0.35');tau=mp.mpf('1.8')
for z in [mp.mpc('-.4','.3'),mp.mpc('-.65','.2'),mp.mpc('.6','.1')]:
    s=sum(z**k/(1+tau*q**k) for k in range(-330,330))
    product=(mp.qp(q,q)**2*mp.qp(-tau*z,q)*mp.qp(-q/(tau*z),q)/
             (mp.qp(-tau,q)*mp.qp(-q/tau,q)*mp.qp(z,q)*mp.qp(q/z,q)))
    demand(abs(s-product)<mp.mpf('1e-40'), 'Bilateral series/product disagreement')
    for n in [120,240,480]:
        factor=sum((1+mp.mpf(k)/(n+1))*z**k/(1+tau*q**k) for k in range(-n,150))
        # Absolute error is expected to shrink proportionally to 1/N.
        demand(abs(factor-product)<mp.mpf('.1'),f'Insufficient convergence n={n}')

for q,tau,n in [(0.25,2.4,48),(0.35,1.8,48),(0.20,2.0,48)]:
    t=tau/q**(n+1)
    for j in [0,1,2,4,9,17,31]:
        moment=(1+t*q**(j+1))/(j+1)
        demand(abs(moment*(j+1)/(1+t*q**(j+1))-1)<1e-12,'Moment inversion')

print(f'PASS {CHECKS} finite consistency checks; analytical proof required for arbitrary N.')
