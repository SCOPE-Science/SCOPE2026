#!/usr/bin/env python3
"""Independent factor-rotation enumeration for a two-marker periodic word.

Run with Python 3. No third-party dependencies. The finite enumeration
checks examples and coefficients, not the universal proof in RESULT.md.
"""
from collections import Counter


def canonical(x):
    return min(x[j:] + x[:j] for j in range(len(x)))


def direct_classes(b, d, n):
    period = "0" + "1" * b + "0" + "1" * d
    p = len(period)
    repeats = (n + 2 * p) // p + 2
    long_word = period * repeats
    factors = {long_word[i:i+n] for i in range(p)}
    candidates = {canonical(x) for x in factors}
    return {x for x in candidates
            if all(x[j:] + x[:j] in factors for j in range(n))}


def proposed_classes(b, d, n):
    assert 1 <= b < d and n >= 1
    p = b + d + 2
    m = min(d, 2 * b + 1)
    groups = set()
    if n == 1:
        groups.add("0")
    if n <= d:
        groups.add("1" * n)
    if 2 <= n <= m + 1:
        groups.add("0" + "1" * (n - 1))
    if n == 2 * b + 2:
        groups.add(("0" + "1" * b) * 2)
    if n % p == 0:
        groups.add(("0" + "1" * b + "0" + "1" * d) * (n // p))
    return groups


def spectrum(b, d, n):
    p = b + d + 2
    m = min(d, 2 * b + 1)
    return int(n == 1) + int(n <= d) + int(2 <= n <= m + 1) + \
        int(n == 2 * b + 2) + int(n % p == 0)


def optimizers(p):
    valid = [(b, p - b - 2) for b in range(1, p - 2)
             if b < p - b - 2]
    masses = {pair: sum(spectrum(*pair, n) for n in range(1, p + 1))
              for pair in valid}
    maximum = max(masses.values())
    return maximum, sorted(b for (b, d), s in masses.items() if s == maximum)


def predicted_optimizers(p):
    if p == 5:
        return [1]
    base = (p - 3) // 3
    if p >= 8 and p % 3 == 2:
        return [base, base + 1]
    return [base]


def main():
    compared = 0
    for b in range(1, 20):
        for d in range(b + 1, 28):
            p = b + d + 2
            for n in range(1, 3 * p + 5):
                observed = direct_classes(b, d, n)
                expected = proposed_classes(b, d, n)
                assert observed == expected, (b, d, n, observed, expected)
                assert len(observed) == spectrum(b, d, n)
                compared += 1
    for p in range(5, 100):
        mass, args = optimizers(p)
        assert mass == (4 * p) // 3 + 1, (p, mass)
        assert args == predicted_optimizers(p), (p, args)
    for b in range(1, 40):
        for d in range(b + 1, 50):
            p = b + d + 2
            sum_spectrum = sum(spectrum(b, d, n) for n in range(1, p + 1))
            assert sum_spectrum == d + 3 + min(d, 2 * b + 1)
            assert (max(spectrum(b, d, n) for n in range(1, p + 1)) == 3) == (d >= 2 * b + 2)
    print(f"VERIFY_OK complete_necklace_sets={compared} sharp_length_extrema=5..99 exact_mass=true peak_transition=true")


if __name__ == "__main__":
    main()
