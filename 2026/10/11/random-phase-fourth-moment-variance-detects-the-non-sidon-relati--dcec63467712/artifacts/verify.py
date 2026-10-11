#!/usr/bin/env python3
"""Exact finite replay for the random-phase fourth-moment variance identity."""
from collections import defaultdict
from itertools import combinations


def relation_counts(A):
    A = tuple(sorted(A))
    S = set(A)
    T = sum(
        1
        for x in A
        for d in range(1, (max(A) - min(A) + 1) if A else 1)
        if x + d in S and x + 2 * d in S
    )
    Q = sum(1 for a, b, c, d in combinations(A, 4) if a + d == b + c)
    return T, Q


def phase_character_variance(A):
    A = tuple(sorted(A))
    S = set(A)
    pos = {a: j for j, a in enumerate(A)}
    coeff = defaultdict(int)
    constant = 0
    diffs = sorted({b - a for a, b in combinations(A, 2)})
    for h in diffs:
        starts = [x for x in A if x + h in S]
        for x in starts:
            for y in starts:
                if x == y:
                    constant += 1
                    continue
                e = [0] * len(A)
                e[pos[x + h]] += 1
                e[pos[y]] += 1
                e[pos[x]] -= 1
                e[pos[y + h]] -= 1
                e = tuple(e)
                assert any(e)
                coeff[e] += 1
    var_E = sum(c * c for c in coeff.values())
    return constant, var_E


checked = 0
U = tuple(range(8))
for r in range(1, len(U) + 1):
    for A in combinations(U, r):
        constant, var_E = phase_character_variance(A)
        T, Q = relation_counts(A)
        assert constant == len(A) * (len(A) - 1) // 2
        assert var_E == 2 * T + 8 * Q
        checked += 1

for n in range(2, 21):
    A = tuple(range(n))
    _, var_E = phase_character_variance(A)
    var_X = 4 * var_E
    if n % 2 == 0:
        closed = 2 * n * (n - 2) * (4 * n - 7) // 3
    else:
        closed = 2 * (n - 1) * (4 * n * n - 11 * n + 3) // 3
    assert var_X == closed

print(f"VERIFY_OK subsets={checked} interval_n=2..20")
