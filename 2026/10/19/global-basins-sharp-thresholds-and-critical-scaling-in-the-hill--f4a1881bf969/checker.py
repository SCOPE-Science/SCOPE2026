#!/usr/bin/env python3
"""Reproducible finite diagnostics for a Hill-feedback planar recurrence.
These checks support but do not replace the analytic proof.
Uses only the Python standard library.
"""
from fractions import Fraction
import math


def g(x, b, m):
    return b / (1 + x**m)


def h(x, b, m):
    return g(g(x, b, m), b, m)


def four(x, y, b, m):
    for _ in range(4):
        x, y = y, g(x, b, m)
    return x, y


def threshold(m):
    a = (m - 1)**(-1 / m)
    return a, a * (1 + a**m)


def bisect(fn, left, right, count=110):
    fl, fr = fn(left), fn(right)
    assert fl * fr < 0, (fl, fr, left, right)
    for _ in range(count):
        mid = (left + right) / 2
        fm = fn(mid)
        if fm == 0:
            return mid
        if fl * fm > 0:
            left, fl = mid, fm
        else:
            right, fr = mid, fm
    return (left + right) / 2


def fix(b, m):
    return bisect(lambda x: g(x, b, m) - x, 0.0, b + 1)


def cycle(b, m):
    w = fix(b, m)
    # Strictly interior at 0 and at w: avoid the trivial fixed-point root.
    low = bisect(lambda x: h(x, b, m) - x, 0.0, 0.99999 * w)
    return low, g(low, b, m)


n = 0
# Exact rational dynamics, including the complete T^4 orbit at quadratic Hill power.
for r in range(2, 15):
    u, v = Fraction(1, r), Fraction(r)
    b = u + v
    assert g(u, b, 2) == v
    assert g(v, b, 2) == u
    assert Fraction(4) / (b*b) < 1
    for x, y in [(u,u), (u,v), (v,u), (v,v)]:
        assert four(x,y,b,2) == (x,y)
        n += 1

# Numeric sign, coordinate-separation and hyperbolicity checks for noninteger exponents.
for m in [1.2, 1.5, 2, 3, 4, 7]:
    a, bc = threshold(m)
    for delta in [0.02, 0.2, 2.0]:
        b = bc + delta
        w = fix(b, m)
        u, v = cycle(b, m)
        assert 0 < u < w < v and v <= b * (1 + 1e-13)
        assert math.isclose(g(u,b,m),v,rel_tol=2e-10)
        assert math.isclose(g(v,b,m),u,rel_tol=2e-10)
        q = m*m*(u*v)**m/((1+u**m)*(1+v**m))
        rho = (m*w**m/(1+w**m))**2
        assert 0 < q < 1 and rho > 1
        s = math.log(v/u)/2
        assert math.isclose(q, (m*math.sinh(s)/math.sinh(m*s))**2, rel_tol=1e-9)
        for x,y in [(u,u),(u,v),(v,v),(v,u),(w,u),(u,w),(w,v),(v,w)]:
            xx,yy = four(x,y,b,m)
            assert math.isclose(xx,x,rel_tol=4e-9)
            assert math.isclose(yy,y,rel_tol=4e-9)
            n+=1

# Critical inverse-square law and its universal coefficient.
for m in [1.5, 2.0, 3.0, 4.0]:
    w, b = threshold(m)
    goal = w*math.sqrt(3/(m*m-1))
    for x0 in [0.7*w, 1.35*w]:
        x = x0
        for _ in range(90000):
            x = h(x,b,m)
        ratio = math.sqrt(90000)*abs(x-w)/goal
        assert 0.985 < ratio < 1.015, (m, ratio)
        n += 1

# Square-root amplitudes in the supercritical branch.
for m in [1.5,2.0,3.0,4.0]:
    w0, bc = threshold(m)
    goal = math.sqrt(6*(m-1)*w0/(m*(m+1)))
    delta=0.0002
    w=fix(bc+delta,m)
    u,v=cycle(bc+delta,m)
    assert abs((v-w)/math.sqrt(delta)/goal-1)<0.05
    assert abs((w-u)/math.sqrt(delta)/goal-1)<0.05
    n+=1

print('PASS:', n, 'exact rational, finite-iteration, and numerical diagnostics')
