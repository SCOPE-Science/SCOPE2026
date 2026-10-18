#!/usr/bin/env python3
"""Reproduce finite consistency tests for a carousel-tournament theorem.

The infinite result depends on the written proof, not these finite tests.
This script uses Python's standard library only.
"""
from itertools import combinations


def majority_stable(n, vertices):
    m = (n - 1) // 2
    allowed = m // 2
    for v in vertices:
        out_inside = sum(1 for w in vertices if 1 <= (w - v) % n <= m)
        if out_inside > allowed:
            return False
    return True


def proposed_set(n):
    k = (n - 1) // 4
    if n % 4 == 1:
        return set(range(0, n, 2))
    return set(range(1, n, 2))


def run():
    enumerated = 0
    tested = 0
    verified_2color = 0
    verified_3color = 0
    for n in range(3, 18, 2):
        m = (n - 1) // 2
        k = m // 2
        alpha = 2 * k + 1
        S = proposed_set(n)
        assert len(S) == alpha, (n, S, alpha)
        assert majority_stable(n, S), (n, S)
        cover = [0] * n
        for shift in range(n):
            for v in S:
                cover[(v + shift) % n] += 1
        assert cover == [alpha] * n
        for mask in range(1 << n):
            subset = {i for i in range(n) if mask & (1 << i)}
            if majority_stable(n, subset):
                assert len(subset) <= alpha, (n, subset)
            enumerated += 1
        if n % 4 == 1:
            assert majority_stable(n, set(range(n)) - S), n
            verified_2color += 1
        else:
            rest = sorted(set(range(n)) - S)
            assert len(rest) == 2 * (k + 1)
            assert majority_stable(n, rest[:k + 1]), n
            assert majority_stable(n, rest[k + 1:]), n
            verified_3color += 1
        tested += 1
    for n in range(19, 502, 2):
        alpha = 2 * ((n - 1) // 4) + 1
        S = proposed_set(n)
        assert len(S) == alpha, n
        assert majority_stable(n, S), n
        if n % 4 == 1:
            assert majority_stable(n, set(range(n)) - S), n
        else:
            rest = sorted(set(range(n)) - S)
            assert len(rest) == 2 * (((n - 1) // 4) + 1)
            h = len(rest) // 2
            assert majority_stable(n, rest[:h]), n
            assert majority_stable(n, rest[h:]), n
        tested += 1
    print(f"PASS: {enumerated} subsets enumerated for n=3,5,...,17")
    print(f"PASS: constructions checked for {tested} orders n=3,5,...,501")
    print(f"PASS: exact two-colour certificates in {verified_2color} small orders")
    print(f"PASS: exact three-colour certificates in {verified_3color} small orders")
    print("Note: finite checks do not prove the formula for all odd orders")


if __name__ == "__main__":
    run()
