#!/usr/bin/env python3
"""Independent exhaustive finite checks of five-supported binary lunar composites.

The formulas for arbitrary degree are proven separately; these checks do
not replace the proof. Requires Python 3 only.
"""
from math import comb
from itertools import combinations


def predicted_composites(m: int) -> int:
    assert m >= 4
    return (2 * ((m - 1) // 2) + (m // 2 - 1 if m % 2 == 0 else 0)
            - 2 * (m % 3 == 0) - 2 * (m % 4 == 0))


def brute_from_two_by_three(m: int) -> set[tuple[int, ...]]:
    composites = set()
    for x in range(1, m + 1):
        for y in range(1, m):
            for z in range(y + 1, m + 1):
                s = {a + b for a in (0, x) for b in (0, y, z)}
                if len(s) == 5 and max(s) == m:
                    composites.add(tuple(sorted(s)))
    return composites


def brute_all_factor_shapes(m: int) -> set[tuple[int, ...]]:
    composites = set()
    factor_sets = []
    for size in (2, 3, 4):
        for chosen in combinations(range(1, m + 1), size - 1):
            factor_sets.append((0,) + chosen)
    for a in factor_sets:
        for b in factor_sets:
            if max(a) + max(b) != m:
                continue
            sums = {i + j for i in a for j in b}
            if len(sums) == 5:
                composites.add(tuple(sorted(sums)))
    return composites


def main():
    for m in range(4, 131):
        explicit = brute_from_two_by_three(m)
        assert len(explicit) == predicted_composites(m), (m, len(explicit), predicted_composites(m))
        assert predicted_composites(m) <= comb(m - 1, 3)
        if m <= 14:
            unrestricted = brute_all_factor_shapes(m)
            assert explicit == unrestricted, (m, explicit.symmetric_difference(unrestricted))
    print('VERIFY_OK: 127 degrees m=4..130; independent 2-by-3 enumeration; all factor shapes m<=14; closed counts.')


if __name__ == '__main__':
    main()
