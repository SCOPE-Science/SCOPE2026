#!/usr/bin/env python3
"""Finite-level numerical comparison for the Cantor/Bergman asymptotic, alpha=1.
Standard library only. Finite calculations are diagnostic, not an infinite proof.
"""
import math

def digits(n):
    arr = [0]
    for j in range(n):
        arr += [a + 2 * 3**j for a in arr]
    return arr

def beta_cdf(k, t):
    u = t / (1.0 + t)
    return ((k + 2) - (k + 1) * u) * u**(k + 1)

def finite_eigenvalue(k, n):
    return sum(beta_cdf(k, a + 1) - beta_cdf(k, a) for a in digits(n))

def profile_F(r, j=7, q=12):
    # nu on [0, 3**j] is 2**j times the pushforward of Cantor probability.
    scale = 3**j
    inv = 3**q
    acc = 0.0
    for a in digits(q):
        x = scale * (a + 0.5) / inv
        acc += math.exp(-r / x) / (x**3)
    return 2**j * r**2 * acc / (2**q)

if __name__ == '__main__':
    for m in (3, 4, 5):
        for r in (1.0, 1.7, 2.5):
            k = math.floor(r * 3**m)
            lhs = (1.5**m) * finite_eigenvalue(k, m + 4)
            rhs = profile_F(r)
            rel = abs(lhs-rhs)/rhs
            print(f'm={m} r={r:.1f} k={k} scaled={lhs:.9f} profile={rhs:.9f} rel={rel:.5f}')
            assert rel < 0.02
