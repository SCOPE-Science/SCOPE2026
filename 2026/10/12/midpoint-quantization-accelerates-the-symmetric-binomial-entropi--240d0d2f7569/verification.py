import math

SQRT2 = math.sqrt(2.0)
LOG2 = math.log(2.0)


def logdiffexp(a, b):
    assert a > b
    return a + math.log1p(-math.exp(b - a))


def log_cdf(x):
    if x < 0.0:
        return math.log(0.5 * math.erfc(-x / SQRT2))
    return math.log1p(-0.5 * math.erfc(x / SQRT2))


def log_interval(lo, hi):
    if hi <= 0.0:
        return logdiffexp(log_cdf(hi), log_cdf(lo))
    if lo >= 0.0:
        a = math.log(0.5 * math.erfc(lo / SQRT2))
        b = math.log(0.5 * math.erfc(hi / SQRT2))
        return logdiffexp(a, b)
    return logdiffexp(log_cdf(hi), log_cdf(lo))


def divergence(n, c):
    root = math.sqrt(n)
    ans = 0.0
    for k in range(n + 1):
        lp = math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1) - n * LOG2
        p = math.exp(lp)
        z = (2 * k - n) / root
        lo = z + (2 * c - 1) / root
        hi = z + (2 * c + 1) / root
        ans += p * (lp - log_interval(lo, hi))
    return ans


def asymptotic(n, c):
    return 2 * c * c / n + (1 / 9 - 2 * c * c / 3) / (n * n)

# Evenness and the strict minimum at zero are theorem-level analytic facts;
# these finite checks are regression tests for the implementation.
for n in (20, 50, 100):
    for c in (0.25, 0.5, 1.0):
        assert abs(divergence(n, c) - divergence(n, -c)) < 2e-13
        assert divergence(n, 0.0) < divergence(n, c)

# The scaled remainders approach the predicted constants.
for c in (0.0, 0.25, 0.5, 1.0):
    errors = []
    for n in (50, 100, 200):
        d = divergence(n, c)
        errors.append(abs((d - asymptotic(n, c)) * n * n))
    assert errors[2] < errors[1] < errors[0]

mid = divergence(200, 0.0) * 200 * 200
boundary_first = divergence(200, 0.5) * 200
boundary_second = (divergence(200, 0.5) - 0.5 / 200) * 200 * 200
assert abs(mid - 1 / 9) < 8e-4
assert abs(boundary_first - 0.5) < 3e-4
assert abs(boundary_second + 1 / 18) < 1.1e-3

print('VERIFY_OK')
print('n=200 midpoint_n2D=%.15f target=%.15f' % (mid, 1/9))
print('n=200 boundary_nD=%.15f target=0.500000000000000' % boundary_first)
print('n=200 boundary_n2_remainder=%.15f target=%.15f' % (boundary_second, -1/18))
