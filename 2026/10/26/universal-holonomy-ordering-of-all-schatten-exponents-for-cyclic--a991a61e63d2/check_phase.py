"""Independent finite-dimensional checks for phase-ordered Schatten sums.

Requires Python 3, numpy, sympy. Run: python check_phase.py
Checks supplement, but do not replace, the analytic argument.
"""
import math
from itertools import product
import numpy as np
import sympy as sp


def gram(n, weights, phi):
    a = np.eye(n, dtype=complex)
    for j in range(n - 1):
        a[j, j + 1] = a[j + 1, j] = weights[j]
    a[n - 1, 0] = weights[-1] * np.exp(1j * phi)
    a[0, n - 1] = weights[-1] * np.exp(-1j * phi)
    return a


def moment(n, weights, phi, p):
    eig = np.linalg.eigvalsh(gram(n, weights, phi))
    assert eig.min() > 0
    return float(sum(x ** p for x in eig))


def exact_characteristic(n, weights):
    x, z = sp.symbols('x z')
    a = sp.eye(n)
    for j in range(n):
        a[j, j] = x - 1
    for j in range(n - 1):
        a[j, j + 1] = a[j + 1, j] = -weights[j]
    a[n - 1, 0] = -weights[-1] * z
    a[0, n - 1] = -weights[-1] / z
    poly = sp.expand(a.det(method='berkowitz'))
    tless = sp.expand(poly + sp.prod(weights) * (z + 1/z))
    assert not tless.has(z), 'More than the single flux monomial survives'
    return sp.expand(tless)


def run():
    checks = 0
    for n in range(4, 8):
        w = [sp.Rational(2 * j + 3, 12 * n + 1) for j in range(n)]
        poly = exact_characteristic(n, w)
        assert sp.degree(poly, sp.symbols('x')) == n
        checks += 1
        rw = list(map(float, w))
        assert all(rw[j - 1] + rw[j] < 1 for j in range(n))
        for phase in (0, np.pi / 5, np.pi / 2, 4 * np.pi / 5, np.pi):
            ev = np.linalg.eigvalsh(gram(n, rw, phase))
            assert np.min(ev) > 0
            e_poly = np.array([float(y) for y in sp.Poly(poly - 2 * sp.prod(w) * sp.cos(phase), sp.symbols('x')).all_coeffs()])
            assert np.max(np.abs(np.polyval(e_poly, ev))) < 2e-7
            checks += 1
        for p in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, n + 0.3, n + 1.0]:
            if p in [1, 2, 3, 4, 5, 6] and p < n:
                continue
            dif = moment(n, rw, 0.0, p) - moment(n, rw, math.pi, p)
            signed_factor = math.prod(p - k for k in range(1, n))
            assert dif * signed_factor > 0, (n, p, dif, signed_factor)
            checks += 1
        for p in range(1, n):
            moments = [moment(n, rw, q, p) for q in (0, 0.4, 1.6, math.pi)]
            assert max(moments) - min(moments) < 5e-8
            checks += 1
        p = n
        assert abs((moment(n, rw, 0, p) - moment(n, rw, math.pi, p)) - 4 * n * math.prod(rw)) < 2e-7
        checks += 1
    print('PASS:', checks, 'symbolic polynomial, positivity, phase-order, flat-moment, and exact-gap checks')


if __name__ == '__main__':
    run()
