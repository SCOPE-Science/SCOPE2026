"""Reproduce symbolic and finite-dimensional checks of a matching-polytope ellipsoid formula.

Run with Python 3 and SymPy: python verify.py
The symbolic identities supplement, but do not replace, the optimization proof.
"""
from __future__ import annotations

import math
import sympy as sp


def formula(n):
    r = n * (n - 2 + math.sqrt(n * n + 12 * n - 4)) / (2 * (2 * n - 1))
    den = 2 * n + (2 * n - 1) * r
    t = r / (n * (1 + r))
    lambdas = ((2 + r) / ((1 + r) ** 2 * den),
               2 / ((1 + r) * den),
               (2 + r) / ((1 + r) * den))
    return r, t, lambdas


def transform(a, lambdas):
    n = len(a)
    mean = sum(map(sum, a)) / (n * n)
    rows = [sum(row) / n - mean for row in a]
    cols = [sum(a[i][j] for i in range(n)) / n - mean for j in range(n)]
    l0, l1, l2 = lambdas
    return [[l0 * mean + l1 * (rows[i] + cols[j]) +
             l2 * (a[i][j] - mean - rows[i] - cols[j])
             for j in range(n)] for i in range(n)]


def ip(a, b):
    return sum(x * y for row, brow in zip(a, b) for x, y in zip(row, brow))


def verify_symbolic():
    n, r = sp.symbols('n r', real=True)
    polynomial = (2*n-1)*r**2-n*(n-2)*r-2*n**2
    den = 2*n+(2*n-1)*r
    l0 = (2+r)/((1+r)**2*den)
    l1 = 2/((1+r)*den)
    l2 = (2+r)/((1+r)*den)
    t = r/(n*(1+r))
    row_error = l0+(n-1)*l1-(1-n*t)**2
    entry_error = (l0+2*(n-1)*l1+(n-1)**2*l2)/n**2-t**2
    assert sp.cancel(row_error) == 0
    assert sp.cancel(entry_error+polynomial/(n*n*(1+r)*den)) == 0
    alpha = (1+r)*den/(2+r)
    beta = r*alpha
    assert sp.cancel(1/l0-alpha-beta) == 0
    assert sp.cancel(2/l1-2*alpha-beta) == 0
    assert sp.cancel(1/l2-alpha) == 0
    for m in range(2, 31):
        root = sp.Rational(m)*(m-2+sp.sqrt(m*m+12*m-4))/(2*(2*m-1))
        assert sp.simplify(polynomial.subs({n:m, r:root})) == 0
        assert root.evalf() > 0
    print('Symbolic identities, multiplier relations, and 29 radical roots: PASS')


def verify_finite():
    tested = 0
    contacts = 0
    for n in range(2, 10):
        r, t, lambdas = formula(n)
        assert r > 0 and 0 < n*t < 1 and min(lambdas) > 0
        eye = [[float(i == j) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                normal = [[float(ii == i and jj == j)
                           for jj in range(n)] for ii in range(n)]
                v = transform(normal, lambdas)
                gauge = math.sqrt(ip(normal, v))
                assert abs(gauge-t) < 1e-12
                touching = [[t-v[ii][jj]/gauge
                             for jj in range(n)] for ii in range(n)]
                assert abs(touching[i][j]) < 1e-12
                for ii in range(n):
                    assert min(touching[ii]) >= -1e-11
                    assert sum(touching[ii]) <= 1+1e-11
                for jj in range(n):
                    assert sum(touching[ii][jj] for ii in range(n)) <= 1+1e-11
                tested += 1
                contacts += 1
        for is_row in (True, False):
            for i in range(n):
                normal = [[float((ii if is_row else jj) == i)
                           for jj in range(n)] for ii in range(n)]
                v = transform(normal, lambdas)
                gauge = math.sqrt(ip(normal, v))
                assert abs(gauge-(1-n*t)) < 1e-12
                touching = [[t+v[ii][jj]/gauge
                             for jj in range(n)] for ii in range(n)]
                assert abs(ip(normal, touching)-1) < 1e-11
                for ii in range(n):
                    assert min(touching[ii]) >= -1e-11
                    assert sum(touching[ii]) <= 1+1e-11
                for jj in range(n):
                    assert sum(touching[ii][jj] for ii in range(n)) <= 1+1e-11
                tested += 1
                contacts += 1
    print(f'Frobenius supports and feasible facet contacts: PASS ({tested} facets, {contacts} contacts, n=2..9)')


if __name__ == '__main__':
    verify_symbolic()
    verify_finite()
    print('ALL CHECKS PASSED')
