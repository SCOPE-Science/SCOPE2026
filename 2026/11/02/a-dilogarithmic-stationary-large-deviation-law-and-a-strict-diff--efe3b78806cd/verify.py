#!/usr/bin/env python3
"""Numerical diagnostics for stationary weak partial-reset large-deviation formulas.

Diagnostics are finite arithmetic checks; the proof of the theorem is analytic.
Run: python verify.py (requires mpmath >= 1.3).
"""
import mpmath as mp
mp.mp.dps = 45
checks = 0

def check(test, message):
    global checks
    if not test:
        raise AssertionError(message)
    checks += 1

def L(theta):
    return mp.polylog(2, theta*theta)/2

def dL(theta):
    return -mp.log(1-theta*theta)/theta if theta else mp.mpf(0)

def root_theta(w):
    if not w:
        return mp.mpf(0)
    if w < 0:
        return -root_theta(-w)
    lo, hi = mp.mpf(0), mp.mpf(1)-mp.mpf('1e-42')
    for _ in range(200):
        mid=(lo+hi)/2
        if dL(mid) > w:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2

def I(w):
    t=root_theta(w)
    return t*w-L(t)

def J(w):
    return mp.log(1+w*w/2)

def finite_cgf(s,theta):
    q=1-s
    total=mp.mpf(0)
    z=theta*theta
    # Tail decays geometrically; exact positive terms.
    for j in range(20000):
        term=-s*mp.log(1-z*q**(2*j))
        total+=term
        if abs(term)<mp.mpf('1e-42'):
            break
    else:
        raise AssertionError('series convergence exceeded diagnostic budget')
    return total

for t in [mp.mpf('0.1'),mp.mpf('0.35'),mp.mpf('0.7'),mp.mpf('0.92')]:
    errors=[abs(finite_cgf(s,t)-L(t)) for s in [mp.mpf('0.2'),mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.025')]]
    check(all(errors[i+1]<errors[i] for i in range(3)), f'CGF convergence: {t}: {errors}')
    check(abs(mp.diff(L,t)-dL(t))<mp.mpf('1e-32'),f'derivative identity: {t}')

for w in [mp.mpf('0.02'),mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2'),mp.mpf('4'),mp.mpf('9')]:
    t=root_theta(w)
    check(abs(dL(t)-w)<mp.mpf('1e-30'), f'critical equation: {w}')
    check(I(w)>J(w), f'global strict tail gap: {w}')
    check(abs(I(-w)-I(w))<mp.mpf('1e-35'), f'rate symmetry: {w}')
    z=-mp.log(1-t*t)
    G=z*z-2*z+2*(1-mp.exp(-z))
    check(G>0,f'analytic inequality diagnostic: {w}')

for w in [mp.mpf('0.03'),mp.mpf('0.06'),mp.mpf('0.12')]:
    delta=I(w)-J(w)
    # 6th-order positive gap, with small higher-order corrections.
    check(abs(delta/(w**6)-mp.mpf(1)/36)<mp.mpf('0.002'),f'sixth-order: {w}')

for w in [mp.mpf('10'),mp.mpf('16')]:
    check(abs(I(w)-(w-mp.pi**2/12))<mp.mpf('0.005'),f'large-w exact rate: {w}')

print('PASS:', checks, 'finite diagnostics')
for w in [mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2'),mp.mpf('5')]:
    print('w=%s I=%s J=%s gap=%s' %
          (mp.nstr(w,8), mp.nstr(I(w),15), mp.nstr(J(w),15), mp.nstr(I(w)-J(w),12)))
