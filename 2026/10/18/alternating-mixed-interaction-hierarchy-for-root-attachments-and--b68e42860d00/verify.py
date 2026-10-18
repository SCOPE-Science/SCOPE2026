"""Exact-rational finite checks of all centered root-attachment/path-length mixed moments.

Run: python verify.py (Python standard library only). Finite checks supplement a proof.
"""
from fractions import Fraction
from functools import reduce
from itertools import product, combinations
from math import factorial


def harmonic(m):
    return sum((Fraction(1, k) for k in range(1, m + 1)), Fraction())


def prediction(n, times):
    assert 3 <= n and times and list(times) == sorted(times)
    assert len(set(times)) == len(times) and 3 <= times[0] <= times[-1] <= n
    denominator = 1
    for t in times:
        denominator *= t * (t - 1)
    return Fraction((-1) ** len(times) * n, denominator) * (harmonic(times[0] - 1) - 1)


def all_parent_sequences(n):
    yield from product(*(range(1, j) for j in range(2, n + 1)))


def check_full(n):
    vals = []
    for parents in all_parent_sequences(n):
        depth = [0] * (n + 1)
        path_length = 0
        for j, parent in enumerate(parents, 2):
            depth[j] = depth[parent] + 1
            path_length += depth[j]
        vals.append((parents, path_length))
    assert len(vals) == factorial(n - 1)
    for k in range(1, n - 1):
        for times in combinations(range(3, n + 1), k):
            total = Fraction()
            for parents, path_length in vals:
                centered = Fraction(1)
                for t in times:
                    centered *= int(parents[t - 2] == 1) - Fraction(1, t - 1)
                total += centered * path_length
            measured = total / len(vals)
            exact = prediction(n, times)
            assert measured == exact, (n, times, measured, exact)


def main():
    for n in range(3, 9):
        check_full(n)
    for n in range(3, 101):
        magnitudes = [-prediction(n, (t,)) for t in range(3, n + 1)]
        assert all(a > b > 0 for a, b in zip(magnitudes, magnitudes[1:]))
    print('PASS: all nonempty marked subsets and all parent sequences, n = 3,...,8.')
    print('PASS: exact first-order strict age ordering, n = 3,...,100.')
    print('Finite tests are supplementary; the universal proof is analytic.')


if __name__ == '__main__':
    main()
