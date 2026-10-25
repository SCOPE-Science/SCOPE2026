#!/usr/bin/env python3
"""Independent exact-integer checks of Ramanujan convolution Smith factors.

Requires Python 3 and SymPy (tested with SymPy 1.13+). These finite checks
illustrate the separately proved all-moduli formula; they are not a proof.
"""
from math import gcd, prod
from sympy import Matrix, divisors, factorint, mobius, totient
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def ramanujan_sum(n, t):
    return sum(int(d) * int(mobius(n // d)) for d in divisors(gcd(n, t)))


def predicted_invariants(n):
    r = int(totient(n))
    return [prod(p ** (a - 1 + (j > r // (p - 1)))
                 for p, a in factorint(n).items())
            for j in range(1, r + 1)] + [0] * (n - r)


def verify(n):
    matrix = Matrix(n, n, lambda i, j: ramanujan_sum(n, i-j))
    smith = smith_normal_form(matrix, domain=ZZ)
    actual = [abs(int(smith[i, i])) for i in range(n)]
    expected = predicted_invariants(n)
    assert actual == expected, (n, actual, expected)
    assert all(x == 0 for x in actual[int(totient(n)):])
    return int(totient(n))


def main():
    cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16,
             18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42]
    for n in cases:
        verify(n)
    print('VERIFY_OK smith_cases', len(cases), 'max_modulus', max(cases),
          'max_dimension', max(cases))


if __name__ == '__main__':
    main()
