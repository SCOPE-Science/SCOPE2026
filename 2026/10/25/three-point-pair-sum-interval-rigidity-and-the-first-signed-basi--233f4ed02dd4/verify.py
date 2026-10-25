#!/usr/bin/env python3
"""Exact finite checks for a three-point, two-summand interval theorem.

No third-party dependencies. Finite tests supplement a universal gap proof.
"""
from itertools import combinations


def pair_sums(A):
    return {A[i] + A[j] for i in range(3) for j in range(i, 3)}


def longest_run(S):
    seq = sorted(S)
    run = best = 0
    for i in range(1, len(seq)):
        run = run + 1 if seq[i] == seq[i-1] + 1 else 0
        best = max(best, run)
    return best


def predicted(x, y):
    if (x, y) in {(1, 1), (1, 2), (2, 1)}:
        return 4
    if min(x, y) == 1 and max(x, y) >= 3:
        return 2
    if min(x, y) >= 2 and abs(x-y) == 1:
        return 1
    return 0


def origin_length(S):
    if 0 not in S:
        return None
    n = 0
    while n in S:
        n += 1
    return n - 1


def main():
    checked = 0
    for x in range(1, 101):
        for y in range(1, 101):
            expected = predicted(x, y)
            for a in (-50, -3, 0, 7, 50):
                A = (a, a+x, a+x+y)
                S = pair_sums(A)
                assert longest_run(S) == expected, (A, expected, S)
                assert origin_length(S) in {None, 0, 1, 2, 4}
                checked += 1
    spectra_signed = set()
    spectra_nonnegative = set()
    for A in combinations(range(-15, 16), 3):
        v = origin_length(pair_sums(A))
        if v is not None:
            spectra_signed.add(v)
            if A[0] >= 0:
                spectra_nonnegative.add(v)
    assert spectra_signed == {0, 1, 2, 4}, spectra_signed
    assert spectra_nonnegative == {0, 2, 4}, spectra_nonnegative
    for A, wanted in [((0, 2, 4), 0), ((-2, -1, 2), 1),
                      ((-1, 0, 1), 2), ((0, 1, 2), 4)]:
        assert origin_length(pair_sums(A)) == wanted
    print('VERIFY_OK', checked, 'translated gap triples; signed',
          sorted(spectra_signed), 'nonnegative', sorted(spectra_nonnegative))


if __name__ == '__main__':
    main()
