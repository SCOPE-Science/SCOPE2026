#!/usr/bin/env python3
"""Independent finite checks of the ruler-word abelian-border rigidity theorem.

Uses direct Parikh-prefix comparison (not the valuation border formula)
and canonical first-occurrence label search for all constrained prefixes.
Only the proof in RESULT.md covers all positive lengths.
"""
from collections import Counter


def valuation(i):
    assert i >= 1
    return (i & -i).bit_length() - 1


def direct_array(word):
    """Compute longest proper abelian-border length by direct equality of multisets."""
    ans = []
    for m in range(1, len(word) + 1):
        prefix = Counter()
        suffix = Counter()
        longest = 0
        for j in range(1, m):
            prefix[word[j-1]] += 1
            suffix[word[m-j]] += 1
            if prefix == suffix:
                longest = j
        ans.append(longest)
    return tuple(ans)


def enumerated_representatives(n):
    """Enumerate all canonical RGS words whose first n borders equal ruler's."""
    target = tuple(i-(i & -i) for i in range(1, n+1))
    word = [0]
    counts = [Counter(), Counter({0: 1})]
    winners = []
    visited = 0

    def descend(mx):
        nonlocal visited
        m = len(word) + 1
        if m > n:
            winners.append(tuple(word))
            return
        for symbol in range(mx + 2):
            visited += 1
            curr = counts[-1].copy()
            curr[symbol] += 1
            counts.append(curr)
            shortest = None
            for j in range(1, m):
                if counts[j] + counts[m-j] == curr:
                    shortest = j
                    break
            border = 0 if shortest is None else m - shortest
            if border == target[m-1]:
                word.append(symbol)
                descend(max(mx, symbol))
                word.pop()
            counts.pop()

    if n == 1:
        return [(0,)], 1
    descend(0)
    return winners, visited


def main():
    for n in (1, 2, 3, 4, 5, 6, 7, 8, 16, 32, 64, 128, 256, 512):
        w = tuple(valuation(i) for i in range(1, n+1))
        got = direct_array(w)
        expect = tuple(i - (i & -i) for i in range(1, n+1))
        assert got == expect, (n, got, expect)
    checked = 0
    for n in range(1, 17):
        words, visited = enumerated_representatives(n)
        ruler = tuple(valuation(i) for i in range(1, n+1))
        assert words == [ruler], (n, words)
        checked += visited
    print('RULER_ABELIAN_BORDER_CHECKS_PASS',
          'direct_lengths=1,2,3,4,5,6,7,8,16,32,64,128,256,512',
          'canonical_lengths=1..16',
          'unique_representative_each=true',
          'search_nodes=' + str(checked))

if __name__ == '__main__':
    main()
