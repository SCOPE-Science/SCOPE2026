"""Exact moment-identity and seeded simulation diagnostics for Gaussian Nyström LOO.
Science: compare a projection residual's exact moments with direct Gaussian sketches.
The analytic proof, not simulation, establishes the general theorem.
"""
from fractions import Fraction
from math import isclose
import numpy as np


def theory(n, m):
    assert n >= 1 and m >= 1
    if m > n:
        return Fraction(0), Fraction(0), Fraction(0)
    nu = n-m+1
    mean = Fraction(nu)
    pair_cov = Fraction(2*nu, nu+3) if m >= 2 else None
    variance = Fraction(2*nu*(n+3), m*(nu+3))
    return mean, pair_cov, variance


def one_sketch(n, m, rng):
    g = rng.standard_normal((n, m))
    y = np.empty(m)
    for j in range(m):
        h = np.delete(g, j, axis=1)
        if h.shape[1]:
            u, *_ = np.linalg.lstsq(h, g[:, j], rcond=None)
            residual = g[:, j]-h@u
        else:
            residual = g[:, j]
        y[j] = residual@residual
    return y


def main():
    # Exact algebra: Beta ratio E(sin^4) and the complete variance identity.
    exact_checks = 0
    for n in range(1, 35):
        for m in range(1, n+3):
            mean, paircov, var = theory(n, m)
            if m > n:
                assert (mean, paircov, var) == (0, 0, 0)
                exact_checks += 1
                continue
            nu = n-m+1
            d = nu+1
            ew = Fraction(d-1, d)
            ew2 = Fraction(d*d-1, d*(d+2))
            assert Fraction(d)*ew == mean
            assert Fraction(2*nu) == Fraction(2*d)*ew  # single chi-square variance
            if m >= 2:
                assert d*d*ew2 - mean*mean == paircov
                assert (2*nu+(m-1)*paircov)/m == var
            else:
                assert var == 2*nu
            exact_checks += 1
    # Variance cliffs: n=m (nonzero) versus m=n+1 (exact), and fixed codimension.
    for n in range(2, 50):
        assert theory(n,n)[2] == Fraction(n+3,2*n)
        assert theory(n,n+1)[2] == 0
        assert theory(n,n-1)[2] == Fraction(4*(n+3), (n-1)*5)
        exact_checks += 3
    # XNysTrace squared posterior proxy formula follows from an exchangeable variance identity.
    for n in range(2, 40):
        for m in range(2, n+1):
            nu = n-m+1
            v_basic = Fraction(2*nu)
            covariance = Fraction(2*nu, nu+3)
            expected_proxy = (v_basic-covariance)/m
            actual_variance = theory(n,m)[2]
            assert expected_proxy == Fraction(2*nu*(nu+2), m*(nu+3))
            assert actual_variance / expected_proxy == 1+Fraction(m,nu+2)
            exact_checks += 2
    print('exact rational identities checked:', exact_checks)
    rng = np.random.default_rng(20261010)
    # Only finite-sample sanity checks: they are not a proof of moment laws.
    for n, m, reps, tolerance in [(4,2,12000,.13), (5,4,12000,.14),
                                   (6,6,12000,.15), (6,7,160,1e-10)]:
        proxies = []
        vals = []
        for _ in range(reps):
            y = one_sketch(n,m,rng)
            vals.append(float((m-1)+y.mean()) if m <= n else float(n))
            if m >= 2:
                proxies.append(float(np.sum((y-y.mean())**2)/(m*(m-1))))
        vals = np.array(vals)
        mu, _, var = theory(n,m)
        observed_mean = float(vals.mean())
        observed_var = float(vals.var())
        assert abs(observed_mean-float(n)) < tolerance
        assert abs(observed_var-float(var)) < tolerance
        expected_proxy = (float(2*(n-m+1)*(n-m+3)) /
                          (m*(n-m+4))) if m <= n else 0.0
        assert abs(float(np.mean(proxies))-expected_proxy) < tolerance
        print('n,m',n,m,'trace mean/variance/proxy',round(observed_mean,5),
              round(observed_var,5),round(float(np.mean(proxies)),5),
              'theory',float(n),float(var),round(expected_proxy,5))
    print('seeded diagnostics passed; no asymptotic inference from simulation')


if __name__ == '__main__':
    main()
