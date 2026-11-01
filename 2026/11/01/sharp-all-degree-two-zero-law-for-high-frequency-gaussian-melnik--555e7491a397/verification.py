#!/usr/bin/env python3
"""Standalone numerical diagnostics for the Gaussian Melnikov two-zero bounds.

Uses only the Python standard library. Finite numerical checks supplement,
but do not replace, the analytical proof.
"""
import math

PI = math.pi

def p1(omega):
    t = 3 * math.sqrt(2) * PI * omega * (1 / math.cosh(PI * omega / 2)) / 4
    return t / math.sqrt(1 + t*t)

def p1_rayleigh_quadrature(omega, steps=24000, rmax=10.0):
    t = 3 * math.sqrt(2) * PI * omega * (1 / math.cosh(PI * omega / 2)) / 4
    h = rmax / steps
    total = 0.0
    for j in range(steps + 1):
        r = j * h
        y = r * math.exp(-r*r/2) * math.erf(t*r/math.sqrt(2))
        total += (1 if j == 0 or j == steps else 4 if j % 2 else 2) * y
    return h * total / 3

def qcoeff(omega):
    return math.exp(-PI*omega/2)

def geometric_tail(q):
    return sum(k*q**k for k in range(2, 300))

def upper_probability_difference(omega):
    q = qcoeff(omega)
    return (3*math.sqrt(2)*PI*omega/2) * q*q*(2-q)/(1-q)**2

def upper_multiple_zeros(omega):
    q = qcoeff(omega)
    # Exact rational summation of sum_{k>=2}(k^2+k^3)q^k.
    S = 2*q*q*(6-6*q+4*q*q-q**3)/(1-q)**4
    return 8*((1+q*q)/q*S)**2

for w in (0.8, 1.0, 1.5, 2.0, 3.0, 5.0):
    v1, v2 = p1(w), p1_rayleigh_quadrature(w)
    assert abs(v1-v2) < 2e-7, (w, v1, v2)
    q = qcoeff(w)
    target = q*q*(2-q)/(1-q)**2
    assert abs(geometric_tail(q)-target) < 1e-12
    tail2 = sum((k*k+k**3)*q**k for k in range(2,300))
    target2 = 2*q*q*(6-6*q+4*q*q-q**3)/(1-q)**4
    assert abs(tail2-target2) < 1e-10
    assert upper_multiple_zeros(w) >= 0 and upper_probability_difference(w)>=0

# Check convergence of the analytic sharp coefficient, and its bounded error.
leading_const = 3*PI/math.sqrt(2)
for w in (4, 5, 6, 7):
    q = qcoeff(w)
    ratio = p1(w)/(w*q)
    assert abs(ratio-leading_const) < 200 * (w*w+1) * q*q
    assert p1(w) <= 1

print('PASS: Rayleigh exact probability, two infinite-series identities,')
print('      sharp leading prefactor, and nonnegative uniform bounds.')
print('Computed N=1 probabilities:', [(w, round(p1(w), 8)) for w in (1,2,3,4)])
print('Asymptotic leading constant:', leading_const)
