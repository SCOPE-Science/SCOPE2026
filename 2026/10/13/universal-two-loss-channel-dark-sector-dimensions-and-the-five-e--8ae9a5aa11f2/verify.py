"""Reproducibility checks for the two-collective-loss dark-sector dimension theorem.
Standard library only. Run with: python3 verify.py
This finite checker corroborates, but does not replace, the all-size proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
from random import Random


def exact_rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    ncols = len(a[0])
    pivot = 0
    for col in range(ncols):
        k = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        base = a[pivot][col]
        for j in range(col, ncols):
            a[pivot][j] /= base
        for i in range(pivot + 1, len(a)):
            coeff = a[i][col]
            if coeff:
                for j in range(col, ncols):
                    a[i][j] -= coeff * a[pivot][j]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def sector_matrix(c, d):
    n = len(c)
    pairs = list(combinations(range(n), 2))
    out = [[0 for _ in pairs] for _ in range(2 * n)]
    for col, (i, j) in enumerate(pairs):
        out[i][col], out[j][col] = c[j], c[i]
        out[n + i][col], out[n + j][col] = d[j], d[i]
    return out


def predicted(n, ratios):
    counts = [ratios.count(v) for v in set(ratios)]
    if n <= 3:
        return 0
    if n == 4:
        if len(counts) == 1:
            return 2
        return 1 if sorted(counts) == [2, 2] else 0
    e = comb(n, 2)
    if len(counts) == 1:
        return e - n
    if max(counts) >= n - 2:
        return e - 2*n + 2
    return e - 2*n + 1


def partitions(n, minpart=1):
    if n == 0:
        yield ()
        return
    for p in range(minpart, n + 1):
        for remainder in partitions(n - p, p):
            yield (p,) + remainder


checks = 0
# Distinct symbolic ratios 1,2,...; all integer partitions cover every equality-pattern size.
for n in range(2, 11):
    for sizes in partitions(n):
        r = [v + 1 for v, size in enumerate(sizes) for _ in range(size)]
        c = [1 + ((i * 7 + n) % 5) for i in range(n)]
        d = [c[i] * r[i] for i in range(n)]
        got = comb(n, 2) - exact_rank(sector_matrix(c, d))
        want = predicted(n, r)
        assert got == want, (n, sizes, got, want)
        checks += 1

# Check arbitrary distinct rational ratio values, not merely 1,2,3,...
rng = Random(20261004)
for n in range(4, 10):
    for case in range(40):
        r = [rng.choice((1, 2, 4, 7, 13, 19)) for _ in range(n)]
        c = [rng.choice((1, 2, 3, 5, 9)) for _ in range(n)]
        d = [x*y for x, y in zip(c, r)]
        got = comb(n, 2) - exact_rank(sector_matrix(c, d))
        want = predicted(n, r)
        assert got == want, (n, case, r, got, want)
        checks += 1

# Directly confirm a nonzero five-emitter vector for c=(1,...,1), d=(1,...,5).
coeffs = (1, -6, 9, -4, 6, -16, 9, 6, -6, 1)
rows = sector_matrix([1]*5, [1,2,3,4,5])
assert all(sum(a*b for a,b in zip(row, coeffs)) == 0 for row in rows)
checks += 1

# Confirm the four-emitter equal-pair exceptional dark vector.
rows = sector_matrix([1]*4, [1,1,2,2])
pairs = list(combinations(range(4), 2))
y = {(0,2):1,(0,3):-1,(1,2):-1,(1,3):1}
v = [y.get(pair, 0) for pair in pairs]
assert all(sum(a*b for a,b in zip(row, v)) == 0 for row in rows)
checks += 1
print('VERIFY_OK', checks, 'exact rational rank and vector checks')
