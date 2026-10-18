#!/usr/bin/env python3
"""Numerical corroboration of large-order Volterra singular-value asymptotics.

Uses Gauss-Laguerre Nyström discretization of the reflected, rescaled
Hankel kernel. This is a finite-precision check, not a proof of limits.
Requires NumPy >= 1.24 and SciPy >= 1.10.
"""
import math
import numpy as np
from scipy.linalg import eigvalsh
from scipy.special import roots_laguerre


def nystrom(alpha, nodes=70):
    z, w = roots_laguerre(nodes)
    s = (z[:, None] + z[None, :]) / 2.0
    f = np.zeros_like(s)
    inside = s < alpha
    f[inside] = np.exp(s[inside] + (alpha-1)*np.log1p(-s[inside]/alpha))
    # The matrix represents the kernel in weighted quadrature coordinates:
    # K_alpha(u,v) = (1-(u+v)/alpha)_+^(alpha-1).
    mat = 0.5*np.sqrt(w[:, None]*w[None, :])*f
    vals = eigvalsh(mat)
    return np.sort(np.abs(vals))[::-1], vals[0], float(np.sum(vals*vals))


def main():
    for alpha in (20, 40, 80, 160, 320):
        sig, negative, hs2 = nystrom(alpha)
        s1, s2, s3 = sig[:3]
        c2 = alpha*s2
        op2 = alpha*alpha*(s1-0.5-1/(8*alpha))
        tail3 = alpha*alpha*s3
        target_hs2 = 1/(4-2/alpha)
        # Finite quadrature tolerances. The asymptotic rates have O(1/alpha)
        # corrections and therefore these conditions are not equality checks.
        assert negative < 0, (alpha, negative)
        assert abs(c2-1/8) < 0.01, (alpha, c2)
        assert abs(op2-1/32) < 0.001, (alpha, op2)
        assert abs(hs2-target_hs2) < 1e-9, (alpha, hs2, target_hs2)
        print(f'alpha={alpha:3d} alpha*s2={c2:.10f}  '
              f'alpha^2*(s1-1/2-1/(8alpha))={op2:.10f}  '
              f'alpha^2*s3={tail3:.9f} HS2-analytic={hs2-target_hs2:+.2e}')
    print('FINITE_NUMERICAL_CHECKS_OK')


if __name__ == '__main__':
    main()
