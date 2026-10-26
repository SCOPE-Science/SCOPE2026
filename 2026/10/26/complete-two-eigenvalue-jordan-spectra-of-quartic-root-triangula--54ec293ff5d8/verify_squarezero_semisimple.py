"""Verify finite-field Jordan spectra for upper-triangular quartic-root matrices.

No external dependencies. Usage: python3 verify_squarezero_semisimple.py
"""
import itertools
from math import comb


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return a * b % q
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # t^2+t+1 over F_2
    return r


def neg(a, q):
    return a if q == 4 else (-a) % q


def mm(A, B, q):
    n = len(A)
    return [[sum_mod((mul(A[i][k], B[k][j], q) for k in range(n)), q)
             for j in range(n)] for i in range(n)]


def sum_mod(xs, q):
    v = 0
    for x in xs:
        v = add(v, x, q)
    return v


def madd(A, B, q, scale=1):
    return [[add(A[i][j], mul(scale, B[i][j], q), q)
             for j in range(len(A))] for i in range(len(A))]


def mrank(M, q):
    A = [row[:] for row in M]
    n = len(A)
    k = 0
    for j in range(n):
        pivot = next((i for i in range(k, n) if A[i][j]), None)
        if pivot is None:
            continue
        A[k], A[pivot] = A[pivot], A[k]
        v = A[k][j]
        inv = next(x for x in range(1, q) if mul(x, v, q) == 1)
        A[k] = [mul(inv, x, q) for x in A[k]]
        for i in range(n):
            if i != k and A[i][j]:
                c = A[i][j]
                A[i] = [add(A[i][h], neg(mul(c, A[k][h], q), q), q)
                        for h in range(n)]
        k += 1
    return k


def squarezero_counts(n, q):
    F = [[0] * (n // 2 + 2) for _ in range(n + 1)]
    F[0][0] = 1
    for m in range(1, n + 1):
        for r in range(m // 2 + 1):
            F[m][r] = q**r * F[m-1][r]
            if r:
                F[m][r] += (q**(m-r) - q**(r-1)) * F[m-1][r-1]
    return F


def predicted(n, q):
    F = squarezero_counts(n, q)
    result = {}
    for a in range(n+1):
        for i in range(a//2+1):
            for j in range((n-a)//2+1):
                # a: dimension of the 1-eigenspace
                # i: square-zero rank on 1-eigenspace
                # j: square-zero rank on 0-eigenspace
                result[(a,i,j)] = comb(n,a) * q**(a*(n-a)) * F[a][i] * F[n-a][j]
    return result


def direct(n, q):
    inds = [(i, j) for i in range(n) for j in range(i, n)]
    ident = [[int(i == j) for j in range(n)] for i in range(n)]
    zero = [[0] * n for _ in range(n)]
    hist = {}
    for coeffs in itertools.product(range(q), repeat=len(inds)):
        A = [[0] * n for _ in range(n)]
        for (i, j), c in zip(inds, coeffs):
            A[i][j] = c
        A2 = mm(A, A, q)
        A3 = mm(A2, A, q)
        IminusA = madd(ident, A, q, neg(1, q))
        if mm(A2, mm(IminusA, IminusA, q), q) != zero:
            continue
        # Canonical idempotent e(A)=3 A^2 - 2 A^3, over any characteristic.
        E = madd([[mul((3 % (2 if q == 4 else q)), z, q) for z in row] for row in A2], A3, q, neg(2 % (2 if q == 4 else q), q))
        N = madd(A, E, q, neg(1, q))
        assert mm(E, E, q) == E
        assert mm(N, N, q) == zero
        assert mm(E, N, q) == mm(N, E, q)
        E0 = madd(ident, E, q, neg(1, q))
        rank1 = mrank(mm(N, E, q), q)
        rank0 = mrank(mm(N, E0, q), q)
        a = sum(E[i][i] for i in range(n))  # entries are 0 or 1
        key = (a, rank1, rank0)
        hist[key] = hist.get(key, 0) + 1
    return hist


def run():
    cases = [(1,2), (2,2), (3,2), (4,2), (5,2), (2,3), (3,3), (3,4), (2,5)]
    for n, q in cases:
        want = {k:v for k,v in predicted(n,q).items() if v}
        got = direct(n,q)
        assert got == want, (n,q,got,want)
        print('PASS',n,q, 'solutions',sum(got.values()), 'Jordan strata',len(got))
    for q in [2,3,4,5,7,9,11]:
        for n in range(0,25):
            F=squarezero_counts(n,q)
            assert sum(F[n]) > 0
            assert sum(predicted(n,q).values()) <= 2**n*q**(n*(n-1)//2)
            assert sum(predicted(n,q).values()) == sum(comb(n,a)*q**(a*(n-a))*sum(F[a])*sum(F[n-a]) for a in range(n+1))
    print('VERIFY_OK_TWO_EIGENVALUE_SQUAREZERO_JORDAN')

if __name__ == '__main__':
    run()
