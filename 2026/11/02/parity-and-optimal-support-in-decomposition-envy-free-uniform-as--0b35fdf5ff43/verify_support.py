"""Exact checks for sparse decomposition-envy-free uniform assignments.

Standard library only. Rank 0 is the best object; lower rank is preferred.
The mathematical universal conclusions are proved separately, not inferred
from this finite test.
"""
from fractions import Fraction
from itertools import permutations


def even_assignments(n):
    assert n >= 2 and n % 2 == 0
    m = n // 2
    base = list(range(m)) + list(range(n - 1, m - 1, -1))
    assert sorted(base) == list(range(n))
    assert all(base[(j + m) % n] == n - 1 - base[j] for j in range(n))
    return [tuple(base[(i + t) % n] for i in range(n)) for t in range(n)]


def odd_assignments(n):
    assert n >= 3 and n % 2 == 1
    forward = [tuple((i + t) % n for i in range(n)) for t in range(n)]
    reversed_part = [tuple(n - 1 - p[i] for i in range(n)) for p in forward]
    return forward + reversed_part


def check_lottery(n, assigns, weights):
    assert len(assigns) == len(weights) == len(set(assigns))
    assert all(sorted(p) == list(range(n)) for p in assigns)
    assert all(w > 0 for w in weights)
    assert sum(weights) == 1
    for i in range(n):
        for j in range(n):
            assert sum((w for p, w in zip(assigns, weights) if p[i] == j), Fraction(0)) == Fraction(1, n)
    for i in range(n):
        for j in range(n):
            if i != j:
                assert sum((w for p, w in zip(assigns, weights) if p[i] > p[j]), Fraction(0)) == Fraction(1, 2)


def rref(matrix):
    """Pure rational reduced row-echelon matrix and pivot coordinates."""
    a = [[Fraction(v) for v in row] for row in matrix]
    m, n = len(a), len(a[0])
    pivots = []
    rank = 0
    for c in range(n):
        q = next((i for i in range(rank, m) if a[i][c]), None)
        if q is None:
            continue
        a[rank], a[q] = a[q], a[rank]
        t = a[rank][c]
        a[rank] = [v/t for v in a[rank]]
        for i in range(m):
            if i == rank:
                continue
            t = a[i][c]
            if t:
                a[i] = [u - t*v for u,v in zip(a[i], a[rank])]
        pivots.append(c)
        rank += 1
        if rank == m:
            break
    return a, pivots


def check_unique_three():
    p = list(permutations(range(3)))
    rows = []
    for i in range(3):
        for j in range(3):
            rows.append([int(a[i] == j) for a in p] + [Fraction(1,3)])
    for i in range(3):
        for j in range(i+1,3):
            rows.append([int(a[i] > a[j]) for a in p] + [Fraction(1,2)])
    red, pivot = rref(rows)
    assert pivot == list(range(6))
    assert all(all(red[k][j] == (1 if k == j else 0) for j in range(6)) and
               red[k][-1] == Fraction(1,6) for k in range(6))
    assert all(not any(row[:-1]) or not row[-1] for row in red[6:])
    check_lottery(3, p, [Fraction(1,6)]*6)
    return pivot, len(rows)


def main():
    tests = 0
    for n in range(2, 21, 2):
        p = even_assignments(n)
        check_lottery(n, p, [Fraction(1,n)]*n)
        tests += 1
    for n in range(3, 20, 2):
        p = odd_assignments(n)
        check_lottery(n, p, [Fraction(1,2*n)]*(2*n))
        tests += 1
    pivot, rows = check_unique_three()
    print('PASS: even sizes n=2,...,20 (10 cases), odd n=3,...,19 (9 cases).')
    print('PASS: exact 3x3 full fairness constraint system, %d rows, rank %d, unique uniform 1/6.' % (rows, len(pivot)))
    print('PASS: every tested probability, uniform marginal and pairwise comparison is exact.')


if __name__ == '__main__':
    main()
