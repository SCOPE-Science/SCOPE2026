"""Reproducibility checks for two exact residual-fitting rules on Gaussian subspaces.

Run: python verification/check.py
Dependencies: numpy, scipy.
These finite checks validate implemented formulas, not a proof of distributional statements.
"""
from fractions import Fraction
from math import gamma, isclose

import numpy as np
from scipy.special import betainc


def ratio_cdf(t, numerator_df, denominator_df):
    if t < 0:
        return 0.0
    return float(betainc(numerator_df / 2, denominator_df / 2, t / (1 + t)))


def exact_witness():
    # One row of J and a two-column deterministic sketch in ambient dimension 3.
    # G has rows (1, 1), (3, 0), (0, 1). The two corrections fit the same row.
    raw_z = (Fraction(1, 2), Fraction(1, 2))
    orth_z = (Fraction(1, 10), Fraction(9, 10))
    assert sum(raw_z) == sum(orth_z) == 1
    raw_norm2 = 1 + (3 * raw_z[0]) ** 2 + raw_z[1] ** 2
    orth_norm2 = 1 + (3 * orth_z[0]) ** 2 + orth_z[1] ** 2
    assert raw_norm2 == Fraction(7, 2)
    assert orth_norm2 == Fraction(19, 10)
    return 3


def matrix_checks(seed=82436):
    rng = np.random.default_rng(seed)
    checks = 0
    for r, l, d in [(1, 1, 3), (1, 2, 4), (1, 3, 5),
                    (2, 3, 7), (2, 5, 8), (3, 5, 10)]:
        J = rng.normal(size=(r, d))
        delta = rng.normal(size=r)
        h_star = -J.T @ np.linalg.solve(J @ J.T, delta)
        assert np.linalg.norm(h_star) > 0
        P = J.T @ np.linalg.solve(J @ J.T, J)
        for _ in range(40):
            G = rng.normal(size=(d, l))
            Q, _ = np.linalg.qr(G, mode='reduced')
            raw_z = np.linalg.lstsq(J @ G, -delta, rcond=None)[0]
            ortho_z = np.linalg.lstsq(J @ Q, -delta, rcond=None)[0]
            h_raw, h_ortho = G @ raw_z, Q @ ortho_z
            for h in (h_raw, h_ortho):
                assert np.linalg.norm(J @ h + delta) < 1e-9
                assert np.linalg.norm(P @ h - h_star) < 1e-9
                assert np.linalg.norm(h) ** 2 + 1e-9 >= np.linalg.norm(h_star) ** 2
                checks += 3
            assert np.linalg.norm(h_raw) ** 2 + 1e-9 >= np.linalg.norm(h_ortho) ** 2
            checks += 1
        if l == r:
            # A unique correction in the r-plane; both coordinate rules coincide.
            assert np.linalg.matrix_rank(J @ G) == r
            checks += 1
    return checks


def distribution_checks(seed=98504):
    rng = np.random.default_rng(seed)
    checks = 0
    # Batch QR and pseudoinverse via row-aligned J; independent across trials.
    for r, l, d, batch in [(1, 1, 3, 14000), (1, 3, 5, 14000),
                           (2, 5, 8, 12000), (2, 9, 12, 10000)]:
        q = d - r
        s = d - l
        nu = l - r + 1
        G = rng.normal(size=(batch, d, l))
        # h_star = e_1, so row J is [I,0] and RHS e_1.
        A = G[:, :r, :]
        rhs = np.broadcast_to(np.eye(r)[0], (batch, r))
        raw_z = np.einsum('bij,bj->bi', np.linalg.pinv(A), rhs)
        raw_h = np.einsum('bij,bj->bi', G, raw_z)
        Q = np.linalg.qr(G, mode='reduced')[0]
        Qtop = Q[:, :r, :]
        ortho_z = np.einsum('bij,bj->bi', np.linalg.pinv(Qtop), rhs)
        ortho_h = np.einsum('bij,bj->bi', Q, ortho_z)
        raw_ratio = np.einsum('ij,ij->i', raw_h[:, r:], raw_h[:, r:])
        ortho_ratio = np.einsum('ij,ij->i', ortho_h[:, r:], ortho_h[:, r:])
        assert np.max(np.abs(raw_h[:, :r] - rhs)) < 1e-8
        assert np.max(np.abs(ortho_h[:, :r] - rhs)) < 1e-8
        assert np.min((raw_ratio - ortho_ratio) / (1 + raw_ratio + ortho_ratio)) > -1e-10
        checks += 3
        # The beta-prime CDF is fully specified by the theorem.
        for threshold in (0.25, 0.7, 1.0, 2.0, 6.0):
            for empirical_ratio, numerator_df in ((raw_ratio, q), (ortho_ratio, s)):
                observed = float(np.mean(empirical_ratio <= threshold))
                expected = ratio_cdf(threshold, numerator_df, nu)
                assert abs(observed - expected) < 0.033, (r, l, d, threshold, numerator_df, observed, expected)
                checks += 1
        if nu > 2:
            for numerator_df in (q, s):
                gamma_ratio = (gamma((numerator_df + 2) / 2) * gamma((nu - 2) / 2)
                               / (gamma(numerator_df / 2) * gamma(nu / 2)))
                assert isclose(gamma_ratio, numerator_df / (nu - 2), rel_tol=1e-12)
                checks += 1
    return checks


def main():
    e = exact_witness()
    m = matrix_checks()
    p = distribution_checks()
    print('PASS exact rational identities:', e)
    print('PASS deterministic matrix assertions:', m)
    print('PASS distributional and moment consistency assertions:', p)
    print('PASS total assertions:', e + m + p)
    print('Finite checks do not certify equality of laws or moment divergence.')


if __name__ == '__main__':
    main()
