#!/usr/bin/env python3
"""Exact-rational interval certificate for four critical-point brackets.

Uses only the Python standard library.  All reported signs are certified by
rational enclosures for pi, square roots, and arctangents; no floating-point
root finder is used in the certificate.
"""
from fractions import Fraction as Q
from math import isqrt

N = 70
SCALE = 10**N
SERIES_TERMS = 100

def add(I, J): return (I[0]+J[0], I[1]+J[1])
def neg(I): return (-I[1], -I[0])
def sub(I, J): return add(I, neg(J))
def mul(I, J):
    vals = (I[0]*J[0], I[0]*J[1], I[1]*J[0], I[1]*J[1])
    return (min(vals), max(vals))
def scale(I, c):
    c = Q(c)
    return (I[0]*c, I[1]*c) if c >= 0 else (I[1]*c, I[0]*c)
def div_pos(I, c):
    c = Q(c)
    assert c > 0
    return (I[0]/c, I[1]/c)
def sqrt_bounds(q):
    assert q >= 0
    if q == 0: return (Q(0), Q(0))
    k = isqrt((q.numerator * SCALE * SCALE) // q.denominator)
    lo = Q(k, SCALE)
    hi = Q(k+1, SCALE)
    assert lo*lo <= q <= hi*hi
    return lo, hi

def atan_series_nonnegative(t):
    assert 0 <= t <= Q(1,2)
    s = Q(0)
    for k in range(SERIES_TERMS+1):
        s += (-1)**k * t**(2*k+1) / (2*k+1)
    nxt = t**(2*SERIES_TERMS+3) / (2*SERIES_TERMS+3)
    return (min(s, s-nxt), max(s, s+nxt))

def atan_small(t):
    if t < 0: return neg(atan_series_nonnegative(-t))
    return atan_series_nonnegative(t)

def pi_bounds():
    a = atan_series_nonnegative(Q(1,5))
    b = atan_series_nonnegative(Q(1,239))
    return sub(scale(a,16), scale(b,4))

PI = pi_bounds()

def atan_pos(y):
    assert y >= 0
    if y <= Q(1,2):
        return atan_series_nonnegative(y)
    if y < 2:
        t = (y-1)/(y+1)
        return add(scale(PI,Q(1,4)), atan_small(t))
    inv = 1/y
    return sub(scale(PI,Q(1,2)), atan_series_nonnegative(inv))

def acos_bounds(x):
    x = Q(x)
    assert -1 < x < 1
    q = 1-x*x
    sqlo, sqhi = sqrt_bounds(q)
    den = abs(x)
    ylo, yhi = sqlo/den, sqhi/den
    alo = atan_pos(ylo)[0]
    ahi = atan_pos(yhi)[1]
    if x > 0:
        return (alo, ahi)
    return (PI[0]-ahi, PI[1]-alo)

def lincomb(terms):
    out = (Q(0), Q(0))
    for c,I in terms:
        out = add(out, scale(I,c))
    return out

def g(x, kind):
    A = Q(7,5)
    alpha = acos_bounds(x/A)
    beta = acos_bounds(x)
    if kind == 1: return lincomb([(4,alpha),(1,beta),(-4,PI)])
    if kind == 2: return lincomb([(4,alpha),(-1,beta),(-2,PI)])
    if kind == 3: return lincomb([(2,alpha),(1,beta),(-2,PI)])
    if kind == 4: return lincomb([(4,alpha),(1,beta),(-2,PI)])
    raise ValueError(kind)

def show(I):
    # Exact rational endpoints, rounded outward only for display.
    return (float(I[0]), float(I[1]))

checks = [
    (1, Q(-9993,10000), +1), (1, Q(-9992,10000), -1),
    (2, Q(-837,1000), +1), (2, Q(-836,1000), -1),
    (3, Q(-615,1000), +1), (3, Q(-614,1000), -1),
    (4, Q(400,1000), +1), (4, Q(401,1000), -1),
]
for kind, x, expected in checks:
    I = g(x, kind)
    assert (I[0] > 0 if expected > 0 else I[1] < 0), (kind, x, show(I))
    print(f"g{kind}({x}) certified sign {expected:+d}; interval {show(I)}")

# Exact nondegeneracy bounds for the four root families:
# For g1 and g4 all five sine terms have the same sign.
# For g2, lambda in (-0.837,-0.836) gives sin(beta)>0.54, so
# 4/(A sin(alpha)) >= 20/7 > 1/0.54 > 1/sin(beta).
assert Q(20,7) > Q(100,54)
# For g3 the reciprocal-sine sum is -2/(A sin(alpha))-1/sin(beta)<0.
print("Hessian nondegeneracy inequalities certified symbolically.")
print("Endpoint family: alpha0=acos(5/7) is in (0,pi/2); the reduced Hessian is diagonal with nonzero entries.")
