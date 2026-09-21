#!/usr/bin/env python3
"""Exact checks accompanying the near F-perfect nonexistence theorem."""

from math import isqrt


def divisors(n: int):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def redundant_divisors(n: int):
    ds = divisors(n)
    sigma2 = sum(d * d for d in ds)
    target = sigma2 - n * n - 3 * n
    if target <= 0:
        return []
    r = isqrt(target)
    if r * r != target or r >= n or n % r != 0:
        return []
    return [r]


def finite_core():
    rows = []
    for n in range(4, 49, 4):
        ds = divisors(n)
        delta = sum(d * d for d in ds) - n * n - 3 * n
        rows.append((n, delta, redundant_divisors(n)))
    return rows


def sieve_scan(limit: int):
    sigma2 = [0] * (limit + 1)
    for d in range(1, limit + 1):
        d2 = d * d
        for m in range(d, limit + 1, d):
            sigma2[m] += d2
    hits = []
    for n in range(1, limit + 1):
        target = sigma2[n] - n * n - 3 * n
        if target > 0:
            r = isqrt(target)
            if r * r == target and r < n and n % r == 0:
                hits.append((n, r))
    return hits


def main():
    print("Finite core (4 | n and n <= 48):")
    for n, delta, hits in finite_core():
        print(f"n={n:2d}  sigma2(n)-n^2-3n={delta:4d}  redundant_divisors={hits}")
    limit = 1_000_000
    hits = sieve_scan(limit)
    print(f"\nDirect exact scan 1 <= n <= {limit}: {len(hits)} hits")
    if hits:
        print(hits)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
