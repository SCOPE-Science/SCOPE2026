"""Exact checks for finite-depth scale-homogeneous Haar projection norms.

No third-party dependencies.  Run: python checker.py
"""
from fractions import Fraction
from itertools import product


def target(d):
    return Fraction(d, 3) + Fraction(7, 9) + Fraction((-1) ** d, 9 * 2 ** (d - 1))


def shell_norm(d, bits):
    """Column norm from the dyadic common-prefix shells, computed exactly."""
    count = 0
    total = Fraction(0)
    for ell in range(d):
        bit = (bits >> ell) & 1
        total += Fraction(abs(count - bit * (2 ** ell)), 2 ** (ell + 1))
        count += bit * 2 ** ell
    return total + Fraction(count, 2 ** d)


def matrix_column_norms(d, bits):
    """Independently construct the finite operator on all dyadic atoms."""
    size = 2 ** d
    cols = []
    for j in range(size):
        col = 0
        for i in range(size):
            scaled = 0
            for m in range(1, d + 1):
                if (bits >> (m - 1)) & 1:
                    if i >> (d - m) == j >> (d - m):
                        scaled += 2 ** m
                    if i >> (d - m + 1) == j >> (d - m + 1):
                        scaled -= 2 ** (m - 1)
            col += abs(scaled)
        cols.append(Fraction(col, size))
    return cols


def bellman_coefficients(d):
    """Derive V_d(t)=a_d+b_d*abs(t-1/2) by exact recursion."""
    a, b = Fraction(1), Fraction(0)
    if d == 1:
        return a, b
    for k in range(2, d + 1):
        a, b = a + (1 + b) / 4, (1 - b) / 2
    return a, b


def expected_maximizers(d):
    if d == 1:
        return {1}
    if d == 2:
        return {3}
    patterns = set()
    for second in (0, 1):
        b = [1, second]
        t = Fraction(1 + 2 * second, 4)
        while len(b) < d - 1:
            next_b = int(t < Fraction(1, 2))
            assert t != Fraction(1, 2)
            b.append(next_b)
            t = (t + next_b) / 2
        b.append(1)
        patterns.add(sum(val << i for i, val in enumerate(b)))
    return patterns


def main():
    matrix_tests = 0
    for d in range(1, 7):
        for bits in range(1 << d):
            columns = matrix_column_norms(d, bits)
            assert len(set(columns)) == 1
            assert columns[0] == shell_norm(d, bits), (d, bits, columns[0], shell_norm(d, bits))
            matrix_tests += 1
    brute_cases = 0
    for d in range(1, 16):
        vals = [(bits, shell_norm(d, bits)) for bits in range(1 << d)]
        maximum = max(v for _, v in vals)
        maximizers = {bits for bits, v in vals if v == maximum}
        a, b = bellman_coefficients(d)
        assert a + b / 2 == maximum == target(d), d
        assert maximizers == expected_maximizers(d), (d, maximizers, expected_maximizers(d))
        brute_cases += len(vals)
        print('d=%2d  sharp=%s  maximizing selections=%s' % (d, maximum, sorted(maximizers)))
    print('PASS: %d finite matrix/column tests and %d selectors checked exactly.' % (matrix_tests, brute_cases))


if __name__ == '__main__':
    main()
