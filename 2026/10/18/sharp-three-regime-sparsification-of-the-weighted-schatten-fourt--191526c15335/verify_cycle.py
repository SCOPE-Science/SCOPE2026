#!/usr/bin/env python3
"""Reproducible exact-arithmetic finite checks for a four-cycle Schatten-fourth identity."""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    Bt = transpose(B)
    return [[sum(u * v for u, v in zip(row, col)) for col in Bt] for row in A]


def trace_square_gram(w, t):
    S = [[F(0) for _ in range(4)] for _ in range(4)]
    for j in range(4):
        S[(j + 1) % 4][j] = w[j]
    St = transpose(S)
    M = [[t * S[i][j] + (1 - t) * St[i][j] for j in range(4)] for i in range(4)]
    G = matmul(transpose(M), M)
    G2 = matmul(G, G)
    return sum(G2[i][i] for i in range(4))


def formula(w, t):
    x = [z*z for z in w]
    A = t**4 + (1-t)**4
    B = 4*t*t*(1-t)**2
    P = w[0]*w[1]*w[2]*w[3]
    return A*sum(v*v for v in x) + B*sum(x[i]*x[(i+1)%4] for i in range(4)) + 2*B*P


def claimed_minimum(t):
    A = t**4+(1-t)**4
    B = 4*t*t*(1-t)**2
    beta = B/A
    if beta <= F(1,2):
        return A/F(4)+3*B/F(8)
    if beta <= 1:
        return A-(2*A-B)**2/(6*A-4*B)
    return A/F(2)


def certificate_check():
    vals = [F(0), F(1,5), F(1,4), F(1,3), F(2,5), F(1,2), F(3,4), F(1)]
    tested = 0
    for t in vals:
        for tup in product([0, 1, 2], repeat=4):
            w = [F(v, 5) for v in tup]
            assert trace_square_gram(w, t) == formula(w, t)
            tested += 1
    # Exact phase-transition comparison of the three analytic branches,
    # using rational beta probes on both sides of their crossing points.
    for beta in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
        A=F(1);B=beta
        U=A/F(4)+3*B/F(8)
        R=A-(2*A-B)**2/(6*A-4*B)
        O=A/F(2)
        if beta<F(1,2): assert U<R and U<O
        if beta==F(1,2): assert U==R and R<O
        if F(1,2)<beta<1: assert R<U and R<O
        if beta==1: assert R==O and R<U
    for t in vals:
        # Exact rational simplex grid: not an exhaustive continuum certificate.
        for a in range(13):
            for b in range(13-a):
                for c in range(13-a-b):
                    d=12-a-b-c
                    x=[F(v,12) for v in (a,b,c,d)]
                    A=t**4+(1-t)**4;B=4*t*t*(1-t)**2
                    val=float(A*sum(v*v for v in x)+B*sum(x[i]*x[(i+1)%4] for i in range(4)))+2*float(B)*sqrt(float(x[0]*x[1]*x[2]*x[3]))
                    assert val+1e-12>=float(claimed_minimum(t)),(t,x,val)
    print('CYCLE_WEIGHTED_SCHATTEN_FOUR_EXACT_TRACE_AND_GRID_CHECK_OK',tested)

if __name__ == '__main__':
    certificate_check()
