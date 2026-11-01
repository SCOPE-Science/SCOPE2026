#!/usr/bin/env python3
"""Exact rational verification of a finite Blaschke Hankel witness."""
from fractions import Fraction as F

N = 5  # coefficients through degree four


def mul(a, b):
    out = [F(0)] * N
    for i in range(N):
        for j in range(N - i):
            out[i + j] += a[i] * b[j]
    return out


# The Schwarz function is (z-3z^2+8z^3)/(8-3z+z^2).
numer = [F(0), F(1), F(-3), F(8), F(0)]
den = [F(8), F(-3), F(1), F(0), F(0)]
w = [F(0)] * N
for k in range(N):
    w[k] = (numer[k] - sum(den[j] * w[k - j] for j in range(1, k + 1))) / den[0]
assert w == [F(0), F(1, 8), F(-21, 64), F(441, 512), F(1491, 4096)]
assert mul(den, w) == numer

sq = mul(w, w)
cu = mul(sq, w)
q = [F(int(i == 0)) + w[i] + sq[i] / 3 - cu[i] / 9 for i in range(N)]
assert q == [F(1), F(1, 8), F(-31, 96), F(1921, 2304), F(1939, 4096)]

a2 = q[1] / 2
a3 = q[2] / 2
a4 = (q[3] + q[1] * a3) / 4
a5 = (q[4] + q[2] * a3) / 4
assert (a2, a3, a4, a5) == (F(1, 16), F(-31, 192), F(3749, 18432), F(19373, 147456))

# Coefficients of z f'(z)/g(z) with g(z)=z+a3*z^3+a5*z^5+...
assert (F(1), 2 * a2, 2 * a3, 4 * a4 - 2 * a2 * a3, 4 * a5 - 2 * a3 * a3) == tuple(q)

hankel = 2 * a2 * a3 * a4 - a3**3 - a4**2 + a3 * a5 - a2**2 * a5
assert hankel == F(-10700387, 169869312)
assert -hankel - F(1, 16) == F(83555, 169869312) > 0
assert -hankel - F(769, 12288) == F(69731, 169869312) > 0

# Blaschke zeros: (3 +/- i*sqrt(23))/16; squared modulus 32/256 = 1/8.
assert F(3**2 + 23, 16**2) == F(1, 8) < 1
print('PASS: exact Schwarz series, target series, class coefficients, identity and both rational gaps')
