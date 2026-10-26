#!/usr/bin/env python3
"""Independent arithmetic checks for the unitary one-pivot tail theorem.

Uses only Python's standard library; finite diagnostics do not replace proofs.
"""
import cmath
import math

count = 0
for n in range(2, 23):
    cutoff_sq = max(2 - 2/n, 1 + n/4 - 2/n)
    for extra in (0.02, 0.5, 5.0):
        t = math.sqrt(cutoff_sq + extra)
        delta = 1 / (n * (t*t - 1) + 2)
        assert delta < 1/n and delta < 4/n**2
        for eta in (0.5, 0.1, 0.0001):
            q = (1-eta)*delta
            theta = 2*math.asin(n*math.sqrt(q)/2)
            z = cmath.exp(1j*theta) - 1
            U = [[(1 if i == j else 0) + z/n for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    s = sum(U[k][i].conjugate()*U[k][j] for k in range(n))
                    assert abs(s - (1 if i==j else 0)) < 1e-10
                    count += 1
            probs = [[abs(U[i][j])**2 / n for j in range(n)] for i in range(n)]
            measured = sum(probs[i][j] for i in range(n) for j in range(n)
                           if n-2+1/abs(U[i][j])**2 > n*t*t)
            assert abs(measured - (n-1)*q) < 1e-10
            assert measured < (n-1)*delta
            count += 4
print('PASS', count, 'unitary, residual, and exact-tail checks')
