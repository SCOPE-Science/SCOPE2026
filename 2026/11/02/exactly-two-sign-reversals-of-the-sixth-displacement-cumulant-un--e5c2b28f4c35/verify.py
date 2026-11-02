#!/usr/bin/env python3
"""Exact and numerical checks and exact algebra for an orientationally reset swimmer.

Recompute the order-six cumulant from the tilted angular generator's
Fourier-coefficient recursion, certify its positive-root count by Descartes,
and compare against finite Fourier-matrix spectral differentiation.
"""
from fractions import Fraction
from math import factorial

import numpy as np
import sympy as sp

Q = sp.symbols('q', positive=True)
C = [
    20782448640000, 181236700108800, 54861583665024,
    -2573265668397984, -6219315460897056, -3549159799788784,
    790599382490714, 1743348986439210, 891840550099254,
    249919114303995, 43934398967304, 5036657759205,
    375256499910, 17440408989, 456634850, 5106569,
]
P = sum(c * Q**j for j, c in enumerate(C))
DEN = (Q + 1)**11 * (Q + 4)**5 * (Q + 9)**4 * (Q + 16)**3 * (Q + 25)**2 * (Q + 36)
PROPOSED_K6 = 4320 * P / DEN


def symbolically_recompute():
    """All coefficients needed for the sixth order lie in n+j <= 6."""
    nmax = 6
    coeff = {(n, 0): Q / (Q + n * n) if n else sp.Integer(1)
             for n in range(nmax + 1)}
    eigen = {}
    for j in range(1, nmax):
        coeff[0, j] = sp.Integer(0)
        eigen[j] = coeff[1, j - 1]
        for n in range(1, nmax - j + 1):
            val = ((coeff[n - 1, j - 1] + coeff[n + 1, j - 1]) / 2
                   - sum(eigen[p] * coeff[n, j - p] for p in range(1, j + 1)))
            coeff[n, j] = sp.cancel(val / (Q + n * n))
    eigen[6] = coeff[1, 5]
    return eigen


def spectral_cumulant(q, cutoff=10, samples=96, radius=0.6):
    """Truncated Fourier spectrum: diagnostic only, not an infinite proof."""
    n = np.arange(-cutoff, cutoff + 1)
    size = len(n)
    matrix = np.diag(-(n * n + q).astype('complex128'))
    matrix[cutoff, :] += q  # a reset replaces every Fourier basis function by 1
    cos_op = np.zeros_like(matrix)
    for i in range(size - 1):
        cos_op[i, i + 1] = 0.5
        cos_op[i + 1, i] = 0.5
    coefficient = 0j
    for j in range(samples):
        angle = 2 * np.pi * j / samples
        z = radius * np.exp(1j * angle)
        eigs = np.linalg.eigvals(matrix + z * cos_op)
        dominant_branch = eigs[np.argmin(abs(eigs))]
        coefficient += (dominant_branch * np.exp(-6j * angle)
                        / (samples * radius**6))
    return factorial(6) * coefficient


def main():
    assert len(C) == 16
    exact = symbolically_recompute()
    assert sp.cancel(factorial(6) * exact[6] - PROPOSED_K6) == 0
    assert sp.cancel(2 * exact[2] - (10*Q + 4)/((Q + 1)**3 * (Q + 4))) == 0
    assert sp.limit(PROPOSED_K6, Q, 0, dir='+') == 145
    signs = [1 if c > 0 else -1 for c in reversed(C)]
    sign_changes = sum(a != b for a, b in zip(signs, signs[1:]))
    assert sign_changes == 2
    assert P.subs(Q, sp.Rational(1, 4)) > 0
    assert P.subs(Q, sp.Rational(13, 50)) < 0
    assert P.subs(Q, sp.Rational(29, 20)) < 0
    assert P.subs(Q, sp.Rational(3, 2)) > 0
    roots = sp.nroots(P, n=32, maxsteps=1000)
    positives = sorted(float(sp.re(x)) for x in roots if abs(float(sp.im(x))) < 1e-20 and float(sp.re(x)) > 0)
    assert len(positives) == 2
    assert abs(positives[0] - .25253781628132383) < 1e-13
    assert abs(positives[1] - 1.451522667963111) < 1e-13
    for q in [0.2, 0.5, 1.0, 2.0, 3.0]:
        symbolic = float(PROPOSED_K6.subs(Q, sp.Rational(str(q))))
        spectral = spectral_cumulant(q)
        assert abs(spectral.real - symbolic) < 1e-7, (q, spectral, symbolic)
        assert abs(spectral.imag) < 1e-7, (q, spectral)
        print(f'q={q:g}: exact={symbolic:.12g}, Fourier-matrix={spectral.real:.12g}')
    print('Exact algebra, root-count certificate, and five independent Fourier-matrix diagnostics: PASS')
    print('Positive critical ratios:', ', '.join(f'{x:.15g}' for x in positives))


if __name__ == '__main__':
    main()
