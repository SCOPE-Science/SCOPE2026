"""Reproduce analytic and finite-path diagnostics for the log-Beta trapping-time theorem.

Run: python verify.py
Dependency: mpmath (declared in requirements.txt).
The probabilistic inequalities for all parameters are proved in RESULT.md;
simulated paths are diagnostics, not a substitute for that proof.
"""
import math
import random
import statistics
import mpmath as mp

mp.mp.dps = 45
checks = 0


def check(statement, why):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(why)


def trap_time(mu, q, C, rng):
    """Exact between-switch integration, in units with the occupation threshold C."""
    t = 0.0
    e_mu_t = 1.0
    accumulated = 0.0
    minus = bool(rng.getrandbits(1))
    for _ in range(100000):
        duration = rng.expovariate(q)
        next_e = e_mu_t * math.exp(mu * duration)
        if minus:
            increase = next_e - e_mu_t
            if accumulated + increase >= C:
                crossing_e = e_mu_t + C - accumulated
                return math.log(crossing_e) / mu
            accumulated += increase
        t += duration
        e_mu_t = next_e
        minus = not minus
    raise RuntimeError('Unexpectedly long simulated trajectory')


# Stationary equations for the normalized exponentially weighted occupation.
for alpha in [mp.mpf('0.5'), mp.mpf('1'), mp.mpf('1.5'), mp.mpf('2'), mp.mpf('3')]:
    p = lambda u: (u * (1 - u)) ** (alpha - 1) / mp.beta(alpha, alpha)
    for k in range(1, 50):
        u = mp.mpf(k) / 50
        residual = u * (1 - u) * mp.diff(p, u) - (alpha - 1) * (1 - 2 * u) * p(u)
        check(abs(residual) < mp.mpf('1e-34'), 'Beta invariant-density ODE')
    integral = mp.quad(p, [0, mp.mpf('0.5'), 1])
    check(abs(integral - 1) < mp.mpf('1e-18'), 'Beta law normalization')

# Exact independent mean formula from Eq. (63) of arXiv:2409.16951v1,
# specialized to mu=v=1, x_0=1+2C and flip rate q=alpha.
for alpha in [mp.mpf('0.5'), mp.mpf('1'), mp.mpf('1.5'), mp.mpf('2'), mp.mpf('3')]:
    m = mp.digamma(2 * alpha) - mp.digamma(alpha)
    variance = mp.polygamma(1, alpha) - mp.polygamma(1, 2 * alpha)
    check(m > 0 and variance > 0, 'Limiting mean/variance positivity')
    for C in [1, 3, 10]:
        C = mp.mpf(C)
        tmean = 1/(2*alpha) + (2*alpha+1)/(alpha+1) * C * mp.hyper(
            [1, 1, 2*(1+alpha)], [2, 2+alpha], -C)
        centered = tmean - mp.log(C)
        check(centered + mp.mpf('1e-26') >= m, 'Exact MFPT lower stochastic bound')
        check(centered <= m + mp.log(1+1/C) + mp.mpf('1e-26'),
              'Exact MFPT upper stochastic bound')
    check(abs(mp.digamma(2)-mp.digamma(1)-1) < mp.mpf('1e-30')
          if alpha == 1 else True, 'Exponential special case')

# Exact-clock simulations at large launch distance, testing nontrivial limits.
rng = random.Random(24100925)
for alpha in [0.5, 1.0, 2.0]:
    C = 1000.0
    samples = 7500
    values = []
    for _ in range(samples):
        z = trap_time(1.0, alpha, C, rng) - math.log(C)
        check(z >= math.log1p(1/C) - 1e-10, 'Deterministic fastest-capture bound')
        values.append(z)
    mean = float(mp.digamma(2*alpha) - mp.digamma(alpha))
    variance = float(mp.polygamma(1, alpha) - mp.polygamma(1, 2*alpha))
    check(abs(statistics.mean(values) - mean) < 0.15,
          'Exact-clock sample mean versus log-Beta limit')
    check(abs(statistics.variance(values) - variance) < 0.5,
          'Exact-clock sample variance versus log-Beta limit')
    for s in [0.3, 0.7, 1.5, 2.5]:
        actual = sum(x > s for x in values)/samples
        u = math.exp(-s)
        tail = float(mp.betainc(alpha, alpha, 0, u, regularized=True))
        # Finite-C true tail is squeezed between the two Beta CDFs;
        # the sampling tolerance accounts for Monte Carlo fluctuations.
        upper = float(mp.betainc(alpha, alpha, 0,
                                min(1, u * (1+1/C)), regularized=True))
        check(tail - 0.04 <= actual <= upper + 0.04,
              'Numerical tail versus analytic stochastic sandwich')
    print('rate', alpha, 'sample mean', round(statistics.mean(values), 5),
          'log-Beta mean', round(mean, 5),
          'sample variance', round(statistics.variance(values), 5),
          'log-Beta variance', round(variance, 5))

print('PASS:', checks, 'analytic and exact-clock diagnostic assertions')
