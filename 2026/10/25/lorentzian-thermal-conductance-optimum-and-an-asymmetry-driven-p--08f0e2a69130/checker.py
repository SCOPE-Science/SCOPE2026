#!/usr/bin/env python3
"""Exact algebra and independent numerical checks for a three-oscillator heat conductor.

Requires Python 3 with sympy, numpy, scipy.  This file contains no research-ledger dependencies.
"""
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov


def symbolic_checks():
    p, q, z = sp.symbols("p q z", positive=True)
    u, d = (p + q) / 2, (p - q) / 2
    S = sp.expand(u + d**2)
    z0 = u - sp.Rational(3, 2) + 1 / (2 * (S + 1))
    D = sp.factor(2 * (S + 2)**2 * (4*S + 3) / (S + 1)
                  + 8 * (S + 1) * (z - z0)**2)
    K = sp.Matrix([[p + 1, -1, 0], [-1, z + 2, -1], [0, -1, q + 1]])
    G = sp.diag(1, 0, 1)
    A = sp.zeros(6)
    A[:3, 3:] = sp.eye(3)
    A[3:, :3] = -K
    A[3:, 3:] = -G
    noise = sp.zeros(6)
    noise[3, 3] = 2  # Unit left-bath temperature, zero right-bath temperature.
    coordinates = [(i, j) for i in range(6) for j in range(i, 6)]
    c = sp.symbols("c0:" + str(len(coordinates)))
    C = sp.zeros(6)
    for (i, j), v in zip(coordinates, c):
        C[i, j] = C[j, i] = v
    eq = A*C + C*A.T + noise
    matrix, rhs = sp.linear_eq_to_matrix([eq[i, j] for i, j in coordinates], c)
    determinant = matrix.det(method="domain-ge")
    current_coordinate = coordinates.index((3, 3))
    replaced = matrix.copy()
    replaced[:, current_coordinate] = rhs
    determinant_replaced = replaced.det(method="domain-ge")
    assert sp.cancel(determinant + 64*K.det()*D) == 0
    assert sp.cancel(determinant - determinant_replaced
                     + 256*K.det()*(S + 2)) == 0
    conductance = sp.factor(4*(S+2)/D)
    claimed = 2*(S+1)*(S+2) / ((S+2)**2*(4*S+3) + 4*(S+1)**2*(z-z0)**2)
    assert sp.cancel(conductance - claimed) == 0
    derivative = sp.factor(sp.diff(claimed, z))
    positive_factor = sp.factor(derivative / (z0-z))
    assert sp.simplify(positive_factor - 16*(S+1)**3*(S+2) / (
        ((S+2)**2*(4*S+3)+4*(S+1)**2*(z-z0)**2)**2)) == 0
    U, Delta = sp.symbols("U Delta", real=True)
    S0 = U + Delta**2
    z00 = U-sp.Rational(3, 2)+1/(2*(S0+1))
    assert sp.cancel(sp.diff(z00, Delta) + Delta/(S0+1)**2) == 0
    print("Symbolic exact determinant, current, derivative and detuning identities: PASS")


def numerical_checks():
    rng = np.random.default_rng(20571)
    count = 0
    for i in range(1400):
        p, q = 10**rng.uniform(-1.0, 1.0, size=2)
        z = rng.uniform(0.0, 18.0)
        tR = rng.uniform(0.15, 3.0)
        tL = tR + rng.uniform(0.12, 6.0)
        K = np.array([[p+1, -1., 0], [-1., z+2, -1], [0, -1., q+1.]])
        A = np.block([[np.zeros((3, 3)), np.eye(3)],
                      [-K, -np.diag([1., 0., 1.])]])
        D = np.diag([0., 0., 0., 2*tL, 0., 2*tR])
        C = solve_continuous_lyapunov(A, -D)
        actual = tL-C[3, 3]
        u, d = (p+q)/2, (p-q)/2
        S = u+d*d
        z0 = u-1.5+1/(2*(S+1))
        predicted = (tL-tR)*2*(S+1)*(S+2)/(
            (S+2)**2*(4*S+3) + 4*(S+1)**2*(z-z0)**2)
        assert np.isclose(actual, predicted, rtol=3e-8, atol=2e-10), (
            p, q, z, actual, predicted)
        assert np.isclose(C[5, 5]-tR, actual, rtol=3e-8, atol=2e-10)
        assert np.isclose(C[0, 4], actual, rtol=3e-8, atol=2e-10)
        assert np.isclose(C[1, 5], actual, rtol=3e-8, atol=2e-10)
        count += 4
    for i in range(700):
        p, q = 10**rng.uniform(-1, 1, size=2)
        u, d = (p+q)/2, (p-q)/2
        S = u+d*d
        z0 = u-1.5+1/(2*(S+1))
        target = max(0, z0)
        def F(z):
            return 2*(S+1)*(S+2)/(
                (S+2)**2*(4*S+3)+4*(S+1)**2*(z-z0)**2)
        for candidate in [0., rng.uniform(0, 20), target/2,
                          target+1.0, target+10.0]:
            assert F(target) >= F(candidate) - 1e-14
            count += 1
    print(f"Independent Lyapunov / energy-balance / optimization checks: {count} PASS")


if __name__ == "__main__":
    symbolic_checks()
    numerical_checks()
