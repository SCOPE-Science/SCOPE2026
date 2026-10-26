"""Independent finite-matrix checks of two Strang orientation formulas.

Requirements: Python 3, NumPy, SciPy. Execute: python verify.py.
This finite verification is not a substitute for the proof in RESULT.md.
"""
import math
import numpy as np
from scipy.linalg import expm


def laplacian(n):
    if n == 2:
        edges = [(0, 1)]
    else:
        edges = [(j, (j + 1) % n) for j in range(n)]
    mat = np.zeros((n, n))
    for i, j in edges:
        mat[i, i] += 1
        mat[j, j] += 1
        mat[i, j] -= 1
        mat[j, i] -= 1
    return mat, (1 if n == 2 else 2)


def reaction(v, h):
    z = math.exp(2 * h)
    return math.exp(h) * v / np.sqrt(1 + (z - 1) * v * v)


def step(v, eta, lap, h, orientation):
    if orientation == 'DRD':
        heat = expm(-eta * lap * h / 2)
        return heat @ reaction(heat @ v, h)
    heat = expm(-eta * lap * h)
    return reaction(heat @ reaction(v, h / 2), h / 2)


def equilibrium_y(delta, h, orientation):
    alpha = 1 - delta
    if orientation == 'DRD':
        return math.sinh(alpha * h) / math.sinh(h)
    return math.sinh(alpha * h) / (math.sinh(alpha * h) + math.sinh(delta * h))


def exact_scalar_step(x, delta, h, orientation):
    growth2 = math.exp(2 * (1 - delta) * h)
    if orientation == 'DRD':
        beta = math.expm1(2 * h) * math.exp(-delta * h)
    else:
        beta = math.expm1(h) * (1 + math.exp((1 - 2 * delta) * h))
    return math.copysign(math.sqrt(growth2 * x * x / (1 + beta * x * x)), x)


def energy(v, eta, lap):
    return eta / 2 * (v @ lap @ v) + .25 * np.sum((v * v - 1) ** 2)


count = 0
energy_tests = 0
for n in (2, 4, 6, 8):
    lap, degree = laplacian(n)
    s = np.array([(-1.)**j for j in range(n)])
    assert np.allclose(lap @ s, 2 * degree * s)
    for delta in (.08, .2, .4, .5, .6, .8, .95):
        eta = delta / (2 * degree)
        alpha = 1 - delta
        for h in (.05, .25, .7, 1.5, 2.5):
            for orientation in ('DRD', 'RDR'):
                y_star = equilibrium_y(delta, h, orientation)
                beta = math.expm1(2 * h) * math.exp(-delta * h) if orientation == 'DRD' else math.expm1(h) * (1 + math.exp((1 - 2 * delta) * h))
                assert abs(y_star - math.expm1(2 * alpha * h) / beta) < 2e-11
                for x in (-.8, -.3, -.08, .01, .2, .7, 1.2):
                    measured = step(x * s, eta, lap, h, orientation)
                    predicted = exact_scalar_step(x, delta, h, orientation) * s
                    assert np.allclose(measured, predicted, atol=2e-13, rtol=3e-13), (n, delta, h, orientation, x)
                    count += 1
                if orientation == 'DRD':
                    assert y_star < alpha
                elif delta < .5:
                    assert y_star > alpha
                elif delta > .5:
                    assert y_star < alpha
                else:
                    assert abs(y_star - alpha) < 2e-15
                eq = math.sqrt(alpha) * s
                after = step(eq, eta, lap, h, orientation)
                change = energy(after, eta, lap) - energy(eq, eta, lap)
                by_identity = n * (after[0] ** 2 - alpha) ** 2 / 4
                assert abs(change - by_identity) < 1e-12
                if not (orientation == 'RDR' and delta == .5):
                    assert by_identity > 0
                energy_tests += 1

for delta in (.1, .4, .5, .9):
    for orientation in ('DRD', 'RDR'):
        h = .6
        y_star = equilibrium_y(delta, h, orientation)
        rate = math.exp(-2 * (1 - delta) * h)
        for x0 in (-.9, -.3, .2, .7, 1.4):
            x = x0
            z0 = 1 / (x0 * x0)
            for j in range(1, 121):
                x = exact_scalar_step(x, delta, h, orientation)
                z_predicted = 1 / y_star + rate ** j * (z0 - 1 / y_star)
                assert abs(1 / (x * x) - z_predicted) < 1e-10

print(f'PASS: {count} full-matrix Strang comparisons; {energy_tests} energy/phase checks; 4800 scalar iterates')
