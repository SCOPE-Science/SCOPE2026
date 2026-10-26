#!/usr/bin/env python3
"""Exact finite checks for a binary alternating-center Ulam ball theorem.

The infinite parameter result is proved in RESULT.md, not by this check.
"""
from itertools import product
from math import comb


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        nxt = [0]
        for j, y in enumerate(b):
            nxt.append(prev[j] + 1 if x == y else max(nxt[-1], prev[j+1]))
        prev = nxt
    return prev[-1]


def recognized(v):
    e = sum(a == b for a,b in zip(v, v[1:]))
    return (e <= 3 or (e == 4 and v[0] == 0))


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def formula(m):
    return (m**4 - 2*m**3 + 5*m**2 + 4)//4


def run_count(m):
    z = m-1
    return 2 + 2*z + 2*z*z + z*z*(m-2) + binom(z, 2)**2


def main():
    for m in range(1, 7):
        n = 2*m
        w = tuple(i % 2 for i in range(n))
        balanced = 0
        for v in product((0, 1), repeat=n):
            predicted = recognized(v)
            observed = lcs(v, w) >= n-2
            assert predicted == observed, (m,v,predicted,observed)
            balanced += int(predicted and sum(v) == m)
        assert balanced == formula(m) == run_count(m), (m,balanced)
        print(f"m={m} all_binary={1<<n} balanced_radius_two={balanced}")
    for m in range(1, 500):
        assert formula(m) == run_count(m)
    print("VERIFY_OK: exhaustive LCS/membership n=2..12, balanced counts and 499 algebraic samples")

if __name__ == '__main__':
    main()
