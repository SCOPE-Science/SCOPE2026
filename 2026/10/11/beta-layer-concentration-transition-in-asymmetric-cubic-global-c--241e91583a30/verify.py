#!/usr/bin/env python3
"""Supplementary numerical checks of the exact period/time-coordinate quadrature."""
import math


def integrate(q, L, steps=24000):
    # u=(1-cos(theta))/2 removes square-root endpoint singularities.
    s0 = s1 = 0.0
    h = math.pi / steps
    for j in range(steps):
        angle = (j + 0.5) * h
        u = (1.0 - math.cos(angle)) / 2.0
        d = (-math.expm1(-L * u)) * (-math.expm1(-q * L * (1.0 - u)))
        term = math.exp((q - 1.0) * L * u / 2.0) * (math.sin(angle) / 2.0) / math.sqrt(d)
        s0 += term
        s1 += term * u
    return h * s0, s1 / s0


def beta(a, b):
    return math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))


def check():
    for q in (0.5, 2.0):
        L = 20.0
        z, mean = integrate(q, L)
        period = 2.0 * L * math.sqrt(q) * math.exp(-q * L / 2.0) * z
        if q < 1.0:
            asym = 2.0 * math.sqrt(q) * beta((1.0-q)/2.0, 0.5) * math.exp(-q*L/2.0)
            assert mean < 0.18
        else:
            asym = 2.0 / math.sqrt(q) * beta((q-1.0)/(2.0*q), 0.5) * math.exp(-L/2.0)
            assert mean > 0.90
        assert abs(period / asym - 1.0) < 0.002, (q, period, asym)
    gamma = 3.0
    L = 100.0
    q = 1.0 + gamma/L
    z, mean = integrate(q, L)
    exact = (math.exp(gamma/2.0) * (gamma/2.0 - 1.0) + 1.0) / ((gamma/2.0) * math.expm1(gamma/2.0))
    # expectation of u under exp(gamma u/2) density
    assert abs(mean - exact) < 0.02, (mean, exact)
    period = 2.0 * L * math.sqrt(q) * math.exp(-q*L/2) * z
    integral = 2.0 * math.expm1(gamma/2.0)/gamma
    target = 2.0 * L * math.exp(-L/2.0-gamma/2.0) * integral
    assert abs(period/target - 1.0) < 0.08
    print('CHECK_OK')

if __name__ == '__main__':
    check()
