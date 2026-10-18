#!/usr/bin/env python3
"""Exact nine-point sixth-moment arithmetic and finite consistency checks."""
import cmath
import itertools
import math


def conv(x, y):
    r = [0] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            r[i + j] += a * b
    return r


def moment9(x):
    c = conv(conv(x, x), x)
    bins = [0] * 9
    for k, a in enumerate(c):
        bins[k % 9] += a
    return sum(b * b for b in bins)


def moment_torus(x):
    c = conv(conv(x, x), x)
    return sum(a * a for a in c)


def sym(x):
    a, b, c, d = x
    A = math.sqrt((a*a + d*d) / 2)
    B = math.sqrt((b*b + c*c) / 2)
    return [A, B, B, A]


def h(t):
    return 5*t**5 + 20*t**4 + 5*t**3 - 30*t - 19


def ratio(t):
    return (10*t**6 + 30*t**5 + 90*t**4 + 60*t**3 + 90*t**2 + 11) / (4*(1+t*t)**3)


def arith_derivative_check():
    # Integer-polynomial products prove the stated derivative identity.
    N = [11, 0, 90, 60, 90, 30, 10]
    T = [1, 0, 1]
    left = conv([i * N[i] for i in range(1, len(N))], T)
    right = conv(N, [0, 6])
    p = [l-r for l, r in itertools.zip_longest(left, right, fillvalue=0)]
    expected = [0, 114, 180, 0, -30, -120, -30, 0]  # -6*t*h(t)
    assert p == expected, (p, expected)


# Exact rational check of the only ninth-period alias.
for x in itertools.product(range(4), repeat=4):
    mt = moment_torus(x)
    assert moment9(x) == mt + 2 * (x[0] * x[3])**3
    R0 = sum(a*a for a in x)
    R1 = sum(x[j]*x[j+1] for j in range(3))
    R2 = sum(x[j]*x[j+2] for j in range(2))
    R3 = x[0]*x[3]
    assert mt == R0**3 + 6*R0*(R1**2+R2**2+R3**2) + 6*R1**2*R2 + 12*R1*R2*R3
    xs = sym(x)
    assert moment9(xs) / (sum(y*y for y in xs)**3 or 1) + 1e-10 >= moment9(x) / (R0**3 or 1)

arith_derivative_check()
lo, hi = 1., 2.
for _ in range(120):
    mid = (lo+hi)/2
    if h(mid) > 0:
        hi = mid
    else:
        lo = mid
r = (lo+hi)/2
K6 = ratio(r)
assert 1.15548 < r < 1.15549
assert abs(K6 - 9.22297799401694) < 2e-12
for j in range(9):
    eta = cmath.exp(2j*math.pi*j/9)
    c = [1, r*eta, r*eta**2, eta**3]
    val = sum(abs(sum(c[k]*cmath.exp(2j*math.pi*k*m/9) for k in range(4)))**6 for m in range(9))/9
    assert abs(val / (sum(abs(x)**2 for x in c))**3 - K6) < 2e-11
# An affine phase not from nine roots gives a strict loss.
eta = cmath.exp(.07j)
c = [1,r*eta,r*eta**2,eta**3]
val = sum(abs(sum(c[k]*cmath.exp(2j*math.pi*k*m/9) for k in range(4)))**6 for m in range(9))/9
assert val/(sum(abs(x)**2 for x in c))**3 < K6 - 1e-5
print('Nine-point cubic Fourier norm certificate: PASS')
print('Exact integer 4^4 positive-input cases and autocorrelation identities: PASS')
print('Analytic ratio derivative polynomial identity: PASS')
print('Root in (1.15548,1.15549): PASS')
print('K_9^6 = %.14f' % K6)
print('Nine projective phase patterns reach the bound (numerically): PASS')
print('Non-ninefold affine phase has strict loss: PASS')
print('Finite tests are consistency checks; universal claims use the proof.')
