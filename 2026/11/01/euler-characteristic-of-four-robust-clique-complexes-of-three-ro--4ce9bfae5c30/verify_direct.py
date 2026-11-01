#!/usr/bin/env python3
"""Independent brute-force face enumeration for short rectangular grids."""
from functools import lru_cache
from math import comb


def direct_euler(width):
    rows = 3
    size = rows * width
    adj = [0] * size
    for r in range(rows):
        for c in range(width):
            u = r*width + c
            if r + 1 < rows:
                v = (r+1)*width + c
                adj[u] |= 1 << v
                adj[v] |= 1 << u
            if c + 1 < width:
                v = r*width + c + 1
                adj[u] |= 1 << v
                adj[v] |= 1 << u

    @lru_cache(None)
    def independence_number(mask):
        if not mask:
            return 0
        one = mask & -mask
        vertex = one.bit_length() - 1
        without = mask ^ one
        return max(independence_number(without),
                   1 + independence_number(without & ~adj[vertex]))

    signed_count = 0
    counts = [0] * (size + 1)
    for subset in range(1 << size):
        if independence_number(subset) < 4:
            cardinality = subset.bit_count()
            counts[cardinality] += 1
            signed_count += -1 if cardinality & 1 else 1
    return signed_count, counts


def main():
    for width in range(2, 7):
        chi, counts = direct_euler(width)
        predicted = comb(2*width-2, 3) if width >= 3 else 0
        assert chi == predicted, (width, chi, predicted)
        print(f'PASS: 3x{width}; signed face count = {chi}; faces = {sum(counts)}')
    print('PASS: independent direct vertex-subset computation for widths 2..6')


if __name__ == '__main__':
    main()
