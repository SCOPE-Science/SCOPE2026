"""Finite exact-rational checks for the eventual width law."""
from fractions import Fraction
from math import comb, isqrt


def norm(n, k):
    total = 0
    for j in range(max(0, 2*k-n), k+1):
        total += (comb(k, j) * comb(n-k, k-j)
                  * abs(n * ((n-1)*j - k*(k-1))))
    return Fraction(total, k*(n-k)*comb(n, k))


def width(n):
    k = max(1, (isqrt(32*n+1)-1)//8)
    return k + (2*k*k + k//2 < n)


for n in (*range(20, 161), 300, 512):
    values = {k: norm(n, k) for k in range(1, n//2+1)}
    k = width(n)
    assert [j for j in values if values[j] == max(values.values())] == [k]
    assert values[k] == 1 + Fraction(2*n*(k-1)*comb(n-k, k),
                                     (n-k)*comb(n, k))

for k in range(3, 51):
    n = 2*k*k + k//2
    assert norm(n, k) > norm(n, k+1)
    assert norm(n+1, k) < norm(n+1, k+1)

print('Exact checks passed: 143 full smaller-width scans, 48 adjacent transition pairs.')
