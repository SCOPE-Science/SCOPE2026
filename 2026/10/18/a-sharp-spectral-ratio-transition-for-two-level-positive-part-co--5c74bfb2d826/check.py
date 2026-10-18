#!/usr/bin/env python3
"""Numerical finite-dimensional spot checks for a sharp spectral clipping profile.
The analytic proof in RESULT.md, not these samples, establishes universality.
"""
import math
import random

ROOT2 = math.sqrt(2.0)
GLOBAL = 2.0 / math.sqrt(3.0)
TESTS = 0


def check(ok, label):
    global TESTS
    TESTS += 1
    if not ok:
        raise AssertionError(label)


def profile(q):
    assert 0.0 <= q <= 1.0
    if q * q <= 0.5:
        return 1.0
    return 2.0 * q * q / math.sqrt(4.0 * q * q - 1.0)


def eval_h(h):
    a, c, d = h
    rad = math.sqrt((a - d) ** 2 + 4.0 * abs(c) ** 2)
    return ((a + d - rad) / 2.0, (a + d + rad) / 2.0)


def norm(h, p):
    lam = eval_h(h)
    if p == 'inf':
        return max(abs(x) for x in lam)
    if p == 1:
        return sum(abs(x) for x in lam)
    if p == 2:
        return math.hypot(*lam)
    raise ValueError(p)


def positive(h):
    lo, hi = eval_h(h)
    if hi <= 0.0:
        return (0.0, 0j, 0.0)
    if lo >= 0.0:
        return h
    a, c, d = h
    scale = hi / (hi - lo)
    return (scale * (a - lo), scale * c, scale * (d - lo))


def add(h, k, coef=1.0):
    return tuple(x + coef*y for x,y in zip(h,k))


def deriv(q, h):
    a,c,d = h
    return (a, q*c, 0.0)


# Scan the entire 1-dimensional selfadjoint-unitary extremal family.
for q in [0.0, 0.2, 0.5, 0.7, 1/math.sqrt(2), 0.71, 0.8, 0.9, 0.99, 1.0]:
    target = profile(q)
    best = 1.0
    for j in range(10001):
        t = j/10000.0
        sym = (t, math.sqrt(max(0.0, 1-t*t)), -t)
        best = max(best, norm(deriv(q, sym), 'inf'))
    check(abs(best-target) < 4e-7, f'operator profile at {q}: {best} vs {target}')
    check(profile(q)<=GLOBAL+1e-12, f'global ceiling at {q}')

# Derivative and trace-dual witness at mixed spectral scales.
for q in [0.1,0.65,1/math.sqrt(2),0.72,0.8,0.93,0.999]:
    a, b = q, 1.0-q
    base = (a,0j,-b)
    if q*q>0.5:
        t = 1/math.sqrt(4*q*q-1)
        p = 2*q*q/(4*q*q-1)
    else:
        t, p = 1.0,1.0
    h_inf = (t, math.sqrt(max(0.0,1-t*t)), -t)
    h_one = (p, math.sqrt(max(0.0,p*(1-p))), 1-p)
    check(abs(norm(h_inf,'inf')-1)<1e-12, 'op normalized reflection')
    check(abs(norm(deriv(q,h_inf),'inf')-profile(q))<1e-11,'op local witness')
    check(abs(norm(h_one,1)-1)<1e-11,'S1 normalized rank one')
    check(abs(norm(deriv(q,h_one),1)-profile(q))<1e-11,'S1 local witness')
    for h in (h_inf,h_one,(0.3,0.2+0.35j,-0.5)):
        for eps in (1e-4,1e-5):
            actual = add(positive(add(base,h,eps)),positive(base),-1.0)
            linear = tuple(eps*x for x in deriv(q,h))
            check(norm(add(actual,linear,-1.0),'inf') < 0.0003*eps, 'derivative finite difference')

# Independent random pairs: none is asserted to prove the global bound.
rng=random.Random(240917)
for j in range(600):
    def mk():
        return (rng.uniform(-2,2),rng.uniform(-2,2)+1j*rng.uniform(-2,2),rng.uniform(-2,2))
    a,b=mk(),mk()
    delta=add(a,b,-1.0)
    result=add(positive(a),positive(b),-1.0)
    for p, bound in [('inf',GLOBAL),(1,GLOBAL),(2,1.0)]:
        check(norm(result,p)<=bound*norm(delta,p)+2e-11, 'random global inequality')

# Sharpness is approached by honest positive/negative eigenvalue pairs.
q=0.999999
base=(q,0j,-(1-q))
t=1/math.sqrt(4*q*q-1)
p=2*q*q/(4*q*q-1)
for h,k in [((t,math.sqrt(1-t*t),-t),'inf'),((p,math.sqrt(p*(1-p)),1-p),1)]:
    eps=1e-9
    quotient=norm(add(positive(add(base,h,eps)),positive(base),-1.0),k)/norm(tuple(eps*x for x in h),k)
    check(quotient>GLOBAL-1e-4, 'sharp limiting ratio')

print(f'PASS: {TESTS} reproducible finite-dimensional checks')
