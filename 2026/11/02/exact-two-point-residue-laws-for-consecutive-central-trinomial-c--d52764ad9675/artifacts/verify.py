#!/usr/bin/env python3
"""Finite checks for consecutive central-trinomial residues and their carry law."""
from collections import Counter
from math import comb, sqrt


def e(n):
    return (n & (n >> 1)).bit_count()


def digit_residue(n):
    return (1 + 2 * ((n >> 1).bit_count() % 2) + 4 * (e(n) % 2)) % 8


def parity_state(n):
    return (n >> 1).bit_count() % 2, e(n) % 2


def verify():
    for n in range(180):
        coefficient = sum(comb(n, 2 * k) * comb(2 * k, k)
                          for k in range(n // 2 + 1))
        assert coefficient % 8 == digit_residue(n), n
    t0, t1 = 1, 1
    for n in range(1, 2048):
        numerator = (2 * n + 1) * t1 + 3 * n * t0
        assert numerator % (n + 1) == 0
        t2 = numerator // (n + 1)
        assert t2 % 8 == digit_residue(n + 1)
        t0, t1 = t1, t2
    for n in range(10000):
        t = ((n + 1) & -(n + 1)).bit_length() - 1
        h = (n >> (t + 1)) % 2
        a0, b0 = parity_state(n)
        a1, b1 = parity_state(n + 1)
        got = ((a1 - a0) % 2, (b1 - b0) % 2)
        want = (0, h) if t == 0 else (t % 2, (h + t - 1) % 2)
        assert got == want, (n, got, want)
    for r in range(7, 17):
        N = 1 << r
        cnt = Counter((digit_residue(n), digit_residue(n + 1))
                      for n in range(N))
        assert len(cnt) == 16
        for j in (1, 3, 5, 7):
            for k in (1, 3, 5, 7):
                aa = ((j - 1) // 2) % 2
                bb = ((k - 1) // 2) % 2
                main = N / (12 if aa == bb else 24)
                # A deliberately loose inequality; not a proof of the theorem.
                assert abs(cnt[j, k] - main) <= 2 * sqrt(N)
        B = sum((-1) ** e(n) for n in range(N))
        assert B == 1 << ((r + 1) // 2)
    print("VERIFY_OK: 180 binomial, 2048 recurrence, 10000 carries, 10 dyadic pair tables")


if __name__ == '__main__':
    verify()
