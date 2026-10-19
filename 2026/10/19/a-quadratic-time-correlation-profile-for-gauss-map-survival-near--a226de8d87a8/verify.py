#!/usr/bin/env python3
"""Independent arithmetic diagnostics for a Gauss-map finite-survival theorem.

Requires mpmath; finite arithmetic cannot establish the quantified theorem.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 45
checks = 0

# Finite continued-fraction branch cylinders: g_i o g_j has endpoints
# whose difference agrees with the closed rational expression.
for k in (3, 4, 7):
    a = Fraction(1, k)
    for i in range(k, k + 13):
        for j in range(k, k + 13):
            gj = lambda y: 1 / (j + y)
            gi = lambda y: 1 / (i + y)
            cylinder = gi(gj(a)) - gi(gj(Fraction(0)))
            closed = a / ((i * j + 1) * (i * j + 1 + i * a))
            assert cylinder == closed
            checks += 1

for k in (3, 4, 5, 8, 13, 21, 34, 55, 89):
    K = mp.mpf(k)
    alpha = 1 / K
    p = mp.zeta(2, K)
    q = mp.zeta(3, K)
    c = 2 * q / p
    lam = p - c * q
    assert p > 0 and lam > 0 and 1 - c * alpha > 0
    checks += 1

    # Direct integral of the transfer image versus its digamma primitive.
    exact_two = mp.digamma(K + alpha) - mp.digamma(K)
    integrated_two = mp.quad(lambda y: mp.zeta(2, K + y), [0, alpha])
    assert abs(exact_two - integrated_two) < mp.mpf('1e-36')
    checks += 1

    # The explicit approximate eigenfunction has uniformly small residual.
    for h in range(9):
        y = alpha * h / 8
        trial = 1 - c * y
        transfer_trial = mp.zeta(2, K + y) - c * mp.zeta(3, K + y)
        relative = abs(transfer_trial / (lam * trial) - 1)
        assert relative <= 128 / K**4
        checks += 1

    # Scalar spectral correction approaches its predicted quadratic scaling.
    deficit = K**2 * (1 - lam / p)
    assert abs(deficit - mp.mpf('0.5')) < 1 / K
    checks += 1

for k in (50, 100, 200, 400):
    K = mp.mpf(k)
    p, q = mp.zeta(2, K), mp.zeta(3, K)
    lam = p - 2 * q*q/p
    # At n=k^2 the correction factor approaches e^(-1/2).
    finite = (lam / p)**(k*k - 1)
    assert abs(finite - mp.exp(-mp.mpf('0.5'))) < 2 / K
    checks += 1

print(f'PASS: {checks} checks (exact rational cylinders, quadrature, residual, asymptotic diagnostics).')
