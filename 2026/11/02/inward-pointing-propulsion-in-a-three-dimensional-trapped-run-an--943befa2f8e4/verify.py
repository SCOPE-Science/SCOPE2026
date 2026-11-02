#!/usr/bin/env python3
"""Independent finite diagnostics for the stationary inward-heading formula.

The mathematical conclusions rely on the proof, not Monte Carlo.
Only Python's standard library is required.
"""
import math
import random


def simpson(function, points=10000):
    assert points % 2 == 0
    step = 1.0 / points
    total = function(0.0) + function(1.0)
    for i in range(1, points):
        total += (4 if i & 1 else 2) * function(step * i)
    return total * step / 3


def density_at_one(y):
    if y >= 1.0:
        return 0.0
    entropy = ((1+y)*math.log1p(y)+(1-y)*math.log1p(-y))/2
    return (math.e/math.pi) * math.cos(math.pi*y/2) * math.exp(-entropy)


def sample_stationary_projection(alpha, rng):
    leftover, result = 1.0, 0.0
    while leftover > 1e-10:
        # A=exp(-E), E exponential with rate alpha; A ~ Beta(alpha,1).
        a = math.exp(-rng.expovariate(alpha))
        contribution = leftover * (1-a)
        result += contribution * rng.uniform(-1, 1)
        leftover *= a
    return result


def checks():
    checks_run = 0
    def close(actual, expected, tol, name):
        nonlocal checks_run
        checks_run += 1
        assert abs(actual-expected) <= tol, (name, actual, expected, tol)

    mass = simpson(density_at_one)
    q_one = simpson(lambda y: density_at_one(y)*y/(1+y))
    second = 2*simpson(lambda y: density_at_one(y)*y*y)
    close(mass, .5, 3e-9, 'one-sided mass at alpha=1')
    close(second, 1/6, 3e-9, 'variance at alpha=1')
    close(q_one, 0.1156967712761374, 2e-10, 'alpha=1 inward fraction')

    rng = random.Random(7312026)
    for alpha in (0.2, 1., 6.):
        positions, indicators = [], []
        conditional_probability = 0.0
        for _ in range(14000):
            y = sample_stationary_projection(alpha, rng)
            positions.append(y)
            # Independently sample last-flight attenuation and heading sign.
            a = math.exp(-rng.expovariate(alpha))
            indicators.append(float(1-a+a*y < 0))
            conditional_probability += 1-(1-y)**(-alpha) if y < 0 else 0
        empirical_var = sum(y*y for y in positions)/len(positions)
        empirical_q = sum(indicators)/len(indicators)
        conditional_probability /= len(positions)
        close(empirical_var, 1/(3*(1+alpha)), .012, f'moment at {alpha}')
        close(empirical_q, conditional_probability, .015, f'last-run conditional identity at {alpha}')
        assert 0 < empirical_q < .5
        checks_run += 1
        print(f'alpha={alpha:g} variance={empirical_var:.6f} Q_MC={empirical_q:.6f} Q_cond={conditional_probability:.6f}')
    print(f'alpha=1 Q_quadrature={q_one:.12f}; CHECKS_PASS={checks_run}')

if __name__ == '__main__':
    checks()
