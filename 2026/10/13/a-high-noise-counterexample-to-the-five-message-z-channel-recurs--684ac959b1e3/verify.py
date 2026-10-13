#!/usr/bin/env python3
"""Exact maximum-likelihood comparison for two explicit 5-word length-8 Z-channel codes.

Uses the Python standard library, integer polynomial coefficients, and exact
rational likelihoods; no optimization or third-party implementation is required.
"""
from fractions import Fraction
from math import comb

N = 8
COLUMNS = (
    (0, 0, 0, 1, 1),
    (0, 0, 1, 0, 1),
    (0, 1, 0, 0, 1),
    (0, 0, 1, 1, 1),
    (0, 1, 0, 1, 1),
)
STAR_ORDER = (0, 1, 2, 0, 1, 2, 3, 4)
PART_ORDER = (2, 2, 1, 1, 1, 0, 0, 0)
EXPECTED_STAR = ('00000000', '00100101', '01001010', '10010011', '11111111')
EXPECTED_PART = ('00000000', '11000000', '00111000', '00000111', '11111111')


def rows(order):
    return tuple(''.join(str(COLUMNS[j][i]) for j in order) for i in range(5))


def mask(word):
    return int(word, 2)


def ml_poly_five_success(cwords):
    """Coefficient vector for 5 * P_success(p) over all 256 possible received words.

    The likelihood for output y of weight w, from an input x of weight m
    containing y, is p**(m-w)*(1-p)**w. The unique maximal likelihood value
    (ties irrelevant) is from the smallest qualifying m for every 0<p<1.
    """
    words = [mask(w) for w in cwords]
    poly = [0] * (N + 1)
    for y in range(1 << N):
        w = y.bit_count()
        qualifying = [x.bit_count() for x in words if y & ~x == 0]
        assert qualifying, f'uncovered output {y:08b}'
        m = min(qualifying)
        for k in range(w + 1):
            deg = (m - w) + k
            poly[deg] += (-1)**k * comb(w, k)
    return tuple(poly)


def independent_rational_likelihood(cwords, p):
    """Separate direct maximum-likelihood method at an exact rational p."""
    words = [mask(w) for w in cwords]
    total = Fraction(0, 1)
    for y in range(1 << N):
        likelihoods = []
        for x in words:
            if y & ~x:
                likelihoods.append(Fraction(0, 1))
            else:
                w = y.bit_count()
                likelihoods.append(p ** (x.bit_count() - w) * (1 - p) ** w)
        total += max(likelihoods)
    return total


def value(coeffs, p):
    return sum((a * p ** k for k, a in enumerate(coeffs)), Fraction(0, 1))


def times_five_star(p):
    # Derived by partitioning output supports by their minimum-weight covering codeword.
    return 5 - 4 * p**3 - 2 * p**5 + 2 * p**7


def times_five_partition(p):
    # Derived from disjoint supports of sizes 2, 3, 3 and their all-ones union.
    return 5 - p**2 - 2*p**3 - 2*p**5 - p**6 + 2*p**8


def cubic(p):
    return 2 * p**3 + p - 1


def main():
    assert rows(STAR_ORDER) == EXPECTED_STAR
    assert rows(PART_ORDER) == EXPECTED_PART
    assert len(set(EXPECTED_STAR)) == len(set(EXPECTED_PART)) == 5

    poly_star = ml_poly_five_success(EXPECTED_STAR)
    poly_part = ml_poly_five_success(EXPECTED_PART)
    expected_star = (5, 0, 0, -4, 0, -2, 0, 2, 0)
    expected_part = (5, 0, -1, -2, 0, -2, -1, 0, 2)
    assert poly_star == expected_star
    assert poly_part == expected_part

    for p in (Fraction(1, 100), Fraction(1, 4), Fraction(1, 2),
              Fraction(59, 100), Fraction(9, 10), Fraction(99, 100)):
        assert independent_rational_likelihood(EXPECTED_STAR, p) == value(poly_star, p)
        assert independent_rational_likelihood(EXPECTED_PART, p) == value(poly_part, p)
        assert times_five_star(p) == value(poly_star, p)
        assert times_five_partition(p) == value(poly_part, p)
        assert times_five_partition(p) - times_five_star(p) == \
               p**2 * (1-p)**2 * (1+p) * cubic(p)

    # The cubic is strictly increasing for p>0 and crosses zero in (0,1).
    assert cubic(Fraction(5897, 10000)) < 0
    assert cubic(Fraction(5898, 10000)) > 0

    p = Fraction(9, 10)
    q_star = value(poly_star, p)
    q_part = value(poly_part, p)
    delta = q_part - q_star
    assert q_star == Fraction(9298069, 5000000)
    assert q_part == Fraction(94025671, 50000000)
    assert delta == Fraction(1044981, 50000000)
    assert delta > 0

    print('STAR=' + ','.join(EXPECTED_STAR))
    print('ALTERNATIVE=' + ','.join(EXPECTED_PART))
    print('FIVE_TIMES_SUCCESS_STAR=' + repr(poly_star))
    print('FIVE_TIMES_SUCCESS_ALTERNATIVE=' + repr(poly_part))
    print('P=9/10; FIVE_TIMES_SUCCESS_STAR=' + str(q_star))
    print('P=9/10; FIVE_TIMES_SUCCESS_ALTERNATIVE=' + str(q_part))
    print('P=9/10; FIVE_TIMES_SUCCESS_GAIN=' + str(delta))
    print('VERIFY_OK n=8 M=5 crossover_root_interval=(0.5897,0.5898) '
          'positive_gain_at_p=0.9 exact_polynomials=true independent_ml=true')


if __name__ == '__main__':
    main()
