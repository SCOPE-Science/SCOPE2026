#!/usr/bin/env python3
"""Independent nine-square enumeration by square-block expansion.

No third-party packages. Python 3.9+.
"""
from collections import defaultdict

TARGET_SQUARES = 9
MAX_LENGTH = 48


def has_overlap(word):
    """Check all start positions and all periods of an axaxa factor."""
    n = len(word)
    for p in range(1, (n - 1) // 2 + 1):
        for start in range(n - 2 * p):
            if all(word[start + k] == word[start + p + k] for k in range(p + 1)):
                return True
    return False


def square_blocks():
    # In a 9-square word of length <=48, eight other blocks use >=16 letters,
    # hence each square has length <=32 and root length <=16.
    roots = [""]
    good = set()
    for root_length in range(1, 17):
        roots = [w + c for w in roots for c in "01" if not has_overlap(w + c)]
        for root in roots:
            square = root + root
            if not has_overlap(square):
                good.add(square)
    return sorted(good, key=lambda w: (len(w), w))


def main():
    blocks = square_blocks()
    count_by_length = {n: sum(len(w) == n for w in blocks)
                       for n in sorted({len(w) for w in blocks})}
    print("METHOD independent_square_block_search")
    print("SQUARE_BLOCK_COUNTS", count_by_length)
    print("TOTAL_ALLOWED_BLOCKS", len(blocks))
    frontier = {"": 1}
    for k in range(1, TARGET_SQUARES + 1):
        next_frontier = defaultdict(int)
        for prefix, multiplicity in frontier.items():
            for square in blocks:
                length = len(prefix) + len(square)
                if length + 2 * (TARGET_SQUARES - k) > MAX_LENGTH:
                    break
                candidate = prefix + square
                if not has_overlap(candidate):
                    next_frontier[candidate] += multiplicity
        frontier = dict(next_frontier)
        shortest = min((len(w) for w in frontier), default=None)
        print("DEPTH", k, "WORDS", len(frontier), "FACTORIZATIONS", sum(frontier.values()),
              "SHORTEST", shortest)
    print("FINAL_WORDS", [(w, frontier[w]) for w in sorted(frontier)])
    assert len(frontier) == 2
    assert list(sorted(frontier.values())) == [1, 1]
    assert set(map(len, frontier)) == {48}
    assert sorted(frontier) == [
        "001001101001011010011001011001101001011010011011",
        "110110010110100101100110100110010110100101100100",
    ]
    print("PASS")


if __name__ == "__main__":
    main()
