#!/usr/bin/env python3
"""Reproduce finite-N checks for the critical Curie-Weiss pair correlation.

Uses only the Python standard library. The analytic proof is in RESULT.md;
finite sums are corroborative, not a proof of the asymptotic expansion.
"""
import math


def pair_correlation(n: int) -> float:
    # At beta=1 and zero field, the magnetization m=(2k-n)/n has weight
    # binom(n,k) exp(n*m^2/2). Subtract the maximum log weight for stability.
    logs = []
    mags = []
    for k in range(n + 1):
        m = (2 * k - n) / n
        logw = (math.lgamma(n + 1) - math.lgamma(k + 1)
                - math.lgamma(n - k + 1) + 0.5 * n * m * m)
        logs.append(logw)
        mags.append(m)
    peak = max(logs)
    weights = [math.exp(v - peak) for v in logs]
    z = sum(weights)
    second_moment = sum(w * m * m for w, m in zip(weights, mags)) / z
    # Exchangeability gives E[M^2] = N + N(N-1)c_N.
    return (n * second_moment - 1.0) / (n - 1)


def main() -> None:
    a = math.sqrt(12.0) * math.gamma(0.75) / math.gamma(0.25)
    target = -(1.0 + a * a / 5.0)
    print(f"a={a:.12f}")
    print(f"target coefficient={target:.9f}")
    print("N,c_N,N*(c_N-a/sqrt(N))")
    for n in (100, 300, 1000, 3000, 10000):
        c = pair_correlation(n)
        scaled = n * (c - a / math.sqrt(n))
        print(f"{n},{c:.12f},{scaled:.9f}")


if __name__ == '__main__':
    main()
