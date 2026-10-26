#!/usr/bin/env python3
"""Direct checks of the shortest-absent-subsequence generating function.

The proof in RESULT.md applies to all word lengths; this script independently
enumerates bounded cases and checks algebraic recurrences.
"""
from itertools import product
from collections import defaultdict
from math import comb


def arch_index(word):
    seen = set()
    k = 0
    for letter in word:
        seen.add(letter)
        if len(seen) == 2:
            k += 1
            seen.clear()
    return k


def subsequences_of_length(word, ell):
    levels = [set() for _ in range(ell+1)]
    levels[0].add("")
    for letter in word:
        for j in range(ell, 0, -1):
            levels[j].update(s + letter for s in levels[j-1])
    return levels[ell]


def absent_vector(word):
    k = arch_index(word)
    present = subsequences_of_length(word, k+1)
    missing = {"".join(bits) for bits in product("01", repeat=k+1)} - present
    return (sum(s[0] == "0" for s in missing),
            sum(s[0] == "1" for s in missing))


def exact_coefficient(n,k):
    if k > n//2:
        return 0
    return 2*sum((-1)**j * comb(k,j) * 3**(k-j) * comb(n-k-j,k)
                 for j in range(min(k,n-2*k)+1))


def main():
    # All source words, independently enumerating all absent subsequences.
    hist = defaultdict(int)
    total_words = 0
    vectors = {}
    for n in range(15):
        for bits in product("01", repeat=n):
            w = "".join(bits)
            k = arch_index(w)
            vec = absent_vector(w)
            hist[n,k] += sum(vec)
            if n <= 12:
                vectors[w] = vec
            total_words += 1
        for k in range(n//2+1):
            expected = exact_coefficient(n,k)
            assert hist[n,k] == expected, (n,k,hist[n,k],expected)

    # Test every one-arch transfer directly, against independently computed SAS sets.
    checked_transfers = 0
    for w, observed in vectors.items():
        if arch_index(w) == 0:
            continue
        head = w[0]
        j = next(i for i,c in enumerate(w) if c != head)
        m = j
        suffix = w[j+1:]
        a,b = vectors[suffix]
        if head == "0":
            predicted = (a if m == 1 else 0, a+b)
        else:
            predicted = (a+b, b if m == 1 else 0)
        assert observed == predicted, (w, observed, predicted)
        checked_transfers += 1

    # Scalar recurrence derived by a separate coefficient calculation.
    totals = [sum(exact_coefficient(n,k) for k in range(n//2+1)) for n in range(61)]
    assert totals[:3] == [2,2,8]
    for n in range(58):
        assert totals[n+3] == totals[n+2] + 3*totals[n+1] - totals[n]
    assert totals[:17] == [2,2,8,12,34,62,152,304,698,1458,3248,
                           6924,15210,32734,71440,154432,336018]
    print(f"VERIFY_OK complete_words={total_words} max_length=14 "
          f"one_arch_transfers={checked_transfers} bivariate_cells={sum(n//2+1 for n in range(15))} "
          "scalar_recurrence_through=60")


if __name__ == "__main__":
    main()
