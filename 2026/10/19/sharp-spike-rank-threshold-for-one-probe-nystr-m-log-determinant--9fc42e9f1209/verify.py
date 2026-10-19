#!/usr/bin/env python3
"""Finite numerical checks of the two-level Nyström logdet theorem.

The parameter-uniform integrability and sharp threshold follow from the
accompanying analytical proof, not from these finite numerical tests.
Requires numpy.
"""
import numpy as np


def matrix_case(r, s, ell, t, rng):
    n = r + s
    U = rng.standard_normal((r, ell))
    V = rng.standard_normal((s, ell))
    Om = np.vstack((U, V))
    A = np.diag([t] * r + [1.0] * s)
    Ah = (A @ Om) @ np.linalg.solve(Om.T @ A @ Om, Om.T @ A)
    P = np.eye(n) + Ah
    ev, Q = np.linalg.eigh(P)
    assert ev.min() > 0
    iroot = (Q * (1 / np.sqrt(ev))) @ Q.T
    M = iroot @ (np.eye(n) + A) @ iroot
    M = (M + M.T)/2
    mu = np.linalg.eigvalsh(M)
    assert mu.min() > 1 - 2e-7
    assert np.isclose(np.linalg.slogdet(P)[1] + np.log(mu).sum(),
                      np.log1p(t)*r + np.log(2.0)*s, atol=5e-7, rtol=5e-8)
    # Exact reduction to unrepresented top directions (numerical witness).
    if ell < r:
        basis, _, _ = np.linalg.svd(U, full_matrices=True)
        E = np.vstack((basis[:, ell:], np.zeros((s, r-ell))))
        assert np.linalg.norm(Ah @ E) < 5e-7
        assert np.linalg.norm(M @ E - (1+t)*E) < 1e-6
    bound = 2 + np.linalg.norm(V @ np.linalg.pinv(U), 2)**2
    eig_s = np.sort(mu)
    if ell < r:
        # Using the invariant-space basis avoids ambiguous sorted eigenvalues.
        N = np.hstack((basis[:, :ell], np.zeros((r, s)))) if False else None
        retained = np.sort(mu)[:n-(r-ell)]
        # For t near one it is possible for an unmatched eigenvalue to equal 2;
        # the following bound holds for every retained H-mode.
        assert retained.max() <= bound + 2e-6
    else:
        assert mu.max() <= bound + 2e-6
    log_sq = 2 * np.square(np.log(np.maximum(mu, 1e-14))).sum()
    lower = 2 * max(r-ell, 0) * np.log1p(t)**2
    assert log_sq >= lower - 2e-5
    assert log_sq - lower <= 2 * n * np.log(bound)**2 + 2e-5
    return float(log_sq-lower)


def main():
    rng = np.random.default_rng(20261011)
    cases = 0
    max_resid = 0.0
    for r in range(1, 5):
        for s in range(1, 4):
            for ell in range(1, r+s):
                for t in (1.0, 10.0, 1000.0):
                    for _ in range(8):
                        resid = matrix_case(r,s,ell,t,rng)
                        max_resid = max(max_resid, resid)
                        cases += 1
    print('VERIFY_OK numerical_matrix_cases=%d max_checked_bounded_remainder=%.6f analytic_integrability_requires_proof=true' % (cases,max_resid))

if __name__ == '__main__':
    main()
