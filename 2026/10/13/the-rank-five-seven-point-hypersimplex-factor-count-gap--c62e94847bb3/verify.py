#!/usr/bin/env python3
"""Exact integer/rational verification of the thirteen rank-five scaling witnesses."""
import itertools
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def rank(matrix):
    a = [[Fraction(z) for z in row] for row in matrix]
    height, width = len(a), len(a[0])
    pivot_row = 0
    for col in range(width):
        pivot = next((i for i in range(pivot_row, height) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        divisor = a[pivot_row][col]
        for j in range(col, width):
            a[pivot_row][j] /= divisor
        for i in range(pivot_row + 1, height):
            if a[i][col]:
                factor = a[i][col]
                for j in range(col, width):
                    a[i][j] -= factor * a[pivot_row][j]
        pivot_row += 1
        if pivot_row == height:
            break
    return pivot_row


def determinant(matrix):
    a = [[Fraction(z) for z in row] for row in matrix]
    n = len(a)
    product = Fraction(1)
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            product = -product
        d = a[col][col]
        product *= d
        for i in range(col + 1, n):
            factor = a[i][col] / d
            for j in range(col + 1, n):
                a[i][j] -= factor * a[col][j]
            a[i][col] = 0
    return product


def partitions(k, top=None):
    if k == 0:
        yield ()
    else:
        for a in range(min(k, top or k), 0, -1):
            for rest in partitions(k - a, a):
                yield (a,) + rest


def expected_patterns():
    for t in range(5, 8):
        for p in partitions(t):
            if max(p) <= t - 4:
                yield p


entries = json.loads((Path(__file__).resolve().parent / 'witnesses.json').read_text(encoding='utf-8'))
patterns = set(expected_patterns())
assert len(patterns) == 13
assert len(entries) == len(patterns)
seen = set()
actual = set()
for entry in entries:
    p = tuple(entry['parallel_classes'])
    assert p in patterns and p not in seen
    seen.add(p)
    assert entry['loop_count'] == 7 - sum(p)
    matrix = entry['matrix']
    assert len(matrix) == 7 and all(len(row) == 7 for row in matrix)
    assert all(isinstance(c, int) and not isinstance(c, bool) for row in matrix for c in row)
    assert all(matrix[i][i] == 0 for i in range(7))
    assert all(matrix[i][j] == matrix[j][i] != 0 for i in range(7) for j in range(i + 1, 7))
    assert rank(matrix) == 5
    k = 0
    dual_bases = set()
    for inds in itertools.combinations(range(7), 5):
        sub = [[matrix[i][j] for j in inds] for i in inds]
        if determinant(sub):
            k += 1
            dual_bases.add(tuple(sorted(set(range(7)) - set(inds))))
    nonloops = {j for pair in dual_bases for j in pair}
    assert len(set(range(7)) - nonloops) == entry['loop_count']
    remaining = set(nonloops)
    sizes = []
    while remaining:
        pivot = min(remaining)
        parallel_class = {pivot} | {j for j in remaining if j != pivot and tuple(sorted((pivot, j))) not in dual_bases}
        assert all(tuple(sorted((i, j))) not in dual_bases for i, j in itertools.combinations(parallel_class, 2))
        assert all(tuple(sorted((i, j))) in dual_bases for i in parallel_class for j in remaining - parallel_class)
        sizes.append(len(parallel_class))
        remaining -= parallel_class
    assert tuple(sorted(sizes, reverse=True)) == p
    assert k == entry['nonzero_order_five_principal_minors']
    assert k == comb(sum(p), 2) - sum(comb(a, 2) for a in p)
    actual.add(k)
assert seen == patterns
assert actual == {10, *range(12, 22)}
print('VERIFY_OK; 13 exact witnesses; possible counts:', sorted(actual))
