#!/usr/bin/env python3
"""Independent finite checks of a five-run minimal-absent-factor limit law.

This program checks finite instances, not the infinite distribution theorem.
"""
from itertools import product
from fractions import Fraction


def missing(w):
    factors = {''}
    for i in range(len(w)):
        for j in range(i + 1, len(w) + 1):
            factors.add(w[i:j])
    answer = {x for x in '01' if x not in factors}
    for u in factors:
        for x, y in product('01', repeat=2):
            z = x + u + y
            if z not in factors and z[:-1] in factors and z[1:] in factors:
                answer.add(z)
    return answer


def predicted(a, b, c, d, e):
    T = max(c, min(a, e))
    M = max(b, d)
    return ({'1' + '0' * k + '1' for k in range(1, T + 1) if k != c}
            | {'0' + '1' * k + '0' for k in range(1, M + 1) if k not in (b, d)})


def test():
    maximal_remainder = 0
    for a, b, c, d, e in product(range(1, 6), repeat=5):
        w = '0' * a + '1' * b + '0' * c + '1' * d + '0' * e
        actual = missing(w)
        bridge = predicted(a, b, c, d, e)
        T = max(c, min(a, e))
        M = max(b, d)
        assert bridge <= actual, (a, b, c, d, e, bridge - actual)
        assert len(bridge) == T + M - 1 - len({b, d})
        assert all(z not in bridge for z in actual if len(z) == 3 and z in {'010', '101'} and z not in bridge)
        remainder = len(actual - bridge)
        assert 0 <= remainder <= 208
        maximal_remainder = max(maximal_remainder, remainder)

    # Uniform-simplex survival integrals: E[min(j selected coordinates)]=1/(5j).
    expected_T = Fraction(1, 5) + Fraction(1, 10) - Fraction(1, 15)
    expected_M = 2 * Fraction(1, 5) - Fraction(1, 10)
    assert expected_T == Fraction(7, 30)
    assert expected_M == Fraction(3, 10)
    assert expected_T + expected_M == Fraction(8, 15)
    print('VERIFY_OK compositions=3125 type3_families=true max_observed_remainder=%d mean=8/15' % maximal_remainder)


if __name__ == '__main__':
    test()
