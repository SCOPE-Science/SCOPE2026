#!/usr/bin/env python3
"""Exact finite-window certificate for the Rudin-Shapiro four-state cover.
Run with Python 3: python verify.py. No external packages are required.
"""
from hashlib import sha256
from pathlib import Path

MORPHISM = {"a": "ab", "b": "ac", "c": "db", "d": "dc"}
EXPECTED_PAIRS = {"ab", "ac", "ba", "bd", "ca", "cd", "db", "dc"}
EXPECTED = {
    1: (4, 4, 4, 4),
    2: (8, 8, 0, 4),
    3: (16, 16, 8, 12),
    4: (24, 16, 0, 16),
    5: (32, 16, 8, 28),
    6: (40, 8, 0, 36),
    7: (48, 4, 4, 48),
    8: (56, 0, 0, 56),
}
EXPECTED_SEVEN = {"acabaca", "babdbab", "cdcacdc", "dbdcdbd"}


def iterate(s, power):
    for _ in range(power):
        s = "".join(MORPHISM[ch] for ch in s)
    return s


def factors(word, length):
    return {word[i : i + length] for i in range(len(word) - length + 1)}


def exact_factors(length, power=3):
    # Every length <= 2**power window is within two adjacent power-blocks.
    # All eight allowed adjacent pairs appear in the fixed point.
    assert 1 <= length <= 2**power
    return set().union(*(factors(iterate(pair, power), length) for pair in EXPECTED_PAIRS))


def main():
    prefix4 = iterate("a", 4)
    assert len(prefix4) == 16
    assert factors(prefix4, 2) == EXPECTED_PAIRS
    assert {MORPHISM[ch] for ch in MORPHISM} == {"ab", "ac", "db", "dc"}
    # Internal pairs are AB, and boundary pairs must lie in BA,
    # with A={a,d}, B={b,c}; these are exactly EXPECTED_PAIRS.
    assert {x + y for x in "ad" for y in "bc"} | {
        x + y for x in "bc" for y in "ad"
    } == EXPECTED_PAIRS

    long_prefix = iterate("a", 13)
    for n in range(1, 9):
        fs = exact_factors(n)
        # Independent generation of fixed-point windows from a 8192-symbol prefix.
        assert fs == factors(long_prefix, n)
        reversible = {x for x in fs if x[::-1] in fs}
        pal = {x for x in fs if x == x[::-1]}
        orbit_count = len(fs) - (len(reversible) - len(pal)) // 2
        assert (len(fs), len(reversible), len(pal), orbit_count) == EXPECTED[n]
        if n == 7:
            assert reversible == pal == EXPECTED_SEVEN
        if n == 8:
            assert not reversible
            # A short fixed certificate is the sorted collection of all 56 factors.
            text = "\n".join(sorted(fs)) + "\n"
            certificate = Path(__file__).with_name("factors8.txt").read_bytes()
            assert certificate == text.encode("ascii")
            assert sha256(certificate).hexdigest() == (
                "2aa97abe490366aad190ec88b638589d77046f871f0d6b69982810e4a6ec0fb4"
            )
            print("F8_SHA256", sha256(text.encode("ascii")).hexdigest())

    # Independent long-window checks of the symbolic 8(n-1) factor law.
    # Morphism-power 8 produces blocks of length 256; two-block windows
    # therefore exhaust all n-factors for n<=256.
    for n in range(2, 257):
        fs = exact_factors(n, power=8)
        assert len(fs) == 8 * (n - 1), (n, len(fs))
    print("F1_TO_F8", [EXPECTED[n] for n in range(1, 9)])
    print("REVERSIBLE_SEVEN", ",".join(sorted(EXPECTED_SEVEN)))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
