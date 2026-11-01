#!/usr/bin/env python3
"""Reproducible finite numerical checks for the Brownian reset-radius ordering theorem.

These tests check closed-form survival, concavity, fixed-mean envelopes,
and both Poisson and deterministic-renewal mean examples. They are not
substitutes for the all-time convex-order / coupling proof.
"""
import math
import random

D = 1.0
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def s_1(t, z, d=D):
    return math.erf(z / math.sqrt(4.0 * d * t))


def s_3(t, z, a=1.0, d=D):
    return 1.0 - a / z * math.erfc((z - a) / math.sqrt(4.0 * d * t))


def numerical_d2(f, x, h):
    return (f(x + h) - 2.0 * f(x) + f(x - h)) / (h * h)


def expectation(q, f):
    return sum(w * f(x) for w, x in q)


def simpson(f, start, stop, steps=8000):
    h = (stop - start) / steps
    total = f(start) + f(stop)
    for k in range(1, steps):
        total += (4 if k % 2 else 2) * f(start + k * h)
    return total * h / 3.0


rng = random.Random(4202026)
for geom, low, high, mean, surv in (
    ('line', 1.0, 3.0, 2.0, s_1),
    ('sphere', 2.0, 4.0, 3.0, s_3),
):
    envelope = ((high - mean) / (high - low), low), ((mean - low) / (high - low), high)
    for t in (0.3, 1.0, 3.0, 10.0, 40.0, 250.0):
        s = lambda z: surv(t, z)
        # Strict midpoint concavity with finite differences at many interior points.
        for j in range(1, 12):
            x = low + (high - low) * j / 12.0
            h = 0.04
            check(numerical_d2(s, x, h) < -1e-14, f'concavity {geom} {t} {x}')
        q_lo = expectation(envelope, s)
        q_hi = s(mean)
        check(q_lo < q_hi, f'endpoint/deterministic strict bound {geom} {t}')
        for i in range(15):
            x = low + (mean - low) * rng.random()
            y = mean + (high - mean) * rng.random()
            w = (y - mean) / (y - x)
            value = w * s(x) + (1 - w) * s(y)
            check(q_lo - 2e-12 < value < q_hi + 2e-12, f'two-point envelope {geom} {t}')
    # Confirm exact Laplace transform and mean of an exponential restart clock.
    if geom == 'line':
        p = lambda z: math.exp(-z)
        x0 = 1.0
        expected = (4.670774270471605, 3.02691522729844)
    else:
        p = lambda z: math.exp(-(z - 1.0)) / z
        x0 = 3.0
        expected = (21.167168296791946, 9.72458187131803)
    deterministic = (1.0 - p(x0)) / p(mean)
    scattered = (1.0 - p(x0)) / expectation(envelope, p)
    check(abs(deterministic - expected[0]) < 1e-11, f'Poisson deterministic MFPT {geom}')
    check(abs(scattered - expected[1]) < 1e-11, f'Poisson endpoint MFPT {geom}')
    check(scattered < deterministic, f'Poisson strict improvement {geom}')
    # For a deterministic renewal interval, integrate survival to compute
    # expected time of one trial, and divide by the trial success probability.
    delta = 1.35
    b0 = simpson(lambda t: 1.0 if t == 0 else surv(t, x0), 0.0, delta)
    q0 = surv(delta, x0)
    def mean_deterministic_clock(q):
        b = simpson(lambda t: 1.0 if t == 0 else expectation(q, lambda x: surv(t, x)), 0.0, delta)
        return b0 + q0 * b / (1.0 - expectation(q, lambda x: surv(delta, x)))
    val_ext = mean_deterministic_clock(envelope)
    val_single = mean_deterministic_clock(((1.0, mean),))
    check(0 < val_ext < val_single < 1e10, f'deterministic clock strict MFPT {geom}')
    print(f'{geom}: Poisson point={deterministic:.12g}, endpoints={scattered:.12g}; '
          f'periodic-clock point={val_single:.12g}, endpoints={val_ext:.12g}')

print(f'PASS: {checks} finite assertions')
