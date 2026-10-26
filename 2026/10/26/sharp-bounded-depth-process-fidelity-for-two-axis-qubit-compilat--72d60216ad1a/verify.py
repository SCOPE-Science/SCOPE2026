"""Finite independent checks of a two-axis unitary-approximation theorem.

Requires NumPy and SciPy. This program tests finite instances only, not
mathematical completeness or literature originality.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

X = np.array([[0., 1.], [1., 0.]], complex)
Y = np.array([[0., -1j], [1j, 0.]], complex)
Z = np.diag([1., -1.]).astype(complex)
I = np.eye(2, dtype=complex)


def A(x):
    return np.cos(x / 2) * I - 1j * np.sin(x / 2) * Z


def B(x, theta):
    return np.cos(x / 2) * I - 1j * np.sin(x / 2) * (
        np.sin(theta) * X + np.cos(theta) * Z
    )


def product(theta, m, phases):
    v = A(phases[0])
    for j in range(m):
        v = v @ B(phases[2 * j + 1], theta) @ A(phases[2 * j + 2])
    return v


def process_fidelity(target, actual):
    return float(abs(np.trace(target.conj().T @ actual)) ** 2 / 4)


def predicted(theta, m, beta):
    c = min(2 * m * theta, np.pi)
    return float(np.cos(max(beta - c, 0) / 2) ** 2)


def mean_error(c):
    return (1 + np.cos(c)) / 4 - (np.pi - c) * np.sin(c) / 8


checks = 0
rng = np.random.default_rng(2071)
for theta, m, beta in [
    (0.31, 1, 1.45), (0.31, 2, 2.50), (0.40, 1, 2.10),
    (0.40, 2, 2.90), (0.70, 1, 2.80), (0.20, 2, 0.30),
]:
    target = np.cos(beta / 2) * I - 1j * np.sin(beta / 2) * Y
    answer = predicted(theta, m, beta)
    best = 0.0
    for trial in range(9):
        start = rng.uniform(-np.pi, np.pi, 2 * m + 1)
        fun = lambda x: -process_fidelity(target, product(theta, m, x))
        opt = minimize(fun, start, method="BFGS", options={"maxiter": 350})
        best = max(best, -float(opt.fun))
        assert -float(opt.fun) <= answer + 1e-7
        checks += 1
    assert abs(best - answer) < 3e-7, (theta, m, beta, best, answer)
    checks += 1

for c in [0., 0.2, 0.7, 1.0, 2.0, np.pi - 0.2, np.pi]:
    numeric, _ = quad(
        lambda beta: np.sin(beta) * np.sin((beta - c) / 2) ** 2 / 2,
        c, np.pi, epsabs=1e-13
    )
    assert abs(numeric - mean_error(c)) < 1e-12
    checks += 1

# Haar SU(2) is the uniform three-sphere of unit quaternions.
samples = rng.normal(size=(70000, 4))
samples /= np.linalg.norm(samples, axis=1)[:, None]
beta = 2 * np.arcsin(np.sqrt(samples[:, 2] ** 2 + samples[:, 3] ** 2))
for theta, m in [(0.25, 0), (0.25, 1), (0.25, 3), (0.7, 1)]:
    c = min(2 * theta * m, np.pi)
    F = np.cos(np.maximum(beta - c, 0) / 2) ** 2
    assert abs(float(np.mean(1 - F)) - mean_error(c)) < 0.006
    checks += 1
    for f in [0.5, 0.7, 0.9, 0.98]:
        minimum = np.sin(c / 2) ** 2
        expected = (
            1.0 if f < minimum else
            (np.sin(c / 2 + np.arccos(np.sqrt(f))) ** 2)
        )
        assert abs(float(np.mean(F >= f)) - expected) < 0.012
        checks += 1

for d in [0.04, 0.07, 0.10]:
    ratio = mean_error(np.pi - d) / (d ** 4 / 96)
    assert abs(ratio - 1) < 0.007
    checks += 1

print(f"PASS: {checks} independent finite checks of fidelity, Haar law, and asymptotics")
