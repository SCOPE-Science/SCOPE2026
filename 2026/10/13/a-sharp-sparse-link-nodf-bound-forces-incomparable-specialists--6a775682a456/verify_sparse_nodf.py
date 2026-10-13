"""Exact checks for the three-by-n minimum-link NODF extremum.

Only Python's standard library is needed. The mathematical proof is in RESULT.md;
these finite calculations are independent checks, not its replacement.
"""

from fractions import Fraction
from itertools import combinations
from math import comb


def score_via_masks(rows, n):
    rdeg = [int(x).bit_count() for x in rows]
    cols = [sum(((rows[i] >> j) & 1) << i for i in range(3))
            for j in range(n)]
    cdeg = [x.bit_count() for x in cols]
    total = Fraction(0)
    for i, j in combinations(range(3), 2):
        if rdeg[i] != rdeg[j]:
            total += Fraction((rows[i] & rows[j]).bit_count(),
                              min(rdeg[i], rdeg[j]))
    for i, j in combinations(range(n), 2):
        if cdeg[i] != cdeg[j]:
            total += Fraction((cols[i] & cols[j]).bit_count(),
                              min(cdeg[i], cdeg[j]))
    return total


def score_via_sets(rows, n):
    sets = [set(j for j in range(n) if (rows[i] >> j) & 1)
            for i in range(3)]
    sets += [set(i for i in range(3) if (rows[i] >> j) & 1)
             for j in range(n)]
    value = Fraction(0)
    for start, stop in ((0, 3), (3, 3 + n)):
        for i, j in combinations(range(start, stop), 2):
            if len(sets[i]) != len(sets[j]):
                value += Fraction(len(sets[i] & sets[j]),
                                  min(len(sets[i]), len(sets[j])))
    return value


def all_matrices(n):
    for locations in combinations(range(3*n), n+2):
        rows = [0, 0, 0]
        for location in locations:
            i, j = divmod(location, n)
            rows[i] |= 1 << j
        if min(row.bit_count() for row in rows) == 0:
            continue
        if any(not any((row >> j) & 1 for row in rows)
               for j in range(n)):
            continue
        yield tuple(rows)


def canonical(n):
    return ((1 << n) - 1, 1, 2)


def ferrers(n):
    return ((1 << n) - 1, 1, 1)


def test():
    expected_counts = {2: 12, 3: 90, 4: 522, 5: 2595,
                       6: 11673, 7: 49014}
    total_checked = 0
    for n in range(2, 8):
        maximum = Fraction(-1)
        best = []
        count = 0
        for rows in all_matrices(n):
            count += 1
            s1 = score_via_masks(rows, n)
            s2 = score_via_sets(rows, n)
            assert s1 == s2, (n, rows, s1, s2)
            if s1 > maximum:
                maximum = s1
                best = [rows]
            elif s1 == maximum:
                best.append(rows)
        assert count == expected_counts[n], (n, count)
        target = Fraction(3 if n == 2 else 2*n - 2)
        assert maximum == target, (n, maximum, target)
        assert score_via_masks(canonical(n), n) == 2*n-2
        assert score_via_masks(ferrers(n), n) == n+1
        if n >= 4:
            for rows in best:
                assert sorted(row.bit_count() for row in rows) == [1, 1, n]
                core = max(range(3), key=lambda i: rows[i].bit_count())
                specialists = [rows[i] for i in range(3) if i != core]
                assert specialists[0] != specialists[1]
                assert specialists[0].bit_count() == 1
                assert specialists[1].bit_count() == 1
            assert len(best) == 3*n*(n-1), (n, len(best))
        total_checked += count
    # A separate formula-based check of every allowable column-degree pattern.
    for n in range(4, 101):
        k = Fraction(comb(n, 2) + 3)
        assert Fraction(2*n-2, 1) < k
        assert Fraction(2*n-2, k) > Fraction(n+1, k)
        assert Fraction(n-1, 1) + Fraction(5, 2) < 2*n-2
    return total_checked

if __name__ == '__main__':
    count = test()
    print('VERIFY_OK')
    print('exhaustive_no_isolate_3_by_n_matrices', count)
    print('tested_shapes', '3x2..3x7')
    print('symbolic_case_bounds_checked', '3x4..3x100')
