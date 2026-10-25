#!/usr/bin/env python3
"""Exact finite verifier for the length-seven two-list, two-deletion code bound."""
from itertools import product
from fractions import Fraction

CODE = (
    "0000000", "0000111", "0001000", "0011101", "0100011",
    "0110101", "1001100", "1100010", "1111000", "1111110", "1111111",
)
WEIGHTS = {
    "00000":52, "00001":7, "00010":0, "00011":26,
    "00100":7, "00101":5, "00110":4, "00111":26,
    "01000":0, "01001":1, "01010":2, "01011":5,
    "01100":4, "01101":1, "01110":16, "01111":7,
    "10000":7, "10001":16, "10010":1, "10011":4,
    "10100":5, "10101":2, "10110":1, "10111":0,
    "11000":26, "11001":4, "11010":5, "11011":7,
    "11100":26, "11101":0, "11110":7, "11111":52,
}

def subsequence(y, x):
    """Return whether y occurs as a subsequence of x, independent of embeddings."""
    j = 0
    for ch in x:
        if j < len(y) and ch == y[j]:
            j += 1
    return j == len(y)

def main():
    words5 = ["".join(p) for p in product("01", repeat=5)]
    words7 = ["".join(p) for p in product("01", repeat=7)]
    assert len(CODE) == len(set(CODE)) == 11
    assert all(len(x) == 7 and set(x) <= {"0", "1"} for x in CODE)
    assert set(WEIGHTS) == set(words5)
    assert all(isinstance(w, int) and w >= 0 for w in WEIGHTS.values())
    assert sum(WEIGHTS.values()) == 326

    loads = {y: sum(subsequence(y, x) for x in CODE) for y in words5}
    assert max(loads.values()) <= 2
    assert [loads[y] for y in words5] == [
        2,2,2,2,2,2,2,2, 2,2,1,2,2,2,2,2,
        2,2,2,2,1,1,1,0, 2,2,2,1,2,2,2,2,
    ]

    constants = {"0000000", "1111111"}
    for x in words7:
        score = sum(w for y, w in WEIGHTS.items() if subsequence(y, x))
        if x in constants:
            assert score == 52
            assert score + 7 == 59
        else:
            assert score >= 59, (x, score)
    dual_numerator = 2 * sum(WEIGHTS.values()) + 14
    assert dual_numerator == 666
    assert Fraction(dual_numerator, 59) < 12
    print("PASS: 11-word witness; all 32 received-word loads <= 2.")
    print("PASS: all 128 dual inequalities; exact upper bound 666/59 < 12.")
    print("CONCLUSION: the optimum is exactly 11.")

if __name__ == "__main__":
    main()
