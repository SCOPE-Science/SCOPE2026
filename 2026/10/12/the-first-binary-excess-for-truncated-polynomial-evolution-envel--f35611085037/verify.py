#!/usr/bin/env python3
"""Exact finite-field certificate for evolution-envelope dimensions of F_2[t]/(t^n), n <= 4."""
from itertools import combinations, product
from math import comb


def upper_indices(n):
    return [(i, j) for i in range(n) for j in range(i, n)]


def gram_mask(linear_mask, n):
    """Upper triangle of the symmetric rank-one tensor ell tensor ell."""
    return sum((((linear_mask >> i) & 1) & ((linear_mask >> j) & 1)) << p
               for p, (i, j) in enumerate(upper_indices(n)))


def multiplication_slices(n):
    """Upper-triangular tables of the coefficients of t^k in a*b mod t^n."""
    return [sum((int(i + j == k) << p) for p, (i, j) in enumerate(upper_indices(n)))
            for k in range(n)]


def echelon(vectors):
    """Exact echelon basis over F_2, using highest-set-pivot elimination."""
    pivots = {}
    for x in vectors:
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return pivots


def in_span(pivots, x):
    while x:
        p = x.bit_length() - 1
        if p not in pivots:
            return False
        x ^= pivots[p]
    return True


def admissible(linears, n):
    basis = echelon([gram_mask(a, n) for a in linears])
    return all(in_span(basis, target) for target in multiplication_slices(n))


def minimum_rank_and_count(n):
    all_linears = tuple(range(1, 1 << n))
    for length in range(1, 1 << n):
        winners = 0
        first = None
        for selection in combinations(all_linears, length):
            if admissible(selection, n):
                winners += 1
                if first is None:
                    first = selection
        if winners:
            return length, winners, first
    raise AssertionError("Unexpected inability to decompose multiplication")


def product_mod_tn(a, b, n):
    answer = 0
    for i in range(n):
        for j in range(n - i):
            answer ^= ((a >> i) & 1) * ((b >> j) & 1) << (i + j)
    return answer


def evaluate_eight_term_algorithm(a, b):
    terms = [(1, 15), (2, 14), (3, 2), (4, 12),
             (5, 4), (6, 8), (8, 8), (9, 8)]
    result = 0
    for ell, output in terms:
        x = (ell & a).bit_count() & 1
        y = (ell & b).bit_count() & 1
        if x & y:
            result ^= output
    return result


def verify():
    for n, expected, expected_count in [(1, 1, 1), (2, 3, 1), (3, 5, 2), (4, 8, 28)]:
        length, count, witness = minimum_rank_and_count(n)
        assert (length, count) == (expected, expected_count), (n, length, count)
        print(f"n={n} min={length} optimal_supports={count} first_support={witness}")
    assert comb(15, 7) == 6435
    assert not any(admissible(subset, 4)
                   for subset in combinations(range(1, 16), 7))
    print("LOWER_BOUND_6435_SEVEN_SUPPORTS_OK")
    linears = [1, 2, 3, 4, 5, 6, 8, 9]
    outputs = [15, 14, 2, 12, 4, 8, 8, 8]
    assert admissible(linears, 4)
    for i in range(4):
        for j in range(4):
            a, b = 1 << i, 1 << j
            assert evaluate_eight_term_algorithm(a, b) == product_mod_tn(a, b, 4)
    for a, b in product(range(16), repeat=2):
        assert evaluate_eight_term_algorithm(a, b) == product_mod_tn(a, b, 4)
    print("EXPLICIT_EIGHT_TERM_DECOMPOSITION_256_PRODUCTS_OK")
    print("VERIFY_OK")


if __name__ == "__main__":
    verify()
