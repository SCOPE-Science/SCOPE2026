#!/usr/bin/env python3
"""Exact checks for fixed-surplus probabilities of the Ulam--Kac adder.

All arithmetic is in Python integers. These finite tests corroborate the
proof; the general polynomiality and asymptotic laws are proved separately.
"""
from collections import defaultdict
from itertools import product
from math import comb, factorial


def path_census(n):
    """Independent exhaustive enumeration of all n! index histories."""
    uk = defaultdict(int)
    inv = defaultdict(int)
    for selections in product(*(range(t + 1) for t in range(n))):
        excess = [0]
        for u in selections:
            excess.append(excess[-1] + u + excess[u])
        uk[excess[-1]] += 1
        inv[sum(selections)] += 1
    assert sum(uk.values()) == factorial(n)
    assert sum(inv.values()) == factorial(n)
    return uk, inv


def prefix_coefficients(r, recursive):
    """Newton-binomial coefficients from the frozen first r indices."""
    states = {(0,): 1}
    for t in range(r):
        next_states = defaultdict(int)
        for e, multiplicity in states.items():
            for u in range(t + 1):
                nxt = e[-1] + (u if not recursive else u + e[u])
                if nxt <= r:
                    next_states[e + (nxt,)] += multiplicity
        states = next_states
    h = [0] * (r + 1)
    for e, multiplicity in states.items():
        remaining = r - e[-1]
        b = [0] * (remaining + 1)
        for j in range(1, r + 1):
            exponent = j + (e[j] if recursive else 0)
            if exponent <= remaining:
                b[exponent] += 1
        power = [1] + [0] * remaining
        for k in range(r + 1):
            h[k] += multiplicity * power[remaining]
            successor = [0] * (remaining + 1)
            for j in range(1, remaining + 1):
                if b[j]:
                    for d in range(remaining - j + 1):
                        successor[d + j] += b[j] * power[d]
            power = successor
    return h


def polynomial_value(h, r, n):
    return sum(c * comb(n - r, k) for k, c in enumerate(h) if k <= n - r)


def main():
    checks = 0
    coeffs = {}
    for r in range(0, 10):
        h = prefix_coefficients(r, True)
        g = prefix_coefficients(r, False)
        coeffs[r] = (h, g)
        assert h[r] == g[r] == 1
        checks += 1
        if r >= 1:
            assert h[r - 1] == g[r - 1] == 2 * (r - 1)
            checks += 1
        if r >= 3:
            assert g[r - 2] - h[r - 2] == r - 2
            checks += 1
        assert all(isinstance(v, int) and v >= 0 for v in h)
        checks += 1
    for n in range(0, 10):
        uk, inv = path_census(n)
        for r in range(n + 1):
            h, g = coeffs[r]
            assert polynomial_value(h, r, n) == uk[r], (n, r, h)
            assert polynomial_value(g, r, n) == inv[r], (n, r, g)
            checks += 2
        if n >= 2:
            assert uk[1] == n - 1
            checks += 1
        if n >= 3:
            assert inv[3] - uk[3] == n - 2
            checks += 1
    # The computed finite sequence has exactly the claimed Newton coefficients.
    assert coeffs[3][0] == [0, 4, 4, 1]
    assert coeffs[4][0] == [3, 10, 12, 6, 1]
    assert coeffs[5][0] == [15, 32, 37, 24, 8, 1]
    checks += 3
    print(f"PASS: {checks} exact coefficient, direct-history, and inversion-count checks")
    print("Direct histories exhausted for n=0,...,9 (9! paths at n=9).")
    print("General n,r statements require the separate analytic proof.")


if __name__ == "__main__":
    main()
