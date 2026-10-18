"""Reproducible checks for transverse Fourier-zero crossings of tetrahedra.

This verifies exact algebraic jets and numerical local zeros; the infinite theorem
uses the analytical Brion formula and the real-analytic Morse lemma.
"""
from fractions import Fraction
from itertools import permutations
import sympy as sp
import mpmath as mp


def barycentric_weights(indices):
    points = (0, *indices)
    return tuple(Fraction(1, sp.prod(points[j] - points[k]
                                      for k in range(4) if k != j))
                 for j in range(4))


def restricted_quadratic(indices):
    w = barycentric_weights(indices)
    mat = sp.Matrix([[w[1] + w[1]*w[1]/w[3], w[1]*w[2]/w[3]],
                     [w[1]*w[2]/w[3], w[2] + w[2]*w[2]/w[3]]])
    return w, mat


def verify_exact():
    count = 0
    for t in permutations((-7, -3, 1, 2, 4, 6), 3):
        w, mat = restricted_quadratic(t)
        assert sum(w) == 0
        assert mat.det() == -w[0]*w[1]*w[2]/w[3]
        assert mat.det() < 0
        assert w[0]*w[1]*w[2]*w[3] > 0
        count += 1
    return count


def transform(frequencies):
    pts = (mp.mpf(0), *frequencies)
    return -1j * sum(mp.exp(-1j*pts[j]) /
                     mp.fprod(pts[j] - pts[k] for k in range(4) if k != j)
                     for j in range(4))


def verify_normalization():
    # Independent integration via polynomial moments on the standard simplex.
    mp.mp.dps = 65
    xi = (mp.mpf('0.37'), mp.mpf('0.91'), mp.mpf('1.37'))
    total = mp.mpc(0)
    for degree in range(43):
        homogeneous = mp.mpf(0)
        for a in range(degree + 1):
            for b in range(degree - a + 1):
                c = degree - a - b
                homogeneous += xi[0]**a * xi[1]**b * xi[2]**c
        total += (-1j)**degree * homogeneous/mp.factorial(degree + 3)
    value = transform(xi)
    error = abs(value - total)
    assert abs(total-mp.mpf(1)/6) < mp.mpf('0.2')
    assert error < mp.mpf('1e-48')
    return error


def numerical_curves():
    mp.mp.dps = 65
    idx = (1, 2, 3)
    base = [2*mp.pi*v for v in idx]
    w, mat = restricted_quadratic(idx)
    assert mat == sp.Matrix([[2, sp.Rational(-3, 2)],
                              [sp.Rational(-3, 2), 1]])
    max_resid = mp.mpf(0)
    slopes = []
    for t in (mp.mpf('0.003'), mp.mpf('0.001')):
        for ratio in (1, 2):
            guesses = (ratio*t, 3*(ratio-1)*t)
            def eqs(d2, d3):
                val = transform((base[0]+t, base[1]+d2, base[2]+d3))
                return mp.re(val), mp.im(val)
            u, v = mp.findroot(eqs, guesses, tol=mp.mpf('1e-50'))
            resid = abs(transform((base[0]+t, base[1]+u, base[2]+v)))
            assert resid < mp.mpf('1e-48')
            # The local curves have the theoretically prescribed first jets.
            assert abs(u/t-ratio) < mp.mpf('0.05')
            assert abs(v/t-3*(ratio-1)) < mp.mpf('0.15')
            max_resid = max(max_resid, resid)
            slopes.append((str(t), ratio, mp.nstr(u/t, 12), mp.nstr(v/t, 12)))
    return slopes, max_resid


if __name__ == '__main__':
    count = verify_exact()
    integration_error = verify_normalization()
    slopes, resid = numerical_curves()
    print('exact_tests', count)
    print('moment_series_error', mp.nstr(integration_error, 8))
    print('numerical_jet_tests', len(slopes))
    for s in slopes:
        print('t, tangent_branch, slope2, slope3', s)
    print('largest_numerical_residual', mp.nstr(resid, 8))
    print('PASS')
