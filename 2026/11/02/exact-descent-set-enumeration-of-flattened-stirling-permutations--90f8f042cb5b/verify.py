#!/usr/bin/env python3
"""Exact integer verification of the flattened Stirling descent-set formula.
No dependencies outside the Python standard library. Run: python3 verify.py
"""
from collections import Counter
from functools import lru_cache
from math import comb


def block_formula(n):
    """For n>=1, return {tuple of 1-based descent indices: exact count}."""
    assert isinstance(n, int) and n >= 1
    out = Counter()

    def append_blocks(rem, pos, descents, multiplicity):
        if rem == 0:
            assert pos == 2 * n
            out[descents] += multiplicity
            return
        for size in range(1, rem + 1):
            choose_labels = comb(rem - 1, size - 1)
            for negative in range(size):
                positive = size - negative
                new_descents = descents
                if negative:
                    new_descents += (pos + 2 * negative,)
                if positive >= 2:
                    new_descents += (pos + 2 * size - 1,)
                append_blocks(
                    rem - size, pos + 2 * size, new_descents,
                    multiplicity * choose_labels * comb(size - 1, negative),
                )

    for zero_size in range(1, n + 1):
        first_desc = (2 * zero_size - 1,) if zero_size >= 2 else ()
        append_blocks(n - zero_size, 2 * zero_size,
                      first_desc, comb(n - 1, zero_size - 1))
    return out


def exhaustive_from_original_definition(n):
    """Independent exhaustive generation of all (2n-1)!! Stirling permutations."""
    found = Counter()

    def insert_next(word, next_value):
        if next_value > n:
            cuts = tuple(i + 1 for i in range(len(word) - 1)
                         if word[i] > word[i + 1])
            starts = (word[0],) + tuple(word[i] for i in cuts)
            if all(a <= b for a, b in zip(starts, starts[1:])):
                found[cuts] += 1
            return
        for index in range(len(word) + 1):
            insert_next(word[:index] + (next_value, next_value) + word[index:],
                        next_value + 1)

    insert_next((1, 1), 2)
    return found


def prescribed_descent_count(n, required_cuts):
    """O(n^3) arithmetic DP for one exact descent set; no word generation."""
    flags = [0] * (2 * n)
    for j in required_cuts:
        if not 1 <= j < 2 * n or flags[j]:
            raise ValueError("Descent indices must be distinct integers from 1 to 2n-1")
        flags[j] = 1
    pref = [0] * (2 * n)
    for j in range(1, 2 * n):
        pref[j] = pref[j - 1] + flags[j]

    @lru_cache(maxsize=None)
    def suffix(remaining):
        if remaining == 0:
            return 1
        offset = 2 * (n - remaining)
        total = 0
        for size in range(1, remaining + 1):
            label_choices = comb(remaining - 1, size - 1)
            demanded = pref[offset + 2 * size - 1] - pref[offset - 1]
            for negative in range(size):
                positive = size - negative
                cuts = ((offset + 2 * negative,) if negative else ())
                if positive >= 2:
                    cuts += (offset + 2 * size - 1,)
                # There are no unspecified/extra descents in this block interval.
                if len(cuts) == demanded and all(flags[j] for j in cuts):
                    total += label_choices * comb(size - 1, negative) * suffix(
                        remaining - size)
        return total

    answer = 0
    for zero_size in range(1, n + 1):
        zero_cut = (2 * zero_size - 1,) if zero_size >= 2 else ()
        desired = pref[2 * zero_size - 1]
        if desired == len(zero_cut) and all(flags[j] for j in zero_cut):
            answer += comb(n - 1, zero_size - 1) * suffix(n - zero_size)
    return answer


def equal_count_sparse(n, d):
    if d <= 0 or (2 * n) % d:
        return 0
    length = 2 * n // d
    return prescribed_descent_count(n, tuple(length * j for j in range(1, d)))


def verify():
    # Full unfiltered Stirling insertion, then independent flattening test.
    for n in range(1, 9):
        direct = exhaustive_from_original_definition(n)
        formula = block_formula(n)
        assert direct == formula, ("descent profile", n)
        for cuts, count in formula.items():
            assert prescribed_descent_count(n, cuts) == count
        print("exhaustive", n, sum(direct.values()), len(direct))
    # Original Table 1 of Buck et al. (2023) through n=10.
    table = {
        1: [1],
        2: [1, 1],
        3: [1, 5],
        4: [1, 15, 8],
        5: [1, 37, 70, 8],
        6: [1, 83, 374, 190],
        7: [1, 177, 1596, 2034, 280],
        8: [1, 367, 6012, 15260, 6720, 280],
        9: [1, 749, 20994, 93764, 88732, 15680],
        10: [1, 1515, 69842, 508538, 866796, 363132, 22400],
    }
    for n, expected in table.items():
        counts = Counter({})
        for descent_indices, count in block_formula(n).items():
            counts[len(descent_indices) + 1] += count
        assert [counts[k] for k in range(1, len(expected) + 1)] == expected
        print("published run counts", n, sum(expected))
    # Refinement not supplied by that table: equal-size run profiles.
    for n, d, want in [(3, 2, 2), (6, 3, 8), (9, 3, 243),
                       (12, 3, 5576), (8, 4, 48), (10, 5, 384)]:
        observed = equal_count_sparse(n, d)
        assert observed == want, (n, d, observed, want)
        if n <= 10:
            full = block_formula(n)
            cuts = tuple((2 * n // d) * j for j in range(1, d))
            assert full[cuts] == observed
        print("equal-length", n, d, observed)
    print("VERIFY_OK")


if __name__ == "__main__":
    verify()
