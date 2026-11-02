"""Independent computational checks for the Gaussian-quadratic two-fidelity risk identity.

Uses only Python's standard library. Finite tests support, but do not replace,
the analytic moment and boundary arguments in RESULT.md.
"""
from fractions import Fraction
from math import isclose
from random import Random

checks = 0

# Exact chi-square inverse-moment algebra, without floating point.
for n in range(5, 41):
    for q in range(1, 36):
        left = (Fraction(1, n * n)
                - Fraction(2, n * (n - 2))
                + Fraction(q + 2, q * (n - 2) * (n - 4)))
        right = Fraction(2 * (n*n + n*q + 4*q),
                         n*n * q * (n-2) * (n-4))
        assert left == right
        checks += 1

# Exact comparison with the high-fidelity-only estimator.
for n in range(5, 41):
    for m in range(n + 1, n + 20):
        q = m - n
        factor = Fraction(2 * q * (n*n + n*q + 4*q),
                          m*m * n*n * (n-2) * (n-4))
        critical = Fraction(n*n + n*q + 4*q,
                            m * n * (n-2) * (n-4))
        assert factor == Fraction(2*q, n*m) * critical
        checks += 1

# Pointwise coupling and the exact square-center decomposition.
rng = Random(26019371)
for n, m in ((2, 7), (3, 8), (5, 11), (10, 19)):
    for _ in range(100):
        z = [rng.gauss(0.0, 1.0) for i in range(m)]
        e = [rng.gauss(0.0, 0.8) for i in range(n)]
        y = [v*v for v in z]
        theta, mu, beta = 7.25, -1.5, 1.35
        low = [theta + a-1 for a in y]
        high = [mu + beta*(a-1) + b for a,b in zip(y[:n],e)]
        lo_n, lo_m = sum(low[:n])/n, sum(low)/m
        hi_n = sum(high)/n
        s = sum((a-lo_n)**2 for a in low[:n])
        bh = sum((a-lo_n)*(b-hi_n) for a,b in zip(low[:n],high))/s
        estimate = hi_n - bh*(lo_n-lo_m)
        residual = sum(e)/n - (bh-beta)*(lo_n-lo_m)
        assert isclose(estimate, mu + beta*(lo_m-theta) + residual,
                       rel_tol=1e-11, abs_tol=1e-11)
        t = sum(y[:n]); w = [a/t for a in y[:n]]
        v = sum((a-1/n)**2 for a in w)
        assert isclose(s, t*t*v, rel_tol=1e-11, abs_tol=1e-11)
        checks += 2

# Separate pseudo-random sequences estimate the two sides of the
# exact finite-variance formula, without relying on a stored reference value.
for n, m in ((8, 17), (12, 26)):
    q = m - n
    sigma, beta, theta, mu = 0.8, 1.25, 7.25, -1.5
    trial_rng = Random(935 * n + m)
    k_rng = Random(793 * m + n)
    trials = 105_000
    sum_sq = 0.0
    sum_cond_ratio = 0.0
    sum_k = 0.0
    for _ in range(trials):
        yy = [trial_rng.gauss(0.0, 1.0)**2 for i in range(m)]
        eps = [trial_rng.gauss(0.0, sigma) for i in range(n)]
        lo_n = sum(yy[:n])/n - 1
        lo_m = sum(yy)/m - 1
        s = sum((a-1-lo_n)**2 for a in yy[:n])
        slope_error = sum((a-1-lo_n)*e for a,e in zip(yy[:n],eps))/s
        error = beta*lo_m + sum(eps)/n - slope_error*(lo_n-lo_m)
        sum_sq += error*error
        sum_cond_ratio += (lo_n-lo_m)**2/s
        gamma = [k_rng.gammavariate(0.5, 2.0) for j in range(n)]
        total = sum(gamma)
        v = sum((x/total-1/n)**2 for x in gamma)
        sum_k += 1/v
    empirical = sum_sq / trials
    k_est = sum_k / trials
    factor = 2*q*(n*n+n*q+4*q)/(m*m*n*n*(n-2)*(n-4))
    theory = sigma*sigma/n + 2*beta*beta/m + sigma*sigma*factor*k_est
    conditional = (sigma*sigma/n + 2*beta*beta/m
                   + sigma*sigma*sum_cond_ratio/trials)
    assert abs(empirical/theory-1) < (0.085 if n == 8 else 0.045), (n, empirical, theory)
    assert abs(conditional/theory-1) < (0.055 if n == 8 else 0.035)
    checks += 2

print('VERIFY_OK', checks)
