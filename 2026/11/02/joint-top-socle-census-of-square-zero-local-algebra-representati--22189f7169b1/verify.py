"""Finite-field verification of the joint radical/socle matrix count.

Uses only Python's standard library. Each configuration is exhaustive.
F4 is represented by F2[u]/(u^2+u+1).
"""
import itertools
import math


def mul(x, y, q):
    if q != 4:
        return x*y % q
    raw = 0
    for i in range(2):
        for j in range(2):
            if ((x >> i) & 1) and ((y >> j) & 1):
                raw ^= 1 << (i+j)
    if raw & 8:
        raw ^= 0b1110
    if raw & 4:
        raw ^= 0b111
    return raw


def add(x, y, q):
    return x ^ y if q in (2, 4) else (x+y) % q


def sub(x, y, q):
    return x ^ y if q in (2, 4) else (x-y) % q


def field_rank(rows, q):
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    nr, nc = len(matrix), len(matrix[0])
    h = 0
    for col in range(nc):
        pivot = next((i for i in range(h, nr) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[h], matrix[pivot] = matrix[pivot], matrix[h]
        inverse = next(z for z in range(1, q) if mul(matrix[h][col], z, q) == 1)
        matrix[h] = [mul(z, inverse, q) for z in matrix[h]]
        for i in range(nr):
            if i != h and matrix[i][col]:
                fac = matrix[i][col]
                matrix[i] = [sub(matrix[i][j], mul(fac, matrix[h][j], q), q)
                             for j in range(nc)]
        h += 1
        if h == nr:
            break
    return h


def gaussian(n, k, q):
    if not 0 <= k <= n:
        return 0
    top = bottom = 1
    for j in range(k):
        top *= q**(n-j)-1
        bottom *= q**(k-j)-1
    return top // bottom


def exact_fiber(a, c, r, q):
    # Two independent subspace-Moebius inversions. This expression
    # is deliberately different from the single-inversion proof formula.
    return sum((-1)**(a-i+c-j)
               * q**(math.comb(a-i, 2)+math.comb(c-j, 2)+r*i*j)
               * gaussian(a, i, q) * gaussian(c, j, q)
               for i in range(a+1) for j in range(c+1))


def theoretical_distribution(d, r, q):
    return {(a,c):gaussian(d,a,q)*gaussian(d-a,c,q)*exact_fiber(a,c,r,q)
            for a in range(d+1) for c in range(d-a+1)}


def matrices(d, q):
    for entries in itertools.product(range(q), repeat=d*d):
        yield tuple(tuple(entries[i*d+j] for j in range(d)) for i in range(d))


def is_zero_product(X, Y, d, q):
    for i in range(d):
        for j in range(d):
            s = 0
            for k in range(d):
                s = add(s, mul(X[i][k], Y[k][j], q), q)
            if s:
                return False
    return True


def enumerate_distribution(d, r, q):
    # Eliminating matrices that are not square-zero greatly reduces the search.
    candidates = [M for M in matrices(d,q) if is_zero_product(M,M,d,q)]
    result = {(a,c):0 for a in range(d+1) for c in range(d-a+1)}
    for tup in itertools.product(candidates, repeat=r):
        if any(not is_zero_product(X, Y, d, q) for X in tup for Y in tup):
            continue
        horizontal = [[tup[t][i][j] for t in range(r) for j in range(d)]
                      for i in range(d)]
        vertical = [[tup[t][i][j] for j in range(d)]
                    for t in range(r) for i in range(d)]
        a, c = field_rank(horizontal,q),field_rank(vertical,q)
        result[a,c] += 1
    return {k:v for k,v in result.items() if v}


def check():
    cases = [(1,1,2),(2,1,2),(3,1,2),(4,1,2),
             (2,2,2),(3,2,2),(2,3,2),(2,2,3),(2,2,4),(3,2,3),(2,3,3),(2,2,5),(3,2,4)]
    for d,r,q in cases:
        actual = enumerate_distribution(d,r,q)
        predicted = {k:v for k,v in theoretical_distribution(d,r,q).items() if v}
        assert actual == predicted, (d,r,q,actual,predicted)
        print('PASS', 'dimension',d,'loops',r,'field',q,
              'total',sum(actual.values()),'joint_distribution',actual)
    print('RADICAL_SQUARE_ZERO_TOP_SOC_CENSUS_OK', len(cases))


if __name__ == '__main__':
    check()
