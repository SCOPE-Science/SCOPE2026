#!/usr/bin/env python3
"""Reproduce the minimal-unique-factor classification and generating-function coefficients.

Usage: python3 mus_checker.py
Uses only Python's standard library. This is finite verification, not the proof.
"""
from collections import Counter


def exhaustive_mus(word):
    """Independently count all contiguous occurrences, not merely distinct factors."""
    occurrence = Counter(
        word[left:right]
        for left in range(len(word))
        for right in range(left + 1, len(word) + 1)
    )
    return {
        factor
        for factor, count in occurrence.items()
        if count == 1
        and (
            len(factor) == 1
            or (occurrence[factor[1:]] > 1 and occurrence[factor[:-1]] > 1)
        )
    }


def predicted_mus(a, b, c):
    """Formula obtained from the four structural categories in the theorem."""
    lengths = (a, b, c)
    top = max(lengths)
    longest_zero_unique = top > 0 and lengths.count(top) == 1
    factors = set()
    if longest_zero_unique:
        factors.add("0" * top)
    if a != b:
        r = min(a, b) + 1
        if not (longest_zero_unique and r == top):
            factors.add("0" * r + "1")
    if b != c:
        r = min(b, c) + 1
        if not (longest_zero_unique and r == top):
            factors.add("1" + "0" * r)
    if a >= b and c >= b:
        factors.add("1" + "0" * b + "1")
    return factors


def coefficient_denom(max_n, degrees):
    """Coefficients of reciprocal product of (1-z**d) for d in degrees."""
    result = [1] + [0] * max_n
    for d in degrees:
        for n in range(d, max_n + 1):
            result[n] += result[n - d]
    return result


def convolve_poly(poly, seq, max_n):
    return [
        sum(coeff * seq[n - d] for d, coeff in enumerate(poly) if d <= n)
        for n in range(max_n + 1)
    ]


def coefficient_tables(max_n):
    # F_1 = (1+z+z^2-z^3)/((1-z^2)(1-z^3))
    # F_2 = (2z+2z^3)/((1-z^2)(1-z^3))
    # F_3 = (4z^2-z^3+z^4)/((1-z)(1-z^2)(1-z^3))
    # F_4 = 2z^3/((1-z)(1-z^2)(1-z^3))
    d23 = coefficient_denom(max_n, (2, 3))
    d123 = coefficient_denom(max_n, (1, 2, 3))
    return {
        1: convolve_poly((1, 1, 1, -1), d23, max_n),
        2: convolve_poly((0, 2, 0, 2), d23, max_n),
        3: convolve_poly((0, 0, 4, -1, 1), d123, max_n),
        4: convolve_poly((0, 0, 0, 2), d123, max_n),
    }


def main():
    highest = 35
    expected = coefficient_tables(highest)
    total_instances = 0
    for zeros in range(highest + 1):
        observed = Counter()
        for a in range(zeros + 1):
            for b in range(zeros - a + 1):
                c = zeros - a - b
                word = "0" * a + "1" + "0" * b + "1" + "0" * c
                direct = exhaustive_mus(word)
                predicted = predicted_mus(a, b, c)
                assert direct == predicted, (a, b, c, direct, predicted)
                observed[len(direct)] += 1
                total_instances += 1
                assert len(direct) in (1, 2, 3, 4)
                assert (len(direct) == 4) == (b < min(a, c) and a != c)
        assert sum(observed.values()) == (zeros + 1) * (zeros + 2) // 2
        for k in (1, 2, 3, 4):
            assert observed[k] == expected[k][zeros], (zeros, k, observed[k], expected[k][zeros])
        if zeros <= 12:
            print(f"zeros={zeros:2d}: MUS multiplicities " +
                  " ".join(f"{k}:{observed[k]}" for k in (1, 2, 3, 4)))
    assert exhaustive_mus("01100") == {"00", "01", "10", "11"}
    assert exhaustive_mus("00110") == {"00", "01", "10", "11"}
    print("PASSED", total_instances, "length-parameter triples across zeros=0..", highest)
    print("Coefficient checks passed through degree", highest)


if __name__ == "__main__":
    main()
