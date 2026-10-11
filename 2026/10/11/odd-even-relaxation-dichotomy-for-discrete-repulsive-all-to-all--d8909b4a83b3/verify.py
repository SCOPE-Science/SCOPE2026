#!/usr/bin/env python3
"""Deterministic numerical checks for finite-dimensional phase-network identities.

The infinite-time and all-dimension claims require the accompanying proof.
"""
import cmath
import math
import random

TOL = 3.0e-11
counts = 0


def demand(condition, message):
    global counts
    counts += 1
    if not condition:
        raise AssertionError(message)


def order_parameter(phases):
    return sum(cmath.exp(1j * t) for t in phases)


def full_step(phases, h):
    return [t + h * sum(math.sin(t - v) for j, v in enumerate(phases) if i != j)
            for i, t in enumerate(phases)]


def reduced_step(u, h):
    return u - 2 * h * math.sin(u) * (1 - math.cos(u))


def family(n, u):
    m = n // 2
    return [u, -u] + [0.0] * (m - 2) + [math.pi] * m


rng = random.Random(905118)
for n in (3, 5, 7, 9):
    for h in (0.09 / n, 0.50 / n, 0.95 / n):
        for _ in range(800):
            phases = [rng.uniform(-math.pi, math.pi) for j in range(n)]
            z = order_parameter(phases)
            if abs(z) <= 0.5:
                new = full_step(phases, h)
                demand(abs(order_parameter(new)) <= (1 - h / 4) * abs(z) + TOL,
                       'odd contraction')
                for idx, (old, now) in enumerate(zip(phases, new)):
                    demand(abs(now - old) <= h * abs(z) + TOL,
                           'phase increment')

for n in (4, 6, 8, 12):
    for h in (0.1 / n, 0.55 / n, 0.95 / n):
        for u in (0.01, 0.3, 1.2, 2.7):
            old = family(n, u)
            new = full_step(old, h)
            v = reduced_step(u, h)
            target = family(n, v)
            demand(0 < v < u, 'strict scalar decrease')
            for a, b in zip(new, target):
                demand(abs(a - b) < 3e-14, 'invariance identity')
            demand(abs(order_parameter(old) - 2 * (math.cos(u) - 1)) < 2e-14,
                   'order-parameter identity')
            # Tail asymptotics: compare two large cutoffs, not a proof of convergence.
            u = 0.35
            q = 3 * h / 2 - 0.25
            residuals = []
            for k in range(1, 60001):
                u = reduced_step(u, h)
                if k in (30000, 60000):
                    residuals.append(1 / u**2 - 2 * h * k - q * math.log(k))
            demand(abs(residuals[1] - residuals[0]) < 0.05,
                   'asymptotic remainder stabilization')

print('VERIFY_OK; deterministic assertions:', counts)
