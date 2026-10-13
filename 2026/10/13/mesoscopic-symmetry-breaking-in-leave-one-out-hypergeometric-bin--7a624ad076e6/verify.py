#!/usr/bin/env python3
import math


def closed_form(N, K):
    p = K / N
    q = 1.0 - p
    H = -(p * math.log(p) + q * math.log(q))
    return -math.lgamma(N + 1) + math.lgamma(K + 1) + math.lgamma(N - K + 1) + (N - 1) * H


def direct_kl(N, K):
    p = K / N
    q = 1.0 - p
    b1 = math.comb(N - 1, K - 1) * p ** (K - 1) * q ** (N - K)
    b2 = math.comb(N - 1, K) * p ** K * q ** (N - K - 1)
    return p * math.log(p / b1) + q * math.log(q / b2)


for N in range(3, 101):
    for K in range(1, N):
        if abs(closed_form(N, K) - direct_kl(N, K)) > 2e-11:
            raise SystemExit("identity mismatch")

for N in (50, 100, 200, 500, 1000):
    vals = [closed_form(N, K) for K in range(1, N)]
    M = max(vals)
    ks = [K for K, v in enumerate(vals, 1) if abs(v - M) < 1e-11]
    y = abs(ks[0] - N / 2) / math.sqrt(N)
    approx = 0.5 * math.log(math.pi * N / 8) + 1 / (4 * N) + 1 / (6 * N * N)
    print(N, ks, "scaled_displacement=", format(y, ".12f"), "max_minus_asymptotic=", format(M - approx, ".3e"))

print("VERIFY_OK exact_identity_N=3..100 asymptotic_regression=50..1000")
