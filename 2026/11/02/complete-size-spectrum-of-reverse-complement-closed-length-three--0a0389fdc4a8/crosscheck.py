#!/usr/bin/env python3
"""Independent exhaustive enumeration of all closed, non-overlapping codebooks for q <= 6."""
from collections import Counter
from itertools import product


def reverse_complement(word):
    return tuple(x + 1 if x % 2 == 0 else x - 1 for x in reversed(word))


def compatible(w, v):
    for span in (1, 2):
        if w[-span:] == v[:span] or v[-span:] == w[:span]:
            return False
    return True


def exact_census(q):
    # Each codebook is a clique in the compatibility graph of RC word pairs.
    seen = set()
    vertices = []
    for word in product(range(q), repeat=3):
        if word in seen:
            continue
        partner = reverse_complement(word)
        seen.update((word, partner))
        if compatible(word, word) and compatible(partner, partner) and compatible(word, partner):
            vertices.append((word, partner))
    n = len(vertices)
    adjacency = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if all(compatible(a, b) for a in vertices[i] for b in vertices[j]):
                adjacency[i] |= 1 << j
    counts = Counter({0: 1})

    def visit(available, picked):
        # The forward-only adjacency records each clique exactly once.
        while available:
            bit = available & -available
            i = bit.bit_length()-1
            available ^= bit
            counts[picked+1] += 1
            visit(available & adjacency[i], picked+1)

    visit((1 << n)-1, 0)
    return [counts.get(j, 0) for j in range(1 + max(counts))]


def main():
    expected = {
        2: [1],
        4: [1, 12, 8],
        6: [1, 60, 726, 3072, 6276, 7344, 5256, 2304, 576, 64],
    }
    for q, histogram in expected.items():
        observed = exact_census(q)
        assert observed == histogram, (q, observed)
        assert sum(observed) == {2: 1, 4: 21, 6: 25679}[q]
    print('CROSSCHECK_OK')


if __name__ == '__main__':
    main()
