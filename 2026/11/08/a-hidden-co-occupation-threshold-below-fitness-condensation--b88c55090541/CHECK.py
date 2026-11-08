#!/usr/bin/env python3
"""Deterministic checks of local moment equations and critical scaling.

Uses the Python standard library only. Numerical checks corroborate the analytic
arguments in RESULT.md; finite checks do not certify asymptotic theorems.
"""
from fractions import Fraction
from math import exp, log, pi, sin


def exact_moments(ell, eta, rate, influx):
    d = eta - ell
    m1 = influx / (d + rate)
    m2 = 2 * (ell + influx) * m1 / (2 * d + rate)
    assert influx - (d + rate) * m1 == 0
    assert 2 * (ell + influx) * m1 - (2 * d + rate) * m2 == 0
    return m1, m2


ell = Fraction(7, 10)
eta = Fraction(11, 10)
rate = Fraction(2, 5)
influx = Fraction(3, 10)
m1, m2 = exact_moments(ell, eta, rate, influx)
assert m1 == Fraction(3, 8)
assert m2 == Fraction(5, 8)
assert m2 + m1 - m1 * m1 == Fraction(55, 64)

# Independently evolve a finite truncation of the forward master equation.
# The tiny tail beyond the truncation is not used in the mathematical proof.
N = 64
p = [0.0] * (N + 1)
p[0] = 1.0
Lf, etaf, rf, af = map(float, (ell, eta, rate, influx))


def generator_forward(prob):
    result = [0.0] * len(prob)
    for n, mass in enumerate(prob):
        if n < N:
            flux = (Lf * n + af) * mass
            result[n] -= flux
            result[n + 1] += flux
        if n > 0:
            flux = etaf * n * mass
            result[n] -= flux
            result[n - 1] += flux
            flux = rf * mass
            result[n] -= flux
            result[0] += flux
    return result


def plus(base, inc, fac):
    return [x + fac * y for x, y in zip(base, inc)]


h = 0.012
for step in range(5000):
    k1 = generator_forward(p)
    k2 = generator_forward(plus(p, k1, h / 2))
    k3 = generator_forward(plus(p, k2, h / 2))
    k4 = generator_forward(plus(p, k3, h))
    p = [x + (h / 6) * (a + 2 * b + 2 * c + d)
         for x, a, b, c, d in zip(p, k1, k2, k3, k4)]
assert abs(sum(p) - 1) < 1e-11
num1 = sum(n * mass for n, mass in enumerate(p))
num2 = sum(n * (n - 1) * mass for n, mass in enumerate(p))
assert abs(num1 - float(m1)) < 1e-8, (num1, m1)
assert abs(num2 - float(m2)) < 1e-8, (num2, m2)

# Independently evaluate the continuum formulas in the admissible example
# q(ell)=2(1-ell), r(ell)=(1-ell)**nu, beta=1/4.
# x=exp(-t) regularizes the endpoint singularity for numerical quadrature.

def simpson(fn, upper=80.0, n=20000):
    assert n % 2 == 0
    h = upper / n
    val = fn(0.0) + fn(upper)
    for j in range(1, n):
        val += (4 if j % 2 else 2) * fn(j * h)
    return val * h / 3


def pair_and_density(z, nu):
    def base(t):
        x = exp(-t)
        R = x ** nu
        ell = 1.0 - x
        d = z + x + R
        return x, ell, R, d
    A = simpson(lambda t: (lambda x, l, R, d: x * l / d)(*base(t)))
    B = simpson(lambda t: (lambda x, l, R, d: 2 * x * x / d)(*base(t)))
    rho = A / (1 - 0.25 * B)
    def pair(t):
        x, l, R, d = base(t)
        b = l + 0.5 * rho * x
        return x * 2 * l * b / (d * (2 * (z + x) + R))
    return simpson(pair), rho

p8, rho8 = pair_and_density(1e-8, 0.5)
p10, rho10 = pair_and_density(1e-10, 0.5)
slope = (p10 - p8) / log(100.0)
assert abs(slope - 4) < 0.012, slope

nu = 0.7
z = 1e-8
p7, rho7 = pair_and_density(z, nu)
a = 1 / nu
J = (pi / nu) * (2 ** (a - 1) - 1) / sin(pi * (a - 1))
leading = 2 * z ** (a - 2) * J
assert abs(p7 / leading - 1) < 0.015, p7 / leading

p4a, _ = pair_and_density(1e-8, 0.4)
p4b, _ = pair_and_density(1e-10, 0.4)
assert p4a > 0 and 0 < (p4b - p4a) / p4b < 0.005
assert 0 < rho10 < 10 and 0 < rho7 < 10
print('PASS: exact stationary moment equations, independent finite-chain evolution,')
print('      critical logarithmic coefficient, power amplitude, and finite branch')
print(f'Check values: m1={num1:.12f}, m2={num2:.12f}, log_slope={slope:.8f},')
print(f'power_ratio={p7 / leading:.8f}, finite_branch_change={p4b - p4a:.8f}')
