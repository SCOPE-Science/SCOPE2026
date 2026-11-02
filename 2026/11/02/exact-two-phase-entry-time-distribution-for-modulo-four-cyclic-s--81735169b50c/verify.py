#!/usr/bin/env python3
"""Exact arithmetic checks for the modulo-four cyclic-sum entry-time law.

Run: python3 verify.py
Only Python standard library is needed. Checks do not replace the proof.
"""
from itertools import product


def image_log_2(A):
    """Number of bits in the image of a square matrix over Z/4Z.

    Elementary row and column operations over Z/4 diagonalize into
    unit, twice-unit, and zero pivots.  Unit entries are processed before 2s.
    """
    M = [[v % 4 for v in row] for row in A]
    n = len(M)
    r = 0
    total = 0
    for pivot_kind in (1, 2):
        while True:
            pivot = next(((i, j) for i in range(r, n) for j in range(r, n)
                          if (M[i][j] % 2 != 0 if pivot_kind == 1 else M[i][j] == 2)), None)
            if pivot is None:
                break
            i, j = pivot
            M[r], M[i] = M[i], M[r]
            for row in M:
                row[r], row[j] = row[j], row[r]
            if pivot_kind == 1:
                inverse = M[r][r]  # 1^{-1}=1 and 3^{-1}=3 (mod 4)
                M[r] = [(inverse * x) % 4 for x in M[r]]
            # Eliminate each remaining row in pivot column.
            for i in range(n):
                if i == r or M[i][r] == 0:
                    continue
                if pivot_kind == 1:
                    mul = M[i][r]
                else:
                    assert M[i][r] == 2
                    mul = 1
                M[i] = [(x - mul * y) % 4 for x, y in zip(M[i], M[r])]
            # Eliminate each remaining column in pivot row.
            for j in range(n):
                if j == r or M[r][j] == 0:
                    continue
                if pivot_kind == 1:
                    mul = M[r][j]
                else:
                    assert M[r][j] == 2
                    mul = 1
                for i in range(n):
                    M[i][j] = (M[i][j] - mul * M[i][r]) % 4
            assert all(M[i][r] == 0 for i in range(n) if i != r)
            assert all(M[r][j] == 0 for j in range(n) if j != r)
            total += 2 if pivot_kind == 1 else 1
            r += 1
    assert all(M[i][j] == 0 for i in range(r, n) for j in range(r, n))
    return total


def length_spectrum(n):
    q = n & -n
    assert q >= 2
    L = 3 * q // 2
    periodic_factor = 4 ** (n - q)
    result = [periodic_factor]
    for t in range(1, L + 1):
        if t <= q // 2:
            result.append(periodic_factor * 3 * 4 ** (t - 1))
        else:
            result.append(periodic_factor * 2 ** (q // 2 + t - 1))
    assert sum(result) == 4 ** n
    return result


def direct_image_matrix(n, t):
    # Columns are D^t applied to standard basis vectors.
    v = [1] + [0] * (n - 1)
    for _ in range(t):
        v = [(v[i] + v[(i - 1) % n]) % 4 for i in range(n)]
    return [[v[(i - j) % n] for j in range(n)] for i in range(n)]


def expected_image_log(n, t):
    q = n & -n
    if t <= q // 2:
        e = 2 * (q - t)
    elif t <= 3 * q // 2:
        e = 3 * q // 2 - t
    else:
        e = 0
    return 2 * (n - q) + e


def iterate(v):
    return tuple((v[i] + v[(i + 1) % len(v)]) % 4 for i in range(len(v)))


def exhaustive(n):
    L = 3 * (n & -n) // 2
    states = list(product(range(4), repeat=n))
    # D^L of every tuple belongs to the periodic component.
    cycle_states = set()
    for state in states:
        u = state
        for _ in range(L):
            u = iterate(u)
        cycle_states.add(u)
    assert len(cycle_states) == 4 ** (n - (n & -n)), (n, len(cycle_states))
    counts = [0] * (L + 1)
    for state in states:
        u = state
        for t in range(L + 1):
            if u in cycle_states:
                counts[t] += 1
                break
            u = iterate(u)
        else:
            raise AssertionError((n, state))
    assert counts == length_spectrum(n), (n, counts, length_spectrum(n))
    return len(states)


def main():
    matrix_checks = 0
    for n in (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 32):
        L = 3 * (n & -n) // 2
        for t in range(L + 3):
            actual = image_log_2(direct_image_matrix(n, t))
            expected = expected_image_log(n, t)
            assert actual == expected, (n, t, actual, expected)
            matrix_checks += 1
    total = sum(exhaustive(n) for n in (2, 4, 6, 8))
    print(f'VERIFY_OK exhaustive_tuples={total} matrix_checks={matrix_checks} even_lengths=12')


if __name__ == '__main__':
    main()
