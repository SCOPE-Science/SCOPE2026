"""Exact finite checks for marked-Poisson type factorization and rank-k kernels.
The closedness and all-n antichain arguments are mathematical proofs, not finite checks.
Run: python verify.py
"""
from fractions import Fraction
from math import comb


def matrix_rank(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        z = a[rank][col]
        a[rank] = [x / z for x in a[rank]]
        for i in range(rank + 1, m):
            if a[i][col] != 0:
                z = a[i][col]
                a[i] = [x - z * y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def threshold(n):
    r = 0
    while comb(r, r // 2) < n:
        r += 1
    return r


def kernel(n, k, delta):
    return [[Fraction((i-j)**2) + delta * (
        1 + sum((i**h)*(j**h) for h in range(3,k))
    ) for j in range(1,n+1)] for i in range(1,n+1)]


def checks():
    count = 0
    for n in range(3, 14):
        q = kernel(n, 3, Fraction(0))
        assert matrix_rank(q) == 3
        count += 1
        assert all(q[i][i] == 0 for i in range(n))
        count += 1
        assert all(q[i][j] > 0 for i in range(n) for j in range(n) if i != j)
        count += 1
        for k in range(3, min(n,7) + 1):
            d = Fraction(1, 2**18)
            a = kernel(n, k, d)
            assert matrix_rank(a) == k, (n, k)
            count += 1
            assert all(a[i][j] > 0 for i in range(n) for j in range(n))
            count += 1
            assert all(a[i][j] == a[j][i] for i in range(n) for j in range(n))
            count += 1
    for n in range(3, 1001):
        r = threshold(n)
        assert comb(r, r // 2) >= n
        count += 1
        assert comb(r-1, (r-1)//2) < n
        count += 1
    assert threshold(4) == 4
    count += 1
    assert threshold(7) == 5
    count += 1
    assert threshold(21) == 7
    count += 1
    # Exact mark-emission normalization for an arbitrary positive rational factorization.
    u = [[Fraction(1+i+h, 2+h) for h in range(3)] for i in range(6)]
    v = [[Fraction(1+h+2*j, 3+j) for j in range(6)] for h in range(3)]
    s = [sum(vh) for vh in v]
    b = [[u[i][h]*s[h] for h in range(3)] for i in range(6)]
    p = [[v[h][j]/s[h] for j in range(6)] for h in range(3)]
    for h in range(3):
        assert sum(p[h]) == 1
        count += 1
    for i in range(6):
        for j in range(6):
            assert sum(b[i][h]*p[h][j] for h in range(3)) == sum(u[i][h]*v[h][j] for h in range(3))
            count += 1
    return count


if __name__ == '__main__':
    total = checks()
    print(f'PASS: {total} exact finite rational checks')
    print('Infinite nonnegative-rank lower bound and perturbation stability require the written proof.')
