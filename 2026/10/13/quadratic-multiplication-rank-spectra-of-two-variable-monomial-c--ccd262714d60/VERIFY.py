#!/usr/bin/env python3
"""Independent finite-field checks of quadratic multiplication-rank formulas.
Run with Python 3. No nonstandard dependencies.
"""
from math import gcd

class Field:
    def __init__(self, q):
        self.q = q
        self.e = {4: 2, 8: 3}.get(q, 1)
        self.mod = {4: 0b111, 8: 0b1011}.get(q)
        if self.e == 1:
            assert q in (2, 3, 5, 7, 11, 13)
            self.p = q
        else:
            self.p = 2

    def add(self, a, b):
        return a ^ b if self.e > 1 else (a + b) % self.q

    def neg(self, a):
        return a if self.e > 1 else (-a) % self.q

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.e == 1:
            return a * b % self.q
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.mod
        return out

    def power(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def inverse(self, a):
        assert a
        return self.power(a, self.q - 2)


def determinant_rec(F, m, a, b, c):
    z = F.mul(a, c)
    d0, d1 = 1, b
    for k in range(2, m):
        d0, d1 = d1, F.sub(F.mul(b, d1), F.mul(z, d0))
    return d1


def predicted_bad(F, m):
    n = m
    while n % F.p == 0:
        n //= F.p
    roots = (gcd(n, F.q - 1) + gcd(n, F.q + 1)) // 2
    if m % F.p:
        roots -= 1
    return (F.q - 1)**2 * roots + 2*(F.q - 1)


def matrix_rank(F, M):
    if not M:
        return 0
    M = [row[:] for row in M]
    height, width = len(M), len(M[0])
    rank = 0
    for col in range(width):
        pivot = next((i for i in range(rank, height) if M[i][col]), None)
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        pi = F.inverse(M[rank][col])
        for j in range(col, width):
            M[rank][j] = F.mul(M[rank][j], pi)
        for i in range(height):
            if i == rank or not M[i][col]:
                continue
            k = M[i][col]
            for j in range(col, width):
                M[i][j] = F.sub(M[i][j], F.mul(k, M[rank][j]))
        rank += 1
        if rank == height:
            break
    return rank


def direct_multiplication_rank(F, m, a, b, c):
    degree_bases = [[(u, d-u) for u in range(m) if 0 <= d-u < m]
                    for d in range(2*m-1)]
    total = 0
    for d in range(2*m-3):
        source = degree_bases[d]
        target = degree_bases[d+2]
        targets = {mon: i for i, mon in enumerate(target)}
        rows = [[0] * len(source) for _ in target]
        for j, (u, v) in enumerate(source):
            for du, dv, coefficient in [(2, 0, a), (1, 1, b), (0, 2, c)]:
                i = targets.get((u+du, v+dv))
                if i is not None:
                    rows[i][j] = F.add(rows[i][j], coefficient)
        total += matrix_rank(F, rows)
    return total


def run():
    ntotal = 0
    for q in (2, 3, 4, 5, 7, 8, 11, 13):
        F = Field(q)
        for m in range(3, 61):
            bad = 0
            for a in range(q):
                for b in range(q):
                    for c in range(q):
                        if not (a or b or c):
                            continue
                        if determinant_rec(F, m, a, b, c) == 0:
                            bad += 1
            assert bad == predicted_bad(F, m), (q, m, bad, predicted_bad(F,m))
            ntotal += 1
        maxima = {2: 8, 3: 7, 4: 6, 5: 5, 7: 4, 8: 4, 11: 3, 13: 3}[q]
        for m in range(3, maxima+1):
            observed = [0, 0, 0]
            for a in range(q):
                for b in range(q):
                    for c in range(q):
                        rank = direct_multiplication_rank(F, m, a, b, c)
                        if (a, b, c) == (0, 0, 0):
                            assert rank == 0, (q,m,a,b,c,rank)
                            observed[0] += 1
                        elif rank == (m-1)**2-1:
                            observed[1] += 1
                        elif rank == (m-1)**2:
                            observed[2] += 1
                        else:
                            raise AssertionError(('unexpected-rank',q,m,a,b,c,rank))
            assert observed == [1, predicted_bad(F,m), q**3-1-predicted_bad(F,m)],(q,m,observed)
    print('VERIFY_OK_QUADRATIC_LEFSCHETZ', ntotal, 'determinant-count cases, independent multiplication checks')

if __name__ == '__main__':
    run()
