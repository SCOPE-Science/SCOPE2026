"""Finite diagnostic checks for the exponential-kernel collision theorem.

These calculations test algebraic identities and asymptotic diagnostics;
the infinite distributional assertions require the written proof.
"""
from fractions import Fraction
from math import exp, expm1, log, isclose
import numpy as np
import mpmath as mp
import sympy as sp


def exact_precision(neighbor_correlations):
    r = [sp.Rational(a, b) for a, b in neighbor_correlations]
    n = len(r) + 1
    K = sp.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            v = sp.prod(r[i:j])
            K[i, j] = K[j, i] = v
    Q = sp.zeros(n)
    Q[0, 0] = 1
    for i, c in enumerate(r):
        d = sp.zeros(n, 1)
        d[i] = -c
        d[i + 1] = 1
        Q += d * d.T / (1-c*c)
    assert K * Q == sp.eye(n)
    return K, Q


exact_sets = [
    [(1, 2)],
    [(1, 2), (2, 3), (3, 4)],
    [(3, 5), (1, 3), (4, 7), (2, 5), (5, 8)],
]
for corr in exact_sets:
    exact_precision(corr)


def tridiag_precision(x, gamma):
    n = len(x)
    Q = np.zeros((n, n), dtype=np.float64)
    Q[0, 0] = 1.0
    for i, h in enumerate(np.diff(x)):
        r = np.exp(-gamma * h)
        den = -np.expm1(-2 * gamma * h)
        d = np.zeros(n)
        d[i], d[i + 1] = -r, 1.0
        Q += np.outer(d, d) / den
    return Q


rng = np.random.default_rng(31415927)
direct_checks = 0
for n in range(2, 9):
    for _ in range(40):
        x = np.sort(rng.uniform(size=n))
        gamma = rng.uniform(0.3, 3.0)
        K = np.exp(-gamma * abs(x[:, None] - x[None, :]))
        Q = tridiag_precision(x, gamma)
        assert np.allclose(Q @ K, np.eye(n), atol=4e-10, rtol=1e-9)
        direct_checks += 1

collision_checks = 0
for n in (2, 3, 5, 7):
    for gamma in (0.5, 1.0, 2.0):
        for h in (1e-4, 1e-5, 1e-6):
            # Exactly one small interior adjacent gap; others stay bounded away.
            x = np.linspace(0.08, 0.92, n)
            x[1] = x[0] + h
            Q = tridiag_precision(x, gamma)
            ratio = gamma * h * np.linalg.eigvalsh(Q)[-1]
            assert abs(ratio - 1.0) < 0.02
            collision_checks += 1


def exact_n2_tail(t, gamma):
    a = min(1.0, -np.log1p(-1.0/t) / gamma)
    return 2*a - a*a

for gamma in (0.5, 1., 2.):
    for t in (100.0, 1e3, 1e5):
        tail = exact_n2_tail(t, gamma)
        assert abs(t * tail - 2/gamma) < (2/gamma) * 0.02

# Exact finite-n uniform minimum-spacing distribution; a sampling check is
# supplementary to the exact volume calculation in the written proof.
spacing_checks = 0
for n in (3, 4, 6):
    a = 0.025
    target = 1.0 - (1.0 - (n-1)*a)**n
    U = np.sort(rng.uniform(size=(200000, n)), axis=1)
    observed = np.mean(np.min(np.diff(U, axis=1), axis=1) <= a)
    assert abs(target-observed) < 0.007
    spacing_checks += 1

mp.mp.dps = 40
ridge_checks = 0
for q in (1, 2):
    for tau in (mp.mpf('0.0001'), mp.mpf('0.00001')):
        gamma = mp.mpf('1.5')
        f = lambda h: 2*(1-h) / (tau + (1-mp.exp(-gamma*h)))**q
        value = mp.quad(f, [0, tau, mp.mpf('0.001'), mp.mpf('0.1'), 1])
        expected = (2/gamma) * (mp.log(1/tau) if q == 1 else tau**(1-q)/(q-1))
        assert abs(value/expected-1) < (mp.mpf('0.20') if q == 1 else mp.mpf('0.01'))
        ridge_checks += 1

print(f'VERIFY_OK exact_precision={len(exact_sets)} direct_precision={direct_checks} '
      f'single_collisions={collision_checks} exact_two_node_tails=9 '
      f'min_spacing={spacing_checks} nugget_integrals={ridge_checks}')
