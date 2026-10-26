"""Reproduce the two-reactive-zone capture probability and speed crossover.

Python 3, NumPy, SciPy. This is a finite numerical check of an analytic proof,
not a substitute for the strict monotonicity argument.
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def coefficients(alpha, kL, LL, kR, LR):
    AL = np.sqrt((alpha + kL) / kL)
    AR = np.sqrt((alpha + kR) / kR)
    BL = LL * np.sqrt(kL * (alpha + kL))
    BR = LR * np.sqrt(kR * (alpha + kR))
    return AL, BL, AR, BR


def formula(a, LL, LR, alpha, kL, kR, v, x=0., orientation_mean=0.):
    AL, BL, AR, BR = coefficients(alpha, kL, LL, kR, LR)
    RL = AL / np.tanh(BL / v)
    RR = AR / np.tanh(BR / v)
    return (RL + alpha * (x + a) / v + orientation_mean) / (RL + RR + 2 * alpha * a / v)


def independent_transfer(a, LL, LR, alpha, kL, kR, v, x=0., orientation_mean=0.):
    def generator(k):
        return np.array([[(alpha / 2 + k) / v, -alpha / (2 * v)],
                         [alpha / (2 * v), -(alpha / 2 + k) / v]])
    T_left = expm(LL * generator(kL))
    T_gap = expm(2 * a * generator(0.))
    T_right = expm(LR * generator(kR))
    one = np.ones(2)
    # Left exterior probability is a constant C_L; propagate its vector.
    # The right trap is affine with fixed vector (1,1), because killing
    # there guarantees the right capture label.
    outer_linear = T_right @ T_gap @ T_left @ one
    outer_affine = one - T_right @ one
    # Boundedness on the right exterior requires equal orientation components.
    C_left = -(outer_affine[0] - outer_affine[1]) / (outer_linear[0] - outer_linear[1])
    u = expm((x + a) * generator(0.)) @ (C_left * T_left @ one)
    return 0.5 * (u[0] + u[1]) + 0.5 * orientation_mean * (u[0] - u[1])


def check():
    random = np.random.default_rng(54177)
    max_error = 0.
    for _ in range(400):
        a, LL, LR = random.uniform(.25, 4, 3)
        alpha, kL, kR, v = np.exp(random.uniform(-1.7, 1.5, 4))
        x = random.uniform(-a, a)
        m = random.uniform(-1, 1)
        p1 = formula(a, LL, LR, alpha, kL, kR, v, x, m)
        p2 = independent_transfer(a, LL, LR, alpha, kL, kR, v, x, m)
        assert 0 < p1 < 1, ('probability bounds', p1)
        max_error = max(max_error, abs(p1 - p2))
        assert abs(p1 - p2) < 3e-10, (p1, p2)

    # Strict derivative of log(R_L/R_R) has the predicted sign.
    for _ in range(300):
        alpha, kL, kR, LL, LR = np.exp(random.uniform(-1.2, 1.2, 5))
        AL, BL, AR, BR = coefficients(alpha, kL, LL, kR, LR)
        t = random.uniform(.2, 2)
        derivative = 2 * BR / np.sinh(2 * BR * t) - 2 * BL / np.sinh(2 * BL * t)
        assert derivative * (BR - BL) < 1e-12
        if abs(BL - BR) > 1e-4:
            assert np.sign(derivative) == np.sign(BL - BR)

    # Rigorous crossover criterion predicted by contrary rankings of
    # local rates and integrated zone strengths; numerical root is unique.
    for _ in range(110):
        alpha, a, kL, kR, LL, LR = np.exp(random.uniform(-1, 1, 6))
        AL, BL, AR, BR = coefficients(alpha, kL, LL, kR, LR)
        condition = (kR - kL) * (kR * LR - kL * LL) < 0
        f = lambda v: AL / np.tanh(BL / v) - AR / np.tanh(BR / v)
        low, high = f(1e-8), f(1e8)
        if condition:
            assert low * high < 0
            root = brentq(f, 1e-8, 1e8, xtol=1e-12)
            assert abs(formula(a, LL, LR, alpha, kL, kR, root) - .5) < 2e-9
        else:
            assert low * high >= 0

    a, LL, LR, alpha, kL, kR = 2., 10., 1., 1., .2, 1.
    AL, BL, AR, BR = coefficients(alpha, kL, LL, kR, LR)
    crossover = brentq(lambda v: AL / np.tanh(BL / v) - AR / np.tanh(BR / v), .01, 100)
    assert abs(crossover - 2.216128236999827) < 1e-10
    assert formula(a, LL, LR, alpha, kL, kR, .5) > .5
    assert formula(a, LL, LR, alpha, kL, kR, 5) < .5
    small = 1e-5
    predicted_slope = (AL - AR) / (4 * alpha * a)
    assert abs((formula(a, LL, LR, alpha, kL, kR, small) - .5) / small - predicted_slope) < 1e-5
    limit = kR * LR / (kL * LL + kR * LR)
    assert abs(formula(a, LL, LR, alpha, kL, kR, 1e6) - limit) < 1e-9
    # Exact symmetry sanity check.
    for speed in np.geomspace(.01, 100, 25):
        assert abs(formula(2, 1.3, 1.3, .6, .8, .8, speed) - .5) < 1e-14
    print('PASS: 400 independent matrix-transfer comparisons; max error %.3g' % max_error)
    print('PASS: 300 strict-derivative tests and 110 crossover comparisons')
    print('PASS: limits, exact symmetry, and reference crossover %.12f' % crossover)


if __name__ == '__main__':
    check()
