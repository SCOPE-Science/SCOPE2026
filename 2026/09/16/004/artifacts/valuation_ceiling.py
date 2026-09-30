"""Recompute the Li-Miao v1/v2 Corollary-2.5 ceilings for Question 4.20.

Uses equations (25), (29), (30) of arXiv:2506.17420v3.
Enumerates every pair 4 <= n <= 10, 3 <= d <= n-1.
Requires only Python stdlib.
"""
from math import comb


def ceiling(n, d, ell=2):
    A = (d - 2) + ell * (n - d + 1)

    def phi(x):
        if x <= d:
            return (ell ** (-(n - d + 1))) * (x ** (n - 1)) * (d * n - (d - 2) * x)
        return (ell ** (-(n - d + 1))) * sum(
            comb(n, j) * (n - d + 2 - j) * (d ** (n - j)) * ((x - d) ** j)
            for j in range(0, n - d + 2)
        )

    def Phi(x):
        if x <= d:
            return (ell ** (-(n - d + 1))) * (x ** n) / (n + 1) * (d * (n + 1) - (d - 2) * x)
        return (ell ** (-(n - d + 1))) * sum(
            comb(n + 1, j) * (n - d + 3 - j) / (n + 1) * (d ** (n + 1 - j)) * ((x - d) ** j)
            for j in range(0, n - d + 3)
        )

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
    print(f"{'n':>3} {'d':>3} {'T2':>10} {'phi2(T)':>16} {'bound':>16} {'ratio2':>9} {'phi1(T)':>16}")
    ratios = []
    for n in range(4, 11):
        for d in range(3, n):
            T2, ph2, _ = ceiling(n, d, ell=2)
            _, ph1, _ = ceiling(n, d, ell=1)
            b = product_bound(n, d)
            ratios.append(ph2 / b)
            print(f"{n:>3} {d:>3} {T2:>10.6f} {ph2:>16.6f} {b:>16d} {ph2 / b:>9.6f} {ph1:>16.6f}")
    assert len(ratios) == 28
    assert min(ratios) > 1.0
    print("pairs:", len(ratios), "min ratio:", min(ratios), "max ratio:", max(ratios))
