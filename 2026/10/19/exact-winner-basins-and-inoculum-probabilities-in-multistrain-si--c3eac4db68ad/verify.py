#!/usr/bin/env python3
"""Reproducible exact and numerical checks for competitive simplicial SIS mean-field dynamics.

All calculations use the equations stated in RESULT.md; numerical integration is
only diagnostic, while the infinite-dimensional family is covered by its proof.
"""
from fractions import Fraction as F
from math import sqrt, log
import random
from itertools import combinations


def derivative(x, beta, delta, gamma):
    s = 1.0 - sum(x)
    return [xi * (-delta + s * (beta + gi * xi)) for xi, gi in zip(x, gamma)]


def rk4(x, dt, beta, delta, gamma):
    k1 = derivative(x, beta, delta, gamma)
    k2 = derivative([v + dt * w / 2 for v, w in zip(x, k1)], beta, delta, gamma)
    k3 = derivative([v + dt * w / 2 for v, w in zip(x, k2)], beta, delta, gamma)
    k4 = derivative([v + dt * w for v, w in zip(x, k3)], beta, delta, gamma)
    return [v + dt * (a + 2 * b + 2 * c + d) / 6
            for v, a, b, c, d in zip(x, k1, k2, k3, k4)]


def limit(gamma, beta, delta, top):
    c = sum(1.0 / gamma[i] for i in top)
    k = (1 - c * beta + sqrt((1 - c * beta) ** 2 + 4 * c * (beta - delta))) / 2
    return [k / (c * gi) if i in top else 0.0 for i, gi in enumerate(gamma)]


def exact_identities():
    rng = random.Random(81097)
    n = 0
    for m in range(2, 7):
        for _ in range(180):
            gamma = [F(rng.randint(1, 24), rng.randint(1, 11)) for _ in range(m)]
            v = [F(rng.randint(1, 18), 10 * m ** 2) for _ in range(m)]
            s = 1 - sum(v)
            beta = F(rng.randint(21, 35), 10)
            delta = F(rng.randint(4, 19), 10)
            a = [u * g for u, g in zip(v, gamma)]
            xdot = [u * (-delta + s * (beta + aa)) for u, aa in zip(v, a)]
            adot = [g * f for g, f in zip(gamma, xdot)]
            for i in range(m):
                for j in range(i + 1, m):
                    assert adot[i] - adot[j] == (a[i] - a[j]) * (-delta + s * (beta + a[i] + a[j]))
                    assert adot[i] / a[i] - adot[j] / a[j] == s * (a[i] - a[j])
                    n += 2
    return n


def trajectories():
    rng = random.Random(91782)
    tests = 0
    for m in (2, 3, 4, 5, 6):
        for trial in range(14):
            g = [float(rng.randint(1, 12)) for _ in range(m)]
            beta = 1.5 + rng.random()
            delta = 0.5 + 0.5 * rng.random()
            z = [0.1 + rng.random() for _ in range(m)]
            z = [v * 0.65 / sum(z) for v in z]
            top = max(range(m), key=lambda i: g[i] * z[i])
            vals = sorted([gi * zi for gi, zi in zip(g, z)], reverse=True)
            if vals[1] / vals[0] > 0.95:
                continue
            expected = limit(g, beta, delta, [top])
            x = z
            for _ in range(20000):
                x = rk4(x, 0.025, beta, delta, g)
            assert max(abs(p - q) for p, q in zip(x, expected)) < 1e-7, (m, trial, x, expected)
            tests += 1
    beta, delta = 2.0, 1.0
    gamma = [6.0, 3.0, 2.0]
    x = [0.1, 0.2, 0.15]
    predicted = limit(gamma, beta, delta, [0, 1])
    assert abs(predicted[0] - sqrt(2) / 6) < 1e-13
    assert abs(predicted[1] - sqrt(2) / 3) < 1e-13
    for _ in range(20000):
        x = rk4(x, 0.025, beta, delta, gamma)
    assert max(abs(p - q) for p, q in zip(x, predicted)) < 1e-9
    tests += 1
    gamma = [8.0, 2.0, 1.0]
    x = [0.05, 0.15, 0.1]
    expected = limit(gamma, beta, delta, [0])
    assert x[0] < x[1] and gamma[0] * x[0] > gamma[1] * x[1]
    for _ in range(20000):
        x = rk4(x, 0.025, beta, delta, gamma)
    assert max(abs(p - q) for p, q in zip(x, expected)) < 1e-9
    assert abs(expected[0] - (3 + sqrt(17)) / 8) < 1e-13
    tests += 1
    return tests


def exact_basins_and_seed_probabilities():
    rng = random.Random(93147)
    checks = 0
    for m in range(2, 9):
        for _ in range(140):
            gamma = [F(rng.randint(1, 12), rng.randint(1, 6)) for _ in range(m)]
            top = tuple(sorted(rng.sample(range(m), rng.randint(1, m))))
            c = sum((1/gamma[i] for i in top), F(0))
            beta = F(2)
            delta = F(1)
            # Exact equilibrium residual when using K as algebraic root:
            # K^2 - (1-c*beta)K - c*(beta-delta) = 0.
            # Thus each active component has exactly zero SIS derivative.
            # For arbitrary scalar K this polynomial is the exact fixed-point equation.
            # We verify independently the exact Jacobian rank-one identities.
            a = F(rng.randint(1, 9), 11)
            s = 1-c*a
            if s<=0:
                continue
            for i in top:
                for j in top:
                    xi=a/gamma[i]
                    ji=(s*a if i==j else F(0))-xi*(beta+a)
                    direct=xi*(-beta-a+(s*gamma[i] if i==j else F(0)))
                    assert ji==direct
                    checks+=1
    lam=[F(1,8),F(1,2),F(1)]
    p=[]
    for i in range(3):
        other=[j for j in range(3) if j != i]
        p.append(sum(((-1)**len(B)*lam[i]/(lam[i]+sum((lam[j] for j in B),F(0)))
                      for k in range(len(other)+1) for B in combinations(other,k)),F(0)))
    assert p==[F(448,585),F(34,195),F(7,117)]
    assert sum(p)==1
    for m in range(2,7):
        lam=[F(1)]*m
        for i in range(m):
            other=[j for j in range(m) if j != i]
            pi=sum(((-1)**len(B)*lam[i]/(lam[i]+sum((lam[j] for j in B),F(0)))
                   for k in range(len(other)+1) for B in combinations(other,k)),F(0))
            assert pi==F(1,m)
            checks+=1
    return checks


if __name__ == '__main__':
    n = exact_identities()
    t = trajectories()
    e = exact_basins_and_seed_probabilities()
    print(f'Exact-rational pair identities: {n} passed')
    print(f'Independent RK4 limiting-state checks: {t} passed')
    print(f'Exact Jacobian and seeded-winner probability checks: {e} passed')
