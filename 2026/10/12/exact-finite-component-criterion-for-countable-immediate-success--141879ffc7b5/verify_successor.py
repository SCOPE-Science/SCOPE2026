"""Standalone finite endpoint-pattern tests for the exact-successor classification.

The all-cardinality assertion is proved in the accompanying mathematical text;
these tests do not certify infinite assertions by enumeration.
"""
from functools import lru_cache
from itertools import product, permutations
from math import factorial

TYPES = ("F", "R", "L", "Z")  # finite, omega, omega*, integers
HAS_FIRST = {"F": 1, "R": 1, "L": 0, "Z": 0}
HAS_LAST = {"F": 1, "R": 0, "L": 1, "Z": 0}


def compatible(left, right):
    return not (HAS_LAST[left] and HAS_FIRST[right])


def count_orders(counts):
    """Number of admissible permutations of individually labelled components."""
    @lru_cache(None)
    def walk(remaining, prev):
        if sum(remaining) == 0:
            return 1
        total = 0
        for idx, kind in enumerate(TYPES):
            amount = remaining[idx]
            if amount and (prev < 0 or compatible(TYPES[prev], kind)):
                new = list(remaining)
                new[idx] -= 1
                total += amount * walk(tuple(new), idx)
        return total

    return walk(tuple(counts), -1)


def theorem(counts):
    return counts[0] <= counts[3] + 1


def check():
    checked_multisets = 0
    nonrealizable = 0
    total_sequences = 0
    for size in range(1, 9):
        for f in range(size + 1):
            for r in range(size - f + 1):
                for l in range(size - f - r + 1):
                    z = size - f - r - l
                    counts = (f, r, l, z)
                    exact = count_orders(counts)
                    predicted = theorem(counts)
                    assert (exact > 0) == predicted, (counts, exact)
                    if size <= 5:
                        assert max(0, f - z - 1) == min(
                            t for t in range(size + 2)
                            if count_orders((f, r, l, z + t)) > 0
                        ), counts
                    checked_multisets += 1
                    nonrealizable += exact == 0
                    total_sequences += exact
    # Separate brute-force permutation test, not using the DP count_orders.
    brute_checked = 0
    for size in range(1, 6):
        for typeseq in product(TYPES, repeat=size):
            found = any(
                all(compatible(a, b) for a, b in zip(p, p[1:]))
                for p in set(permutations(typeseq))
            )
            assert found == (typeseq.count("F") <= typeseq.count("Z") + 1)
            brute_checked += 1
    # Special obstructions and realizations.
    assert count_orders((2, 0, 0, 0)) == 0
    assert count_orders((2, 0, 0, 1)) > 0
    assert count_orders((3, 6, 6, 1)) == 0
    assert count_orders((3, 6, 6, 2)) > 0
    print("PASS", "endpoint multisets", checked_multisets,
          "unrealizable", nonrealizable,
          "brute labelled-type sequences", brute_checked,
          "total admissible component permutations", total_sequences)


if __name__ == "__main__":
    check()
