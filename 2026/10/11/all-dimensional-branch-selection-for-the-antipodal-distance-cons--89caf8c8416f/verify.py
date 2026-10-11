from fractions import Fraction
from math import factorial

PI_LO = Fraction(3, 1)
PI_HI = Fraction(22, 7)
SQRT3_HI = Fraction(7, 4)

def odd_double_factorial(m):
    out = 1
    for j in range(1, m + 1, 2):
        out *= j
    return out

def omega_upper(m):
    # Exact formula with pi replaced by the upper rational bound 22/7.
    if m % 2 == 0:
        k = m // 2
        return PI_HI**k / factorial(k)
    k = (m - 1) // 2
    return Fraction(2**(k + 1), odd_double_factorial(2*k + 1)) * PI_HI**k

def normalized_lower_certificate(n):
    # P <= positive first factor base? We need a lower bound, so pi -> PI_LO.
    P_lo = Fraction(2**(n - 1) * n, 1) * PI_LO
    # Q = 2/(sqrt(3)*(n+1)!*omega_{n+1}); use upper bounds in denominator.
    Q_lo = Fraction(2, 1) / (SQRT3_HI * factorial(n + 1) * omega_upper(n + 1))
    # A_n > 1/sqrt(n) iff A_n^(n(n+1)) * n^(n(n+1)/2) > 1.
    return (
        P_lo**(n + 1)
        * Q_lo**n
        * Fraction(n, 1)**(n * (n + 1) // 2)
    )

certs = {n: normalized_lower_certificate(n) for n in range(3, 14)}
assert all(c > 1 for c in certs.values())
n_min = min(certs, key=certs.get)
assert n_min == 3
assert certs[3] == Fraction(1944365472, 1771561)
assert certs[3] > 1000

# Elementary exact checks used in the analytic tail.
assert Fraction(12, 5)**2 < 6       # sqrt(6) > 12/5, hence sqrt(6)-2 > 2/5
assert 56 > 49                      # 2*sqrt(14) > 7, hence 1/(2 sqrt(14)) < 1/7
assert 729 > 686                    # terminal square check for 13 sqrt(6) > 28 + sqrt(14)
assert Fraction(125, 64) < 2        # 2^(1/3) > 5/4
assert Fraction(15625, 4096) > 3    # 3^(1/6) < 5/4

print("VERIFY_OK")
print("finite_block=3..13 exact_rational")
print("minimum_certificate_n=3")
print("minimum_certificate=1944365472/1771561")
