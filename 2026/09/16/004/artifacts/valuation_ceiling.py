"""Reproducible ceiling computation for Li-Miao Question 4.20.

Compares the (1^{d-2},2^{n-d+1}) weighted-blowup valuative ceiling phi(T)
(Eqs. 25-29 of arXiv:2506.17420v3) against the conjectured stratified bound
vol(P^{d-1} x P^{n-d+1}). Also compares ell=1 vs ell=2 valuations.

Usage: python3 valuation_ceiling.py  (requires only stdlib)
"""
from math import comb


def ceiling(n, d, ell=2):
    A = (d - 2) + ell * (n - d + 1)

    def phi(x):
        if x <= d:
            return (ell ** (-(n - d + 1))) * (x ** (n - 1)) * (d * n - (d - 2) * x)
        s = 0.0
        for j in range(0, n - d + 2):
            s += comb(n, j) * (n - d + 2 - j) * (d ** (n - j)) * ((x - d) ** j)
        return (ell ** (-(n - d + 1))) * s

    def Phi(x):
        if x <= d:
            return (ell ** (-(n - d + 1))) * (x ** n) / (n + 1) * (d * (n + 1) - (d - 2) * x)
        s = 0.0
        for j in range(0, n - d + 3):
            s += comb(n + 1, j) * (n - d + 3 - j) / (n + 1) * (d ** (n + 1 - j)) * ((x - d) ** j)
        return (ell ** (-(n - d + 1))) * s

    def Psi(x):
        return (x - A) * phi(x) - Phi(x)

    lo, hi = float(A), float(A + 1)
    while Psi(hi) < 0:
        hi = hi * 1.5 + 1.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if Psi(mid) < 0:
            lo = mid
        else:
            hi = mid
    T = (lo + hi) / 2.0
    return T, phi(T), A


def product_bound(n, d):
    return comb(n, d - 1) * (d ** (d - 1)) * ((n - d + 2) ** (n - d + 1))


if __name__ == "__main__":
    print(f"{'n':>3} {'d':>3} {'T':>9} {'phi(T)':>16} {'strat.bound':>16} {'ratio':>7}")
    for n in [4, 5, 6, 7, 8, 10]:
        for d in range(3, n):
            T, ph, _ = ceiling(n, d, ell=2)
            cb = product_bound(n, d)
            print(f"{n:>3} {d:>3} {T:>9.4f} {ph:>16.1f} {cb:>16d} {ph / cb:>7.4f}")
