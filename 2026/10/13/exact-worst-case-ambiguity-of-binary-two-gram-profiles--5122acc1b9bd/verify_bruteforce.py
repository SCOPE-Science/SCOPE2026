"""Exhaustively enumerate all binary words for length 3 through 18.
This verifier uses direct bit extraction and accumulation, not the run formulas.
"""
from collections import defaultdict
from math import comb


def expected(n):
    m = n - 1
    j = (m + 3) // 4
    return m * comb(m // 2 - 1, j - 1) * comb((m + 1) // 2 - 1, j - 1) // j


def theoretical_modes(n):
    m = n - 1
    j = (m + 3) // 4
    candidates = {j}
    if m % 4 == 1:
        candidates.add(j - 1)
    result = set()
    for t in candidates:
        if t <= 0:
            continue
        total_loops = m - 2 * t
        for a in range(total_loops + 1):
            b = total_loops - a
            if t == 1 or abs(a - b) <= 1:
                result.add((a, t, t, b))
    return result


for n in range(3, 19):
    fibers = defaultdict(int)
    for word_int in range(1 << n):
        # Bits ordered left to right, with the leftmost in position n-1.
        bits = [(word_int >> i) & 1 for i in range(n - 1, -1, -1)]
        vec = [0, 0, 0, 0]
        for t in range(n - 1):
            vec[2 * bits[t] + bits[t + 1]] += 1
        fibers[tuple(vec)] += 1
    top = max(fibers.values())
    modes = {profile for profile, count in fibers.items() if count == top}
    assert top == expected(n), (n, top, expected(n))
    assert modes == theoretical_modes(n), (n, modes, theoretical_modes(n))
    assert sum(fibers.values()) == 2**n
    print(f'n={n}, maximum={top}, modes={len(modes)}')
print('PASS: direct word enumeration, n=3..18')
