"""Exact rational finite-digit check of an affine expanding/inverse-branch random map.

No external libraries. Run with Python 3. This verifies finite instances, not
by itself the universal claims, which follow from the written proof.
"""
from fractions import Fraction
from math import comb

checks = 0


def check(b, expansion_numerator, denominator, steps):
    global checks
    assert b >= 2 and 0 < expansion_numerator < denominator
    depth = steps + 2
    size = b ** depth
    head = b ** (depth - 1)
    weight = denominator * b
    a = expansion_numerator
    q = denominator - a
    digits = [2 * j - (b - 1) for j in range(b)]
    # Weighted expectation numerator after each random-map choice.
    numerator = [digits[x // head] for x in range(size)]
    variance = Fraction(b * b - 1, 3)
    theta = Fraction(a * q, denominator * denominator)
    for lag in range(steps + 1):
        observed = Fraction(sum(digits[x // head] * v
                                for x, v in enumerate(numerator)),
                            size * weight ** lag)
        predicted = (variance * Fraction(comb(lag, lag // 2), lag // 2 + 1)
                     * theta ** (lag // 2) if lag % 2 == 0 else Fraction(0))
        assert observed == predicted, (b, a, denominator, lag, observed, predicted)
        checks += 1
        if lag == steps:
            break
        new = [0] * size
        for state, v in enumerate(numerator):
            if v:
                shift_prefix = (state % head) * b
                inverse_suffix = state // b
                for digit in range(b):
                    new[shift_prefix + digit] += a * v
                    new[digit * head + inverse_suffix] += q * v
        numerator = new


for args in [(2, 2, 5, 12), (3, 3, 5, 8), (4, 1, 2, 6), (2, 1, 3, 10)]:
    check(*args)

# Independent Catalan recurrence and moment-summation checks.
for m in range(1, 40):
    assert Fraction(comb(2 * m, m), m + 1) == sum(
        Fraction(comb(2 * j, j), j + 1)
        * Fraction(comb(2 * (m - 1 - j), m - 1 - j), m - j)
        for j in range(m))
    checks += 1

for a, d in [(1, 2), (2, 5), (1, 3), (3, 5), (1, 4)]:
    p = Fraction(a, d)
    theta = p * (1 - p)
    for N in range(1, 41):
        by_pairs = Fraction(N)
        for m in range(1, (N - 1) // 2 + 1):
            by_pairs += 2 * (N - 2 * m) * Fraction(comb(2*m, m), m+1) * theta**m
        by_full_covariance = sum(
            sum(Fraction(comb(abs(i-j), abs(i-j)//2), abs(i-j)//2 + 1)
                * theta**(abs(i-j)//2) if abs(i-j)%2 == 0 else Fraction(0)
                for i in range(N)) for j in range(N))
        assert by_pairs == by_full_covariance
        checks += 1

print(f"PASS: {checks} exact integer/rational assertions")
