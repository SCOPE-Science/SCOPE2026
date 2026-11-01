#!/usr/bin/env python3
"""Finite independent diagnostics for a Stuart-Landau graph synchronization bound.
This file is self-contained and requires only Python 3's standard library.
"""
import cmath
import math
import random


def inner(z, w):
    return sum((a.conjugate() * b).real for a, b in zip(z, w))


def mean(z):
    return sum(z) / len(z)


def discrepancy(z):
    m = mean(z)
    return sum(abs(v - m) ** 2 for v in z)


def rhs(z, mu, c, edges):
    v = [(mu - abs(a) ** 2) * a for a in z]
    for i, j in edges:
        v[i] -= c * (z[i] - z[j])
        v[j] -= c * (z[j] - z[i])
    return v


def ds_dt(z, mu, c, edges):
    m = mean(z)
    v = rhs(z, mu, c, edges)
    vm = mean(v)
    return 2 * inner([w - m for w in z], [dw - vm for dw in v])


def step(z, h, mu, c, edges):
    k1 = rhs(z, mu, c, edges)
    k2 = rhs([a + h * b / 2 for a, b in zip(z, k1)], mu, c, edges)
    k3 = rhs([a + h * b / 2 for a, b in zip(z, k2)], mu, c, edges)
    k4 = rhs([a + h * b for a, b in zip(z, k3)], mu, c, edges)
    return [a + h * (b + 2 * d + 2 * e + f) / 6 for a, b, d, e, f in zip(z, k1, k2, k3, k4)]


def test():
    rng = random.Random(281031)
    trials = 0
    for _ in range(4000):
        x = complex(rng.uniform(-3, 3), rng.uniform(-3, 3))
        y = complex(rng.uniform(-3, 3), rng.uniform(-3, 3))
        lhs = ((x-y).conjugate() * (abs(x)**2*x-abs(y)**2*y)).real
        rhsid = (abs(x)**2+abs(y)**2)*abs(x-y)**2/2 + (abs(x)**2-abs(y)**2)**2/2
        assert math.isclose(lhs, rhsid, rel_tol=1e-11, abs_tol=1e-10)
        assert lhs + 1e-10 >= abs(x-y)**4 / 4
        trials += 1

    graphs = [(3, [(0,1), (1,2), (0,2)], 3.),
              (3, [(0,1), (1,2)], 1.),
              (2, [(0,1)], 2.)]
    for n, edges, lam2 in graphs:
        for delta in (0., .15, .5):
            mu = 1.
            c = (mu + delta)/lam2
            for k in range(16):
                z = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for i in range(n)]
                s0 = discrepancy(z)
                assert ds_dt(z, mu, c, edges) <= -2*delta*s0 - s0*s0/(2*n)+2e-10
                h = .002
                for t_index in range(700):
                    z = step(z, h, mu, c, edges)
                    t = (t_index+1)*h
                    s = discrepancy(z)
                    upper = s0 * math.exp(-2*delta*t) if delta > 0 else (2*n*s0)/(2*n+t*s0)
                    assert s <= upper + 1e-6, (n, delta, k, t, s, upper)
                trials += 1
    # Direct asymptotic critical antiphase and nontrivial subcritical stationary branches.
    n, edges, lam2 = graphs[-1]
    mu, c = 1., .5
    a0 = 0.67 + .21j
    z = [a0, -a0]
    for j in range(1300):
        z = step(z, .002, mu, c, edges)
        t = (j+1)*.002
        expected = 2*abs(a0)**2/(1 + 2*abs(a0)**2*t)
        assert abs(discrepancy(z)-expected) <= 1e-8
        trials += 1
    for c in (.1, .2, .4):
        a = math.sqrt(mu-2*c)
        f = rhs([a, -a], mu, c, edges)
        assert max(abs(v) for v in f) < 1e-12
        trials += 1
    print('PASS', trials, 'finite checks; analytic infinite-time proof is in RESULT.md')


if __name__ == '__main__':
    test()
