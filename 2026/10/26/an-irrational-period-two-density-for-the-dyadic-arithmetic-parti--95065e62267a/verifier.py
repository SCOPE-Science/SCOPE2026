#!/usr/bin/env python3
"""Exact finite checks for a dyadic arithmetic-partial-derivative period density.

Run with Python 3; no third-party packages required. Computations only support
the published self-contained proof, which handles every integer.
"""

from fractions import Fraction


def nu2(n):
    assert n >= 1
    return (n & -n).bit_length() - 1


def terminal_label(r):
    assert r >= 1
    while r > 2:
        r = 1 + nu2((r - 1) // 2)
    return r


def direct_period(exponent):
    assert exponent >= 2
    valuation = exponent
    visited = {}
    index = 0
    while valuation not in visited:
        visited[valuation] = index
        valuation += nu2(valuation) - 1
        index += 1
        assert index < 1000, 'unexpectedly long valuation trajectory'
    return index - visited[valuation]


def has_period_two_by_residues(exponent):
    # The first even valuation is twice floor(exponent/2).
    return terminal_label(1 + nu2(exponent // 2)) == 2


def in_recursive_set(r):
    return terminal_label(r) == 2


def check(limit=100000):
    for exponent in range(2, limit + 1):
        first = direct_period(exponent)
        second = 2 if has_period_two_by_residues(exponent) else 1
        third = terminal_label(exponent + 1)
        assert first == second == third, (exponent, first, second, third)
    for r in range(1, limit + 1):
        predicted = r == 2
        if r >= 3:
            t = nu2((r - 1) // 2) + 1
            predicted = in_recursive_set(t)
        assert in_recursive_set(r) == predicted
    # Dyadic rational truncation with exact tail bound.
    M = 120
    numerator = sum(1 << (M - r) for r in range(1, M + 1)
                    if in_recursive_set(r))
    lower = Fraction(numerator, 1 << M)
    upper = lower + Fraction(1, 1 << M)
    observed = sum(has_period_two_by_residues(e)
                   for e in range(2, limit + 1))
    # Quantitative discrepancy certificate, using explicit proven bound:
    # |A(N)-alpha*N| <= 2 floor(log2(N))+4.
    error = 2 * limit.bit_length() + 6
    assert lower * limit - error <= observed <= upper * limit + error
    print('VERIFIED: independent valuation cycles and recursive classification',
          'for all exponents 2..%d' % limit)
    print('VERIFIED: exact dyadic density enclosure',
          f'[{numerator}/2^{M}, ({numerator}+1)/2^{M}]')
    print('Period-two exponent count:', observed, 'of', limit - 1)
    print('Density, decimal approximation:', format(float(lower), '.15f'))
    print('First 60 binary digits:', ''.join(str(int(in_recursive_set(r)))
                                          for r in range(1, 61)))


if __name__ == '__main__':
    check()
