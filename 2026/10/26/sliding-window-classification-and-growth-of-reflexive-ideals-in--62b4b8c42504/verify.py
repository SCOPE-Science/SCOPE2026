#!/usr/bin/env python3
"""Independent finite tests for normalized reflexive ideals of terminal-gap semigroups.

Uses direct ideal inclusion and direct double quotient, not the window formula
for constructing reflexive candidates. Requires only Python 3 standard library.
"""
from itertools import product


def semigroup(m, r):
    c = 2 * m
    return lambda x: x == 0 or (m <= x < c - r) or x >= c


def direct_reflexive_ideal_gap_sets(m, r):
    c = 2 * m
    S = semigroup(m, r)
    inside = [x for x in range(c) if S(x)]
    pos = [x for x in inside if x]
    gaps = [x for x in range(c) if not S(x)]
    solutions = set()
    candidates = 0
    for mask in range(1 << len(gaps)):
        added = frozenset(g for i, g in enumerate(gaps) if mask & (1 << i))
        I = lambda x: S(x) or x in added
        if any(not I(g + s) for g in added for s in pos):
            continue
        candidates += 1
        # For t>=c all t+I is in S. For t<c, test the definition S-I.
        T = [t for t in inside if all(S(t + x) for x in added)]
        # For each gap x, every t>=c is harmless, so test only T below c.
        double_added = frozenset(g for g in gaps if all(S(g + t) for t in T))
        if double_added == added:
            solutions.add(added)
    return solutions, candidates


def window_reflexive_gap_sets(m, r):
    L = m - r
    B = frozenset(range(2 * m - r, 2 * m))
    predicted = {frozenset()}
    for bits in product((0, 1), repeat=L):
        j = 0
        good = True
        while j < L:
            if bits[j] == 0:
                j += 1
                continue
            start = j
            while j < L and bits[j] == 1:
                j += 1
            if start > 0 and j < L and j - start < r:
                good = False
                break
        if not good:
            continue
        Z = {i for i, bit in enumerate(bits) if bit}
        U = frozenset(x for x in range(1, m)
            if all(i in Z for i in range(L) if 2*m-r <= m+i+x < 2*m))
        predicted.add(U | B)
    return predicted


def word_count(L, r):
    count = 0
    for bits in product((0, 1), repeat=L):
        runs = []
        i = 0
        while i < L:
            if not bits[i]:
                i += 1
                continue
            a = i
            while i < L and bits[i]:
                i += 1
            runs.append((a, i))
        if all(a == 0 or b == L or b - a >= r for a, b in runs):
            count += 1
    return count


def gf_coefficients(r, length):
    # D(z)=(1-z)^2-z^(r+1), and G(z)=1/(1-z)+z/((1-z)D(z)).
    # Invert D formally, then 1/(1-z) by taking partial sums.
    inv = [0] * (length + 1)
    inv[0] = 1
    for n in range(1, length + 1):
        inv[n] = 2 * inv[n-1] - (inv[n-2] if n >= 2 else 0)
        if n >= r+1:
            inv[n] += inv[n-(r+1)]
    ans = [1] * (length+1)
    for n in range(1, length+1):
        ans[n] += sum(inv[:n])
    return ans


def main():
    cases = 0
    total_ideals_checked = 0
    for r in range(3, 7):
        max_L = 6 if r <= 5 else 4
        coeff = gf_coefficients(r, max_L)
        for L in range(1, max_L+1):
            m = L+r
            direct, num_ideals = direct_reflexive_ideal_gap_sets(m, r)
            predicted = window_reflexive_gap_sets(m, r)
            assert direct == predicted, (m, r, sorted(map(tuple, direct ^ predicted)))
            assert len(direct) == 1 + word_count(L, r) == 1 + coeff[L]
            cases += 1
            total_ideals_checked += num_ideals
    print(f"VERIFY_OK cases={cases} normalized_ideals={total_ideals_checked} direct_double_quotients=checked word_bijection=checked rational_series=checked")

if __name__ == '__main__':
    main()
