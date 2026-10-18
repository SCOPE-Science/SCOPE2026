#!/usr/bin/env python3
"""Reproduce finite-matrix endpoint norms for an absorbing pure-birth chain.

Python 3 standard library only. Numeric tests do not replace the proofs.
"""
import math


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def identity(n):
    return [[float(i == j) for j in range(n)] for i in range(n)]


def matrix_exponential(a):
    """Taylor expansion after scaling, followed by repeated squaring."""
    n = len(a)
    rowbound = max(sum(abs(x) for x in row) for row in a)
    squares = max(0, math.ceil(math.log2(max(rowbound, 1e-30) / 0.4)))
    b = [[x / (2**squares) for x in row] for row in a]
    out = identity(n)
    term = identity(n)
    for k in range(1, 45):
        term = matmul(term, b)
        term = [[x / k for x in row] for row in term]
        for i in range(n):
            for j in range(n):
                out[i][j] += term[i][j]
    for _ in range(squares):
        out = matmul(out, out)
    return out


def generator(n):
    q = [[0.0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        q[i][i], q[i][i+1] = -1.0, 1.0
    return q


def predicted_norms(n, t):
    p = [math.exp(-t)]
    for k in range(1, n):
        p.append(p[-1] * t/k)
    mode = min(math.floor(t), n-1)
    infinity_norm = 2*p[mode]
    nonabsorbing = (2*p[mode]-p[-1]) if t < n-1 else p[-1]
    one_norm = max(nonabsorbing, sum(p))
    return infinity_norm, one_norm


def direct_norms(n, t):
    q = generator(n)
    expq = matrix_exponential([[t*x for x in row] for row in q])
    derivative = matmul(q, expq)
    return (max(sum(abs(x) for x in row) for row in derivative),
            max(sum(abs(derivative[i][j]) for i in range(n+1))
                for j in range(n+1)))


def main():
    checks = 0
    for n in range(1, 11):
        for t in (.02, .1, .25, .51, .9, 1., 1.03, 1.5, 1.99,
                  2.01, 2.7, 3.8, 4.99, 6.2, 8.7, 11.3):
            expect = predicted_norms(n, t)
            found = direct_norms(n, t)
            for x, y in zip(expect, found):
                assert abs(x-y) <= 2e-10 * max(1, abs(x))
                checks += 1
    for n in range(1, 21):
        optimal = 2*math.exp((n+1)*math.log(n)-n-math.lgamma(n+1))
        for k in range(1, 101):
            t = n*k/60.
            norm = predicted_norms(n, t)[0]
            assert t*norm <= optimal + 3e-12
            checks += 1
        norm = predicted_norms(n, float(n))[0]
        assert abs(n*norm-optimal) <= 1e-10*max(1, optimal)
        checks += 1
    for n in (20, 50, 100, 200):
        def f(t):
            p = [math.exp(-t)]
            for k in range(1, n):
                p.append(p[-1]*t/k)
            return sum(p)-t*p[-1]
        a, b = n/3., float(n)
        assert f(a)>0 and f(b)<0
        checks += 2
        for _ in range(100):
            c = (a+b)/2
            if f(c)>0:
                a=c
            else:
                b=c
        root = (a+b)/2
        assert abs(f(root)) < 5e-11
        assert root < n
        checks += 2
    print('CHECKER_OK', checks, 'finite comparisons')

if __name__ == '__main__':
    main()
