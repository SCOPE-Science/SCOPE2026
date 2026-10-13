#!/usr/bin/env python3
import math


def theta_c(k):
    return (k - 1) / (k + 1)


def lambda_c(k, theta):
    return ((k + 1) / k) ** k / (k - 1 - (k + 1) * theta)


def ratio(k, t):
    return math.sinh((k - 1) * t) / math.sinh((k + 1) * t)


def lam_of_t(k, theta, t):
    den = math.sinh((k - 1) * t) - theta * math.sinh((k + 1) * t)
    return (math.sinh((k + 1) * t) / math.sinh(k * t)) ** k * math.sinh(t) / den


def uv(k, theta, t):
    den = math.sinh((k - 1) * t) - theta * math.sinh((k + 1) * t)
    q = (math.sinh(t) / den) ** (1.0 / k)
    return math.exp(t) * q, math.exp(-t) * q


def residual(k, theta, t):
    u, v = uv(k, theta, t)
    lam = lam_of_t(k, theta, t)
    a = lam ** (1.0 / k)
    denom = 1.0 + u ** k + v ** k
    r1 = u - a * (1.0 + u ** k + theta * v ** k) / denom
    r2 = v - a * (1.0 + theta * u ** k + v ** k) / denom
    return max(abs(r1), abs(r2))


max_residual = 0.0
cases = 0
for k in (2, 3, 4, 5, 8, 15, 30):
    tc = theta_c(k)
    for frac in (0.0, 0.15, 0.5, 0.9):
        theta = frac * tc
        if theta == 0.0:
            ts = (0.05, 0.2, 0.7, 1.5)
        else:
            lo, hi = 0.0, 1.0
            while ratio(k, hi) > theta:
                hi *= 2.0
            for _ in range(100):
                mid = (lo + hi) / 2.0
                if ratio(k, mid) > theta:
                    lo = mid
                else:
                    hi = mid
            endpoint = (lo + hi) / 2.0
            ts = (0.05 * endpoint, 0.2 * endpoint, 0.5 * endpoint, 0.85 * endpoint)

        values = []
        for t in ts:
            err = residual(k, theta, t)
            max_residual = max(max_residual, err)
            assert err < 2.0e-10
            values.append(lam_of_t(k, theta, t))
            cases += 1
        assert all(values[j + 1] > values[j] for j in range(len(values) - 1))
        eps = 1.0e-7
        rel = abs(lam_of_t(k, theta, eps) / lambda_c(k, theta) - 1.0)
        assert rel < 2.0e-6

    for theta in (tc, min(0.999, tc + 0.05)):
        for t in (1.0e-4, 0.02, 0.2, 1.0):
            assert ratio(k, t) < tc + 1.0e-12
            assert not (ratio(k, t) > theta)

print(f"VERIFY_OK cases={cases} max_residual={max_residual:.3e}")
