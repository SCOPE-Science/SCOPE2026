#!/usr/bin/env python3
import math
from itertools import combinations

def rows_from_mask(m, n, mask):
    return [{j for j in range(n) if (mask >> (i*n+j)) & 1} for i in range(m)]

def total_expansive(m, n, mask):
    rows = rows_from_mask(m, n, mask)
    if any(not row for row in rows):
        return False
    for i in range(m):
        for j in range(i+1, m):
            for u in rows[i]:
                if not any(u < v for v in rows[j]):
                    return False
            for v in rows[j]:
                if not any(u < v for u in rows[i]):
                    return False
    return True

def endpoint_characterization(m, n, mask):
    rows = rows_from_mask(m, n, mask)
    if any(not row for row in rows):
        return False
    mins = [min(row) for row in rows]
    maxs = [max(row) for row in rows]
    return all(mins[i] < mins[i+1] and maxs[i] < maxs[i+1] for i in range(m-1))

def endpoint_count(m, n):
    if m > n:
        return 0
    total = 0
    seqs = list(combinations(range(n), m))
    for a in seqs:
        for b in seqs:
            if all(a[i] <= b[i] for i in range(m)):
                total += 2 ** sum(max(b[i]-a[i]-1, 0) for i in range(m))
    return total

for m in range(1, 5):
    for n in range(1, 5):
        masks = []
        for mask in range(1 << (m*n)):
            direct = total_expansive(m, n, mask)
            endpoint = endpoint_characterization(m, n, mask)
            assert direct == endpoint, (m, n, mask)
            if direct:
                masks.append(mask)

        assert len(masks) == endpoint_count(m, n)
        assert bool(masks) == (m <= n)

        if masks:
            sizes = [mask.bit_count() for mask in masks]
            assert min(sizes) == m
            assert max(sizes) == m * (n-m+1)
            assert sum(size == m for size in sizes) == math.comb(n, m)

            maxima = [mask for mask in masks if mask.bit_count() == m*(n-m+1)]
            assert len(maxima) == 1
            expected = 0
            for i in range(m):
                for j in range(i, i+n-m+1):
                    expected |= 1 << (i*n+j)
            assert maxima[0] == expected

print("VERIFY_OK")
