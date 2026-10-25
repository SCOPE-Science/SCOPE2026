"""Finite reproducibility checks for the exact two-by-two Schatten-four phase formula.

Run: python3 check_s4_phase.py (NumPy required). These diagnostics are not
substitutes for the proof of the universal inequality or cb equality.
"""
import math
import cmath
import numpy as np


def norm4_fourth(x):
    gram = x.conj().T @ x
    return float(np.trace(gram @ gram).real)


def formula(delta):
    c = math.cos(delta)
    b = 9.0 - c
    return (b + math.sqrt(max(0.0, (b - 8.0) * (b + 8.0)))) / 8.0


def witness(delta):
    if delta == 0:
        return np.ones((2, 2), dtype=np.complex128)
    k = formula(delta)
    z = complex((math.cos(delta) - k) / (3 * (k - 1)),
                -math.sin(delta) / (3 * (k - 1)))
    assert abs(abs(z) - 1) < 5e-9
    return np.array([[1.0, 1.0], [1.0, z]], dtype=complex)


def check():
    rng = np.random.default_rng(26082026)
    tests = 0
    angles = [0.0, 0.05, 0.2, 0.75, 1.4, 2.2, math.pi]
    for delta in angles:
        symbol = np.array([[1.0, 1.0], [1.0, cmath.exp(1j * delta)]],
                          dtype=complex)
        k = formula(delta)
        assert abs(8 * k * k - 2 * (9 - math.cos(delta)) * k + 8) < 1e-11
        tests += 1
        x = witness(delta)
        r = norm4_fourth(symbol * x) / norm4_fourth(x)
        assert abs(r - k) < 5e-9, (delta, r, k)
        tests += 1
        for _ in range(1200):
            x = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
            r = norm4_fourth(symbol * x) / norm4_fourth(x)
            assert r <= k + 3e-12, (delta, r, k)
            tests += 1
    for delta in [0.05, 0.7, 1.8, math.pi]:
        # The formula is invariant under entrywise left/right phase gauges.
        row = np.exp(1j * rng.uniform(-math.pi, math.pi, size=2))
        col = np.exp(1j * rng.uniform(-math.pi, math.pi, size=2))
        m = np.outer(row, col) * np.array([[1.0, 1.0], [1.0, cmath.exp(1j*delta)]])
        eta = m[0, 0]*m[1, 1]/(m[0, 1]*m[1, 0])
        assert abs(formula(abs(cmath.phase(eta))) - formula(delta)) < 1e-11
        tests += 1
    print(f"PASS: {tests} deterministic tests; seven sharp witnesses; random inequalities")


if __name__ == '__main__':
    check()
