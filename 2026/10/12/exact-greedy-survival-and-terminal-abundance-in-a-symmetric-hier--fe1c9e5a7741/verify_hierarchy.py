"""Standalone numerical checks of explicit formulae for a directed ecological competition chain.

The mathematical theorem relies on the analytical proof, not on finite simulations.
Requires Python 3, NumPy and SciPy.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp


def chain_rhs(t, x, r, d, predation):
    total = sum(x)
    out = np.empty_like(x)
    for i in range(len(x)):
        loss = 0.0 if i == 0 else predation[i - 1] * x[i - 1]
        out[i] = x[i] * (r * (1.0 - total) - d - loss)
    return out


def greedy_support(x):
    remaining = [i for i, xi in enumerate(x) if xi > 0.0]
    chosen = []
    while remaining:
        i = remaining.pop(0)
        chosen.append(i)
        remaining = [j for j in remaining if j != i + 1]
    return chosen


def solve(x0, p, r=0.9, d=0.18, horizon=1500.0):
    result = solve_ivp(chain_rhs, (0.0, horizon), np.array(x0, dtype=float),
                       args=(r, d, np.array(p, dtype=float)),
                       method='DOP853', rtol=4e-12, atol=2e-14)
    assert result.success, result.message
    return result.y[:, -1]


def check():
    r, d = 0.9, 0.18
    x0 = [0.18, 0.13, 0.15]
    p = [0.42, 0.63]
    out = solve(x0, p, r, d)
    k = 1.0 - d / r
    ratio = (x0[2] / x0[0]) * math.exp(-(p[1] / p[0]) * (x0[1] / x0[0]))
    expected = np.array([k / (1.0 + ratio), 0.0, k * ratio / (1.0 + ratio)])
    assert np.max(np.abs(out - expected)) < 2e-9, (out, expected)

    for x0, p in [
        ([0.08, 0.07, 0.11, 0.06, 0.09], [0.32, 0.45, 0.5, 0.36]),
        ([0.08, 0.07, 0.0, 0.09, 0.06, 0.0, 0.08], [0.32, 0.45, 0.5, 0.36, 0.48, 0.24]),
        ([0.0, 0.0, 0.14, 0.11, 0.12, 0.05], [0.32, 0.45, 0.5, 0.36, 0.48]),
        ([0.05, 0.07, 0.09, 0.06, 0.1, 0.08, 0.07], [0.32, 0.45, 0.5, 0.36, 0.48, 0.24]),
    ]:
        out = solve(x0, p, r, d)
        chosen = greedy_support(x0)
        assert abs(sum(out) - k) < 3e-9, (out, chosen)
        assert all(out[i] > 1e-6 for i in chosen), (out, chosen)
        assert all(abs(out[i]) < 2e-9 for i in range(len(out)) if i not in chosen), (out, chosen)
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
