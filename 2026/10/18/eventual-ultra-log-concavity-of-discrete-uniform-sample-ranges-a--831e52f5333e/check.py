#!/usr/bin/env python3
"""Exact independent checks for finite-uniform sample-range ULC assertions.
No external data, packages, or floating-point arithmetic are used.
"""
from collections import defaultdict


def formula_counts(m, n):
    assert m >= 1 and n >= 1
    return [m + 1] + [(m + 1 - r) * ((r + 1)**n - 2 * r**n + (r - 1)**n)
                      for r in range(1, m + 1)]


def dynamic_counts(m, n):
    # Independent enumeration of endpoint states, not the closed-form formula.
    state = {(x, x): 1 for x in range(m + 1)}
    for _ in range(2, n + 1):
        newer = defaultdict(int)
        for (lo, hi), count in state.items():
            for x in range(m + 1):
                newer[(min(lo, x), max(hi, x))] += count
        state = newer
    counts = [0] * (m + 1)
    for (lo, hi), count in state.items():
        counts[hi - lo] += count
    return counts


def deficits(a):
    return [k * a[k]**2 - (k + 1) * a[k - 1] * a[k + 1]
            for k in range(1, len(a) - 1)]


def main():
    # Every possible ULC interior comparison for all finite cases not
    # covered by the analytic n >= m*m theorem, for the six-sided die.
    for n in range(2, 25):
        closed = formula_counts(5, n)
        independent = dynamic_counts(5, n)
        assert closed == independent
        assert sum(closed) == 6**n
        dd = deficits(closed)
        assert len(dd) == 4
        if n in (2, 3):
            assert dd[1] < 0  # k=2 exact counterexample
        else:
            assert all(value > 0 for value in dd)
        if n in (2, 3, 4, 24):
            print(f'n={n}, k=2 defect={dd[1]}, all-signs={[x>0 for x in dd]}')
    # Ordinary support/trial stress-tests (not an infinite proof).
    tests = 0
    for m in range(2, 19):
        for n in range(max(m*m, 4), max(m*m, 4) + 4):
            a = formula_counts(m, n)
            assert sum(a) == (m + 1)**n
            assert all(d > 0 for d in deficits(a))
            tests += 1
    print('PASS: 23 finite die trial sizes; 23 independent formula/DP comparisons; 92 integer ULC comparisons;'
          ' 68 supplemental large-trial checks; the infinite range uses the paper proof.')


if __name__ == '__main__':
    main()
