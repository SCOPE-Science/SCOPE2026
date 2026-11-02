#!/usr/bin/env python3
"""Exact-integer checks of binary-carry subset-sum criteria."""
from fractions import Fraction
from math import comb


def is_complete_prefix(s, alpha):
    previous = 0
    for value in s:
        digit = (alpha.numerator * value) // alpha.denominator
        if digit > previous + 1:
            return False
        previous += digit
    return True


def classification(s_prefix, alpha):
    values = [(alpha.numerator * v) // alpha.denominator for v in s_prefix]
    previous = 0
    for value in values:
        H = 1 + previous - value
        if H < 0:
            return False
        previous += value
    y = alpha * s_prefix[-1]
    frac = y - (y.numerator // y.denominator)
    den = frac.denominator
    if den & (den - 1):
        return False
    return frac.numerator.bit_count() <= H


def full_sequence(s_prefix, steps):
    s = list(s_prefix)
    for _ in range(steps):
        s.append(2 * s[-1])
    return s


def test():
    checks = 0
    strata = 0
    for m in range(2, 13):
        s = list(range(2, 2*m + 1))
        h = (m-1)**2
        for L in range(2, 12):
            expected = sum(comb(L-2, j) for j in range(min(h,L-2)+1))
            actual = 0
            for u in range(1 << (L-2)):
                alpha = Fraction(m*(1 << L)+u, 2*m*(1 << L))
                claim = (u.bit_count() <= h)
                assert classification(s, alpha) == claim
                assert is_complete_prefix(full_sequence(s, L+5), alpha) == claim
                actual += claim
                checks += 1
            assert actual == expected, (m,L,actual,expected)
            strata += 1
    # Exhaust all rational dyadic scales on several different eventual-doubling prefixes.
    pref_cases = [(2,), (3,4,5), (2,3,4,5), (2,3,5,8), (4,7,11), (1,2,4,6)]
    extra = 0
    for pref in pref_cases:
        for L in range(0,9):
            for p in range(1, 5*pref[-1]*(1 << L)+1):
                alpha = Fraction(p, pref[-1]*(1 << L))
                expect = classification(pref, alpha)
                obs = is_complete_prefix(full_sequence(pref, L+9), alpha)
                assert expect == obs, (pref,L,p,alpha)
                extra += 1
    # The pure geometric subfamily has only reciprocal powers of two.
    pure = 0
    for m in range(1,15):
        for L in range(0,11):
            for p in range(1, 4*m*(1 << L)+1):
                alpha = Fraction(p,m*(1 << L))
                expect = any(alpha == Fraction(1,m*(1 << k)) for k in range(L+1))
                assert classification((m,),alpha)==expect
                pure += 1
    print(f'VERIFY_OK stratum_cases={strata} stratum_points={checks} arbitrary_prefix_tests={extra} pure_geometric_tests={pure} exact_integer_rational=yes')


if __name__ == '__main__':
    test()
