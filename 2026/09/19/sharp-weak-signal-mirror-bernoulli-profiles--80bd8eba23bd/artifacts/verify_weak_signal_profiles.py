#!/usr/bin/env python3
"""Standalone numerical checks for the weak-signal formulas in RESULT.md.

Uses only the Python standard library. The checks are confirmatory; the proof in
RESULT.md is analytic.
"""

from __future__ import annotations

import itertools
import math
import random


def delta(a):
    prod = 1.0
    for x in a:
        prod *= 1.0 - x * x
    return math.sqrt(max(0.0, 1.0 - prod))


def tau_enum(a):
    m = len(a)
    total = 0.0
    for eps in itertools.product((-1.0, 1.0), repeat=m):
        plus = 1.0
        minus = 1.0
        for x, e in zip(a, eps):
            plus *= 1.0 + x * e
            minus *= 1.0 - x * e
        total += 0.5 * abs(plus - minus)
    return total / (2 ** m)


def kappa_enum(a):
    q = sum(x * x for x in a)
    if q == 0.0:
        return 0.0
    scale = math.sqrt(q)
    w = [x / scale for x in a]
    total = 0.0
    for eps in itertools.product((-1.0, 1.0), repeat=len(a)):
        total += abs(sum(x * e for x, e in zip(w, eps)))
    return total / (2 ** len(a))


def tau_equal(m, a):
    # Exact binomial aggregation of the 2^m computational-basis outcomes.
    total = 0.0
    for k in range(m + 1):
        p = (1.0 + a) ** k * (1.0 - a) ** (m - k)
        q = (1.0 - a) ** k * (1.0 + a) ** (m - k)
        total += math.comb(m, k) * 0.5 * abs(p - q)
    return total / (2 ** m)


def binom_pmf(n, p):
    if p == 0.0:
        return [1.0] + [0.0] * n
    if p == 1.0:
        return [0.0] * n + [1.0]
    out = []
    for k in range(n + 1):
        logv = (
            math.lgamma(n + 1)
            - math.lgamma(k + 1)
            - math.lgamma(n - k + 1)
            + k * math.log(p)
            + (n - k) * math.log1p(-p)
        )
        out.append(math.exp(logv))
    return out


def tv_binomial(n, p, q):
    P = binom_pmf(n, p)
    Q = binom_pmf(n, q)
    return 0.5 * sum(abs(x - y) for x, y in zip(P, Q))


def tv_doubled_identical(n, p, q):
    P = binom_pmf(n, p)
    Q = binom_pmf(n, q)
    return 0.5 * sum(
        abs(P[k] * Q[l] - Q[k] * P[l])
        for k in range(n + 1)
        for l in range(n + 1)
    )


def source_V(n, p, q):
    lam = p * (1.0 - q) + (1.0 - p) * q
    a = abs(p - q) / lam if lam else 0.0
    return n * lam * a * a


def main():
    print("two-equal-coordinate weak-signal efficiency")
    target = 1.0 / math.sqrt(2.0)
    for t in (0.20, 0.10, 0.05, 0.02):
        a = [t / math.sqrt(2.0), t / math.sqrt(2.0)]
        ratio = tau_enum(a) / delta(a)
        print(f"q={t*t:.6g} ratio={ratio:.12f} target={target:.12f}")

    print("\ndiffuse equal-coordinate efficiency")
    target_g = math.sqrt(2.0 / math.pi)
    q = 1e-4
    for m in (4, 16, 64, 256):
        x = math.sqrt(q / m)
        ratio = tau_equal(m, x) / math.sqrt(1.0 - (1.0 - x * x) ** m)
        print(f"m={m:3d} ratio={ratio:.12f} gaussian={target_g:.12f}")

    print("\nquantitative bound spot-check: |tau/Delta-kappa| <= 2q")
    rng = random.Random(260919)
    worst = 0.0
    for m in range(2, 8):
        for _ in range(100):
            q = 0.5 * rng.random()
            raw = [rng.random() for _ in range(m)]
            norm = math.sqrt(sum(x * x for x in raw))
            a = [math.sqrt(q) * x / norm for x in raw]
            err = abs(tau_enum(a) / delta(a) - kappa_enum(a))
            if err > 2.0 * q + 1e-12:
                raise AssertionError((m, q, err))
            if q > 0:
                worst = max(worst, err / q)
    print(f"largest observed error/q={worst:.12f}; theorem bound=2")

    print("\ndiffuse Bernoulli-product LAN corollary")
    r = 0.30
    for n in (100, 400, 1600):
        d = 1.0 / n
        p = r + d / 2.0
        qq = r - d / 2.0
        V = source_V(n, p, qq)
        tv = tv_binomial(n, p, qq)
        print(f"n={n:4d} TV/sqrt(V/pi)={tv / math.sqrt(V / math.pi):.12f}")

    print("\ndoubled-experiment corollary")
    for n in (50, 100, 200, 400):
        d = 1.0 / n
        p = r + d / 2.0
        qq = r - d / 2.0
        V = source_V(n, p, qq)
        tv = tv_binomial(n, p, qq)
        tv2 = tv_doubled_identical(n, p, qq)
        print(
            f"n={n:4d} doubled/sqrt(2V/pi)={tv2 / math.sqrt(2.0 * V / math.pi):.12f} "
            f"doubled/original={tv2 / tv:.12f}"
        )


if __name__ == "__main__":
    main()
