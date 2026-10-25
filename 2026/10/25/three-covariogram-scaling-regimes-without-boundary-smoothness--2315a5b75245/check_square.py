"""Reproducible scalar and square checks for radial (-p) covariogram limits.

Requires: numpy, sympy. Quadrature is illustrative, not an infinite proof.
"""
import numpy as np
import sympy as sp

q, z = sp.symbols('q z', positive=True, real=True)
E = (1 + sp.exp(q * z)) / 2 - ((1 + sp.exp(-z)) / 2)**(-q)
assert sp.simplify(E.subs(z, 0)) == 0
assert sp.simplify(sp.diff(E, z).subs(z, 0)) == 0
assert sp.simplify(sp.diff(E, z, 2).subs(z, 0) - q * (q + 1) / 4) == 0

N = 200000
ang = (np.arange(N) + 0.5) * (2 * np.pi / N)
v = np.column_stack((np.cos(ang), np.sin(ang)))
a = 1 / np.max(np.abs(v), axis=1)


def deficit(p, x):
    # For [-1,1]^2+x, the positive-ray exit is the least coordinate exit.
    b = np.min((1 + np.sign(v) * x) / np.abs(v), axis=1)
    zeta = p * np.log(b / a)
    q = 2 / p
    ell = np.logaddexp(zeta / 2, -zeta / 2) - np.log(2)
    Egap = np.exp(q * zeta / 2) * (
        np.cosh(q * zeta / 2) - 1 - np.expm1(-q * ell))
    return float(np.mean(a*a * Egap) * np.pi)

c = np.array([0.6, -0.4]); lim = 4 * np.log(np.cosh(c/2)).sum()
for p in (100, 400, 1200):
    val = p * deficit(p, c / p)
    print('critical', p, val, 'limit', lim)
assert abs(1200 * deficit(1200, c / 1200) - lim) < 0.002
u = np.array([0.2, 0.3])
for alpha in (-0.5, -1.5):
    expected = 2 * np.sum(abs(u)) if alpha > -1 else np.dot(u, u) / 2
    val = deficit(2000, u * (2000**alpha if alpha > -1 else 2000**((alpha - 1)/2))) / (2000**alpha)
    print('alpha', alpha, 'value', val, 'limit', expected)
    assert abs(val - expected) < (0.15 if alpha > -1 else 0.003)
print('All exact scalar and diagnostic square checks passed.')
