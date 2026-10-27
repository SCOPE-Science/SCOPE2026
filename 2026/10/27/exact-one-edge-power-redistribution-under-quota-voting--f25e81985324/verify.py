#!/usr/bin/env python3
"""Exact arithmetic verification for the one-edge quota-voting theorem."""
from itertools import product
from math import comb
from fractions import Fraction

PLUS = "+"
MINUS = "-"
EDGE_TO_B = ("delegate", 1)

def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def resolved_votes(actions, n):
    out = []
    for start in range(n):
        u = start
        seen = set()
        while isinstance(actions[u], tuple):
            if u in seen:
                raise AssertionError("unexpected delegation cycle in one-edge DAG")
            seen.add(u)
            u = actions[u][1]
        out.append(actions[u])
    return out

def outcome(actions, n, r):
    return sum(v == PLUS for v in resolved_votes(actions, n)) >= r

def enumerated_powers(n, r):
    # The only potential delegation is 0 -> 1. Every available action is equiprobable.
    powers = []
    for target in range(n):
        others = [j for j in range(n) if j != target]
        opts = [([PLUS, MINUS, EDGE_TO_B] if j == 0 else [PLUS, MINUS]) for j in others]
        denominator = 1
        for op in opts:
            denominator *= len(op)
        critical = 0
        for choices in product(*opts):
            actions = {j: act for j, act in zip(others, choices)}
            actions[target] = PLUS
            yes = outcome(actions, n, r)
            actions[target] = MINUS
            no = outcome(actions, n, r)
            if yes != no:
                critical += 1
        powers.append(Fraction(critical, denominator))
    return powers

def formula_powers(n, r):
    m = (n - 1) // 2
    s = r - (m + 1)
    B = Fraction(C(n - 1, r - 1), 2 ** (n - 1))
    R = Fraction(2 * (C(n - 3, r - 1) + C(n - 3, r - 3)), C(n - 1, r - 1))
    expected = [B, Fraction(4, 3) * B] + [B * (Fraction(2, 3) + R / 3)] * (n - 2)
    total = n * B + Fraction(2 * s * s, 3 * m) * B
    return expected, total, B, R

def main():
    checked = 0
    for n in (3, 5, 7, 9, 11):
        m = (n - 1) // 2
        for r in range(m + 1, n + 1):
            got = enumerated_powers(n, r)
            want, total, B, R = formula_powers(n, r)
            assert got == want, (n, r, got, want)
            assert sum(got, Fraction(0)) == total, (n, r, sum(got, Fraction(0)), total)
            s = r - (m + 1)
            assert R == Fraction(n - 3, n - 2) + Fraction(2 * s * s, m * (n - 2))
            if s == 0:
                assert total == n * B
            else:
                assert total > n * B
            checked += 1
    print(f"VERIFY_OK: {checked} exact quota/electorate cases; n=3,5,7,9,11; all thresholds r>n/2; exact enumeration matches closed forms and total-power law")

if __name__ == '__main__':
    main()
