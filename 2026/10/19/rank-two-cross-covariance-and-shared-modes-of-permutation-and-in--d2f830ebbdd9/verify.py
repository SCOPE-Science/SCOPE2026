#!/usr/bin/env python3
"""Finite, exact tests for position-versus-value comparison covariances.

Run: python3 verify_inverse_comparison.py
No nonstandard modules are required. Finite tests do not replace the proof.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def expected_cross(n, left, right):
    i, j = left
    a, b = right
    z = Fraction(1, 2*n*(n-1))
    if n >= 3:
        z += Fraction((j-i-1)*(b-a-1), n*(n-1)*(n-2))
    return z


def exact_rank(rows):
    a = [[Fraction(x) for x in r] for r in rows]
    rows_n = len(a)
    cols_n = len(a[0]) if a else 0
    rank = 0
    for col in range(cols_n):
        pivot = next((r for r in range(rank, rows_n) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for r in range(rank+1, rows_n):
            if a[r][col]:
                ratio = a[r][col] / a[rank][col]
                for c in range(col, cols_n):
                    a[r][c] -= ratio*a[rank][c]
        rank += 1
        if rank == rows_n:
            break
    return rank


def exhaustive(n):
    edges = list(combinations(range(1, n+1), 2))
    m = len(edges)
    inv_sum = [0]*m
    inverse_sum = [0]*m
    cross_sum = [[0]*m for _ in range(m)]
    total = factorial(n)
    for p in permutations(range(1, n+1)):
        pos = [0]*(n+1)
        for k, val in enumerate(p, 1):
            pos[val] = k
        left = [int(p[i-1]>p[j-1]) for i,j in edges]
        right = [int(pos[a]>pos[b]) for a,b in edges]
        weighted_inversions = sum((j-i)*x for (i,j), x in zip(edges,left))
        squared_displacement = sum((k-p[k-1])**2 for k in range(1,n+1))
        assert 2*weighted_inversions == squared_displacement
        assert sum(left) == sum(right)
        assert sum((b-a)*x for (a,b),x in zip(edges,right)) == weighted_inversions
        for i in range(m):
            inv_sum[i] += left[i]
            inverse_sum[i] += right[i]
            if left[i]:
                for j in range(m):
                    cross_sum[i][j] += right[j]
    for e in range(m):
        assert 2*inv_sum[e] == total
        assert 2*inverse_sum[e] == total
    for i,left in enumerate(edges):
        for j,right in enumerate(edges):
            covariance = Fraction(cross_sum[i][j],total) - Fraction(1,4)
            assert covariance == expected_cross(n,left,right), (n,left,right,covariance)
    if n <= 6:
        exact_matrix = [[expected_cross(n,a,b) for b in edges] for a in edges]
        assert exact_rank(exact_matrix) == (2 if n>=3 else 1)
    return total, m*m


def symbolic_rank_and_positivity():
    checks = 0
    for n in range(3,65):
        e = list(combinations(range(1,n+1),2))
        u = [1]*len(e)
        v = [j-i-1 for i,j in e]
        assert len(set(v))>1
        assert sum(v)==n*(n-1)*(n-2)//6
        assert 12*sum(w*w for w in v)==n*(n-1)**2*(n-2)
        # Exact two-dimensional Gram determinant: positive because v is nonconstant.
        det = len(e)*sum(w*w for w in v) - sum(v)**2
        assert det > 0
        # Both coefficients in the cross kernel are strictly positive.
        assert Fraction(1,2*n*(n-1)) > 0
        assert Fraction(1,n*(n-1)*(n-2)) > 0
        checks += 6
    return checks


def main():
    tested = 0
    for n in range(2,8):
        perms, entries = exhaustive(n)
        print('n=%d permutations=%d exact cross entries=%d' % (n,perms,entries))
        tested += entries
    structural = symbolic_rank_and_positivity()
    print('PASS: %d exhaustive cross-covariance entries, %d structural checks.' % (tested,structural))

if __name__ == '__main__':
    main()
