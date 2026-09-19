from fractions import Fraction
from math import comb
import mpmath as mp

N = 80
A = [Fraction(0) for _ in range(N + 1)]
C = [Fraction(0) for _ in range(N + 1)]
A[0], A[1] = Fraction(1), Fraction(6)
C[0], C[1] = Fraction(0), Fraction(1)

for n in range(1, N):
    alpha = 4 * n * n * (16 * n * n - 1)
    p = 65*n**4 + 130*n**3 + 105*n**2 + 40*n + 6
    den = (n + 1)**4
    A[n + 1] = (p*A[n] - alpha*A[n - 1]) / den
    C[n + 1] = (p*C[n] - alpha*C[n - 1]) / den

assert all(a.denominator == 1 for a in A)

def W_closed(n):
    return Fraction(
        (4*n + 1) * comb(4*n, 2*n) * comb(2*n, n),
        (n + 1)**4,
    )

for n in range(N):
    W = A[n]*C[n + 1] - A[n + 1]*C[n]
    assert W == W_closed(n)

mp.mp.dps = 240
zeta3 = mp.zeta(3)
cA = 2*mp.sqrt(6)/(3*mp.pi**2)
cE = mp.sqrt(2)*mp.pi**3/84
cL = mp.sqrt(3)*mp.pi/9

print(f"exact Casoratian checks: {N}/{N}")
print("n   A_ratio              quotient_error_ratio  linear_form_ratio")
for n in (10, 20, 40, 80):
    an = mp.mpf(A[n].numerator)
    cn = mp.mpf(C[n].numerator) / C[n].denominator
    A_approx = cA * mp.mpf(64)**n / n**2 * (1 - mp.mpf(29)/(48*n))
    E_approx = cE * mp.mpf(64)**(-n) * (1 - mp.mpf(35)/(48*n))
    L_approx = cL / n**2 * (1 - mp.mpf(4)/(3*n))
    A_ratio = an / A_approx
    E_ratio = (zeta3/7 - cn/an) / E_approx
    L_ratio = (zeta3*an - 7*cn) / L_approx
    print(
        f"{n:<3d} "
        f"{mp.nstr(A_ratio, 18):<20} "
        f"{mp.nstr(E_ratio, 18):<21} "
        f"{mp.nstr(L_ratio, 18)}"
    )
