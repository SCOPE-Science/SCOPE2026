import math

def logbinom(n, k):
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)

def log_taa_source(m, ell):
    k = 1 << m
    return 0.5 * sum(
        logbinom(k // (1 << (j - 1)), k // (1 << j))
        for j in range(m - ell + 1, m + 1)
    )

def log_taa_reindexed(ell):
    return 0.5 * sum(logbinom(1 << (r + 1), 1 << r) for r in range(ell))

def logadd(a, b):
    hi = max(a, b)
    return hi + math.log(math.exp(a - hi) + math.exp(b - hi))

def displayed_log_cost(m, ell, C=6.751):
    k = 1 << m
    s = 1 << ell
    return (
        logbinom(k, k // s)
        + logadd((k / s) * math.log(C), math.log(s))
        + log_taa_source(m, ell)
    )

# Exact level reindexing and geometric sum.
for m in range(4, 14):
    k = 1 << m
    for ell in range(1, m + 1):
        a = log_taa_source(m, ell)
        b = log_taa_reindexed(ell)
        assert abs(a - b) < 1e-9
        s = sum(k // (1 << j) for j in range(m - ell + 1, m + 1))
        assert s == (1 << ell) - 1

# The source-range sum differs from the top-level sum except at full depth.
k = 1 << 10
m = 10
ell = 3
bottom = sum(k // (1 << j) for j in range(m - ell + 1, m + 1))
top = sum(k // (1 << j) for j in range(1, ell + 1))
assert bottom == 7
assert top == 896
assert bottom != top

# Fixed-level logarithmic rate approaches H(2^-ell) + 2^-ell log C.
C = 6.751
for ell in (2, 3):
    p = 2.0 ** (-ell)
    target = -p * math.log(p) - (1.0 - p) * math.log(1.0 - p) + p * math.log(C)
    vals = [displayed_log_cost(m, ell, C) / (1 << m) for m in (12, 16, 20)]
    assert abs(vals[-1] - target) < abs(vals[0] - target)
    assert abs(vals[-1] - target) < 1e-5

# A growing level near sqrt(k log k) has a shrinking per-k exponent.
vals = []
for m in (12, 16, 20, 24):
    k = 1 << m
    ell = max(1, min(m, round(0.5 * (m + math.log2(m)))))
    vals.append(displayed_log_cost(m, ell, C) / k)
assert all(vals[i + 1] < vals[i] for i in range(len(vals) - 1))
assert vals[-1] < 0.002

print('VERIFY_OK')
