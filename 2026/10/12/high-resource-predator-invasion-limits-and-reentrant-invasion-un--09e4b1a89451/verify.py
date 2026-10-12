#!/usr/bin/env python3
"""Standalone checks for the smooth-maturation renewal invasion theorem.

The infinite-domain theorem is proved analytically in RESULT.md. This executable
checks the explicit rational inequalities and independently integrates a few
instances of the defined renewal kernel; finite quadrature is not the proof.
"""
from fractions import Fraction as Q
from math import exp, log1p, tanh, factorial, isfinite

# Exact part of the explicit construction.
low_birth = Q(3, 2) * Q(99, 100) * Q(19, 25)
assert low_birth == Q(5643, 5000) and low_birth > 1
# The first five terms of the exponential series prove exp(10) > 300.
series = sum((Q(10) ** j / factorial(j) for j in range(5)), Q(0))
assert series == Q(1933, 3) and series > 300
# An elementary lower bound on 100 tanh(0.01).
# For u>=0, tanh(u) >= u - u^3/3 because its difference has
# derivative u^2-tanh(u)^2 >= 0.
assert Q(1) - Q(1, 30000) > Q(99, 100)

nu = 10.0
T = 1.0
g = 0.01
k = 3.0
m = 0.1
mu_M = 0.01
# H(a)=integral_0^a phi_J(s) ds, exact antiderivative.
base_log = log1p(exp(nu * T))
def juvenile_hazard_integral(age):
    return (base_log - log1p(exp(nu * (T - age)))) / nu

def adult_fraction(age):
    z = nu * (age - T)
    return 1.0 / (1.0 + exp(-z)) if z < 600 else 1.0

def base_birth(age):
    return 0.01 * (age - T) * exp(-(age - T)) if age >= T else 0.0

def reproduction(x, saturated=False):
    h = 100.0 * tanh(x / 100.0) if saturated else x
    eta = m + mu_M * exp(-x)
    def kernel(age):
        birth = k * h * adult_fraction(age) + (1.0 - exp(-x)) * base_birth(age)
        survival = exp(-eta * age - g * x * juvenile_hazard_integral(age))
        return birth * survival
    # Composite midpoint rule; long tail decays at least as exp(-0.1 age).
    # Numerical checks only, not a certificate of the limit or threshold count.
    length = 240.0
    n = 120000
    step = length / n
    return step * sum(kernel((j + 0.5) * step) for j in range(n))

assert abs(adult_fraction(0.0) / (1.0 - adult_fraction(0.0)) - exp(-10)) < 1e-12
assert abs(juvenile_hazard_integral(0.0)) < 1e-12
assert juvenile_hazard_integral(T) > 0
for saturated in (False, True):
    at_one = reproduction(1.0, saturated)
    at_small = reproduction(0.001, saturated)
    assert isfinite(at_one) and at_one > 1.12, (saturated, at_one)
    assert isfinite(at_small) and at_small < 1.0, (saturated, at_small)
assert k / g * exp(-nu * T) < 1
assert k / g * exp(-nu * T) > 0
print('VERIFY_OK exact bounds and independent finite-quadrature checks')
