"""Independent finite arithmetic checks for the Catalan valuation census.

Usage: python3 verify.py
All computations use Python's integer arithmetic and the standard library.
"""
from collections import Counter
from fractions import Fraction


def factorial_valuation(n):
    total = 0
    while n:
        n //= 3
        total += n
    return total


def catalan_valuation(n):
    return (factorial_valuation(2*n)
            - factorial_valuation(n) - factorial_valuation(n+1))


def carry_valuation(n):
    digits = n
    carries = 0
    carry = 0
    while digits or carry:
        digit = digits % 3
        digits //= 3
        carry = (2 * digit + carry) // 3
        carries += carry
    m = n + 1
    while m % 3 == 0:
        carries -= 1
        m //= 3
    return carries


def recurrence_polynomials(limit):
    polys = [[1], [3]]
    for L in range(2, limit + 1):
        previous = polys[-1]
        preprevious = polys[-2]
        new = [0] * (len(previous) + 1)
        for r, count in enumerate(previous):
            new[r] += 2 * count
            new[r+1] += 2 * count
        for r, count in enumerate(preprevious):
            new[r+1] -= 3 * count
        while len(new) > 1 and new[-1] == 0:
            new.pop()
        polys.append(new)
    return polys[:limit + 1]


def theoretical_moments(L):
    q = Fraction(1, 3 ** L)
    expectation = Fraction(L, 2) - Fraction(3, 4) + 3*q/4
    variance = (8*L - 15 + 24*q - 9*q*q)/16
    return expectation, variance


def run():
    polys = recurrence_polynomials(14)
    sample_count = 0
    for n in range(10000):
        assert catalan_valuation(n) == carry_valuation(n), n
    for L in range(10):
        observed = Counter(catalan_valuation(n) for n in range(3**L))
        sample_count += 3**L
        expected = {r: x for r, x in enumerate(polys[L]) if x}
        assert observed == expected, (L, observed, expected)
        assert sum(expected.values()) == 3**L, L
        assert all(x >= 0 for x in expected.values())
        E = Fraction(sum(r*v for r,v in expected.items()), 3**L)
        V = Fraction(sum(r*r*v for r,v in expected.items()), 3**L) - E*E
        assert (E,V) == theoretical_moments(L), (L,E,V,theoretical_moments(L))
        if L > 0:
            assert observed[0] == 3*(2**(L-1))
            assert set(observed) == set(range(L))
    for L in range(15):
        assert sum(polys[L]) == 3**L
    assert polys[4] == [24,24,21,12]
    print(f'VERIFY_OK: {sample_count} valuation-census instances through L=9; '
          '10000 digit-carry comparisons; exact rational moments and polynomial normalization')


if __name__ == '__main__':
    run()
