"""Exact-rational checks for symbolic cylinders of a two-branch interval map.

The script is supporting finite verification, not a proof of statements for all words.
No external dependencies are required.
"""
from fractions import Fraction
from itertools import product
from math import log

Q = ((1, 1), (1, 3))
M = (((1, 1), (0, 4)), ((1, 1), (4, 0)))


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def mat_word(w):
    P = ((1, 0), (0, 1))
    for d in w:
        P = mul(P, M[d])
    return mul(P, Q)


def odds(w):
    K = mat_word(w)
    a, b = K[0]
    c, d = K[1]
    assert min(a, b, c, d) > 0
    return Fraction(a * d, b * c)


def ordered_endpoints(w):
    K = mat_word(w)
    a, b = K[0]
    c, d = K[1]
    return tuple(sorted((Fraction(a, c), Fraction(b, d))))


def mass(w):
    return abs(log(float(odds(w)))) / log(3.0)


def verify():
    # Independent symbolic interval construction and reversal invariant cross ratios.
    checked = 0
    for n in range(1, 12):
        words = list(product((0, 1), repeat=n))
        intervals = []
        for w in words:
            L, R = ordered_endpoints(w)
            assert Fraction(1, 3) <= L < R <= 1
            assert odds(w) == odds(w[::-1]) or odds(w) == 1 / odds(w[::-1])
            assert mat_word(w[::-1]) == tuple(zip(*mat_word(w)))
            intervals.append((L, R))
            checked += 1
        intervals.sort()
        assert intervals[0][0] == Fraction(1, 3)
        assert intervals[-1][1] == 1
        assert all(intervals[i][1] == intervals[i + 1][0]
                   for i in range(len(intervals) - 1))
        assert abs(sum(mass(w) for w in words) - 1) < 5e-10
    for n in range(1, 60):
        w = (0,) * n
        left, right = ordered_endpoints(w)
        assert left == Fraction(1, 3)
        assert right == Fraction(1, 3) + Fraction(2, 3 * 4 ** n)
        assert odds(w) == Fraction(1) + Fraction(2, 4 ** n)
    # Invariance of dz/(z log 3): the two branch density contributions sum to 1/z.
    for z in (Fraction(1, 3), Fraction(3, 7), Fraction(1, 2), Fraction(5, 8), Fraction(1)):
        g0 = (1 + z) / 4
        g1 = (1 + z) / (4 * z)
        lhs = Fraction(1, 1) / (4 * g0) + Fraction(1, 1) / (4 * z * z * g1)
        assert lhs == 1 / z
    assert mass((0, 0)) < mass((0,)) ** 2 - 0.02
    print('VERIFY_OK', checked)


if __name__ == '__main__':
    verify()
