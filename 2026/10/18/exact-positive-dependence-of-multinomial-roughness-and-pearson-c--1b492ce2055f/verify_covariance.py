#!/usr/bin/env python3
"""Exact rational checks for multinomial collision/roughness covariance identities.

Standard-library only; enumerations are complete at the finite specified sizes.
"""
from fractions import Fraction as F
from math import factorial


def compositions(total, cells):
    if cells == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, cells - 1):
            yield (first,) + rest


def multinomial_probability(counts, probabilities):
    out = F(factorial(sum(counts)))
    for k, p in zip(counts, probabilities):
        out *= p ** k / factorial(k)
    return out


def mean(N, p, function):
    return sum((multinomial_probability(x, p) * function(x)
                for x in compositions(N, len(p))), F(0))


def doubled(counts, i):
    y = list(counts)
    y[i] += 2
    return tuple(y)


def separated(counts, i, j):
    y = list(counts)
    y[i] += 1
    y[j] += 1
    return tuple(y)


def collision_statistic(x, p):
    N = sum(x)
    return sum((F(x[i] * (x[i] - 1)) / p[i]
                for i in range(len(p))), F(0)) / (N * (N - 1)) - 1


def convex_identity(N, p, f):
    cov = mean(N, p, lambda x: f(x) * collision_statistic(x, p))
    rhs = F(0)
    n = len(p)
    for x in compositions(N - 2, n):
        px = multinomial_probability(x, p)
        for i in range(n):
            for j in range(n):
                gap = (f(doubled(x, i)) + f(doubled(x, j))) / 2 - f(separated(x, i, j))
                rhs += px * p[i] * p[j] * gap
    return cov, rhs


def edge_covariance(N, n):
    p = (F(1, n),) * n
    def q(x):
        return F(n, N) * sum(v * v for v in x) - N
    def edge(x):
        return abs(x[1] - x[0])
    return mean(N, p, lambda x: edge(x) * q(x)) - mean(N, p, edge) * mean(N, p, q)


def edge_formula(N, n):
    p = (F(1, n),) * n
    q = F(1, n)
    m = N - 2
    P0 = mean(m, p, lambda x: int(x[1] == x[0]))
    P1 = mean(m, p, lambda x: int(x[1] - x[0] == 1))
    return 4 * (N - 1) * q * (q * P0 + (1-q) * P1)


def graph_tv(x, edges):
    return sum(w * abs(x[i] - x[j]) for i,j,w in edges)

for n in range(2, 7):
    for N in range(2, 8):
        assert edge_covariance(N, n) == edge_formula(N, n), (n, N)
print('all 30 uniform single-edge cases agree exactly (2 <= n <= 6, 2 <= N <= 7)')

for p in ((F(1,2), F(1,3), F(1,6)), (F(1,3),)*3, (F(1,2),)*2):
    for N in range(2,8):
        for f in (
            lambda x: F(sum((x[i]-x[(i+1)%len(x)])**2 for i in range(len(x)))),
            lambda x: F(sum(abs(x[i]-x[i+1]) for i in range(len(x)-1))),
            lambda x: F(sum(v*v for v in x))):
            lhs, rhs = convex_identity(N, p, f)
            assert lhs == rhs and lhs > 0, (p,N,lhs,rhs)
print('54 multinomial convex covariance identities agree exactly, with positive covariance')

# Two nonisomorphic simple graphs with four vertices, plus a weighted graph.
for N in range(2,7):
    n = 4; p = (F(1,n),)*n
    for edges in (
        [(0,1,F(1)), (1,2,F(1)), (2,3,F(1))],
        [(0,1,F(1)), (0,2,F(1)), (0,3,F(1))],
        [(0,1,F(2)), (1,3,F(3,2)), (2,3,F(1,3))]):
        tv = lambda x: graph_tv(x, edges)
        Q = lambda x: F(n,N)*sum(v*v for v in x)-N
        cov = mean(N,p,lambda x:tv(x)*Q(x))-mean(N,p,tv)*mean(N,p,Q)
        assert cov == sum((e[2] for e in edges), F(0))*edge_formula(N,n)
print('15 weighted-graph checks agree exactly')
