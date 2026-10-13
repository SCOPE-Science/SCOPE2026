"""Reproduce analytic identities and numerical stationary points for an exponentiated Haq CDF.

Requires mpmath and sympy. This numerical suite does not prove global root counts:
those follow from the analytic sign/implicit-function arguments in RESULT.md.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp

mp.mp.dps = 65


def terms(tau, y):
    tau, y = mp.mpf(tau), mp.mpf(y)
    D = 2 * (1 + tau) ** 2
    k = 2 * tau * (tau + 2)
    G = -mp.expm1(-y) - mp.exp(-y) * (2*y + y**2) / D
    g = mp.exp(-y) * (y**2 + k) / D
    A = 2 * y / (y**2 + k) - 1
    B = g / G
    return G, g, A, B


def log_derivative(tau, eps, y):
    _G, _g, A, B = terms(tau, y)
    return A + mp.mpf(eps) * B


def roots(tau, eps):
    # Change of signs on log-scale; find brackets; mpmath root stabilization.
    tau, eps = mp.mpf(tau), mp.mpf(eps)
    grid = [mp.power(10, -10 + i / 65) for i in range(950)]
    discovered = []
    for a, b in zip(grid, grid[1:]):
        fa, fb = log_derivative(tau, eps, a), log_derivative(tau, eps, b)
        if fa * fb >= 0:
            continue
        aa, bb = a, b
        for _ in range(210):
            m = (aa + bb) / 2
            if log_derivative(tau, eps, aa) * log_derivative(tau, eps, m) > 0:
                aa = m
            else:
                bb = m
        y = (aa + bb) / 2
        if not discovered or abs(y - discovered[-1]) > mp.mpf('1e-30'):
            discovered.append(y)
    return discovered


def symbolic_checks():
    y, tau, eps = sp.symbols('y tau eps', positive=True, real=True)
    D = 2 * (1 + tau) ** 2
    k = 2 * tau * (tau + 2)
    G = 1 - sp.exp(-y) * (1 + (y + y**2 / 2) / (1 + tau)**2)
    g = sp.exp(-y) * (y**2 + k) / D
    assert sp.simplify(sp.diff(G, y) - g) == 0
    A = sp.factor(sp.diff(sp.log(g), y))
    assert sp.simplify(A - (2*y/(y*y + k) - 1)) == 0
    assert sp.simplify(sp.diff(sp.log(g) + eps*sp.log(G), y) - A - eps*g/G) == 0
    t0 = -1 + sp.sqrt(sp.Rational(3, 2))
    assert sp.simplify(k.subs(tau, t0) - 1) == 0
    crit_A = - (y-1)**2 / (y*y + 1)
    assert sp.diff(crit_A, y, 2).subs(y, 1) == -1
    print('SYMBOLIC: derivative identities and critical curvature PASS')


def main():
    symbolic_checks()
    critical = mp.sqrt(mp.mpf('1.5')) - 1
    expected_coeff = 2 / mp.sqrt(3 * (mp.e - 2))
    _, _, _, critical_B = terms(critical, 1)
    assert mp.almosteq(critical_B, 2/(3*(mp.e-2)), rel_eps=mp.mpf('1e-59'))
    assert mp.almosteq(expected_coeff**2, 2*critical_B, rel_eps=mp.mpf('1e-59'))
    print('CRITICAL: tau_c =', mp.nstr(critical, 25), '; square-root coefficient =', mp.nstr(expected_coeff, 25))
    for tau in [mp.mpf('0.2'), critical, mp.mpf('0.25')]:
        for eps in [mp.mpf('0.01'), mp.mpf('0.001'), mp.mpf('0.0001')]:
            rs = roots(tau, eps)
            target = 3 if tau <= critical else 1
            assert len(rs) == target, (tau, eps, rs)
            assert abs(rs[0]/eps - 1) < mp.mpf('0.08')
            if tau == critical:
                left = (1-rs[1])/mp.sqrt(eps)
                right = (rs[2]-1)/mp.sqrt(eps)
                print('CRITICAL roots eps', mp.nstr(eps, 8), 'y', list(map(lambda q: mp.nstr(q, 15), rs)), 'split coeff', mp.nstr(left, 12), mp.nstr(right, 12))
            else:
                print('ROOTS tau', mp.nstr(tau, 8), 'eps', mp.nstr(eps, 8), ':', [mp.nstr(z, 14) for z in rs])
    print('NUMERIC: root-count examples and onset scaling PASS')

if __name__ == '__main__':
    main()
