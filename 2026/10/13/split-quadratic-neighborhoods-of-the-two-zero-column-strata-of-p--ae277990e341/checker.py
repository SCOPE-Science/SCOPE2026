"""Exact finite checks for complementary-permanent normal form.
Run: python3 permanent_transverse_checker.py
The proof of the all-n statement is algebraic and does not depend on this enumeration.
"""
import math
import random

def perm(M):
    n = len(M)
    assert all(len(row) == n for row in M)
    dp = [0] * (1 << n)
    dp[0] = 1
    for mask in range(1 << n):
        i = mask.bit_count()
        if i == n or not dp[mask]:
            continue
        for j in range(n):
            if not (mask >> j) & 1:
                dp[mask | (1 << j)] += dp[mask] * M[i][j]
    return dp[-1]

def det(M):
    n = len(M)
    a = [list(map(int, row)) for row in M]
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            t = next((i for i in range(k+1,n) if a[i][k]), None)
            if t is None:
                return 0
            a[k], a[t] = a[t], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer = a[i][j]*pivot-a[i][k]*a[k][j]
                assert numer % prev == 0
                a[i][j] = numer // prev
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]

def A_from(B):
    n = len(B)
    return [[0 if i == j else perm([B[r] for r in range(n) if r not in (i,j)])
             for j in range(n)] for i in range(n)]

def test():
    rng = random.Random(29173)
    identities = determinants = 0
    for n in range(3,9):
        B_ones = [[1]*(n-2) for _ in range(n)]
        A = A_from(B_ones)
        coefficient = math.factorial(n-2)
        assert A == [[0 if i == j else coefficient for j in range(n)] for i in range(n)]
        assert det(A) == (-1)**(n-1)*(n-1)*coefficient**n
        determinants += 1
        for t in range(7):
            B = B_ones if t == 0 else [[rng.randrange(-2,4) for _ in range(n-2)] for _ in range(n)]
            u = [rng.randrange(-3,4) for _ in range(n)]
            v = [rng.randrange(-3,4) for _ in range(n)]
            A = A_from(B)
            M = [[u[i],v[i]]+B[i] for i in range(n)]
            w = [sum(A[i][j]*v[j] for j in range(n)) for i in range(n)]
            assert perm(M) == sum(u[i]*w[i] for i in range(n))
            assert A == [list(r) for r in zip(*A)]
            assert all(A[i][i] == 0 for i in range(n))
            identities += 1
    print('PASS exact rational/integer computations')
    print('matrix sizes n=3,4,5,6,7,8')
    print(f'permanent-to-quadric polynomial specializations: {identities}')
    print(f'nonzero all-ones complementary determinants: {determinants}')
    print('No finite test is used as an all-parameter proof.')
if __name__ == '__main__':
    test()
