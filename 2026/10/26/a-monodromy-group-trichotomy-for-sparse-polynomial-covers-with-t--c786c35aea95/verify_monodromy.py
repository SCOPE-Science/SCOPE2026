#!/usr/bin/env python3
"""Finite exact permutation-group checks for the branch-cycle representatives.

Run: python verify_monodromy.py
Requires SymPy (tested with SymPy 1.13).
"""
from math import factorial
from sympy.combinatorics import Permutation, PermutationGroup


def permutation(n, cycles):
    values = list(range(n))
    for cycle in cycles:
        for old, new in zip(cycle, cycle[1:] + cycle[:1]):
            values[old] = new
    return Permutation(values)


def nonsymmetric(d):
    n = d + 4
    c = permutation(n, [list(range(d-1)) + [n-1]])
    a = permutation(n, [[d, d+1], [d-1, d+2]])
    b = permutation(n, [[d, d+2], [d-1, n-1]])
    return c, a, b


def symmetric(k):
    m = k + 2
    n = 2 * m
    values = list(range(n))
    for i in range(k-1):
        values[2*i] = 2*(i+1)
        values[2*i+1] = 2*(i+1)+1
    values[2*(k-1)] = 1
    values[2*(k-1)+1] = 0
    t = Permutation(values)
    s = permutation(n, [[2*(k-1), 2*k], [2*(k-1)+1, 2*k+1]])
    u = permutation(n, [[2*k, 2*(k+1)], [2*k+1, 2*(k+1)+1]])
    return t, s, u


def check():
    for d in range(3, 15):
        n = d + 4
        p, a, b = nonsymmetric(d)
        assert len((p*a*b).cyclic_form) == 1
        assert len((p*a*b).cyclic_form[0]) == n
        actual = PermutationGroup(p, a, b).order()
        expected = factorial(n) if d % 2 == 0 else factorial(n) // 2
        assert actual == expected, (d, actual, expected)
    for k in range(2, 10):
        m = k+2
        p, a, b = symmetric(k)
        assert len((p*a*b).cyclic_form) == 1
        assert len((p*a*b).cyclic_form[0]) == 2*m
        assert len(p.cyclic_form) == 1 and len(p.cyclic_form[0]) == 2*k
        assert len(a.cyclic_form) == 2 and len(b.cyclic_form) == 2
        actual = PermutationGroup(p, a, b).order()
        expected = (2 ** m) * factorial(m)
        assert actual == expected, (k, actual, expected)
    print('VERIFY_OK nonsymmetric_d=3..14 symmetric_k=2..9 exact_group_orders')


if __name__ == '__main__':
    check()
