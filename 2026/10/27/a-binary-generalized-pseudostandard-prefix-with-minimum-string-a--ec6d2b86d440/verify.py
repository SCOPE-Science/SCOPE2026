#!/usr/bin/env python3
"""Exact finite verification of a six-point string-attractor witness.

Only the Python standard library is required. Positions are indexed from zero.
"""
from itertools import combinations

DELTA = "11011111"
THETA = "RRRERERE"
LENGTHS = (1, 2, 5, 12, 22, 46, 90, 182)
WITNESS = (23, 43, 72, 101, 130, 152)

# Twelve factors witnessing the impossibility of a five-position attractor.
OBSTRUCTIONS = (
    "000100011101101110001001",
    "100100011101101110001000",
    "111011100010010001110111",
    "000100011101101110001000",
    "111011100010010001110110",
    "011011100010010001110111",
    "01101110001000",
    "11101110001001",
    "1110111",
    "0001000",
    "10010001110111",
    "00010001110110",
)

# For a position p, the bit set j indicates that p lies in an occurrence
# of OBSTRUCTIONS[j]. The following are exactly the inclusion-maximal sets.
MAXIMAL_INCIDENCE = (
    "101000000001",
    "000000000011",
    "001001000010",
    "000110000100",
    "010010000100",
    "010100000100",
    "101000001000",
    "100001001000",
    "001001001000",
    "000110010000",
    "000000110000",
    "010100100000",
)


def anti_reverse(s, kind):
    t = s[::-1]
    return t if kind == "R" else t.translate(str.maketrans("01", "10"))


def closure(s, kind):
    # Construct the shortest fixed point of the specified antimorphism
    # having s as prefix, by its longest pseudopalindromic suffix.
    for k in range(len(s), -1, -1):
        suffix = s[len(s) - k:]
        if suffix == anti_reverse(suffix, kind):
            return s + anti_reverse(s[:len(s) - k], kind)
    raise AssertionError("unreachable")


def produce_word():
    w = ""
    for i, (letter, kind) in enumerate(zip(DELTA, THETA)):
        w = closure(w + letter, kind)
        assert len(w) == LENGTHS[i]
        assert w == anti_reverse(w, kind)
    return w


def occurrence_start_positions(w, u):
    return [i for i in range(len(w) - len(u) + 1)
            if w[i:i + len(u)] == u]


def confirm_upper(w):
    # Independent of the obstruction calculation: enumerate every
    # nonempty factor and every interval that can witness it.
    covered = {}
    n = len(w)
    for i in range(n):
        for j in range(i + 1, n + 1):
            factor = w[i:j]
            if any(i <= p < j for p in WITNESS):
                covered[factor] = True
            else:
                covered.setdefault(factor, False)
    assert all(covered.values())
    assert len(WITNESS) == len(set(WITNESS)) == 6
    return len(covered)


def confirm_lower(w):
    assert len(set(OBSTRUCTIONS)) == 12
    incidence = [0] * len(w)
    occurrences = []
    for j, u in enumerate(OBSTRUCTIONS):
        starts = occurrence_start_positions(w, u)
        assert starts, (j, u)
        occurrences.append(starts)
        for i in starts:
            for p in range(i, i + len(u)):
                incidence[p] |= 1 << j

    unique = set(incidence)
    maximal = {a for a in unique if a != 0
               and not any(a != b and (a & b) == a for b in unique)}
    required = {int(s, 2) for s in MAXIMAL_INCIDENCE}
    assert len(maximal) == len(required) == 12
    assert maximal == required

    target = (1 << len(OBSTRUCTIONS)) - 1
    # Any set of five positions is dominated, obstruction by obstruction,
    # by five of the maximal incidence types. Verify all C(12, 5)=792 cases.
    tested = 0
    for indices in combinations(sorted(maximal), 5):
        tested += 1
        cover = 0
        for mask in indices:
            cover |= mask
        assert cover != target, indices
    assert tested == 792
    return tested, occurrences


def main():
    word = produce_word()
    assert len(word) == 182
    factor_count = confirm_upper(word)
    count, starts = confirm_lower(word)
    print("PSEUDOSTANDARD_ATTRACTOR_6_PASS", "length=182",
          "distinct_factors=" + str(factor_count),
          "obstructions=12", "maximal_incidence=12",
          "five_type_cases=" + str(count))


if __name__ == "__main__":
    main()
