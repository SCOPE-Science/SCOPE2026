#!/usr/bin/env python3
"""Reproduce a finite factor certificate and exact small-shift pseudoperiod census.

All computations use Python's standard library.  The independent RS check uses
binary digit pairs rather than the substitution from the factor certificate.
"""
from itertools import combinations
from math import comb
from pathlib import Path

MORPHISM = {"0": "01", "1": "02", "2": "31", "3": "32"}
CODING = {"0": "0", "1": "0", "2": "1", "3": "1"}
WIDTH = 65
BOUND = 64
EXPECTED = [
    (1, 4, 16, 17), (1, 4, 32, 33), (1, 4, 48, 49),
    (1, 7, 8, 9), (1, 7, 32, 33),
    (1, 15, 16, 17), (1, 16, 17, 20), (1, 23, 24, 25),
    (1, 25, 32, 33), (1, 26, 32, 33), (1, 27, 32, 33),
    (1, 31, 32, 33), (1, 32, 33, 36), (1, 32, 33, 39),
    (1, 39, 40, 41), (1, 47, 48, 49), (1, 48, 49, 52),
    (1, 55, 56, 57),
    (2, 3, 4, 5), (2, 5, 7, 12), (2, 15, 16, 18),
    (2, 31, 32, 34), (2, 47, 48, 50), (3, 4, 5, 6),
]


def substitution(word):
    return "".join(MORPHISM[c] for c in word)


def parity_11(n):
    assert n >= 0
    bits = bin(n)[2:]
    return sum(bits[i:i+2] == "11" for i in range(len(bits) - 1)) % 2


def factors(word, k):
    return {word[i:i+k] for i in range(len(word)-k+1)}


def verify():
    word = "0"
    for _ in range(10):
        word = substitution(word)
    assert len(word) == 1024
    alphabet_factors = factors(word, WIDTH)
    assert len(alphabet_factors) == 512
    # All length-65 factors of sigma(v), for every v in the current
    # length-65 language, remain in that language.  This proves the
    # language is EXACT for the infinite fixed point by prefix induction.
    closure_count = 0
    for v in alphabet_factors:
        longer = substitution(v)
        assert len(longer) == 2 * WIDTH
        for i in range(len(longer) - WIDTH + 1):
            assert longer[i:i+WIDTH] in alphabet_factors
            closure_count += 1
    assert closure_count == 512 * 66
    binary_factors = sorted({"".join(CODING[c] for c in v)
                             for v in alphabet_factors})
    assert len(binary_factors) == 512
    # The four-state substitution agrees with an independent definition
    # of Rudin-Shapiro as parity of occurrences of 11 in binary integers.
    direct_prefix = "".join(str(parity_11(n)) for n in range(16384))
    assert direct_prefix[:len(word)] == "".join(CODING[c] for c in word)
    assert factors(direct_prefix, WIDTH) == set(binary_factors)

    nfactor = len(binary_factors)
    full = (1 << nfactor) - 1
    matches = [0] * (BOUND + 1)
    # Each integer bitmask encodes all factors on which one shift matches
    # the initial symbol, so four shifts are a pseudoperiod iff their OR
    # equals the full mask.
    for i, v in enumerate(binary_factors):
        for d in range(1, BOUND + 1):
            if v[0] == v[d]:
                matches[d] |= (1 << i)
    solutions = [shifts for shifts in combinations(range(1, BOUND+1), 4)
                 if matches[shifts[0]] | matches[shifts[1]]
                 | matches[shifts[2]] | matches[shifts[3]] == full]
    assert len(solutions) == 24
    assert solutions == EXPECTED
    tab = Path(__file__).with_name("census.tsv")
    assert tab.exists(), "The 24-row census file is required."
    rows = tab.read_text(encoding="utf-8").splitlines()
    assert rows[0] == "a\tb\tc\td"
    assert [tuple(map(int, x.split("\t"))) for x in rows[1:]] == EXPECTED
    assert comb(BOUND, 4) == 635376
    # Separate nested-loop check of every quadruple through shift 32,
    # without the bit-mask enumeration used for the full census.
    short_factors = sorted(factors(direct_prefix, 33))
    assert len(short_factors) == 256
    brute_small = [s for s in combinations(range(1, 33), 4)
                   if all(any(v[0] == v[d] for d in s) for v in short_factors)]
    assert brute_small == [s for s in EXPECTED if s[3] <= 32]
    assert len(brute_small) == 9
    # Independent direct check on every purported survivor, using the
    # digit-pair definition rather than the substitution construction.
    for shifts in solutions:
        for i in range(8192):
            assert any(direct_prefix[i] == direct_prefix[i+d] for d in shifts)

    # Independent finite stress tests of the infinite family.  Its
    # universal validity follows from the four-residue proof, not tests.
    for m in range(1, 130):
        q = 8*m
        for i in range(4096):
            a = parity_11(i)
            assert any(a == parity_11(i+d) for d in (1, q-1, q, q+1))
    print("RUDIN_SHAPIRO_FOUR_PSEUDOPERIOD_PASS",
          "alphabet_factors=", len(alphabet_factors),
          "closure_windows=", closure_count,
          "binary_factors=", nfactor,
          "candidate_quadruples=", comb(BOUND, 4),
          "valid_quadruples=", len(solutions),
          "infinite_family_tested_m=1..129")
    return solutions


if __name__ == "__main__":
    verify()
