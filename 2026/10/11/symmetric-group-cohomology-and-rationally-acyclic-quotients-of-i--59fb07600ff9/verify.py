#!/usr/bin/env python3
"""Finite checks for the coordinate-permutation character of injective-word moment-angle complexes.

The cochain traces and the induced-character formula are evaluated by separate algorithms.
This verifies finite examples, not the all-n topological theorem.
"""
from itertools import combinations, permutations
from math import comb, factorial


def sign_images(seq):
    return -1 if sum(a > b for i, a in enumerate(seq) for b in seq[i + 1:]) % 2 else 1


def sign_action(g, subset):
    indices = tuple(sorted(subset))
    if not indices:
        return 1
    assert set(g[x] for x in indices) == set(indices)
    return sign_images(tuple(indices.index(g[x]) for x in indices))


def derangements(k):
    return sum((-1)**j * factorial(k)//factorial(j) for j in range(k + 1))


def falling(f, j):
    ans = 1
    for i in range(j):
        ans *= f - i
    return ans


def fixed_word_cochain_trace(g, A):
    """Alternating signed trace on all *cells* of multidegree A.

    Every cell has a directed injective word w of D-type coordinates,
    and T-type coordinates B equals A minus letters(w); its degree is |A|+len(w).
    A permutation stabilizing A fixes a cell iff it fixes each letter of w.
    Its orientation sign is the sign of its permutation on odd T coordinates B.
    """
    k = len(A)
    result = 0
    for r in range(k + 1):
        for w in permutations(A, r):
            if any(g[x] != x for x in w):
                continue
            B = set(A) - set(w)
            result += (-1)**(k + r) * sign_action(g, B)
    return result


def closed_derived_trace(g, A):
    """Independent derangement-character computation with determinant sign."""
    k = len(A)
    f = sum(g[x] == x for x in A)
    return sign_action(g, A) * (-1)**k * sum((-1)**j * falling(f, j) for j in range(k + 1))


def all_checks():
    observed = 0
    signed_cells = 0
    class_checks = 0
    quotient_checks = 0
    for n in range(2, 7):
        total_char = [0]*(n + 1)
        for g in permutations(range(n)):
            for k in range(2, n + 1):
                trace_1 = trace_2 = 0
                for A in combinations(range(n), k):
                    if {g[x] for x in A} != set(A):
                        continue
                    trace_1 += fixed_word_cochain_trace(g, A)
                    trace_2 += closed_derived_trace(g, A)
                    signed_cells += sum(factorial(sum(g[x] == x for x in A))//factorial(sum(g[x] == x for x in A) - r)
                                        for r in range(sum(g[x] == x for x in A) + 1))
                assert trace_1 == trace_2, (n, g, k, trace_1, trace_2)
                if g == tuple(range(n)):
                    assert trace_1 == comb(n, k)*derangements(k), (n, k, trace_1)
                total_char[k] += trace_1
                observed += 1
                class_checks += 1
        for k in range(2, n + 1):
            assert total_char[k] == 0, (n, k, total_char[k])
            quotient_checks += 1
    assert closed_derived_trace((1,0), (0,1)) == -1  # S_2 top 4-cell class reverses
    print('VERIFY_OK')
    print(f'comparison_cases={observed} oriented_fixed_cell_terms={signed_cells} quotient_vanishing_checks={quotient_checks}')
    print('n=2 degree-four transposition trace=-1')


if __name__ == '__main__':
    all_checks()
