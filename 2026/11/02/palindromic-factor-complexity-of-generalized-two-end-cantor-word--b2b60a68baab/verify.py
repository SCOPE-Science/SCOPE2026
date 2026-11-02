#!/usr/bin/env python3
"""Independent finite regression tests for Cantor-word palindrome spectra.

Runs with Python's standard library.  Finite regressions are not a substitute
for the complete, all-length valuation argument in RESULT.md.
"""
from itertools import product


def digit_indicator(position, base):
    """Evaluate the Cantor symbol using its base-digit definition."""
    while position:
        position, digit = divmod(position, base)
        if digit not in (0, base - 1):
            return "0"
    return "1"


def substitution_prefix(base, minimum_length):
    word = "1"
    while len(word) < minimum_length:
        word = "".join("1" + "0" * (base - 2) + "1" if symbol == "1"
                       else "0" * base for symbol in word)
    return word


def predicted_count(base, length):
    a = base - 2
    total = 1 + int(length % 2 == 1 and length <= 2 * a + 1)
    j = 0
    while a * base ** j + 2 <= length:
        gap = a * base ** j
        if ((length - gap) % 2 == 0
                and length <= (2 * a + 1) * base ** (j + 1)):
            total += 1
        j += 1
    return total


def verify():
    checked = 0
    for base in range(3, 8):
        word = substitution_prefix(base, 25000)
        # Independent access: digit test, not substitution recursion.
        for pos in range(min(5000, len(word))):
            assert word[pos] == digit_indicator(pos, base), (base, pos)
        for length in range(1, 150):
            factors = {word[start:start + length]
                       for start in range(len(word) - length + 1)}
            observed = sum(factor == factor[::-1] for factor in factors)
            expected = predicted_count(base, length)
            assert observed == expected, (base, length, observed, expected)
            checked += 1
        # Independent gap valuation and block palindromicity for first 511 gaps.
        ones = [index for index, c in enumerate(word) if c == "1"]
        for index in range(1, min(512, len(ones))):
            j = (index & -index).bit_length() - 1
            assert ones[index] - ones[index - 1] - 1 == (base - 2) * base ** j
        for j in range(5):
            core = "1"
            for _ in range(j + 1):
                core = "".join("1" + "0" * (base - 2) + "1"
                               if symbol == "1" else "0" * base
                               for symbol in core)
            assert core == core[::-1]
    print(f"VERIFY_OK: {checked} palindrome length/base checks; 25000-symbol prefixes; digit/gap/core checks")


if __name__ == "__main__":
    verify()
