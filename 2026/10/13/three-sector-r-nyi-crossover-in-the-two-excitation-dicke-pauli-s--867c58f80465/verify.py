"""Exact finite checks for the two-excitation Dicke Pauli-spectrum theorem.

Run: python3 verify.py
Requires only Python 3 standard library. These tests do not prove the limit theorem.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb


def direct_magnitude_numerator(n, pauli, support):
    """Numerator N times |<D|P|D>|, from computational-basis action."""
    total = 0j
    for state in support:
        image = state
        phase = 1 + 0j
        for pos, gate in enumerate(pauli):
            occupied = (state >> pos) & 1
            if gate == 'X':
                image ^= 1 << pos
            elif gate == 'Y':
                image ^= 1 << pos
                phase *= -1j if occupied else 1j
            elif gate == 'Z' and occupied:
                phase = -phase
        if image in support:
            total += phase
    assert total.imag == 0
    return abs(int(total.real))


def predicted_magnitude_numerator(n, pauli):
    r = sum(gate in 'XY' for gate in pauli)
    y = pauli.count('Y')
    c = pauli.count('Z')
    if y % 2 or r not in (0, 2, 4):
        return 0
    if r == 0:
        return abs(((n - 2 * c) ** 2 - n) // 2)
    if r == 2:
        return 2 * abs(n - 2 - 2 * c)
    return 6 if y in (0, 4) else 2


def closed_moment(n):
    return Fraction(4 * (91*n*n - 427*n + 492), n**3 * (n - 1)**3)


def sector_count_moment(n):
    N = comb(n, 2)
    a = sum(comb(n, c) * (((n - 2*c)**2 - n)//2)**4
            for c in range(n + 1))
    b = 2*N * sum(comb(n-2,c) * (2*(n-2-2*c))**4
                  for c in range(n - 1))
    c = comb(n, 4) * 2**(n-4) * (2*6**4 + 6*2**4)
    return Fraction(a+b+c, 2**n * N**4)


def main():
    total_strings = 0
    for n in range(4, 9):
        support = {sum(1 << i for i in pair)
                   for pair in combinations(range(n), 2)}
        assert len(support) == comb(n, 2)
        aggregate_fourth = 0
        for pauli in product('IXYZ', repeat=n):
            actual = direct_magnitude_numerator(n, pauli, support)
            prediction = predicted_magnitude_numerator(n, pauli)
            assert actual == prediction, (n, pauli, actual, prediction)
            aggregate_fourth += actual**4
            total_strings += 1
        assert Fraction(aggregate_fourth, 2**n * comb(n,2)**4) == closed_moment(n)
    for n in range(4, 31):
        assert sector_count_moment(n) == closed_moment(n), n
    print('VERIFY_OK', total_strings, 'Pauli actions and 27 exact moments')

if __name__ == '__main__':
    main()
