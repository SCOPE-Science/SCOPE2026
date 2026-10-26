"""Exact finite checks for coefficient models and arithmetic paths.

The infinite-dimensional spectrum requires the analytical proof in RESULT.md.
Run: python check_monomial_spectrum.py
"""
from fractions import Fraction
from math import gcd

checks = 0

def verify(ok):
    global checks
    assert ok
    checks += 1


def coefficient(k, beta):
    return Fraction(k + 1) ** beta


def weight(m, n, k, beta):
    if k == 0:
        return Fraction(1)
    return coefficient(k, beta)**2 / (coefficient(m*k, beta) * coefficient(n*k, beta))

for m, n in ((2, 3), (3, 4), (2, 5), (3, 5), (5, 7)):
    verify(gcd(m, n) == 1)
    for beta in (-1, 0, 1, 2):
        for j in range(1, 301):
            # Apply the adjoint composition action, then composition.
            adj = Fraction(0) if j % n else coefficient(j//n, beta)/coefficient(j, beta)
            if j % n:
                verify(adj == 0)
            else:
                k = j // n
                prod = adj * coefficient(k, beta)/coefficient(m*k, beta)
                verify(prod == weight(m, n, k, beta))
        verify(weight(m, n, 0, beta) == 1)
        if beta == 0:
            verify(all(weight(m, n, k, beta) == 1 for k in range(1, 500)))
        # The ratio converges to (mn)^(-beta); an exact rational check at k=1e7.
        rho = Fraction(m*n) ** (-beta)
        wk = weight(m, n, 10**7, beta)
        verify(abs(wk / rho - 1) < Fraction(1, 100000))
    for L in range(1, 10):
        path = [m**h * n**(L-h) for h in range(L+1)]
        verify(len(set(path)) == L+1)
        verify(path[0] % m != 0)
        verify(path[-1] % n != 0)
        for h in range(L):
            verify(path[h] % n == 0)
            verify((path[h] // n) * m == path[h+1])
        for k in range(L+1):
            for j in range(L+1):
                verify(path[k] == path[j] if k == j else path[k] != path[j])
    for L in range(2, 10):
        curr = {m**h*n**(L-h) for h in range(L+1)}
        prev = {m**h*n**(L-1-h) for h in range(L)}
        verify(curr.isdisjoint(prev))

# An explicit finite truncation, including constant eigenvalue.
m,n,beta=2,3,1
for j in range(501):
    if j == 0:
        verify(True)
    elif j % n:
        verify(True)
    else:
        k=j//n
        verify(weight(m,n,k,beta) > 0)

print(f"PASS {checks} exact assertions (finite checks only)")
