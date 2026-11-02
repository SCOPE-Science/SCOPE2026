"""Exact polynomial verification and independent quadrature for two switching disks.

Requires Python 3 standard library only. Numerical tests diagnose, but do not prove,
the all-parameter persistence/zero-count arguments in RESULT.md.
"""
from fractions import Fraction as F
from math import cos, pi, sin, sqrt


def add(a, b):
    z = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a): z[i] += x
    for i, x in enumerate(b): z[i] += x
    return trim(z)


def neg(a): return [-x for x in a]


def mul(a, b):
    z = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): z[i + j] += x*y
    return trim(z)


def trim(a):
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a


def diff(a): return [a[i]*i for i in range(1, len(a))]


def val(a, x):
    s = F(0)
    for coefficient in reversed(a): s = s*x + coefficient
    return s


p = [F(-9), F(10), F(-1)]
q = [F(-4), F(12), F(-1)]
W = add(mul(diff(p), q), neg(mul(p, diff(q))))
assert W == [F(68), F(-10), F(-2)], W
assert p == mul([F(-1), F(1)], [F(9), F(-1)])
quarter = add(p, [-a/4 for a in q])
assert quarter == [F(-8), F(7), F(-3,4)]
assert val(quarter, F(4,3)) == 0
assert val(quarter, F(8)) == 0
assert val(diff(quarter), F(4,3)) == F(5)
assert val(diff(quarter), F(8)) == F(-5)
assert val(p, F(4,3))*4 == val(q, F(4,3))
assert val(p, F(8))*4 == val(q, F(8))
assert val(W, F(4,3)) > 0 > val(W, F(8))
# Quotient at the unique critical t, with s^2=161:
# 64(15s-161) = (47-s)(17s-161).
assert 64*15 == 47*17 + 161
assert -64*161 == -47*161 - 17*161
# Critical derivative quadratic: t^2+5t-34, positive root only in (1,9).
s = sqrt(161)
tstar = (s-5)/2
assert 1 < tstar < 9
eta = sqrt((47-s)/64)
assert 0.5 < eta < 1
assert abs((float(val(p,F(8))) / float(val(q,F(8)))) - .25) < 1e-15
assert abs(15/(2*sqrt(23)) - 1.563858) < 1e-5
assert abs(-5/(2*sqrt(7)) + .944911) < 1e-5


def fminus(r):
    if not (1 < r < 3): return 0.0
    return sqrt(max(0.0, 1 - ((r*r+3)/(4*r))**2))


def fplus(r):
    if not (2-sqrt(2) < r < 2+sqrt(2)): return 0.0
    return sqrt(max(0.0, 1 - ((r*r+2)/(4*r))**2))


def M(r): return 2*(fminus(r)-fplus(r)/2)


def radial_arc_quadrature(r, N=160000):
    # Midpoint quadrature evaluates radial forcing c(theta)*cos(theta)
    # without using the analytic fminus/fplus expressions.
    total = 0.0
    for j in range(N):
        theta = 2*pi*(j+0.5)/N
        x,y = r*cos(theta),r*sin(theta)
        if (x+2)**2+y*y < 1: c = -1.0
        elif (x-2)**2+y*y < 2: c = -0.5
        else: c = 0.0
        total += c*cos(theta)
    return (2*pi/N)*total


for r in [0.8, 1.08, 1.5, 2.1, 2.75, 3.2]:
    assert abs(radial_arc_quadrature(r)-M(r)) < 0.00015, (r,radial_arc_quadrature(r),M(r))
assert abs(M(2/sqrt(3))) < 1e-12
assert abs(M(2*sqrt(2))) < 1e-12
print('PASS: exact coefficient and root identities; critical ratio; independent arc quadratures.')
