"""Finite reproducibility tests for a disappearing square-root cusp family.
These computations corroborate the analytical theorem, not establish its limits.
Requirements: Python 3, NumPy. Run: python verify.py
"""
import math
import numpy as np


def model(epsilon, points=100001, steps=120):
    theta = 2.0 - epsilon
    K = epsilon / (2.0 * math.sqrt(2.0))
    grid = np.linspace(0.0, 1.0, points)
    u = (np.sqrt(K * K + theta * (1.0 - grid)) - K) / theta
    g0 = 0.5 - u * u
    g1 = 0.5 + u * u
    weights = u / (K + theta * u)
    h = np.ones(points)
    for _ in range(steps):
        hnew = weights * (np.interp(g0, grid, h) + np.interp(g1, grid, h))
        hnew /= np.trapezoid(hnew, grid)
        h = hnew
    return grid, h


def right(z):
    return 1 - 1 / math.sqrt(1 + 16 * z)


def left(z, terms=64):
    return sum(2**(-j) * right(z / 2**j) for j in range(1, terms + 1))


def test():
    for z in (0.001, 0.1, 1.0, 10.0):
        assert abs(left(z) - 0.5*(left(z/2) + right(z/2))) < 3e-15
    for epsilon in (0.08, 0.04):
        grid, h = model(epsilon)
        assert abs(float(np.trapezoid(h, grid)) - 1) < 1e-11
        assert abs(h[0]) < 0.000001 and abs(h[-1]) < 0.000001
        hc = float(np.interp(0.5, grid, h))
        print('epsilon', epsilon, 'center', hc, 'L1_to_1', float(np.trapezoid(abs(h-1), grid)))
        for z in (0.1, 1.0, 10.0):
            observed_right = float(np.interp(1 - epsilon**2*z, grid, h))
            observed_left = float(np.interp(epsilon**2*z, grid, h))
            err_r = abs(observed_right-right(z)); err_l=abs(observed_left-left(z))
            print('   z',z,'right error',err_r,'left error',err_l)
            assert err_r < 0.11 and err_l < 0.12
        slope_right_exact = -hc * 8 / epsilon**2
        slope_left_exact = hc * 8 / (epsilon**2 * ((2 - epsilon/2)**2 - 1))
        assert slope_right_exact < 0 < slope_left_exact
        print('   predicted exact endpoint slopes', slope_left_exact, slope_right_exact)
    print('All finite checks passed. Infinite-limit assertions require the paper proof.')


if __name__ == '__main__':
    test()
