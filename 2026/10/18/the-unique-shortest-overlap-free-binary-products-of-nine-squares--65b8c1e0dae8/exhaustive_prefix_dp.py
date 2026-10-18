#!/usr/bin/env python3
"""Exact prefix-DP enumeration for overlap-free binary square products.

No third-party packages. Python 3.9+.
"""
from collections import Counter

LIMIT = 48
BLOCKS = 9


def new_overlap_at_end(word):
    """Every new overlap must end in the last appended letter."""
    n = len(word)
    for period in range(1, (n - 1) // 2 + 1):
        start = n - 2 * period - 1
        if word[start:start + period + 1] == word[start + period:n]:
            return True
    return False


def square_suffix_roots(word):
    n = len(word)
    for root_length in range(1, n // 2 + 1):
        if word[n - 2 * root_length:n - root_length] == word[n - root_length:n]:
            yield root_length


def evaluate():
    words = {"": (1,) + (0,) * BLOCKS}
    layer = [""]
    layer_totals = [(0, 1, 0)]
    for length in range(1, LIMIT + 1):
        next_layer = []
        for prefix in layer:
            for letter in "01":
                word = prefix + letter
                if new_overlap_at_end(word):
                    continue
                counts = [0] * (BLOCKS + 1)
                for root_length in square_suffix_roots(word):
                    parent_counts = words[word[:-2 * root_length]]
                    for j in range(1, BLOCKS + 1):
                        counts[j] += parent_counts[j - 1]
                words[word] = tuple(counts)
                next_layer.append(word)
        layer = next_layer
        max_squares = max((max((j for j, count in enumerate(words[word]) if count), default=0)
                           for word in layer), default=0)
        layer_totals.append((length, len(layer), max_squares))
    targets = sorted((word, words[word][BLOCKS]) for word, counts in words.items()
                     if 1 <= len(word) <= LIMIT and counts[BLOCKS] > 0)
    return words, layer_totals, targets


def paths(word, counts, blocks):
    if blocks == 0:
        if word == "":
            yield ()
        return
    for root_length in square_suffix_roots(word):
        prefix = word[:-2 * root_length]
        if counts[prefix][blocks - 1] > 0:
            for earlier in paths(prefix, counts, blocks - 1):
                yield earlier + (root_length,)


def main():
    counts, totals, targets = evaluate()
    print("METHOD prefix_dynamic_program")
    print("DOMAIN all overlap-free binary words of lengths 0 through 48")
    print("WORD_COUNTS_BY_EVEN_LENGTH", [(n, v) for n, v, _ in totals if n % 2 == 0])
    print("MAX_SQUARE_FACTORIZATION_BY_EVEN_LENGTH", [(n, k) for n, _, k in totals if n % 2 == 0])
    print("TOTAL_PREFIX_WORDS", len(counts))
    print("NINE_SQUARE_WORDS_LENGTH_LE_48", len(targets))
    for word, multiplicity in targets:
        decomps = list(paths(word, counts, BLOCKS))
        print("WITNESS", word, "length", len(word), "factorizations", multiplicity,
              "root_lengths", decomps)
        assert len(decomps) == multiplicity
        assert len(word) == 48
        assert multiplicity == 1
    assert len(targets) == 2
    assert targets[0][0] == "001001101001011010011001011001101001011010011011"
    assert targets[1][0] == "110110010110100101100110100110010110100101100100"
    assert targets[0][0][::-1] == targets[1][0]
    assert all(counts[word][9] == 0 for word in counts if len(word) < 48)
    print("PASS")


if __name__ == "__main__":
    main()
