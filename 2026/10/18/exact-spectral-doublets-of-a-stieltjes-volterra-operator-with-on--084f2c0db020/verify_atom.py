"""Reproduce numeric diagnostics for one-atom Stieltjes integration.

Usage: python verify_atom.py (requires numpy). Analytic statements are proved
in RESULT.md; finite matrix and root tests are supplementary diagnostics.
"""
import math
import numpy as np

PI = math.pi


def cot_root(a, m, branch):
    """Monotone bisection: cot(k/2) = a*k + branch, branch in {+1,-1}."""
    lo = 2.0 * PI * m + 1e-10
    hi = 2.0 * PI * (m + 1) - 1e-10
    assert a > 0 and branch in (1, -1)
    for _ in range(75):
        mid = (lo + hi) / 2
        # reduce by whole periods to avoid large-angle cancellation
        r = mid - 2.0 * PI * m
        val = 1.0 / math.tan(r / 2.0) - a * mid - branch
        if val > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def roots(a, count):
    return [x for m in range(count) for x in
            (cot_root(a, m, 1), cot_root(a, m, -1))]


def characteristic(a, k):
    return math.cos(k) - a * k * math.sin(k) + (a*k)**2 * math.sin(k/2)**2


def factored(a, k):
    sn, cs = math.sin(k/2), math.cos(k/2)
    return (cs-(a*k+1)*sn)*(cs-(a*k-1)*sn)


def quadrature_kernel(a, n=240):
    # Midpoint Nyström discretization plus an EXACT separate point-mass sample.
    xs = np.r_[(np.arange(n)+0.5)/n, 0.5]
    masses = np.r_[np.full(n, 1.0/n), a]
    order = np.argsort(xs, kind='stable')
    x, w = xs[order], masses[order]
    mat = (x[:, None] > x[None, :])*np.sqrt(w[:, None]*w[None, :])
    return mat


def main():
    for a in (0.2, 0.5, 1.0, 2.0):
        rr = roots(a, 5)
        assert all(0 < x < y for x, y in zip(rr, rr[1:]))
        for j in range(5):
            kplus, kminus = rr[2*j:2*j+2]
            assert 2*PI*j < kplus < kminus < 2*PI*(j+1)
            assert abs(math.cos(kplus/2)-(a*kplus+1)*math.sin(kplus/2)) < 5e-11
            assert abs(math.cos(kminus/2)-(a*kminus-1)*math.sin(kminus/2)) < 5e-11
        for k in (0.37, 1.1, 2.7, 4.3, 6.45, 8.8):
            assert abs(characteristic(a,k)-factored(a,k)) < 2e-12
        for m in (100, 300):
            kp, kn = cot_root(a,m,1), cot_root(a,m,-1)
            observed = m**4 * (1/kp-1/kn)
            predicted = 1/(4*PI**4*a**2)
            assert abs(observed/predicted-1) < 0.0005
        mat = quadrature_kernel(a)
        sig = np.linalg.svd(mat, compute_uv=False)
        assert abs(np.sum(mat**2)-(0.5+a)) < 0.004
        assert np.max(np.abs(sig[:6] - 1/np.array(rr[:6]))) < 0.004
        print('mass',a,'first roots',rr[:4],
              'matrix discrepancy',float(np.max(abs(sig[:6]-1/np.array(rr[:6])))))
    print('ATOMIC_STIELTJES_SPECTRUM_CHECKS_OK')


if __name__ == '__main__':
    main()
