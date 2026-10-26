"""Numerical cross-checks of the exact two-level stochastic Rayleigh--Ritz gap law.

Run with Python 3, NumPy and SciPy: python verify.py.
The infinite-dimensional/finite-time theorem is proved analytically in RESULT.md;
these finite checks are not substitutes for that proof.
"""
import math
import numpy as np
from scipy.special import beta, digamma

rng = np.random.default_rng(20261018)
count = 0

def chk(predicate, message):
    global count
    count += 1
    if not predicate:
        raise AssertionError(message)

for d in (3, 4, 6, 11):
    m = d - 1
    for s in range(1, m + 1):
        for _ in range(24):
            e = rng.normal(size=d); e /= np.linalg.norm(e)
            v = rng.normal(size=d); v /= np.linalg.norm(v)
            lam_low, lam_high = .4, 3.1
            H = lam_low * np.eye(d) + (lam_high - lam_low) * np.outer(e, e)
            G = rng.normal(size=(d, s))
            G -= np.outer(v, v @ G)
            Q, _ = np.linalg.qr(G)
            V = np.column_stack((v, Q))
            M = V.T @ H @ V
            eig, vec = np.linalg.eigh(M)
            updated = V @ vec[:, -1]
            old_gap = lam_high - v @ H @ v
            gap_new = lam_high - updated @ H @ updated
            w = e - (v @ e) * v
            w /= np.linalg.norm(w)
            predicted = 1 - np.linalg.norm(Q.T @ w) ** 2
            chk(abs(gap_new / old_gap - predicted) < 3e-11,
                (d, s, gap_new, old_gap, predicted))
            if s == m:
                chk(abs(gap_new) < 3e-11, 'full tangent recovers eigenvector')

for d in (3, 5, 12, 36):
    m = d - 1
    for s in range(1, m):
        a, b = (m-s)/2, s/2
        for p in (1, 2, 3):
            expected = math.prod((a + j)/(a+b + j) for j in range(p))
            chk(abs(beta(a+p, b)/beta(a,b)-expected)<3e-13, 'beta moment')
        chk(abs((digamma(m/2)-digamma((m-s)/2)) +
                (digamma((m-s)/2)-digamma(m/2))) < 1e-13, 'log moment')
        if s >= 2:
            chk(1-s/m < (1-1/m)**s, 'strict block budget gain')

for d in (3, 4, 7, 19):
    m=d-1
    for s in range(1,m):
        a,b=(m-s)/2,s/2
        draws = rng.beta(a,b, size=250000)
        mean = float(draws.mean())
        true = 1-s/m
        std = math.sqrt((a*b)/((a+b)**2*(a+b+1))/len(draws))
        chk(abs(mean-true) < max(7*std, 0.002), 'sampled Beta mean')

print(f'PASS: {count} deterministic finite assertions, including exact Ritz and sampled Beta moments')
