#!/usr/bin/env python3
"""Exact exhaustive verification of length-eight composition-spectrum fibers."""
from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial, prod

N = 8


def integer_partitions(rem, ceiling=None):
    if ceiling is None:
        ceiling = rem
    if not rem:
        yield ()
    else:
        for first in range(min(ceiling, rem), 0, -1):
            for tail in integer_partitions(rem - first, first):
                yield (first,) + tail


def multiset_words(multiplicities, prefix=()):
    if not any(multiplicities):
        yield prefix
        return
    for letter, available in enumerate(multiplicities):
        if available:
            rest = list(multiplicities)
            rest[letter] -= 1
            yield from multiset_words(tuple(rest), prefix + (letter,))


def spectrum(word, alphabet_size):
    """The exact multiset of all 36 nonempty substring Parikh vectors."""
    accum = [[0] * alphabet_size]
    for symbol in word:
        row = accum[-1].copy()
        row[symbol] += 1
        accum.append(row)
    return tuple(sorted(
        tuple(accum[j][letter] - accum[i][letter]
              for letter in range(alphabet_size))
        for i in range(len(word)) for j in range(i + 1, len(word) + 1)
    ))


def predicted_fiber(w):
    predicted = {w, w[::-1]}
    if w[0] == w[3] == w[6] and w[1] == w[4] == w[7]:
        swapped = w[:2] + (w[5],) + w[3:5] + (w[2],) + w[6:8]
        predicted |= {swapped, swapped[::-1]}
    return predicted


def verify_earlier_lengths():
    checked = 0
    for n in range(1, N):
        for counts in integer_partitions(n):
            fibers = defaultdict(set)
            for w in multiset_words(counts):
                fibers[spectrum(w, len(counts))].add(w)
                checked += 1
            for fiber in fibers.values():
                w = next(iter(fiber))
                assert fiber == {w, w[::-1]}, (n, counts, fiber)
    print(f"lengths 1..7: {checked} canonical words; every fiber consists only of reversals")


def verify_partition_reduction():
    patterns = tuple(integer_partitions(N))
    assert len(patterns) == 22
    checked = 0
    four_types = Counter()
    for counts in patterns:
        fibers = defaultdict(set)
        for w in multiset_words(counts):
            fibers[spectrum(w, len(counts))].add(w)
            checked += 1
        expected_words = factorial(N) // prod(factorial(x) for x in counts)
        assert sum(map(len, fibers.values())) == expected_words
        for fiber in fibers.values():
            exemplar = next(iter(fiber))
            predicted = predicted_fiber(exemplar)
            assert fiber == predicted, (counts, fiber, predicted)
            if len(fiber) == 4:
                four_types[counts] += 1
            assert len(fiber) in (1, 2, 4)
    assert checked == 95503, checked
    assert four_types == Counter({(4, 4): 1, (4, 3, 1): 1,
                                  (3, 3, 1, 1): 1}), four_types
    print(f"22 multiplicity partitions; {checked} canonical words; all fibers match reversal/interleaving prediction")
    print(f"four-word fiber multiplicity types: {dict(sorted(four_types.items()))}")


def verify_direct_alphabets():
    for q in (2, 3, 4):
        fibers = defaultdict(int)
        for w in product(range(q), repeat=N):
            fibers[spectrum(w, q)] += 1
        counts = Counter(fibers.values())
        four = comb(q, 2) ** 2
        single = q ** 4
        double = (q ** 8 - single - 4 * four) // 2
        assert counts == Counter({1: single, 2: double, 4: four}), (q, counts)
        assert len(fibers) == (q ** 8 + q ** 4) // 2 - four
        print(f"q={q}: {q ** 8} words, {len(fibers)} observations, fiber histogram {dict(sorted(counts.items()))}")


if __name__ == "__main__":
    verify_earlier_lengths()
    verify_partition_reduction()
    verify_direct_alphabets()
    print("VERIFY_OK")
