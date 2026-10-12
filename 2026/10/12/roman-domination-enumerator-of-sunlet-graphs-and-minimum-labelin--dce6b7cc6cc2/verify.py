"""Reproduce exact Roman-domination enumeration for sunlet graphs.

Python 3 standard library only. Run: python verify.py
"""
from itertools import product
from collections import Counter
from math import ceil


def add(p, q):
    r = [0] * max(len(p), len(q))
    for i, x in enumerate(p): r[i] += x
    for i, x in enumerate(q): r[i] += x
    return trim(r)


def trim(p):
    while len(p) > 1 and p[-1] == 0: p.pop()
    return p


def mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        if x:
            for j, y in enumerate(q):
                if y: r[i+j] += x*y
    return trim(r)


def power(p, k):
    r = [1]
    for _ in range(k): r = mul(r, p)
    return r

A = [0, 0, 1, 1, 1]
B = [0, 1, 2, 1]
C = [0, 0, 2, 1]

def matmul(X, Y):
    q = len(X)
    Z = [[[0] for _ in range(q)] for _ in range(q)]
    for i in range(q):
        for k in range(q):
            if any(X[i][k]):
                for j in range(q):
                    if any(Y[k][j]): Z[i][j] = add(Z[i][j], mul(X[i][k], Y[k][j]))
    return Z

T = [
    [C, B, [0], [0]],
    [[0], [0], A, A],
    [B, B, [0], [0]],
    [[0], [0], A, A]
]

def trace(p):
    return trim(sum_polys([p[i][i] for i in range(len(p))]))

def sum_polys(xs):
    r = [0]
    for x in xs: r = add(r, x)
    return r

def matrix_values(up_to):
    R = {}
    P = T
    for n in range(1, up_to+1):
        R[n] = trace(P)
        P = matmul(P, T)
    return R

def subset_formula(n):
    r = [0]
    for mask in range(1 << n):
        t = mask.bit_count()
        d = sum(bool((mask >> ((i-1) % n)) & 1 or (mask >> ((i+1) % n)) & 1)
                for i in range(n) if not ((mask >> i) & 1))
        rem = n-t-d
        p = mul(mul(power(A, t), power(B, d)), power(C, rem))
        r = add(r, p)
    return r

def brute(n):
    counts = Counter()
    for vals in product(range(3), repeat=2*n):
        bases = vals[:n]
        leaves = vals[n:]
        if not all((leaves[i] != 0 or bases[i] == 2)
                   and (bases[i] != 0 or leaves[i] == 2
                        or bases[(i-1) % n] == 2
                        or bases[(i+1) % n] == 2)
                   for i in range(n)):
            continue
        counts[sum(vals)] += 1
    r = [counts[i] for i in range(4*n+1)]
    return trim(r)


def min_count_expected(n):
    k, rem = divmod(n, 3)
    if rem == 0: return 3
    if rem == 1: return n*(k+6)//2
    return n


def main():
    mat = matrix_values(14)
    n_brute = 0
    for n in range(3, 7):
        b = brute(n)
        assert b == mat[n] == subset_formula(n), (n, b, mat[n])
        n_brute += 3**(2*n)
    for n in range(7, 13):
        assert mat[n] == subset_formula(n), n
    P = [0,0,3,2,1]                 # A + C
    Q = [0,0,0,1,1,1]               # z*A
    R = mul(mul(A,B), [0,1])        # z*A*B
    for n in range(4, 15):
        cand = add(add(mul(P,mat[n-1]),mul(Q,mat[n-2])),mul(R,mat[n-3]))
        assert cand == mat[n], n
    assert mat[3] == [0,0,0,0,3,18,54,81,75,47,21,6,1]
    for n in range(3,15):
        p=mat[n]
        nz=next(i for i,c in enumerate(p) if c)
        assert nz == n + ceil(n/3), (n,nz)
        assert p[nz] == min_count_expected(n), (n,p[nz],min_count_expected(n))
        assert p[-1] == 1
    print('VERIFY_OK brute_orders=3..6 assignments='+str(n_brute)
          +' subset_orders=3..12 trace_orders=3..14'
          +' polynomial_recurrence_orders=4..14 minimum_counts=3..14')

if __name__ == '__main__': main()
