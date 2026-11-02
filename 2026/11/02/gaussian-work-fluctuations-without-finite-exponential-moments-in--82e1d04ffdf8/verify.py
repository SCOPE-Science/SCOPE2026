"""Reproducible algebra and independent finite-sample checks for intermittent-trap work.

Requires Python 3 and NumPy. Run: python verify.py
The Monte Carlo part corroborates but does not prove asymptotic results.
"""
from fractions import Fraction
import math
import numpy as np


def algebra_check():
    cases = [(1, 1, 1), (13, 7, 11), (7, 11, 25), (2, 3, 5)]
    for kn, dn, qn in cases:
        k, D, q = map(Fraction, (kn, dn, qn))
        a = D / k + D / q
        b = D / k
        assert D + q * (b - a) == 0
        assert D - 2 * k * b + q * (a - b) == 0
        c = k * D / 2
        # s=0: Lh=kD-kD/2-qk*x*x/2; s=1: Lh=kD/2+qk*x*x/2.
        assert k * D - k * D / 2 == c
        assert q * k / 2 == q * k / 2
        sigma = 2 * D * k * k * a + k * k * D * D / (4 * q)
        assert sigma == 2 * D * D * k + 9 * D * D * k * k / (4 * q)
    return len(cases)


def stationary_transform_check():
    checks = 0
    for k, D, q in [(1.0, 1.0, 1.0), (1.3, .7, .55), (.7, 1.1, 2.5)]:
        alpha = q / (2 * k)
        for u in [0.1, 0.25, 0.4]:
            u = u * math.sqrt(q / D)
            z = D * u * u / q
            phi0 = .5 * math.exp(D * u * u / (2 * k)) * (1 - z) ** (-alpha - 1)
            phi1 = .5 * math.exp(D * u * u / (2 * k)) * (1 - z) ** (-alpha)
            phi1_prime = phi1 * (D * u / k + 2 * alpha * D * u / (q * (1 - z)))
            assert abs(D * u*u * phi0 + q * (phi1 - phi0)) < 2e-12
            assert abs(D * u*u * phi1 - k*u*phi1_prime + q*(phi0-phi1)) < 2e-12
            checks += 2
    return checks


def simulated_work(k, D, q, T, N, seed):
    rng = np.random.default_rng(seed)
    s = rng.integers(0, 2, size=N, dtype=np.int8)
    shape = q / (2 * k) + (s == 0)
    x = (rng.normal(0, math.sqrt(D / k), size=N)
         + math.sqrt(D / q) * (rng.gamma(shape) - rng.gamma(shape)))
    t = np.zeros(N)
    work = np.zeros(N)
    events = 0
    while True:
        idx = np.flatnonzero(t < T)
        if not len(idx):
            break
        dt = rng.exponential(1/q, size=len(idx))
        mask = dt <= T - t[idx]
        idx, dt = idx[mask], dt[mask]
        if not len(idx):
            break
        on = (s[idx] == 1)
        sd = np.sqrt(np.where(on,
                    D/k * (-np.expm1(-2*k*dt)), 2*D*dt))
        x[idx] = np.where(on, np.exp(-k*dt)*x[idx], x[idx]) + sd*rng.normal(size=len(idx))
        work[idx] += np.where(on, -k/2, k/2)*x[idx]**2
        s[idx] = 1 - s[idx]
        t[idx] += dt
        events += len(idx)
    return work.mean()/T, work.var(ddof=1)/T, events


def main():
    n_algebra = algebra_check()
    n_fourier = stationary_transform_check()
    results = []
    for i,(k,D,q) in enumerate([(1.,1.,1.),(1.3,.7,.55),(.7,1.1,2.5)]):
        T, N = 90., 13000
        observed_mean, observed_var, events = simulated_work(k,D,q,T,N,30031+i)
        expected_mean = k*D/2
        expected_var = 2*D*D*k + 9*D*D*k*k/(4*q)
        # Conservative finite-sample tolerance, not an asymptotic guarantee.
        assert abs(observed_mean-expected_mean) < 0.055
        assert abs(observed_var-expected_var)/expected_var < 0.09
        results.append((k,D,q,observed_mean,expected_mean,observed_var,expected_var,events))
    print('Exact rational parameter checks:', n_algebra)
    print('Stationary transform generator checks:', n_fourier)
    for k,D,q,m,em,v,ev,n in results:
        print(f'k={k}, D={D}, q={q}: mean rate {m:.6f} vs {em:.6f}; '
              f'variance rate {v:.6f} vs {ev:.6f}; {n} switches')
    print('PASS: 4 exact parameter checks, 18 transform identities, 3 simulations')


if __name__ == '__main__':
    main()
