"""Exact-rational checks for symbolic separation in a piecewise-affine contraction."""
from fractions import Fraction
from itertools import combinations


def run_case(alpha, lam1, lam2, length):
    delta = min(1 - lam1, 1 - lam2)
    assert Fraction(0) < alpha < Fraction(1, 2)
    assert Fraction(0) < lam1 < 1 and Fraction(0) < lam2 < 1
    assert delta > 0
    assert max(2 * alpha, lam1, lam2) < 1
    histories = []
    for code in range(1 << length):
        q = Fraction(7 * code + 1, 7 * (1 << length))
        x, y, z = (1 - q) / 2, q / 2, Fraction(1, 2)
        bits = []
        zs = [z]
        for j in range(length):
            if y < x:
                bits.append(0)
                x, y, z = alpha * (x - y), 2 * alpha * y, lam1 * z
            elif y > x:
                bits.append(1)
                x, y, z = 2 * alpha * x, alpha * (y - x), 1 - lam2 + lam2 * z
            else:
                raise AssertionError('discontinuity encountered')
            zs.append(z)
            assert x >= 0 and y >= 0 and x + y <= 1 and 0 <= z <= 1
        assert tuple(bits) == tuple((code >> j) & 1 for j in range(length - 1, -1, -1))
        histories.append((tuple(bits), zs))
    for (bits1, z1), (bits2, z2) in combinations(histories, 2):
        j = next(t for t, (b1, b2) in enumerate(zip(bits1, bits2)) if b1 != b2)
        assert z1[j] == z2[j]
        assert abs(z1[j + 1] - z2[j + 1]) >= delta


if __name__ == '__main__':
    cases = [
        (Fraction(2, 5), Fraction(1, 3), Fraction(2, 5)),
        (Fraction(12, 25), Fraction(4, 5), Fraction(3, 4)),
        (Fraction(49, 100), Fraction(1, 2), Fraction(1, 2)),
        (Fraction(2, 5), Fraction(99, 100), Fraction(1, 50)),
    ]
    for case in cases:
        for n in range(1, 9):
            run_case(*case, length=n)
    print('VERIFY_OK: exact admissible coding and strict first-difference separation (four regimes, lengths 1..8)')
