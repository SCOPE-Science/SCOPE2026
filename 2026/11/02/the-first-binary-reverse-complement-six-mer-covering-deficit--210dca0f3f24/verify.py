#!/usr/bin/env python3
"""Reproduce an exact binary reverse-complement six-mer covering certificate.

Requires only Python 3 standard library. This is a finite verification
of the explicit proof data, not a replacement for the telescoping argument.
"""

from collections import Counter
from itertools import product

WITNESSES = {
    2: "0010",
    4: "0010100001100",
    6: "00101111110111000110010011000011101010110100",
}
HIGH = {"00011", "00101", "10011", "11010", "11100"}
LOW = {"00110", "00111", "01011", "10100", "11000"}


def rc(word):
    return "".join("1" if b == "0" else "0" for b in reversed(word))


def orbit(word):
    return min(word, rc(word))


def words(k):
    return ("".join(t) for t in product("01", repeat=k))


def phi(word):
    assert len(word) == 5
    return 2 if word in HIGH else 0 if word in LOW else 1


def cost(word):
    assert len(word) == 6
    return 1 + phi(word[:-1]) - phi(word[1:])


def check():
    assert len(HIGH) == len(LOW) == 5
    assert HIGH.isdisjoint(LOW)
    assert {rc(x) for x in HIGH} == LOW
    for x in words(5):
        assert phi(rc(x)) == 2 - phi(x)

    for x in LOW:
        for b in "01":
            assert x[1:] + b not in HIGH

    all_six = list(words(6))
    fixed = [x for x in all_six if x == rc(x)]
    assert len(fixed) == 8
    assert sum(cost(x) for x in fixed) == 18
    assert sum(cost(x) for x in all_six) == 64
    assert all(cost(x) >= 0 and cost(x) == cost(rc(x)) for x in all_six)

    classes = {orbit(x) for x in all_six}
    assert len(classes) == 36
    orbit_costs = {orbit(x): cost(x) for x in all_six}
    assert sum(orbit_costs.values()) == 41

    # Independent string-level and integer-level orbit representations.
    for k, word in WITNESSES.items():
        all_classes = {orbit(x) for x in words(k)}
        factors = [word[i:i+k] for i in range(len(word) - k + 1)]
        seen = Counter(orbit(x) for x in factors)
        assert set(seen) == all_classes
        if k < 6:
            assert len(factors) == len(all_classes)
        else:
            assert len(word) == 44 and len(factors) == 39
            assert Counter(seen.values()) == {1: 33, 2: 3}
            assert {x for x, mult in seen.items() if mult == 2} == {
                "001100", "001110", "011100"
            }
            assert sum(cost(x) for x in factors) == 41
            assert phi(word[:5]) == 2 and phi(word[-5:]) == 0
            assert all(orbit_costs[x] == 0 for x, mult in seen.items() if mult > 1)

            def int_rc(z, bits):
                return sum((1 - ((z >> i) & 1)) << (bits - 1 - i)
                           for i in range(bits))

            ints = [int(x, 2) for x in factors]
            int_classes = {min(x, int_rc(x, 6)) for x in ints}
            assert int_classes == {int(x, 2) for x in classes}

    # Check the two smaller alphabetic optima at their orbit bounds directly.
    small_counts = {}
    for k in (2, 4):
        m = len({orbit(x) for x in words(k)})
        n = m + k - 1
        count = sum(1 for x in words(n)
                    if {orbit(x[i:i+k]) for i in range(n-k+1)}
                    == {orbit(y) for y in words(k)})
        small_counts[k] = count
    assert small_counts == {2: 6, 4: 12}

    print("VERIFY_OK")
    print("six_mer_classes=36 six_mer_windows=39 minimal_word_length=44")
    print("fixed_point_cost=18 all_edges_cost=64 orbit_cost=41 potential_range=2")
    print("smaller_optimal_word_counts", small_counts)


if __name__ == "__main__":
    check()
