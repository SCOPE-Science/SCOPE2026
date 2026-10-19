"""Exact finite checks for fixed-point/local ordinal-pattern covariance.

Run with Python 3 (standard library only): python verify_patterns.py
An exhaustive finite test supplements, and does not replace, the proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def patt(values):
    return tuple(1 + sum(y < x for y in values) for x in values)


def expect_cov(n, k, i, pat, j):
    """Indices i,j are 1-based; pat is a rank-permutation of 1..k."""
    if not (i <= j < i + k):
        return Fraction(0)
    r = pat[j - i]
    cond = Fraction(comb(j - 1, r - 1) * comb(n - j, k - r),
                    factorial(n - 1) // factorial(n - k))
    return (cond - Fraction(1, factorial(k))) / n


def rank_q(rows, cols):
    a = [list(map(Fraction, row)) for row in rows]
    piv = 0
    for c in range(cols):
        chosen = next((r for r in range(piv, len(a)) if a[r][c]), None)
        if chosen is None:
            continue
        a[piv], a[chosen] = a[chosen], a[piv]
        v = a[piv][c]
        a[piv] = [z / v for z in a[piv]]
        for r in range(piv + 1, len(a)):
            v = a[r][c]
            if v:
                a[r] = [u - v*w for u, w in zip(a[r], a[piv])]
        piv += 1
        if piv == len(a):
            break
    return piv


def test_exhaustive():
    count = 0
    for n in range(2, 9):
        hist = defaultdict(int)
        for pi in permutations(range(1, n + 1)):
            fixed = [j for j, x in enumerate(pi, 1) if x == j]
            for k in range(1, n + 1):
                for i in range(1, n-k+2):
                    pattern = patt(pi[i-1:i-1+k])
                    for j in fixed:
                        hist[(k, i, pattern, j)] += 1
        for k in range(1, n + 1):
            for i in range(1, n - k + 2):
                for p in permutations(range(1, k + 1)):
                    for j in range(1, n+1):
                        measured = Fraction(hist[(k, i, p, j)], factorial(n)) - Fraction(1, n*factorial(k))
                        expected = expect_cov(n, k, i, p, j)
                        assert measured == expected, (n, k, i, p, j, measured, expected)
                        count += 1
        print('exact covariance enumeration passed for n=', n)
    return count


def test_ranks():
    count=0
    for n in range(2, 13):
        for k in range(1, min(n, 4)+1):
            rows = ([expect_cov(n,k,i,p,j) for j in range(1,n+1)]
                    for i in range(1,n-k+2)
                    for p in permutations(range(1,k+1)))
            got=rank_q(rows,n)
            need=0 if k==1 else (n-1 if k==2 else n)
            assert got==need,(n,k,got,need)
            count+=1
    return count


def test_determinant():
    count=0
    for n in range(3,501):
        for j in range(1,n-1):
            a=lambda j:(n-j)*(n-3*j+1)
            b=lambda j:(j-1)*(2*n-3*j+2)
            determinant=a(j)*b(j+1)-b(j)*a(j+1)
            assert determinant==2*(n-2)*(3*j*j-3*j*n+n*n-1)
            assert determinant>0
            count+=1
    return count

if __name__ == '__main__':
    e=test_exhaustive()
    r=test_ranks()
    d=test_determinant()
    print(f'PASS exact_covariance_cells={e} rank_cases={r} determinant_cases={d}')
