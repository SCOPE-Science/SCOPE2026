#!/usr/bin/env python3
"""Independent numerical spot checks for sharp retraction moduli; stdlib only.

These finite checks corroborate but do not replace the analytic proof.
"""
import math
import random

N = 0


def check(p, message):
    global N
    N += 1
    if not p:
        raise AssertionError(message)


def deriv(mu, t):
    return (1.0 + t / math.hypot(t, 2.0 * math.sqrt(mu))) / 2.0


def delta(sigma):
    r = sigma ** (1.0 / 3.0)
    return (1.0 - r) / (2.0 * math.sqrt(1.0 + r + r * r))


def golden_max(fn, lo, hi):
    q = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c, d = b - q * (b - a), a + q * (b - a)
    fc, fd = fn(c), fn(d)
    for _ in range(140):
        if fc < fd:
            a, c, fc = c, d, fd
            d = a + q * (b - a)
            fd = fn(d)
        else:
            b, d, fd = d, c, fc
            c = b - q * (b - a)
            fc = fn(c)
    return (a + b) / 2, max(fc, fd)


rng = random.Random(20261025)
for sigma in [0.0001, .001, .01, .125, .333, .5, .9, .99]:
    r = sigma ** (1 / 3)
    z_star = 2 * r / math.sqrt(1 + r)
    for mu in [1.e-12, 1.e-6, 1., 1.e6]:
        t = z_star * math.sqrt(mu)
        actual = deriv(sigma * mu, t) - deriv(mu, t)
        check(abs(actual - delta(sigma)) < 2.e-13, 'closed-form maximum')
        check(abs((deriv(sigma * mu, -t) - deriv(mu, -t)) + actual) < 2.e-13, 'symmetry')
        _, measured = golden_max(lambda z: deriv(sigma, z) - deriv(1., z), 0., 10.)
        check(abs(measured - delta(sigma)) < 3.e-12, 'independent optimizer')
        for _ in range(90):
            x = rng.uniform(-20, 20) * math.sqrt(mu)
            check(abs(deriv(sigma * mu, x) - deriv(mu, x)) <= delta(sigma) + 1.e-13, 'barrier global bound')

for mu in [1.e-8, .003, 1., 10000.]:
    for h in [-17 * math.sqrt(mu), -.2 * math.sqrt(mu), 0.,
              .04 * math.sqrt(mu), 4 * math.sqrt(mu), 30 * math.sqrt(mu)]:
        bound = abs(h) / math.hypot(h, 4 * math.sqrt(mu))
        center = deriv(mu, h / 2) - deriv(mu, -h / 2)
        check(abs(abs(center) - bound) < 2.e-14, 'state-shift maximum')
        for _ in range(120):
            t = rng.uniform(-50, 50) * math.sqrt(mu)
            check(abs(deriv(mu, t + h) - deriv(mu, t)) <= bound + 2.e-13, 'state-shift global bound')

for sigma in [.01, .125, .5, .9]:
    for mu in [.00001, 1.0, 900.]:
        for _ in range(130):
            old = rng.uniform(-15, 15) * math.sqrt(mu)
            new = old + rng.uniform(-6, 6) * math.sqrt(mu)
            h = new - old
            lhs = abs(deriv(sigma * mu, -new) - deriv(mu, -old))
            rhs = delta(sigma) + abs(h) / math.hypot(h, 4 * math.sqrt(sigma * mu))
            check(lhs <= min(1.0, rhs) + 2.e-13, 'joint matrix bound')
            # One-constraint KKT block with Q=A=1 and no equalities:
            # J=[[0,-1],[-1,-d]], J^{-1}=[[d,-1],[-1,0]].
            d0 = deriv(mu, -old)
            d1 = deriv(sigma * mu, -new)
            Jdiff = abs(d1 - d0)
            check(abs(lhs-Jdiff) < 1.e-14, 'KKT operator norm (exact diagonal difference)')
            res = (rng.uniform(-2, 2), rng.uniform(-2, 2))
            step = (-(d0 * res[0] - res[1]), res[0])
            defect = (0., -(d1 - d0) * step[1])
            normr = math.hypot(*res)
            invnorm = (d0 + math.sqrt(d0*d0+4))/2
            check(math.hypot(*defect) <= Jdiff*invnorm*normr + 2.e-12, 'frozen Newton residual bound')

for mu in [1.e-12, 1.e-5, .1, 1., 800.]:
    t = math.sqrt(2 * mu)
    logder = abs(t*mu / (t*t + 4*mu)**1.5)
    check(abs(logder - 1/(6 * math.sqrt(3))) < 1.e-14, 'log-barrier sharp differential modulus')

print('PASS:', N, 'deterministic and seeded assertions. This is not an infinite proof.')
