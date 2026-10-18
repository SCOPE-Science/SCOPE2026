#!/usr/bin/env python3
"""Independent exact checks for odd-independent-set enumerators of C_n Cartesian K_2.

Usage: python verify_prism_odd_independence.py
Requires only Python's standard library; no external data or packages.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def closed_formula(n):
    assert n >= 3
    coefficients = {0: 1}
    for k in range(1, n // 2 + 1):
        excess = n - 2 * k
        if excess:
            total = sum(
                comb(k, r) * comb(excess - 1, r - 1) * 2**r
                for r in range(1, min(k, excess) + 1)
            )
            assert (n * total) % k == 0
            value = n * total // k
        else:
            value = 4 if k % 2 == 0 else 0
        if value:
            coefficients[k] = value
    if n % 2 == 0:
        coefficients[n] = 2
    return coefficients


def locally_valid(a, b, c):
    """Three consecutive rungs, states 0=empty, 1/2=chosen row.

    Tests odd independence at the middle rung, including independence
    of the chosen vertex and odd neighborhood counts for unchosen ones.
    """
    if b == 0:
        return not (a == c and a != 0)
    if a == b or c == b:
        return False
    other = 3 - b
    return (a == other) == (c == other)


def transfer_enumeration(n):
    # Trace of the 9-state de Bruijn transfer, with a weight z for
    # each selected middle rung. Counts every indexed cyclic word once.
    states = list(product((0, 1, 2), repeat=2))
    answer = Counter()
    for start in states:
        dp = {(start, 0): 1}
        for _ in range(n):
            nxt = defaultdict(int)
            for ((a, b), k), weight in dp.items():
                for c in (0, 1, 2):
                    if locally_valid(a, b, c):
                        nxt[((b, c), k + (b != 0))] += weight
            dp = nxt
        for (state, k), weight in dp.items():
            if state == start:
                answer[k] += weight
    return {k: v for k, v in answer.items() if v}


def explicit_enumeration(n):
    # Directly check every possible choice of 0/1 vertex per rung.
    # Such rung words exhaust all graph-independent candidates.
    answer = Counter()
    for word in product((0, 1, 2), repeat=n):
        chosen = {(i, word[i] - 1) for i in range(n) if word[i]}
        valid = True
        for i in range(n):
            for layer in (0, 1):
                neighbors = (
                    ((i - 1) % n, layer),
                    ((i + 1) % n, layer),
                    (i, 1 - layer),
                )
                count = sum(v in chosen for v in neighbors)
                if (i, layer) in chosen:
                    if count:
                        valid = False
                elif count == 2:
                    valid = False
                if not valid:
                    break
            if not valid:
                break
        if valid:
            answer[len(chosen)] += 1
    return dict(answer)


def main():
    brute = 0
    for n in range(3, 12):
        expected = closed_formula(n)
        observed = explicit_enumeration(n)
        assert expected == observed, (n, expected, observed)
        brute += 3**n
    for n in range(3, 101):
        expected = closed_formula(n)
        observed = transfer_enumeration(n)
        assert expected == observed, (n, expected, observed)
        if n % 2:
            assert max(expected) == n // 2
            assert expected[n // 2] == 2 * n
        else:
            assert max(expected) == n and expected[n] == 2
    print(f"PASS: {brute} exhaustive ternary rung words across n=3..11")
    print("PASS: two independently specified exact enumerators for n=3..100")
    print("PASS: all extremal and parity claims for n=3..100")


if __name__ == "__main__":
    main()
