#!/usr/bin/env python3
"""Exact finite diagnostic of exterior-Gram identities; Python standard library only.

This is not an infinite-dimensional proof. The proof uses an analytic summable
remainder bound, which the finite computation cannot replace.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, prod

assertions = 0

def require(condition):
    global assertions
    assert condition
    assertions += 1

def det(M):
    size = len(M)
    if size == 0:
        return F(1)
    if size == 1:
        return M[0][0]
    return sum((-1)**j * M[0][j] * det([row[:j] + row[j+1:] for row in M[1:]])
               for j in range(size))

def vector(n):
    return (F(1, n), F(2, n*n), F(3, n*n*n))

def gram(rows):
    return [[sum(a*b for a, b in zip(v, u)) for u in rows] for v in rows]

def gram_minor(indices):
    return det(gram([vector(n) for n in indices]))

def elementary_sum(M, k):
    return sum((det([[M[i][j] for j in I] for i in I])
                for I in combinations(range(len(M)), k)), F(0))

D = [F(1), F(14), F(133, 64), F(1, 324)]
for k in range(1, 4):
    require(gram_minor(tuple(range(1, k+1))) == D[k])
    require(D[k] > 0)

for N in range(4, 10):
    for R in range(1, 5):
        G = [[sum(F(vector(n)[i] * vector(n)[j], n**(2*R))
                  for n in range(1, N+1))
              for j in range(3)] for i in range(3)]
        for k in range(1, 4):
            coeffs = [(I, gram_minor(I)) for I in combinations(range(1, N+1), k)]
            total = sum((minor * F(1, prod(I)**(2*R))
                         for I, minor in coeffs), F(0))
            require(elementary_sum(G, k) == total)
            leading = D[k] * F(1, factorial(k)**(2*R))
            require(total >= leading)
            remainder = total - leading
            p1 = factorial(k-1) * (k+1)
            # Every other tuple has product at least p1.
            require(all(prod(I) >= p1
                        for I, _ in coeffs if I != tuple(range(1, k+1))))
            reference_tail = sum((minor * F(1, prod(I)**2)
                                  for I, minor in coeffs
                                  if I != tuple(range(1, k+1))), F(0))
            require(remainder <= reference_tail * F(1, p1**(2*(R-1))))
print(f"PASS: {assertions} exact rational finite diagnostic assertions")
