"""Exact rational checks for complementary truncated logarithm valuations.

Uses Python integer arithmetic and Fraction; no external libraries required.
"""
from fractions import Fraction
from math import comb


def valuation(p, q):
    num, den = q.numerator, q.denominator
    if num == 0:
        raise ValueError('zero has no finite valuation')
    ans = 0
    while num % p == 0:
        num //= p
        ans += 1
    while den % p == 0:
        den //= p
        ans -= 1
    return ans


def truncated_sum(p, a, N):
    x, y = Fraction(p, a), Fraction(p, p - a)
    total = Fraction(0)
    xp = yp = Fraction(1)
    for k in range(1, N + 1):
        xp *= x
        yp *= y
        total += (xp + yp) / k
    return total


count = 0
for p, maxr in [(3, 4), (5, 2), (7, 2), (11, 1), (13, 1), (17, 1), (19, 1)]:
    for r in range(1, maxr + 1):
        N = 2 * p**r
        for a in {-2, -1, 1, 2, p - 1, p + 1}:
            if a % p == 0:
                continue
            actual = valuation(p, truncated_sum(p, a, N))
            expected = N + r + 2
            assert actual == expected, (p, a, r, actual, expected)
            count += 1

coeff_count = 0
for N in (6, 10, 14, 18, 50):
    for j in range(1, 25):
        coeff = Fraction(comb(N + j, j) - 1, N + j + 1)
        telescoped = Fraction(N, N + j + 1) * sum(
            (Fraction(comb(N + h - 1, h - 1), h) for h in range(1, j + 1)),
            Fraction(0)
        )
        assert coeff == telescoped
        coeff_count += 1

print('VERIFIER_OK')
print('exact_rational_valuation_cases=' + str(count))
print('exact_binomial_coefficient_identities=' + str(coeff_count))
print('highest_test_index=' + str(2 * 3**4))
print('proof_scope=all_odd_primes_all_positive_exponents_all_prime_units')
print('finite_checks_do_not_replace_the_symbolic_proof')
