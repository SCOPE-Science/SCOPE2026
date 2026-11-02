#!/usr/bin/env python3
"""Reproducible mathematical checks for the seasonal occupancy allocation theorem.

No third-party dependencies. Finite checks complement, and do not replace, the
analytic proof of the global claim.
"""
import math
import random
from fractions import Fraction


def cost(E, F, p, q):
    return E * p / (q * (1.0 - p)) + F * q / (p * (1.0 - q))


def prediction(E, F, u, v):
    r = u * math.sqrt(E / (F * (1.0 - u)))
    v0 = r / (1.0 + r)
    s = u / (1.0 - u) * math.sqrt(E / F)
    v1 = 2.0 * s / (math.sqrt(s * s + 4.0) + s)
    if v <= v0:
        p, q = u, v0
        budget = E * u / (1.0 - u) + 2.0 * math.sqrt(E * F / (1.0 - u))
        phase = 1
    elif v <= v1:
        p, q = u, v
        budget = cost(E, F, p, q)
        phase = 2
    else:
        t = v * math.sqrt(F / (E * (1.0 - v)))
        p, q = t / (1.0 + t), v
        budget = F * v / (1.0 - v) + 2.0 * math.sqrt(E * F / (1.0 - v))
        phase = 3
    return p, q, budget, phase, v0, v1


def close(a, b, rel=2e-10):
    return abs(a - b) <= rel * max(1.0, abs(a), abs(b))


def verify():
    rng = random.Random(450101)
    assertions = 0
    counts = {1: 0, 2: 0, 3: 0}
    for i in range(550):
        # These parameters span three orders of magnitude, asymmetry and
        # equality-adjacent cases, and all three active-constraint regimes.
        E = math.exp(rng.uniform(-3.3, 1.8))
        F = math.exp(rng.uniform(-3.3, 1.8))
        u = rng.uniform(.025, .95)
        v = rng.uniform(.025, .95)
        p, q, B, phase, v0, v1 = prediction(E, F, u, v)
        counts[phase] += 1
        assert 0.0 < v0 < v1 < 1.0; assertions += 1
        assert u - 1e-12 <= p < 1.0 and v - 1e-12 <= q < 1.0; assertions += 1
        assert close(cost(E, F, p, q), B); assertions += 1
        assert B > 2.0 * math.sqrt(E * F); assertions += 1
        if phase == 1:
            assert close(p, u) and close(q, v0); assertions += 1
        elif phase == 2:
            assert close(p, u) and close(q, v); assertions += 1
        else:
            assert close(q, v) and p >= u; assertions += 1
        # Invert the equilibrium balance and test both ODE nullclines.
        e, f = E / 1.3, F / 1.7
        a = e * p / (q * (1.0 - p))
        b = f * q / (p * (1.0 - q))
        assert close(a * q * (1 - p), e * p); assertions += 1
        assert close(b * p * (1 - q), f * q); assertions += 1
        assert a * b > e * f; assertions += 1
        assert close(1.3 * a + 1.7 * b, B); assertions += 1
        assert close(p, (a*b - e*f)/(b*(a+e))); assertions += 1
        assert close(q, (a*b - e*f)/(a*(b+f))); assertions += 1
        # The formulas are global rather than merely stationary:
        # compare numerous admissible pairs, including edges near both targets.
        for j in range(160):
            if j % 5 == 0:
                px = u
                qx = v + rng.random() * (1 - v) * .999999
            elif j % 5 == 1:
                px = u + rng.random() * (1 - u) * .999999
                qx = v
            else:
                px = u + rng.random() * (1 - u) * .999999
                qx = v + rng.random() * (1 - v) * .999999
            assert cost(E, F, px, qx) >= B - 1e-10 * max(1, B)
            assertions += 1
    assert all(counts.values()); assertions += 1
    # Exact rational equilibrium at equal targets and equal seasonal rates.
    e = f = Fraction(1, 5)
    p = q = Fraction(1, 2)
    a = e * p / (q * (1-p))
    b = f * q / (p * (1-q))
    assert a == b == Fraction(2, 5); assertions += 1
    assert a+b == Fraction(4, 5); assertions += 1
    assert a*q*(1-p) == e*p and b*p*(1-q) == f*q; assertions += 1
    _, _, B, phase, v0, v1 = prediction(.2, .2, .5, .5)
    assert phase == 2 and close(B, .8); assertions += 1
    assert close(v0, math.sqrt(2)-1); assertions += 1
    assert close(v1, (math.sqrt(5)-1)/2); assertions += 1
    print('VERIFY_OK assertions=%d phases=%s' % (assertions, counts))


if __name__ == '__main__':
    verify()
