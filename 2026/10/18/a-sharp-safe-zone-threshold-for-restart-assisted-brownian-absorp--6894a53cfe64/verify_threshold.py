"""Independent finite-difference and numerical checks of a threshold-triggered reset model.

Requires Python 3, NumPy, SciPy. No data or network required.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.sparse import diags, lil_matrix
from scipy.sparse.linalg import spsolve


def relative_mean(y, c):
    if y == 0:
        return 1.0
    return (math.sinh(y / 2) / (y / 2)) ** 2 / math.cosh(c * y)


def analytic_mean(length, safe, rate):
    if rate == 0:
        return length * length
    y = length * math.sqrt(2 * rate)
    return length * length * relative_mean(y, 1 - safe / length)


def finite_difference_mean(length, safe, rate, interior=801):
    assert interior % 2 == 1
    dx = 2 * length / (interior + 1)
    x = -length + dx * np.arange(1, interior + 1)
    main = np.full(interior, 1 / dx**2 + rate)
    off = np.full(interior - 1, -0.5 / dx**2)
    operator = diags([off, main, off], [-1, 0, 1], format='lil')
    middle = interior // 2
    for i, xx in enumerate(x):
        if abs(xx) < safe:
            operator[i, middle] -= rate
    out = spsolve(operator.tocsr(), np.ones(interior))
    return float(out[middle])


def check():
    comparisons = 0
    max_relative_error = 0.0
    for safe in (0.3, 0.5, 0.7):
        for rate in (0.0, 0.1, 1.0, 5.0):
            exact = analytic_mean(1.0, safe, rate)
            numerical = finite_difference_mean(1.0, safe, rate)
            relative_error = abs(exact - numerical) / exact
            max_relative_error = max(relative_error, max_relative_error)
            assert relative_error < 0.003, (safe, rate, exact, numerical)
            comparisons += 1
    c0 = 1 / math.sqrt(6)
    for c in (0.05, 0.3, c0):
        for y in np.linspace(0.05, 15.0, 45):
            assert relative_mean(float(y), c) >= 1 - 5e-13
            comparisons += 1
    for c in (0.42, 0.5, 0.7, 0.9):
        vals = [relative_mean(float(y), c) for y in np.linspace(0.0001, 3, 1000)]
        assert min(vals) < 1 - 1e-7
        comparisons += 1
    for delta in (1e-4, 3e-4, 1e-3):
        c = math.sqrt(1/6 + delta)
        result = minimize_scalar(lambda y: relative_mean(y, c), bounds=(0.001, 6), method='bounded', options={'xatol': 1e-13})
        asymp_rate = (540 / 7) * delta
        observed_rate = result.x**2 / 2
        asymp_gain = (270 / 7) * delta**2
        observed_gain = 1 - result.fun
        assert abs(observed_rate / asymp_rate - 1) < 0.01
        assert abs(observed_gain / asymp_gain - 1) < 0.02
        comparisons += 2
    print(f'PASS {comparisons} independent checks; max finite-difference relative error={max_relative_error:.6g}')


if __name__ == '__main__':
    check()
