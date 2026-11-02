#!/usr/bin/env python3
"""Exact integer checks for the first four modular-energy fibers.

Requires NumPy for efficient exhaustive arithmetic over the periods at m=17,18.
No finite enumeration is used as a proof for unbounded m.
"""
from math import comb, lcm
import numpy as np


def primes_upto(n):
    return [p for p in range(2, n + 1)
            if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def fiber_counts_full(m, chunk=300000):
    period = 1
    for k in range(1, m + 1):
        period = lcm(period, k)
    counts = np.zeros(5, dtype=np.int64)
    for lo in range(0, period, chunk):
        entries = np.arange(lo, min(lo + chunk, period), dtype=np.int64)
        energy = np.zeros(len(entries), dtype=np.int16)
        for k in range(2, m + 1):
            energy += (entries % k).astype(np.int16)
        counts += np.bincount(energy[energy <= 4], minlength=5)
    return period, list(map(int, counts))


def predicted(m):
    primes = primes_upto(m)
    r = sum(2 * p > m for p in primes)
    s = sum(3 * p > m >= 2 * p for p in primes)
    return [comb(r + j - 1, j) for j in range(4)] + [comb(r + 3, 4) + s]


def crt_term(p, v, period):
    part = period // p
    return (v * part * pow(part, -1, p)) % period


def check_constructed(m):
    ps = primes_upto(m)
    hi = [p for p in ps if p * 2 > m]
    mid = [p for p in ps if p * 3 > m >= 2 * p]
    period = 1
    for k in range(1, m + 1):
        period = lcm(period, k)
    # Enumerate all compositions of total low energy <= 4 among the high primes.
    tested = 0
    def visit(i, left, point):
        nonlocal tested
        if i == len(hi):
            if left == 0:
                point %= period
                assert sum(point % k for k in range(2, m + 1)) == target
                tested += 1
            return
        p = hi[i]
        for digit in range(left + 1):
            visit(i + 1, left - digit, point + crt_term(p, digit, period))
    for target in range(5):
        visit(0, target, 0)
    for p in mid:
        point = crt_term(p, 2, period)
        assert sum(point % k for k in range(2, m + 1)) == 4
        tested += 1
    assert tested == sum(predicted(m))
    return tested


def main():
    for m in (16, 17, 18):
        period, actual = fiber_counts_full(m)
        target = predicted(m)
        print(f'm={m} period={period} actual={actual} formula={target}')
        if m == 18:
            assert actual == target
        elif m == 17:
            assert actual != target and actual[3] == target[3] + 1
    for m in (18, 19, 23, 37, 64, 100):
        tested = check_constructed(m)
        print(f'm={m} CRT classes checked={tested}')
    print('VERIFICATION_OK')

if __name__ == '__main__':
    main()
