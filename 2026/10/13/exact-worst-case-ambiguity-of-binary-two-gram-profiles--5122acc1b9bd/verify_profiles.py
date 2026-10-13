"""Independently check run-composition counts, maximizing profiles, and partition sizes.
This checks all four-count vectors at lengths 3 through 80, without generating words.
"""
from math import comb


def fiber_formula(a, c, d, b):
    m = a + b + c + d
    if c == d == 0:
        return 1 if (a == m and b == 0) or (b == m and a == 0) else 0
    if c == d and c >= 1:
        j = c
        return m * comb(a + j - 1, j - 1) * comb(b + j - 1, j - 1) // j
    if abs(c - d) == 1:
        j = max(c, d)
        return comb(a + j - 1, j - 1) * comb(b + j - 1, j - 1)
    return 0


def predicted(n):
    m = n - 1
    k = (m + 3) // 4
    top = m * comb(m // 2 - 1, k - 1) * comb((m + 1) // 2 - 1, k - 1) // k
    set_of_modes = set()
    for j in (k, k - 1) if m % 4 == 1 else (k,):
        if j <= 0:
            continue
        for a in range(m - 2*j + 1):
            b = m - 2*j - a
            if j == 1 or abs(a-b) <= 1:
                set_of_modes.add((a, j, j, b))
    return top, set_of_modes


for n in range(3, 81):
    m = n - 1
    max_count = 0
    modes = set()
    total = 0
    for a in range(m + 1):
        for c in range(m - a + 1):
            for d in range(m - a - c + 1):
                b = m - a - c - d
                v = fiber_formula(a, c, d, b)
                total += v
                if v > max_count:
                    modes = {(a, c, d, b)}
                    max_count = v
                elif v == max_count:
                    modes.add((a, c, d, b))
    target, target_modes = predicted(n)
    assert (max_count, modes) == (target, target_modes), n
    assert total == 1 << n, (n, total, 1 << n)
    if n in [3, 4, 5, 6, 7, 9, 18, 33, 64, 80]:
        print(f'n={n}, maximum={max_count}, modal_profiles={len(modes)}, total={total}')
print('PASS: all feasible and infeasible profiles, n=3..80')
