"""Independent moment-generator checks for the stated stationary correlation theorem.

Dependencies: Python 3, NumPy, SciPy. Run: python verify_covariance.py
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

Q = np.zeros((4, 4))
for i in range(4):
    Q[i, i] = -1
    Q[i, (i+1) % 4] = 1
q = np.array([1., 0., -1., 0.])
pi = np.ones(4) / 4


def direct_formula(h, t):
    return 0.5 / (h**4 + 4) * (
        (2-h*h)/h * np.exp(-h*t)
        + np.exp(-t) * (h*h*np.cos(t) + 2*np.sin(t))
    )


def independent_moment_solution(h, t):
    # Solve stationary joint mixed moments without the scalar convolution formula.
    stationary_mixed = np.linalg.solve(h*np.eye(4) - Q.T, pi*q)
    stationary_x2 = q @ stationary_mixed / h
    gen = np.zeros((5, 5))
    gen[0, 0] = -h
    gen[0, 1:] = q
    gen[1:, 1:] = Q.T
    return (expm(gen*t) @ np.r_[stationary_x2, stationary_mixed])[0]


def first_trough(h):
    return np.arctan2(2., h*h) + np.pi - np.arctan(1.-h)


def first_defect(h):
    gap = 1-h
    A = (2-h*h)/h
    M = np.sqrt(h**4+4) * np.exp(-gap*first_trough(h)) / np.sqrt(1+gap*gap)
    return A-M


def number_of_negative_intervals(h):
    assert 0 < h < 1
    gap = 1-h
    A = (2-h*h)/h
    M = np.sqrt(h**4+4) * np.exp(-gap*first_trough(h)) / np.sqrt(1+gap*gap)
    return max(0, int(np.ceil(np.log(M/A)/(2*np.pi*gap))))


def run():
    maximum_error = 0.
    for h in np.exp(np.linspace(np.log(.07), np.log(8.), 26)):
        for t in np.linspace(0., 22., 30):
            maximum_error = max(maximum_error, abs(direct_formula(h,t) - independent_moment_solution(h,t)))
    assert maximum_error < 3e-13, maximum_error
    hstar = brentq(first_defect, .8, .98, xtol=1e-14)
    assert abs(hstar - .8914223658803029) < 3e-13
    assert abs(first_defect(hstar)) < 1e-12
    examples = [(.7,0),(.85,0),(.9,1),(.95,2),(.97,4),(.98,6),(.99,12),(.995,25)]
    for h, expected in examples:
        count = number_of_negative_intervals(h)
        assert count == expected, (h,count,expected)
        sign = direct_formula(h, first_trough(h))
        assert (sign < 0) == (expected > 0), (h,sign)
    for h in [1., 1.01, 1.5, 4.]:
        assert direct_formula(h,4.) < 0 and direct_formula(h,7.) > 0
    for h in [.999, .9995, .9998]:
        count=number_of_negative_intervals(h)
        asym=np.log(5)/(4*np.pi*(1-h))
        assert abs(count/asym-1) < .05, (h,count,asym)
    print('PASS: 780 independent matrix-exponential comparisons; max abs error:', maximum_error)
    print('PASS: unique analytic threshold root checked numerically:', hstar)
    print('PASS: lobe counts, trough signs, oscillatory cases, leading lobe divergence')


if __name__ == '__main__':
    run()
