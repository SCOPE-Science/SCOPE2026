#!/usr/bin/env python3
"""Exact finite checks for a parity-mode localization theorem.

This checks explicit witnesses and finite parameter grids only. The universal
claim is proved analytically in RESULT.md, not by the finite experiment.
"""
from fractions import Fraction
from itertools import product


def convolve_integer_polynomials(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def modal_sets(coefficients):
    even = coefficients[0::2]
    odd = coefficients[1::2]
    if not sum(even) or not sum(odd):
        return None
    epeak, opeak = max(even), max(odd)
    e = [k for k, v in enumerate(even) if v == epeak]
    o = [k for k, v in enumerate(odd) if v == opeak]
    return e, o


def verify_case(polynomial):
    modes = modal_sets(polynomial)
    if modes is None:
        return False
    e, o = modes
    assert len(e) <= 2 and e[-1] - e[0] <= 1
    assert len(o) <= 2 and o[-1] - o[0] <= 1
    lo, hi = e[0], e[-1]
    for k in o:
        assert lo - 1 <= k <= hi, (polynomial, e, o)
    for i in e:
        for j in o:
            assert abs(Fraction(2*i - (2*j+1), 2)) <= Fraction(3, 2)
            if len(e) == 1:
                assert abs(2*i-(2*j+1)) == 1
    return True


def run():
    grid = [(l, t, 4-l-t) for l in range(5) for t in range(5-l)]
    checked = 0
    for n in range(1, 5):
        count = 0
        greatest = Fraction(0)
        for factors in product(grid, repeat=n):
            poly = [1]
            for factor in factors:
                poly = convolve_integer_polynomials(poly, factor)
            if verify_case(poly):
                count += 1
                even, odd = modal_sets(poly)
                separation = max(abs(Fraction(2*i-(2*j+1), 2)) for i in even for j in odd)
                greatest = max(greatest, separation)
        assert greatest == (Fraction(1, 2) if n == 1 else Fraction(3, 2))
        checked += count
        print(f"n={n}: admissible nonzero-parity cases={count}; exact largest gap={greatest}")
    first = (0, 1, 3)
    second = (2, 0, 2)
    witness = convolve_integer_polynomials(first, second)
    assert witness == [0, 2, 6, 2, 6]
    assert modal_sets(witness) == ([1, 2], [0, 1])
    assert verify_case(witness)
    print(f"TOTAL checked admissible cases={checked}; sharp witness passes")


if __name__ == '__main__':
    run()
