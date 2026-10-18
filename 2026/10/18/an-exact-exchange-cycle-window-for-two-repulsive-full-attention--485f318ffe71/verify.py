"""Numerical diagnostics for the self-inclusive repulsive two-token map.

The analytic theorem is proved in RESULT.md; finite checks here do not
certify its all-parameter conclusions. Standard-library-only reproducibility.
"""
import math
import random


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def unit(x):
    n = math.sqrt(dot(x, x))
    assert n > 0
    return [z / n for z in x]


def step(x, y, eta, kappa):
    c = dot(x, y)
    a = 1.0 / (1.0 + math.exp(-kappa * (1.0 - c)))
    b = 1.0 - a
    xx = [(1 - eta * a) * xi - eta * b * yi for xi, yi in zip(x, y)]
    yy = [(1 - eta * a) * yi - eta * b * xi for xi, yi in zip(x, y)]
    return unit(xx), unit(yy)


def G(t, eta, kappa):
    tau = math.tanh(kappa * t / (1.0 + t))
    return t * ((1.0 - eta * tau) / abs(1.0 - eta)) ** 2


def test_conjugacy():
    rng = random.Random(2026)
    checks = 0
    for kappa in (0.03, 0.2, 1.0 / 3):
        threshold = 2 / (1 + math.tanh(kappa))
        for eta in (0.1, 0.7, 1.12, (1+threshold)/2, threshold, (threshold+2)/2, 2.0):
            for dimension in (2, 3, 7):
                for _ in range(30):
                    x = unit([rng.uniform(-1, 1) for j in range(dimension)])
                    y = unit([rng.uniform(-1, 1) for j in range(dimension)])
                    c = dot(x, y)
                    if abs(c) >= 1 - 1e-7:
                        continue
                    t = (1-c)/(1+c)
                    xp, yp = step(x, y, eta, kappa)
                    tp = G(t, eta, kappa)
                    expected_c = (1-tp)/(1+tp)
                    assert abs(dot(xp, yp)-expected_c) < 3e-10
                    # The sum direction flips for eta>1, the difference does not.
                    u = unit([xi+yi for xi,yi in zip(x,y)])
                    v = unit([xi-yi for xi,yi in zip(x,y)])
                    up = unit([xi+yi for xi,yi in zip(xp,yp)])
                    vp = unit([xi-yi for xi,yi in zip(xp,yp)])
                    assert abs(dot(u,up) - (1 if eta<1 else -1)) < 3e-10
                    assert abs(dot(v,vp)-1) < 3e-10
                    checks += 1
    return checks


def test_global_patterns():
    checks = 0
    for kappa in (0.06, 0.2, 1 / 3):
        threshold = 2/(1+math.tanh(kappa))
        for eta in (0.3, 1.17, (threshold+2)/2):
            for t in (0.001, .3, 2, 15, 100):
                vals = []
                for _ in range(1200):
                    t = G(t,eta,kappa)
                    vals.append(t)
                    if t > 1e150:
                        break
                if eta < threshold:
                    assert vals[-1] > vals[0]
                else:
                    target = math.atanh(2/eta -1)/(kappa-math.atanh(2/eta-1))
                    assert abs(t-target) < 1e-8 * max(1,target)
                checks += 1
    return checks


def test_critical():
    # Scalar iterates in ordinary double precision converge only slowly at
    # criticality; the stated tolerances reflect the O(log n / n) correction.
    kappa = 0.2
    eta = 2/(1+math.tanh(kappa))
    t = 3.0
    for _ in range(30000):
        t = G(t,eta,kappa)
    measured = 60000 / (1+t)
    expected = 1/(2*kappa*(1+math.tanh(kappa)))
    assert abs(measured/expected-1) < 2e-3, (measured,expected)
    t = 3.0
    for _ in range(30000):
        t = G(t,2.0,kappa)
    measured = 60000*t/(1+t)
    expected = 1/(2*kappa)
    assert abs(measured/expected-1) < 2e-3, (measured,expected)
    return (measured, expected)


if __name__ == '__main__':
    c = test_conjugacy()
    g = test_global_patterns()
    crit = test_critical()
    print('PASS full update/conjugacy/orientation checks:',c)
    print('PASS phase-region trajectories:',g)
    print('PASS critical-inverse-time checks; last observed/limit:',crit)
