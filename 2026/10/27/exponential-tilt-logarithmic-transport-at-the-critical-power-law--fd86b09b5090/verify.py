"""Finite numerical checks for a restarted three-state lattice quantum walk.

Requires numpy and scipy. Finite diagnostics do not establish limiting claims.
"""
import numpy as np
from scipy.special import zeta


def renewal_age_distribution(n, parameter):
    exponent = 2 + parameter / np.log(n)
    z = zeta(exponent, 1)
    p = np.zeros(n + 1)
    p[1:] = np.arange(1, n + 1, dtype=float) ** (-exponent) / z
    renew = np.zeros(n + 1)
    renew[0] = 1
    for j in range(1, n + 1):
        renew[j] = np.dot(p[1:j+1], renew[j-1::-1])
    survival = np.array([zeta(exponent, j + 1) / z for j in range(n+1)])
    age = renew[::-1] * survival
    assert abs(np.sum(age) - 1.0) < 5e-10
    assert np.min(renew) > 0
    assert np.max(np.diff(renew)) < 1e-12  # geometric-mixture monotonicity
    return age, renew, survival


def flat_band_weight(ell, chi, mesh=1800):
    s = np.array([1, np.sqrt(ell), 1], dtype=complex) / np.sqrt(ell+2)
    anti = np.array([1, 0, -1], dtype=complex) / np.sqrt(2)
    exact = (np.sqrt(ell+2) * abs(np.vdot(s, chi))**2
             + np.sqrt(2) * abs(np.vdot(anti, chi))**2) / (np.sqrt(ell+2)+np.sqrt(2))
    coin = 2 * np.outer(s, s.conj()) - np.eye(3)
    accum = 0.
    maxerr = 0.
    for k in (np.arange(mesh) + 0.5) * 2*np.pi/mesh:
        U = np.diag([np.exp(-1j*k), 1, np.exp(1j*k)]) @ coin
        vals, vecs = np.linalg.eig(U)
        idx = np.argmin(abs(vals - 1))
        maxerr = max(maxerr, abs(vals[idx] - 1))
        v = vecs[:, idx]/np.linalg.norm(vecs[:, idx])
        accum += abs(np.vdot(v, chi))**2
    computed = accum / mesh
    assert maxerr < 3e-12
    assert abs(computed - exact) < 1e-6, (ell, computed, exact)
    return exact


def main():
    for ell in [0.4, 1.0, 3.0]:
        s = np.array([1, np.sqrt(ell), 1], dtype=complex)/np.sqrt(ell+2)
        dark = np.array([np.sqrt(ell), -2, np.sqrt(ell)], dtype=complex)/np.sqrt(2*(ell+2))
        assert abs(np.vdot(s, dark)) < 2e-15
        assert abs(flat_band_weight(ell, dark)) < 1e-10
        assert 0 < flat_band_weight(ell, s) < 1
        assert 0 < flat_band_weight(ell, np.array([1., 0, 0])) < 1
    for lam in [-2., 0., 2.]:
        for n in [300, 900, 1800]:
            ages, renew, survival = renewal_age_distribution(n, lam)
            integral = -np.expm1(-lam)/lam if lam else 1.
            estimate = np.sum(survival[:-1])/(np.log(n)/float(zeta(2., 1))*integral)
            assert .6 < estimate < 1.65
            # These distributional comparisons have slowly vanishing finite-size corrections.
            for x in [.25, .5, .75]:
                empirical = ages[:int(n**x)+1].sum()
                target = np.expm1(-lam*x)/np.expm1(-lam) if lam else x
                assert abs(empirical-target) < .28, (n, lam, x, empirical, target)
    print('PASS: 9 flat-band quadratures, 9 renewal normalizations, 27 log-age finite diagnostics')


if __name__ == '__main__':
    main()
