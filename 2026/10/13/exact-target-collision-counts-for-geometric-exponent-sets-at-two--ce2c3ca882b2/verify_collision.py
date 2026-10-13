#!/usr/bin/env python3
"""Finite corroboration of exact geometric target-collision counts.

Execute with Python 3.9 or later; no external packages. The theorem is
proved separately by a carrying argument; exhaustive finite tests alone
cannot prove its unbounded scope.
"""
from itertools import combinations_with_replacement


def formula(base, length, factor):
    standard = 2 if (base - 1) % factor == 0 else 0
    ternary = (length - 3) if (
        base == 3 and length >= 4 and 4 % factor == 0
    ) else 0
    return 1 + standard + ternary


def direct_count(base, length, factor):
    mod = factor * base ** (length - 2)
    exponents = [base ** i - 1 for i in range(length)]
    target = sum(exponents) % mod
    count = 0
    for chosen in combinations_with_replacement(range(length), length):
        if sum(exponents[i] for i in chosen) % mod == target:
            count += 1
    return count


def main():
    checks = 0
    for base in range(3, 10):
        for length in range(2, 9):
            for factor in range(1, 40):
                actual = direct_count(base, length, factor)
                predicted = formula(base, length, factor)
                assert actual == predicted, (base, length, factor, actual, predicted)
                checks += 1
    assert formula(3, 3, 4) == 1
    assert formula(3, 4, 4) == 2
    assert formula(3, 6, 1) == 6
    assert formula(4, 7, 3) == 3
    assert formula(4, 7, 4) == 1
    print(f"VERIFY_OK exhaustive_parameter_triples={checks} "+
          "ternary_boundary=PASS divisor_case=PASS")


if __name__ == "__main__":
    main()
