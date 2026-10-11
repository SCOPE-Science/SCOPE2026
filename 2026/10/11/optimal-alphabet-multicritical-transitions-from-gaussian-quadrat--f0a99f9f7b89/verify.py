"""Finite diagnostics for Gaussian-quadrature multicritical full shifts.

Requires NumPy. These numerical tests are not proofs of the statements
for arbitrary alphabet size or all inverse temperatures.
"""
import math
import numpy as np
from numpy.polynomial.hermite_e import hermegauss


def quadrature(q):
    x, raw = hermegauss(q)  # integrates exp(-x^2/2) * f(x)
    return x, raw / math.sqrt(2.0 * math.pi)


def gauss_moment(j):
    if j % 2:
        return 0
    return math.prod(range(1, j, 2))  # (j-1)!!


def p(y, x, w):
    a = y * x
    m = np.max(a)
    return float(m + math.log(np.dot(w, np.exp(a - m))))


def main():
    trials = 0
    for q in range(2, 10):
        x, w = quadrature(q)
        assert np.all(w > 0)
        assert abs(np.sum(w) - 1) < 3e-13
        assert np.allclose(x, -x[::-1], atol=1e-12, rtol=0)
        assert np.allclose(w, w[::-1], atol=1e-12, rtol=0)
        for j in range(0, 2*q):
            exact = gauss_moment(j)
            observed = float(np.dot(w, x**j))
            assert abs(observed - exact) / max(1, abs(exact)) < 5e-11, (q, j, observed, exact)
            trials += 1
        # Degree 2q quadrature error is exactly q!, analytically.
        exact_err = float(gauss_moment(2*q) - np.dot(w, x**(2*q)))
        assert abs(exact_err / math.factorial(q) - 1) < 1e-10, (q, exact_err)
        trials += 1
        for y in (-2.5, -1.0, 1.0, 2.5):
            assert p(y,x,w) < y*y/2 - 1e-14, (q, y)
            trials += 1
        # The exact first non-Gaussian pressure term has coefficient
        # -q!/(2q)!, checked in symbolic cumulant algebra separately.
    print('PASS', trials, 'finite diagnostics for q=2..9')


if __name__ == '__main__':
    main()
