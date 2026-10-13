#!/usr/bin/env python3
"""Exact checks for two-tier nested bipartite modularity.

Usage: python verify.py
Requires Python >=3.9 standard library only.
"""
from fractions import Fraction


def partitions(n):
    """All unlabeled set partitions of range(n), each once."""
    def visit(k, blocks):
        if k == n:
            yield tuple(tuple(block) for block in blocks)
            return
        for block in blocks:
            block.append(k)
            yield from visit(k + 1, blocks)
            block.pop()
        blocks.append([k])
        yield from visit(k + 1, blocks)
        blocks.pop()
    yield from visit(0, [])


def matrix(p, q, a, b):
    # Specialist rows followed by generalist rows; shared columns first.
    return [[1] * a + [0] * b for _ in range(p)] + \
           [[1] * (a + b) for _ in range(q)]


def score_from_partition(A, blocks):
    rows, cols = len(A), len(A[0])
    E = sum(map(sum, A))
    rd = [sum(row) for row in A]
    cd = [sum(A[i][j] for i in range(rows)) for j in range(cols)]
    label = {}
    for k, block in enumerate(blocks):
        for vertex in block:
            label[vertex] = k
    numerator = sum(E * A[i][j] - rd[i] * cd[j]
                    for i in range(rows) for j in range(cols)
                    if label[i] == label[rows + j])
    return Fraction(numerator, E * E)


def optimum_by_row_partitions(A):
    """Exact global optimum: optimize column labels for each row partition."""
    rows, cols = len(A), len(A[0])
    E = sum(map(sum, A))
    rd = [sum(row) for row in A]
    cd = [sum(A[i][j] for i in range(rows)) for j in range(cols)]
    B = [[E * A[i][j] - rd[i] * cd[j] for j in range(cols)]
         for i in range(rows)]
    opt = 0
    for blocks in partitions(rows):
        value = sum(max(sum(B[i][j] for i in block) for block in blocks)
                    for j in range(cols))
        opt = max(opt, value)
    return Fraction(opt, E * E)


def theorem(p, q, a, b):
    return Fraction(2 * p * q * a * b, ((p + q) * a + q * b) ** 2)


def main():
    checked = 0
    for p in range(1, 5):
        for q in range(1, 5):
            if p + q > 6:
                continue
            for a in range(1, 4):
                for b in range(1, 5):
                    A = matrix(p, q, a, b)
                    got = optimum_by_row_partitions(A)
                    target = theorem(p, q, a, b)
                    assert got == target, (p, q, a, b, got, target)
                    assert got <= Fraction(p, 2 * (p + q))
                    assert (got == Fraction(p, 2 * (p + q))) == \
                           (q * b == (p + q) * a)
                    checked += 1
    directly_checked = 0
    # Independent exhaustive partitions of *all* vertices, not the row reduction.
    for p, q, a, b in ((1, 1, 1, 1), (1, 1, 1, 2),
                       (1, 1, 2, 2), (1, 1, 2, 3),
                       (2, 1, 1, 1), (2, 1, 1, 2),
                       (2, 1, 1, 3)):
        A = matrix(p, q, a, b)
        n = len(A) + len(A[0])
        vals = [score_from_partition(A, blocks) for blocks in partitions(n)]
        assert max(vals) == theorem(p, q, a, b)
        assert vals.count(max(vals)) == 1, (p, q, a, b, vals.count(max(vals)))
        directly_checked += len(vals)
    for m in range(2, 25):
        assert theorem(m-1, 1, 1, m) == Fraction(m-1, 2*m)
        assert theorem(m-1, 1, 1, m) < Fraction(1, 2)
    print('VERIFY_OK parametric_profiles=%d full_vertex_partitions=%d' %
          (checked, directly_checked))


if __name__ == '__main__':
    main()
