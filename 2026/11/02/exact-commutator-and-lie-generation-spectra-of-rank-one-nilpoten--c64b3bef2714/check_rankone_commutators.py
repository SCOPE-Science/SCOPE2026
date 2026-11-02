#!/usr/bin/env python3
"""Exhaustive small-field tests for rank-one nilpotent commutator strata.

Usage: python3 check_rankone_commutators.py
No external packages, files, or network access required.
"""
from itertools import product


class Field:
    def __init__(self, q):
        assert q in (2, 3, 4)
        self.q = q
        self.p = 2 if q in (2, 4) else 3

    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.p

    def neg(self, a):
        return a if self.p == 2 else (-a) % self.p

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.q != 4:
            return a * b % self.p
        t = 0
        for i in range(2):
            if (b >> i) & 1:
                t ^= a << i
        for shift in (1, 0):
            if (t >> (shift + 2)) & 1:
                t ^= 7 << shift  # x^2 + x + 1
        return t

    def inv(self, a):
        assert a != 0
        return next(b for b in range(1, self.q) if self.mul(a, b) == 1)


def dot(f, u, v):
    total = 0
    for x, y in zip(u, v):
        total = f.add(total, f.mul(x, y))
    return total


def all_rankone_squarezero(f, n):
    vs = list(product(range(f.q), repeat=n))
    result = []
    for u in vs:
        if not any(u):
            continue
        c = next(x for x in u if x)
        if c != 1:
            continue  # normalize the first nonzero coordinate
        for v in vs:
            if any(v) and dot(f, u, v) == 0:
                result.append((u, v))
    return result


def outer(f, u, v):
    return [[f.mul(a, b) for b in v] for a in u]


def multiply(f, A, B):
    n = len(A)
    return [[sum_products(f, ((A[i][k], B[k][j]) for k in range(n)))
             for j in range(n)] for i in range(n)]


def sum_products(f, pairs):
    z = 0
    for a, b in pairs:
        z = f.add(z, f.mul(a, b))
    return z


def mat_sub(f, A, B):
    return [[f.sub(a, b) for a, b in zip(row, row2)] for row, row2 in zip(A, B)]


def mat_scale(f, a, A):
    return [[f.mul(a, x) for x in row] for row in A]


def matrix_rank(f, A):
    mat = [list(row) for row in A]
    if not mat:
        return 0
    rows, cols = len(mat), len(mat[0])
    r = 0
    for j in range(cols):
        k = next((i for i in range(r, rows) if mat[i][j]), None)
        if k is None:
            continue
        mat[r], mat[k] = mat[k], mat[r]
        inv = f.inv(mat[r][j])
        mat[r] = [f.mul(inv, v) for v in mat[r]]
        for i in range(rows):
            if i != r and mat[i][j]:
                c = mat[i][j]
                mat[i] = [f.sub(v, f.mul(c, w)) for v, w in zip(mat[i], mat[r])]
        r += 1
        if r == rows:
            break
    return r


def is_zero(A):
    return all(x == 0 for row in A for x in row)


def flatten(A):
    return tuple(x for row in A for x in row)


def evaluate(f, n, X, Y):
    AB = multiply(f, X, Y)
    BA = multiply(f, Y, X)
    C = mat_sub(f, AB, BA)
    lamb = 0
    for i in range(n):
        lamb = f.add(lamb, AB[i][i])
    r = matrix_rank(f, C)
    assert r in (0, 1, 2)
    assert r == 2 if lamb else r in (0, 1)
    CC = multiply(f, C, C)
    if lamb == 0:
        assert is_zero(CC)
    else:
        assert mat_sub(f, multiply(f, CC, C), mat_scale(f, f.mul(lamb, lamb), C)) == [[0]*n for _ in range(n)]
    generated_dim = matrix_rank(f, [flatten(X), flatten(Y), flatten(C)])
    assert generated_dim == (3 if r else (1 if generated_dim == 1 else 2))
    twice = f.add(lamb, lamb)
    assert is_zero(mat_sub(f, mat_sub(f, multiply(f, C, X), multiply(f, X, C)), mat_scale(f, twice, X)))
    assert is_zero(mat_sub(f, mat_sub(f, multiply(f, C, Y), multiply(f, Y, C)), mat_scale(f, f.neg(twice), Y)))
    return r, lamb, generated_dim


def check(f, n, full=False):
    mats = all_rankone_squarezero(f, n)
    q = f.q
    M = (q**n - 1) * (q**(n-1) - 1) // (q-1)
    Z = M - 2*q**(n-1)*(q**(n-2)-1) - (q-1)*q**(2*n-3)
    R1 = 2*q**(n-1)*(q**(n-2)-1)
    R2 = (q-1)*q**(2*n-3)
    assert len(mats) == M, (q, n, len(mats), M)
    pairs = mats if full else [((1,)+(0,)*(n-1), (0,1)+(0,)*(n-2))]
    totals = [0,0,0]
    for u,v in pairs:
        X = outer(f,u,v)
        freq = [0,0,0]
        eig = {l:0 for l in range(1,q)}
        lies = {1:0,2:0,3:0}
        for s,t in mats:
            Y = outer(f,s,t)
            r,lam,dim = evaluate(f,n,X,Y)
            freq[r] += 1
            lies[dim] += 1
            if lam:
                eig[lam] += 1
            assert (dim != 1) or (r == 0)
        assert freq == [Z,R1,R2], (q,n,freq,[Z,R1,R2])
        assert all(eig[a] == q**(2*n-3) for a in eig), (q,n,eig)
        assert lies == {1:q-1, 2:Z-(q-1), 3:R1+R2}, (q,n,lies)
        totals = [a+b for a,b in zip(totals,freq)]
    print('OK field=%s dim=%s matrices=%s tested_pairs=%s full=%s rank_counts=%s per_eigenvalue=%s' %
          (q,n,M,len(pairs)*M,full,[Z,R1,R2],q**(2*n-3)))
    assert totals == [Z*len(pairs),R1*len(pairs),R2*len(pairs)]


if __name__ == '__main__':
    for q,n,full in [(2,2,True),(3,2,True),(4,2,True),
                     (2,3,True),(3,3,True),(4,3,False),
                     (2,4,True),(2,5,False),(3,4,False)]:
        check(Field(q),n,full)
    print('RANKONE_NILPOTENT_COMMUTATOR_SPECTRUM_OK')
