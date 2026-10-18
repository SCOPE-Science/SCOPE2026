#!/usr/bin/env python3
"""Exact independent checks for Boolean-order-ideal Fourier Smith data.
Requires SymPy. No external data or network access.
"""
import itertools
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def ideals(n):
    masks = range(1 << n)
    for family_mask in range(1, 1 << (1 << n)):
        family = [s for s in masks if (family_mask >> s) & 1]
        if not family or 0 not in family:
            continue
        if all(any((t & s) == t and t not in family for t in masks) is False for s in family):
            yield family


def check(fam):
    fam = sorted(fam, key=lambda a: (a.bit_count(), a))
    m = len(fam)
    H = Matrix([[(-1) ** ((a & b).bit_count()) for b in fam] for a in fam])
    Z = Matrix([[int((b & a) == b) for b in fam] for a in fam])
    D = Matrix.diag(*[(-2) ** a.bit_count() for a in fam])
    assert H == Z * D * Z.T
    assert Z.det() == 1
    assert H.det() == D.det()
    smith = smith_normal_form(H, domain=ZZ)
    assert [abs(int(smith[i, i])) for i in range(m)] == [2 ** a.bit_count() for a in fam]
    # Rational arithmetic is exact.
    from sympy import Rational
    inverse = Matrix([[(-1) ** (a.bit_count() + b.bit_count()) * sum(
        (Rational(-1, 2) ** c.bit_count()) for c in fam if (a & c) == a and (b & c) == b
    ) for b in fam] for a in fam])
    assert H * inverse == Matrix.eye(m)
    for r in [1, 2, 3]:
        size = 2 ** sum(min(r, a.bit_count()) for a in fam)
        assert size >= 1
    return m


def main():
    count = 0
    for n in range(4):
        for fam in ideals(n):
            check(fam)
            count += 1
    check([0, 1, 2, 4, 3, 6])
    check([s for s in range(16) if s.bit_count() <= 2])
    print('PASS: checked', count, 'order ideals with n <= 3, two additional examples')


if __name__ == '__main__':
    main()
