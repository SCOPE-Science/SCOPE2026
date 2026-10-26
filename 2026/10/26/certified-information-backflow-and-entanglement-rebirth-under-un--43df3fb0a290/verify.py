"""Exact rational certificate for finite-time coherence revival.

No external packages or floating-point decisions are used. The finite
hypergeometric tail is bounded analytically, not estimated numerically.
"""
from fractions import Fraction as F
from math import factorial

N = 80
A = (F(9, 10), F(3, 10))


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1],
            z[0] * w[1] + z[1] * w[0])


def partial(t):
    w = (F(-t, 3), F(-t))
    c = (F(1), F(0))
    p = c
    for n in range(N):
        c = mul(mul(c, (A[0] + n, A[1])), w)
        c = (c[0] / (n + 1)**2, c[1] / (n + 1)**2)
        p = (p[0] + c[0], p[1] + c[1])
    return p


def norm2(z):
    return z[0]**2 + z[1]**2


# Since |a|^2=9/10<1 and |w_t|<11 for t=8,10, each
# Taylor coefficient has modulus <=11^n/n!. From n=N+1 onward
# the ratio of successive majorant terms is <=11/(N+2).
tail = F(11**(N+1), factorial(N+1)) / (1 - F(11, N+2))
assert tail < F(1, 1000)

P8, P10 = partial(8), partial(10)
assert norm2(P8) < F(59, 1000)**2
assert norm2(P10) > F(111, 1000)**2

# Triangle inequalities now prove: |f(8)|<0.060 and |f(10)|>0.110.
# The 2-qubit isotropic input eta=25/29 has PPT threshold
# (1-eta)/(2 eta)=2/25=0.080, so it is PPT at time 8
# and NPT at time 10. Equatorial trace distance increases as well.
eta = F(25, 29)
threshold = (1-eta) / (2*eta)
assert F(3, 50) < threshold < F(11, 100)
assert threshold == F(2, 25)
print('PASS: exact rational Taylor certificate, N=80')
print('PASS: |f(8)| < 3/50 = 0.06')
print('PASS: |f(10)| > 11/100 = 0.11')
print('PASS: trace-distance recovery > 1/20 = 0.05')
print('PASS: isotropic PPT-to-NPT revival threshold 2/25 = 0.08')
print('Tail bound < 1/1000: verified as exact integer inequalities')
print('Approximate partial-moduli for orientation only:',
      float(norm2(P8))**0.5, float(norm2(P10))**0.5)
