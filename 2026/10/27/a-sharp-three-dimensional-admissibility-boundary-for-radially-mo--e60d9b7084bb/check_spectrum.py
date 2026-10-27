#!/usr/bin/env python3
"""Exact polynomial identity and numerical Fourier checks for a radial covariance theorem.

Python 3 standard library only. Units are arbitrary positive length units.
"""
from collections import defaultdict
from math import cos, exp, pi, sin, sqrt

# Sparse integer-coefficient polynomials in (a, w, s).
ZERO = (0, 0, 0)
def atom(which):
    out = [0, 0, 0]
    out[which] = 1
    return {tuple(out): 1}
def scalar(n):
    return {ZERO: n} if n else {}
def add(*parts):
    z = defaultdict(int)
    for p in parts:
        for mon, c in p.items():
            z[mon] += c
    return {k: v for k, v in z.items() if v}
def mul(p, q):
    z = defaultdict(int)
    for x, c in p.items():
        for y, d in q.items():
            z[tuple(x[j] + y[j] for j in range(3))] += c * d
    return {k: v for k, v in z.items() if v}
def power(p, n):
    v = scalar(1)
    for _ in range(n):
        v = mul(v, p)
    return v
def scale(p, k):
    return {m: k * c for m, c in p.items() if k * c}

A, W, S = (atom(j) for j in range(3))
A2, W2, S2 = (power(v, 2) for v in (A, W, S))
Dplus = add(A2, power(add(S, W), 2))
Dminus = add(A2, power(add(S, scale(W, -1)), 2))
N = add(mul(add(S, W), power(Dminus, 3)),
        mul(add(S, scale(W, -1)), power(Dplus, 3)))
B = add(scale(power(A, 4), 3), scale(mul(A2, W2), 6),
        scale(power(W, 4), -5))
C = add(scale(A2, 3), scale(W2, 9))
P = add(power(S2, 3), mul(C, power(S2, 2)), mul(B, S2),
        mul(power(add(A2, W2), 2),
            add(A2, scale(W2, -5))))
assert N == mul(scale(S, 2), P), 'Exact spectral numerator identity failed.'
print('PASS: exact three-variable polynomial identity,', len(N), 'nonzero terms')

def spectral(a, w, s):
    x = s * s
    p = (x**3 + (3*a*a + 9*w*w)*x*x
         + (3*a**4 + 6*a*a*w*w - 5*w**4)*x
         + (a*a + w*w)**2 * (a*a - 5*w*w))
    dp = (a*a + (s + w)**2)**3
    dm = (a*a + (s - w)**2)**3
    return 32*pi*a**3 * p/(dp*dm)

def radial_integral(a, w, s, steps=100000):
    assert s > 0 and steps % 2 == 0
    # The omitted tail is exponentially negligible for these test parameters.
    bound = 65 / a
    h = bound / steps
    def f(i):
        r = i * h
        return r*(1 + a*r)*exp(-a*r)*cos(w*r)*sin(s*r)
    v = f(0) + f(steps)
    for i in range(1, steps):
        v += (4 if i % 2 else 2)*f(i)
    return 4*pi/s*(h/3)*v

for a, w, s in [(1.0, 0.2, 0.1), (1.0, 1.0, 0.1),
                (1.0, 1.0, 2.0), (sqrt(5), 1.0, 0.6)]:
    exact = spectral(a, w, s)
    quadrature = radial_integral(a, w, s)
    assert abs(exact - quadrature) <= 1e-7 * max(1, abs(exact)), (a,w,s,exact,quadrature)
    print('PASS: radial transform', (a,w,s), 'spectral density', round(exact, 11))

for a, w in [(1.0, 0.2), (sqrt(5), 1.0), (1.0, 1.0)]:
    at_zero = spectral(a, w, 0.0)
    print('Origin density sign for (a,w)=', (a, w), ':',
          '+' if at_zero > 1e-9 else ('-' if at_zero < -1e-9 else '0'))
print('All checks passed; polynomial coefficient sign proof is in the written theorem.')
