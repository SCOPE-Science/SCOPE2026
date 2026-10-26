#!/usr/bin/env python3
"""Supplementary finite-matrix checks for a Schatten-four commutator theorem."""
import numpy as np


def cost(x, y):
    sx = np.linalg.svd(x, compute_uv=False)
    sy = np.linalg.svd(y, compute_uv=False)
    return float((np.sum(sx ** 4) * np.sum(sy ** 4)) ** 0.25)


def check_sample(x, y):
    t = x @ y - y @ x
    q = x @ y + y @ x
    scale = 1 + np.linalg.norm(x) ** 3 * np.linalg.norm(y) ** 3
    assert abs(np.trace(t @ t @ t) + 3 * np.trace(q @ q @ t)) < 5e-9 * scale
    if np.linalg.norm(t) > 1e-10:
        moment = abs(np.trace(t @ t @ t))
        rhs = (np.linalg.norm(t, 'fro') ** 2 + moment / (3 * np.linalg.norm(t, 2))) / 4
        assert cost(x, y) ** 2 >= rhs - 5e-9 * (1 + rhs)


def run():
    rng = np.random.default_rng(20260917)
    count = 0
    for n in (2, 3, 4, 6):
        for _ in range(160):
            x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            y = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            check_sample(x, y)
            count += 1
    for spectrum in ([1, -1], [2, -2, 3, -3], [1j, -1j, 2, -2], [3, -3, 2j, -2j, 1, -1]):
        vals = np.asarray(spectrum, dtype=complex)
        n = len(vals)
        j = np.zeros((n, n), dtype=complex)
        for i in range(n):
            choices = np.flatnonzero(np.isclose(vals, -vals[i]))
            assert len(choices) == 1
            j[i, choices[0]] = 1
        d = np.diag(np.sqrt(np.abs(vals)))
        u = np.diag(vals / np.abs(vals))
        x = j @ d
        y = 0.5 * j @ u @ d
        t = x @ y - y @ x
        assert np.allclose(t, np.diag(vals))
        assert np.isclose(cost(x, y), np.linalg.norm(vals) / 2)
        check_sample(x, y)
        count += 1
    shift = np.roll(np.eye(3), 1, axis=0)
    d = np.diag([-1, 0, 1])
    x = shift @ np.diag([1, 0, 1])
    y = d @ shift.T
    t = x @ y - y @ x
    assert np.allclose(t, np.diag([2, -1, -1]))
    assert np.isclose(cost(x, y), np.sqrt(2))
    assert np.isclose(abs(np.trace(t @ t @ t)), 6)
    check_sample(x, y)
    count += 1
    print(f"PASS: {count} deterministic finite-matrix cases; analytic proof required for theorem")


if __name__ == '__main__':
    run()
