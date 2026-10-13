import math


def log_increment(n, alpha, mu):
    L = math.log(mu)
    a = L * (n ** alpha)
    delta_exp = L * (((n + 1) ** alpha) - (n ** alpha))
    return a + math.log(math.expm1(delta_exp))


def tail_ratio(n, alpha, mu):
    ld = log_increment(n, alpha, mu)
    if ld > math.log(745.0):
        return 0.0
    d = math.exp(ld)
    return math.exp(-d) if d < 745.0 else 0.0


def log_survival_ge(n, alpha, mu):
    z = math.log(mu) * (n ** alpha)
    if z > 709.0:
        return float('-inf')
    return 1.0 - math.exp(z)


def cdf(n, alpha, mu):
    ls = log_survival_ge(n + 1, alpha, mu)
    return 1.0 if ls == float('-inf') else 1.0 - math.exp(ls)


def upper_quantile(q, alpha, mu):
    a = (math.log(1.0 + math.log(1.0 / q)) / math.log(mu)) ** (1.0 / alpha)
    return max(0, math.ceil(a - 1e-14) - 1)


# Exact log-increment eventually increases, including a relatively slow-onset case.
params = [
    (0.55, 1.15),
    (0.7, 1.2),
    (1.0, 1.5),
    (1.4, 1.4),
]
for alpha, mu in params:
    ns = [50, 150, 400, 1000]
    logs = [log_increment(n, alpha, mu) for n in ns]
    assert logs[-1] > logs[0]
    r0 = tail_ratio(ns[0], alpha, mu)
    r1 = tail_ratio(ns[-1], alpha, mu)
    if r0 > 0.0:
        assert r1 < r0

# Exact quantile check at ordinary finite values.
for alpha, mu in [(0.7, 1.2), (1.3, 1.5), (2.0, 1.1)]:
    for q in (1e-2, 1e-4, 1e-7):
        n = upper_quantile(q, alpha, mu)
        assert cdf(n, alpha, mu) >= 1 - q - 1e-14
        if n > 0:
            assert cdf(n - 1, alpha, mu) < 1 - q + 1e-14

# Positive-exponential upper-bound summands eventually decrease strongly.
for alpha, mu, t, n0, n1 in [
    (0.55, 1.15, 0.7, 1000, 3000),
    (0.8, 1.2, 2.0, 200, 600),
    (1.0, 1.2, 3.0, 50, 150),
]:
    l0 = t * n0 + log_survival_ge(n0, alpha, mu)
    l1 = t * n1 + log_survival_ge(n1, alpha, mu)
    assert l1 < l0

# Maximum concentration checked deterministically on log scale, not by simulation.
for alpha, mu, eps in [(0.5, 1.2, 0.2), (1.0, 1.5, 0.15), (1.7, 1.1, 0.1)]:
    logm = 1e6
    a = (math.log(logm) / math.log(mu)) ** (1.0 / alpha)
    nlo = (1 - eps) * a
    nhi = (1 + eps) * a
    log_mS_lo = logm + 1.0 - math.exp(math.log(mu) * (nlo ** alpha))
    log_mS_hi = logm + 1.0 - math.exp(math.log(mu) * (nhi ** alpha))
    assert log_mS_lo > 100
    assert log_mS_hi < -100

print('VERIFY_OK')
