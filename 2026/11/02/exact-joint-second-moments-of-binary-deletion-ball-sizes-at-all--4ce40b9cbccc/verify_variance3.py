#!/usr/bin/env python3
"""Exact rational-function certificate for binary three-deletion-ball moments.

Only Python's standard library is needed. All algebra is over Q[t].
The 9-state, bivariate-truncated transfer formula establishes the
all-length identities; direct word enumeration provides a separate check.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb

STATES = (None, 0, 1)

def matrix(bits, deletion=False):
    a = [[Q(0) for _ in range(3)] for _ in range(3)]
    for j, s in enumerate(STATES):
        if deletion:
            if s is None or s != bits:
                a[j][j] = Q(1)
        else:
            a[STATES.index(bits)][j] = Q(1)
    return a

def kron(a, b):
    return [[a[i // len(b)][j // len(b[0])] *
             b[i % len(b)][j % len(b[0])]
             for j in range(len(a[0]) * len(b[0]))]
            for i in range(len(a) * len(b))]

def add_matrix(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]

def half(a):
    return [[x / 2 for x in row] for row in a]

H0, H1 = matrix(0), matrix(1)
D0, D1 = matrix(0, True), matrix(1, True)
A = half(add_matrix(kron(H0, H0), kron(H1, H1)))
B = half(add_matrix(kron(D0, H0), kron(D1, H1)))
C = half(add_matrix(kron(H0, D0), kron(H1, D1)))
D = half(add_matrix(kron(D0, D0), kron(D1, D1)))
A1 = half(add_matrix(H0, H1))
B1 = half(add_matrix(D0, D1))

# Each polynomial is a dict exponent -> rational coefficient.
def p_add(a, b):
    c = defaultdict(Q)
    for i, x in a.items(): c[i] += x
    for i, x in b.items(): c[i] += x
    return {i: x for i, x in c.items() if x}

def p_mul(a, b):
    c = defaultdict(Q)
    for i, x in a.items():
        for j, y in b.items(): c[i + j] += x * y
    return {i: x for i, x in c.items() if x}

T = {1: Q(1)}
ONE_MINUS_T = {0: Q(1), 1: Q(-1)}

def v_add(a, b):
    return [p_add(x, y) for x, y in zip(a, b)]

def matvec(m, v):
    out = []
    for row in m:
        p = {}
        for c, q in zip(row, v):
            if c: p = p_add(p, {k: c * x for k, x in q.items()})
        out.append(p)
    return out

def scale_vector(p, v):
    return [p_mul(p, x) for x in v]

def fundamental(a, v):
    # ((1-t) I + t A) v, so U=((1-t)I+t A)/(1-t).
    return v_add(scale_vector(ONE_MINUS_T, v), scale_vector(T, matvec(a, v)))

def num_moment2():
    # N_ab/(1-t)^(a+b+1) is the coefficient of z^a w^b
    # in (I-t E[M_X(z) tensor M_X(w)])^-1 e_(empty,empty).
    v0 = [{} for _ in range(9)]; v0[0] = {0: Q(1)}
    N = {}
    for a in range(4):
        for b in range(4):
            if a == b == 0:
                N[a, b] = fundamental(A, v0)
                continue
            v = [{} for _ in range(9)]
            if a > 0: v = v_add(v, matvec(B, N[a - 1, b]))
            if b > 0: v = v_add(v, matvec(C, N[a, b - 1]))
            if a > 0 and b > 0:
                v = v_add(v, scale_vector(ONE_MINUS_T, matvec(D, N[a - 1, b - 1])))
            N[a, b] = scale_vector(T, fundamental(A, v))
    p = {}
    for x in N[3, 3]: p = p_add(p, x)
    return p

def num_mean():
    v = [{} for _ in range(3)]; v[0] = {0: Q(1)}
    v = fundamental(A1, v)
    for _ in range(3): v = scale_vector(T, fundamental(A1, matvec(B1, v)))
    p = {}
    for x in v: p = p_add(p, x)
    return p

EXPECTED_MEAN = {i + 3: Q(v, 8) for i, v in enumerate((8, -17, 14, -4))}
EXPECTED_SECOND = {i + 3: Q(v, 16) for i, v in enumerate((16, -54, 112, -117, 68, -24, 4))}

assert num_mean() == EXPECTED_MEAN, (num_mean(), EXPECTED_MEAN)
assert num_moment2() == EXPECTED_SECOND, (num_moment2(), EXPECTED_SECOND)

# Coefficient of t^n in polynomial numerator / (1-t)^d.
def gf_coeff(p, d, n):
    return sum(v * Q(comb(n - e + d - 1, d - 1))
               for e, v in p.items() if n >= e)

def ball3_greedy(word):
    dp = {(None, 0): 1}
    for bit in word[::-1]:
        nxt = defaultdict(int)
        for (s, deleted), v in dp.items():
            nxt[bit, deleted] += v  # keep the current bit
            if deleted < 3 and (s is None or s != bit):
                nxt[s, deleted + 1] += v  # canonical deletion
        dp = nxt
    return sum(v for (s, deleted), v in dp.items() if deleted == 3)

for n in range(3, 14):
    sum1 = sum2 = 0
    for wordint in range(1 << n):
        w = tuple((wordint >> i) & 1 for i in range(n))
        b = ball3_greedy(w)
        if n <= 11:
            # Independent deletion-mask enumeration (not the greedy automaton).
            brute = len({tuple(w[i] for i in range(n) if i not in rem)
                         for rem in combinations(range(n), 3)})
            assert b == brute, (n, wordint, b, brute)
        sum1 += b
        sum2 += b * b
    assert Q(sum1, 1 << n) == gf_coeff(EXPECTED_MEAN, 4, n)
    assert Q(sum2, 1 << n) == gf_coeff(EXPECTED_SECOND, 7, n)
    en = Q((n + 1) * (n*n - n + 6), 48)
    variance = Q((n - 3)*(n - 2)*(3*n**3 - 12*n*n - 13*n + 94), 768)
    assert Q(sum2, 1 << n) - en*en == variance

print('EXACT_GF_MEAN_NUMERATOR', sorted(EXPECTED_MEAN.items()))
print('EXACT_GF_SECOND_NUMERATOR', sorted(EXPECTED_SECOND.items()))
print('ALL_LENGTH_SYMBOLIC_IDENTITIES_OK')
print('DIRECT_ENUMERATION_AND_GREEDY_CHECKS_OK n=3..13; mask-brute n=3..11')
print('VARIANCE_FORMULA_OK n=3..13')
