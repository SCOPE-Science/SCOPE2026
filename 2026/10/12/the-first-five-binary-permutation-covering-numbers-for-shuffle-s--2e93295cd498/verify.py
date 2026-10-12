#!/usr/bin/env python3
"""Exact exhaustive certificate for small binary permutation-covering numbers."""
from itertools import combinations, permutations, product

OBSTRUCTION_6 = (
    "000000111111",
    "011111100000",
    "000011111100",
    "000111111000",
    "001111100001",
    "000111110001",
    "001110000001",
    "000000111001",
    "011110000110",
)


def even_words(n):
    return ["".join(t) for t in product("01", repeat=2*n)
            if t.count("1") % 2 == 0]


def direct_cover(word, permutation):
    """Directly test all balanced ordered partitions of positions."""
    n = len(permutation)
    for chosen in combinations(range(2*n), n):
        selected = set(chosen)
        u = [word[i] for i in chosen]
        v = [word[i] for i in range(2*n) if i not in selected]
        if all(u[permutation[i]] == v[i] for i in range(n)):
            return True
    return False


def neighbor_masks(n, words):
    """Bit i records membership of permutation i in a word's neighborhood."""
    ps = list(permutations(range(n)))
    blocks = list(product("01", repeat=n))
    by_pair = {}
    for u in blocks:
        for v in blocks:
            mask = 0
            for index, p in enumerate(ps):
                if all(u[p[i]] == v[i] for i in range(n)):
                    mask |= 1 << index
            by_pair[u, v] = mask
    word_masks = []
    for word in words:
        neighbors = 0
        for chosen in combinations(range(2*n), n):
            selected = set(chosen)
            u = tuple(word[i] for i in chosen)
            v = tuple(word[i] for i in range(2*n) if i not in selected)
            neighbors |= by_pair[u, v]
        word_masks.append(neighbors)
    assert all(word_masks)
    return ps, word_masks


def signatures(word_masks, permutation_count):
    return sorted({sum(1 << i for i, mask in enumerate(word_masks)
                       if mask >> j & 1)
                   for j in range(permutation_count)})


def assert_no_three_cover(signatures_9):
    """Nine-bit exhaustive subset DP tests all choices of three permutations."""
    target = (1 << 9) - 1
    upward = [False] * (1 << 9)
    for value in signatures_9:
        upward[value] = True
    for digit in range(9):
        for subset in range(1 << 9):
            if (subset >> digit) & 1 == 0:
                upward[subset] |= upward[subset | (1 << digit)]
    # upward[subset] means some permutation covers every bit of subset.
    assert not any(upward[target & ~(a | b)]
                   for a in signatures_9 for b in signatures_9)


def main():
    maxima = {2: (6, 8), 3: (28, 32), 4: (108, 126), 5: (434, 496)}
    for n in range(2, 7):
        all_even = even_words(n)
        assert len(all_even) == 1 << (2*n-1)
        selected = OBSTRUCTION_6 if n == 6 else all_even
        assert len(set(selected)) == len(selected)
        assert all(len(word) == 2*n and word.count("1") % 2 == 0
                   for word in selected)
        ps, neighbors = neighbor_masks(n, selected)
        sig = signatures(neighbors, len(ps))
        best_single = max(value.bit_count() for value in sig)
        if n < 6:
            best_pair = max((a | b).bit_count() for a in sig for b in sig)
            assert (best_single, best_pair) == maxima[n]
            if n < 4:
                assert best_single < len(selected)  # one permutation fails
            else:
                assert best_pair < len(selected)   # two permutations fail
        else:
            assert len(selected) == 9 and len(sig) == 73
            assert best_single == 5
            assert_no_three_cover(sig)
        rotations = [tuple((i + k) % n for i in range(n))
                     for k in range(n//2 + 1)]
        assert all(any(direct_cover(word, p) for p in rotations)
                   for word in all_even)
    print("VERIFY_OK m2(2..6)=2,2,3,3,4 upper-even=8,32,128,512,2048 "
          "n6_obstructions=9 n6_signatures=73 max_pair_n4=126 max_pair_n5=496")


if __name__ == "__main__":
    main()
