"""Exact and high-precision checks for a squared-Hamming Gaussian kernel.

Run: python check.py. Repeats the finite character diagonalization, exact
rational boundary cases and a sharp critical-root bracket.
"""
from fractions import Fraction
from itertools import product
from math import comb
import mpmath as mp


def eigen(n, k, q):
    return sum(
        sum((-1)**h * comb(k, h) * comb(n-k, j-h)
            for h in range(max(0, j-(n-k)), min(j, k)+1)) * q**(j*j)
        for j in range(n+1)
    )


def parity(n, q):
    return sum((-1)**j*comb(n, j)*q**(j*j) for j in range(n+1))


def direct(n, k, q):
    ans = 0
    for x in product((0,1), repeat=n):
        ans += (-1)**sum(x[:k]) * q**sum(x)**2
    return ans


checks = 0
for q in (Fraction(1,16), Fraction(1,19), Fraction(7,128)):
    for n in range(1, 8):
        for k in range(n+1):
            assert direct(n, k, q) == eigen(n, k, q)
            checks += 1
for q in (Fraction(1,16), Fraction(1,17), Fraction(7,128)):
    m = q.denominator // q.numerator
    for n in (m-1,m,m+1,m+2):
        vals = [eigen(n, k, q) for k in range(n+1)]
        assert min(vals) == vals[-1]
        assert (min(vals) >= 0) == (parity(n,q) >= 0)
        if n <= m:
            assert all(v > 0 for v in vals)
        if n >= m+2:
            assert parity(n,q) < 0
        checks += n+1
mp.mp.dps = 70
for n in (17, 19, 24, 40):
    def B(q):
        return mp.fsum([(-1)**j*comb(n,j)*q**(j*j) for j in range(n+1)])
    a,b = mp.mpf(1)/n,mp.mpf(1)/(n-1)
    assert B(a)>0 and B(b)<0
    for _ in range(190):
        c=(a+b)/2
        if B(c)>0:
            a=c
        else:
            b=c
    root=(a+b)/2
    predicted = mp.mpf(1)/n + 1/(2*mp.mpf(n)**3)
    print(f'n={n}: root={mp.nstr(root,23)}, leading approximation={mp.nstr(predicted,23)}')
    assert abs(root-predicted) < 3 / mp.mpf(n)**4
print('PASS exact/numerical checks:', checks)
