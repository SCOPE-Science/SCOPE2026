#!/usr/bin/env python3
"""Exact small-field and combinatorial checks for a characteristic-two quartic."""
from itertools import combinations
from math import comb, factorial


def fmul(a, b):
    z = 0
    while b:
        if b & 1:
            z ^= a
        a <<= 1
        if a & 4:
            a ^= 7
        b >>= 1
    return z


def finv(a):
    if not a:
        raise ZeroDivisionError
    for b in (1, 2, 3):
        if fmul(a, b) == 1:
            return b
    raise AssertionError


def coeff(counts, degree):
    e = [0] * (degree + 1)
    e[0] = 1
    for value, many in enumerate(counts):
        for _ in range(many):
            for j in range(degree, 0, -1):
                e[j] ^= fmul(value, e[j - 1])
    return e[degree]


def singular(counts):
    if coeff(counts, 4):
        return False
    for v, many in enumerate(counts):
        if many:
            c = list(counts)
            c[v] -= 1
            if coeff(c, 3):
                return False
    return True


def predicted(counts):
    nonzero = [a for a in counts if a]
    if len(nonzero) == 1:
        return True
    if len(nonzero) == 2:
        return sorted([a % 8 for a in nonzero]) == [1, 2]
    if len(nonzero) == 3:
        return all(a % 8 == 1 for a in nonzero)
    return False


def compositions4(n):
    for a in range(n + 1):
        for b in range(n + 1 - a):
            for c in range(n + 1 - a - b):
                yield (a, b, c, n - a - b - c)


def plane_count(n):
    subtotal = 0
    for a in range(1, n - 1, 8):
        for b in range(1, n - a, 8):
            c = n - a - b
            if c > 0 and c % 8 == 1:
                subtotal += factorial(n) // (factorial(a) * factorial(b) * factorial(c))
    assert subtotal % 6 == 0
    return subtotal // 6


def hessian(n, groups, values):
    assert sum(groups) == n
    vals = [value for size, value in zip(groups, values) for _ in range(size)]
    h = [[0] * n for _ in range(n)]
    base = [0] * 4
    for v in vals:
        base[v] += 1
    for i in range(n):
        for j in range(i + 1, n):
            cc = list(base)
            cc[vals[i]] -= 1
            cc[vals[j]] -= 1
            h[i][j] = h[j][i] = coeff(cc, 2)
    return h


def rank(a):
    a = [row[:] for row in a]
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        inv = finv(a[row][col])
        a[row] = [fmul(inv, x) for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                factor = a[i][col]
                a[i] = [x ^ fmul(factor, y) for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def join_blocks(pair1, pair2, n=11):
    parent = list(range(n))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(i, j):
        parent[find(i)] = find(j)
    for pair in (pair1, pair2):
        rest = [i for i in range(n) if i not in pair]
        for i in rest[1:]:
            union(rest[0], i)
    return len({find(i) for i in range(n)})


def main():
    assert fmul(2, 2) == 3 and fmul(2, 3) == 1
    for n in (11, 19):
        assert n % 8 == 3
        assert all(comb(n - j, 4 - j) % 2 == 0 for j in range(4))
        checked = 0
        singular_patterns = 0
        for counts in compositions4(n):
            if sum(counts) != n:
                raise AssertionError
            got = singular(counts)
            assert got == predicted(counts), (n, counts, got)
            checked += 1
            singular_patterns += got
        print('n', n, 'field GF(4) multiplicity patterns', checked,
              'singular', singular_patterns, 'planes', plane_count(n))
    assert plane_count(11) == 55
    assert plane_count(19) == 462061
    assert rank(hessian(11, [9, 1, 1], [0, 1, 2])) == 8
    assert rank(hessian(19, [9, 9, 1], [0, 1, 2])) == 16
    pairs = list(combinations(range(11), 2))
    line_intersections = 0
    point_intersections = 0
    for p, q in combinations(pairs, 2):
        number_blocks = join_blocks(p, q)
        assert number_blocks in (1, 2)
        if set(p).intersection(q):
            assert number_blocks == 2
            line_intersections += 1
        else:
            assert number_blocks == 1
            point_intersections += 1
    assert line_intersections == 495
    assert point_intersections == comb(55, 2) - 495
    print('n11 plane pairs: line intersections', line_intersections,
          'point intersections', point_intersections)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
