#!/usr/bin/env python3
"""Independent finite checks of chain-parameter type enumeration.

Run: python3 verify.py
Only Python's standard library is required. Exhaustive checks are finite tests,
not a proof of the universal-arity statement.
"""
from itertools import combinations, product
from math import comb


def labelled_posets(r):
    pairs = list(combinations(range(r), 2))
    for choices in product((0, 1, 2), repeat=len(pairs)):
        R = [[False] * r for _ in range(r)]
        for (i, j), c in zip(pairs, choices):
            if c == 1:
                R[i][j] = True
            elif c == 2:
                R[j][i] = True
        C = [row.copy() for row in R]
        for k in range(r):
            for i in range(r):
                if C[i][k]:
                    for j in range(r):
                        C[i][j] |= C[k][j]
        if not any(C[i][i] for i in range(r)) and C == R:
            yield R


def endpoint_order(R):
    r = len(R)
    N = 2 * r
    E = [[False] * N for _ in range(N)]
    for i in range(r):
        E[i][r + i] = True
        for j in range(r):
            if i == j:
                continue
            if R[i][j]:
                E[i][j] = True
                E[r + i][r + j] = True
            elif not R[j][i]:
                E[i][r + j] = True
    for k in range(N):
        for i in range(N):
            if E[i][k]:
                for j in range(N):
                    E[i][j] |= E[k][j]
    assert all(not E[i][i] for i in range(N))
    return E


def onto_order_map_coefficients(E):
    """c[k] = surjective isotone maps E -> {1,...,k}."""
    N = len(E)
    pred = [sum(1 << i for i in range(N) if E[i][j]) for j in range(N)]
    ideals = [s for s in range(1 << N)
              if all(not (s >> j & 1) or (pred[j] & s) == pred[j]
                     for j in range(N))]
    ways = {0: 1}
    coefficients = [0] * (N + 1)
    for k in range(1, N + 1):
        nxt = {}
        for upper in ideals:
            nxt[upper] = sum(v for lower, v in ways.items()
                             if lower != upper and lower & upper == lower)
        ways = nxt
        coefficients[k] = ways[(1 << N) - 1]
    return coefficients


def spectrum_coefficients(r):
    coeff = [0] * (2 * r + 1)
    number = 0
    for R in labelled_posets(r):
        number += 1
        c = onto_order_map_coefficients(endpoint_order(R))
        coeff = [a + b for a, b in zip(coeff, c)]
    return number, coeff


def spectrum_value(coeff, n):
    return sum(c * comb(n + 1, k) for k, c in enumerate(coeff)
               if k <= n + 1)


def direct_extension_counts(n, r):
    """No endpoint order polynomials: build and close each full relation matrix."""
    N = n + r
    newpairs = [(i, j) for i in range(N) for j in range(i + 1, N)
                if j >= n]
    base = [0] * N
    for i in range(n):
        for j in range(i + 1, n):
            base[i] |= 1 << j
    total = 0
    orientations = [0, 0, 0]  # incomparable, first below second, reverse
    for states in product((0, 1, 2), repeat=len(newpairs)):
        closure = base.copy()
        for (i, j), status in zip(newpairs, states):
            if status == 1:
                closure[i] |= 1 << j
            elif status == 2:
                closure[j] |= 1 << i
        for k in range(N):
            bit = 1 << k
            for i in range(N):
                if closure[i] & bit:
                    closure[i] |= closure[k]
        if any((closure[i] >> i) & 1 for i in range(N)):
            continue
        if any((((closure[i] >> j) & 1) != (status == 1) or
                ((closure[j] >> i) & 1) != (status == 2))
               for (i, j), status in zip(newpairs, states)):
            continue
        total += 1
        if r == 2:
            idx = newpairs.index((n, n + 1))
            orientations[states[idx]] += 1
    return total, orientations


def main():
    spectra = {}
    known_poset_counts = {1: 1, 2: 3, 3: 19, 4: 219}
    expected = {
        1: [0, 1, 1],
        2: [0, 3, 13, 18, 8],
        3: [0, 19, 181, 624, 996, 750, 216],
        4: [0, 219, 3793, 24246, 76964, 134820, 132912, 69216, 14832],
    }
    for r in range(1, 5):
        number, coeff = spectrum_coefficients(r)
        assert number == known_poset_counts[r]
        assert coeff == expected[r]
        spectra[r] = coeff
        assert all(c > 0 for c in coeff[1:])
        print('ARITY', r, 'LABELLED_POSETS', number,
              'BINOMIAL_COEFFICIENTS', coeff)
        print('ARITY', r, 'COUNTS_n0..6',
              [spectrum_value(coeff, n) for n in range(7)])

    def closed_formula(r, n):
        if r == 1:
            return (n + 1) * (n + 2) // 2
        if r == 2:
            return (n + 1) * (n + 2) * (2 * n*n + 8*n + 9) // 6
        if r == 3:
            return ((n + 1) * (n + 2) * (n*n + 4*n + 5)
                    * (6*n*n + 29*n + 38) // 20)
        raise ValueError(r)

    closed_checks = 0
    for r in range(1, 4):
        for n in range(11):
            assert spectrum_value(spectra[r], n) == closed_formula(r, n)
            closed_checks += 1
    print('CLOSED_FORMULA_COMPARISONS', closed_checks)

    brute_cases = [(1, n) for n in range(5)]
    brute_cases += [(2, n) for n in range(6)]
    brute_cases += [(3, n) for n in range(4)]
    for r, n in brute_cases:
        direct, orientations = direct_extension_counts(n, r)
        assert direct == spectrum_value(spectra[r], n), (r, n, direct)
        if r == 2:
            comparable = (n + 1) * (n + 2)**2 * (n + 3) // 12
            incomparable = (n + 1) * (n + 2) * (n*n + 3*n + 3) // 6
            assert orientations == [incomparable, comparable, comparable], (n, orientations)
        print('BRUTE_EXTENSION_CHECK', 'r', r, 'n', n, 'count', direct,
              'orientations' if r == 2 else '', orientations if r == 2 else '')
    print('BRUTE_EXTENSION_COMPARISONS', len(brute_cases))
    print('TWO_TYPE_ORIENTATION_COMPARISONS', 3 * 6)
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
