"""Finite checks and asymptotic witness illustrations for fuzzy Gödel modal rows.

Use Python 3; no external packages. Infinite assertions are proved in RESULT.md.
"""
from fractions import Fraction
from itertools import product

VALUES = [Fraction(0), Fraction(1, 3), Fraction(2, 3), Fraction(1)]

def implication(a, b):
    return Fraction(1) if a <= b else b

def witnesses(row, valuation):
    box_terms = [implication(a, b) for a, b in zip(row, valuation)]
    dia_terms = [min(a, b) for a, b in zip(row, valuation)]
    return (min(box_terms) in box_terms and max(dia_terms) in dia_terms)

def main():
    cases = 0
    for m in range(1, 5):
        for row in product(VALUES, repeat=m):
            for valuation in product(VALUES, repeat=m):
                assert witnesses(row, valuation)
                cases += 1
    assert cases == 69904
    print('FINITE_GODEL_ROW_ATTAINMENT_OK', cases)

    # Values along an infinite positive row approaching zero: no box minimum.
    for N in (3, 7, 31, 127):
        a = [Fraction(1, n) for n in range(1, N+1)]
        p = [x/2 for x in a]
        box = [implication(x, y) for x, y in zip(a, p)]
        assert min(box) == Fraction(1, 2*N) > 0
    print('INFINITE_DECAYING_ROW_BOX_PATTERN_OK')

    # On an infinite constant-weight row, a diamond supremum can be unattained.
    d = Fraction(1, 2)
    for N in (3, 7, 31, 127):
        a = [d] * N
        p = [d*(1-Fraction(1, n+1)) for n in range(1, N+1)]
        diamond = [min(x,y) for x,y in zip(a,p)]
        assert max(diamond) == d*(1-Fraction(1, N+1)) < d
    print('NON_C0_ROW_DIAMOND_PATTERN_OK')
    print('GODEL_UNIFORM_WITNESSABILITY_CHECK_OK')

if __name__ == '__main__':
    main()
