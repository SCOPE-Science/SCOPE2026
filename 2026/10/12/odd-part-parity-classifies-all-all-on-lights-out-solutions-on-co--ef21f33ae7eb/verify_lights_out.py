#!/usr/bin/env python3
"""Independent finite checks for parity Lights Out on multipartite graphs.

Standard two-state rule: pressing a vertex toggles its closed neighborhood.
The search exhausts all press masks for all ordered part-size profiles of
length 1 through 5, with each size in {1, 2, 3}. No graph-solving package is used.
"""
from collections import Counter
from itertools import product


def rank_binary(rows, width):
    rows = list(rows)
    pivot = 0
    for bit in range(width):
        candidate = next((j for j in range(pivot, len(rows))
                          if (rows[j] >> bit) & 1), None)
        if candidate is None:
            continue
        rows[pivot], rows[candidate] = rows[candidate], rows[pivot]
        for j in range(len(rows)):
            if j != pivot and ((rows[j] >> bit) & 1):
                rows[j] ^= rows[pivot]
        pivot += 1
    return pivot


def expected_solutions(parts):
    odd = [a for a in parts if a % 2]
    if not odd:
        return Counter({sum(parts): 1})
    result = Counter()
    for sel in range(1 << len(odd)):
        if sel.bit_count() % 2:
            result[sum(a for k, a in enumerate(odd) if (sel >> k) & 1)] += 1
    return result


def verify_profile(parts):
    n = sum(parts)
    indices = []
    for k, size in enumerate(parts):
        indices.extend([k] * size)
    toggle = []
    rows = []
    for i in range(n):
        mask = sum(1 << j for j in range(n)
                   if i == j or indices[i] != indices[j])
        toggle.append(mask)
        rows.append(mask)
    want = expected_solutions(parts)
    got = Counter()
    cur = 0
    last_gray = 0
    target = (1 << n) - 1
    # Gray-code traversal updates the actual resulting light configuration.
    for mask in range(1 << n):
        gray = mask ^ (mask >> 1)
        if mask:
            change = gray ^ last_gray
            idx = change.bit_length() - 1
            cur ^= toggle[idx]
        last_gray = gray
        if cur == target:
            got[gray.bit_count()] += 1
    assert got == want, (parts, want, got)
    odd_count = sum(a % 2 for a in parts)
    expected_nullity = max(0, odd_count - 1)
    assert n - rank_binary(rows, n) == expected_nullity, parts
    return 1 << n


def main():
    count = total = maximum = 0
    for r in range(1, 6):
        for sizes in product(range(1, 4), repeat=r):
            total += verify_profile(sizes)
            maximum = max(maximum, sum(sizes))
            count += 1
    print('ordered_part_profiles:', count)
    print('tested_press_subsets:', total)
    print('maximum_order:', maximum)
    print('weight_enumerator_and_binary_nullity: PASS')


if __name__ == '__main__':
    main()
