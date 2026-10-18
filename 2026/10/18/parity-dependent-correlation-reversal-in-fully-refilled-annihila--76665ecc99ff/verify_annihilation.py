"""Independent full-generator check of the finite complete-graph annihilation law.
Run: python verify_annihilation.py (requires numpy and scipy)."""
from math import prod, comb
import numpy as np
from scipy.linalg import solve

def theoretical(n, r):
    levels = list(range(n, -1, -2))
    probs = {}
    reached = 1.0
    for k in levels:
        a = k * (k - 1)
        probs[k] = reached * r / (r + a)
        if a:
            reached *= a / (r + a)
    return probs

def generator(n, r):
    m = 1 << n
    Q = np.zeros((m, m))
    full = m - 1
    for x in range(m):
        for i in range(n):
            if not (x & (1 << i)):
                continue
            for j in range(n):
                if i == j:
                    continue
                if x & (1 << j):
                    y = x & ~(1 << i) & ~(1 << j)
                else:
                    y = x ^ (1 << i) ^ (1 << j)
                Q[x, y] += 1
        Q[x, full] += r
        Q[x, x] -= Q[x, :].sum()
    return Q

def main():
    comparisons = 0
    for n in range(2, 8):
        for r in (0.13, 0.7, 2.5, 9.0):
            Q = generator(n, r)
            A = Q.T.copy()
            A[-1, :] = 1
            b = np.zeros(1 << n)
            b[-1] = 1
            pi = solve(A, b, assume_a='gen')
            p = theoretical(n, r)
            for x, actual in enumerate(pi):
                k = x.bit_count()
                predicted = p.get(k, 0.0) / comb(n, k)
                assert abs(actual-predicted) < 3e-12, (n, r, x, actual, predicted)
                comparisons += 1
            mu = sum(k*v for k,v in p.items()) / n
            c = sum(k*(k-1)*v for k,v in p.items()) / (n*(n-1)) - mu*mu
            empirical = sum(pi[x] for x in range(1<<n) if (x & 3)==3) - (sum(pi[x] for x in range(1<<n) if x&1))* (sum(pi[x] for x in range(1<<n) if x&2))
            assert abs(c-empirical) < 3e-12
    print(f'PASS: {comparisons} state probabilities and 24 pair covariances, independent full generators')
if __name__ == '__main__':
    main()
