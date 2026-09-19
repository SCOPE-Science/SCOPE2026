from fractions import Fraction
from math import comb
import mpmath as mp

mp.mp.dps = 320
N = 100
A = [0] * (N + 1)
C = [Fraction(0) for _ in range(N + 1)]
A[0], A[1] = 1, 6
C[0], C[1] = Fraction(0), Fraction(1)

for n in range(1, N):
    an = 4*n*n*(16*n*n - 1)
    pn = 65*n**4 + 130*n**3 + 105*n*n + 40*n + 6
    den = (n + 1)**4
    numA = pn*A[n] - an*A[n-1]
    assert numA % den == 0
    A[n+1] = numA // den
    C[n+1] = (pn*C[n] - an*C[n-1]) / den

# Independent finite checks of the binomial representation from AESZ #28.
for n in range(0, 13):
    s = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j >= n:
                s += comb(n, i)**2 * comb(n, j)**2 * comb(i + j, n)**2
    assert s == A[n]

# Exact Wronskian identity.
for n in range(0, N):
    W = A[n]*C[n+1] - A[n+1]*C[n]
    closed = Fraction((4*n + 1) * comb(4*n, 2*n) * comb(2*n, n), (n + 1)**4)
    assert W == closed

K = 2*mp.sqrt(6)/(3*mp.pi**2)
E = mp.sqrt(2)*mp.pi**3/84
print('mpmath', mp.__version__)
print('K = 2*sqrt(6)/(3*pi^2) =', mp.nstr(K, 60))
print('E = sqrt(2)*pi^3/84      =', mp.nstr(E, 60))
print('n  A_n*n^2/64^n                  ratio_to_K')
for n in (20, 50, 100):
    scaled_A = mp.mpf(A[n]) * n*n / mp.power(64, n)
    print(n, mp.nstr(scaled_A, 45), mp.nstr(scaled_A/K, 30))
print('n  64^n*(zeta(3)/7-C_n/A_n)     ratio_to_E')
for n in (20, 50, 100):
    r = mp.mpf(C[n].numerator) / mp.mpf(C[n].denominator) / mp.mpf(A[n])
    scaled_E = mp.power(64, n) * (mp.zeta(3)/7 - r)
    print(n, mp.nstr(scaled_E, 45), mp.nstr(scaled_E/E, 30))
