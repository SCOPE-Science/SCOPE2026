#!/usr/bin/env python3
"""Independent exact counting routes for CCA synchronization on rook graphs.

Uses only Python's standard library; no source datasets are required.
"""
from math import comb


def covered_binary_rectangles(rows: int, cols: int) -> int:
    return sum(
        (-1) ** (i + j) * comb(rows, i) * comb(cols, j)
        * (1 << ((rows - i) * (cols - j)))
        for i in range(rows + 1) for j in range(cols + 1)
    )


def inclusion_exclusion_count(m: int, n: int) -> tuple[int, int]:
    exceptional = sum(
        comb(m, r) * comb(n, u) * covered_binary_rectangles(r, u)
        * ((1 << ((m-r)*(n-u))) - 1)
        for r in range(1, m) for u in range(1, n)
    )
    return 3 * ((1 << (m*n)) - 1 + exceptional), exceptional


def column_dp_count(m: int, n: int) -> tuple[int, int]:
    # Masks tell which rows have ever encountered 0 or 2, respectively.
    candidates = []
    for code in range(3**m):
        z = t = 0
        q = code
        for i in range(m):
            value = q % 3
            q //= 3
            if value == 0:
                z |= 1 << i
            if value == 2:
                t |= 1 << i
        if not (z and t):
            candidates.append((z, t))
    states = {(0, 0): 1}
    for _ in range(n):
        new = {}
        for (z, t), count in states.items():
            for dz, dt in candidates:
                if (z & dt) or (t & dz):
                    continue
                key = (z | dz, t | dt)
                new[key] = new.get(key, 0) + count
        states = new
    exceptional = sum(count for (z, t), count in states.items() if z and t)
    return 3 * ((1 << (m*n)) - 1 + exceptional), exceptional


def main():
    for m, n in ((2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                 (3, 3), (3, 4), (3, 5), (4, 4), (4, 5),
                 (5, 5), (6, 6)):
        a = inclusion_exclusion_count(m, n)
        b = column_dp_count(m, n)
        assert a == b, (m, n, a, b)
        print(f'm={m} n={n} sync={a[0]} exceptional={a[1]} verified=YES')
    print('ALL_COUNT_CHECKS_PASS')


if __name__ == '__main__':
    main()
