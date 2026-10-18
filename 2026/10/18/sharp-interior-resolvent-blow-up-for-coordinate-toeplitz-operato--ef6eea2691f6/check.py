#!/usr/bin/env python3
"""Finite-section numerical diagnostics for the harmonic Bergman coordinate resolvent.

Requires numpy and scipy. Not a proof of infinite-dimensional norm convergence.
"""
import numpy as np
from scipy.linalg import svdvals
from scipy.special import gammaln


def moment_log(alpha, n):
    return gammaln(n + 1) + gammaln(alpha + 2) - gammaln(n + alpha + 2)


def diagnostic(alpha, r, width=160):
    labels = np.arange(-width, width)
    logs = np.array([-.5 * moment_log(alpha, -k) if k < 0
                     else .5 * moment_log(alpha, k) for k in labels])
    row, col = labels[:, None], labels[None, :]
    # Coefficient from e_col to e_row of the inverse Laurent series.
    coeff = np.where(row < col,
                     np.power(r, np.maximum(col - row - 1, 0))
                     * np.exp(logs[:, None] - logs[None, :]), 0.)
    cross = coeff[:width, width:]
    sv = svdvals(cross)
    S = (1 - r*r)**(-alpha - 2)
    exact = np.sqrt(S*(S - 1))/r
    rel = abs(sv[0]/exact - 1)
    assert rel < 0.0005, (alpha, r, 'cross finite-section tail', rel)
    assert sv[1] < 1e-10 * sv[0], (alpha, r, 'rank one defect', sv[:2])
    full_sv = svdvals(coeff)[0]
    assert full_sv + 1e-9 >= sv[0]
    print(f'alpha={alpha:5.2f}, r={r:.2f}, '
          f'cross={sv[0]:.8g}, predicted={exact:.8g}, '
          f'full section={full_sv:.8g}, relative cross error={rel:.3g}')


if __name__ == '__main__':
    for a in (-0.5, 0.0, 2.0):
        for r in (0.7, 0.85, 0.93):
            diagnostic(a, r)
    print('All finite-section diagnostics passed.')
