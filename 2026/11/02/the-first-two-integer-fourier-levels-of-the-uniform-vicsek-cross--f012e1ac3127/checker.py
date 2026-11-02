#!/usr/bin/env python3
"""Supplementary finite checks for two Fourier levels of the five-map Vicsek cross.
This numerical checker is NOT a proof of the all-integer-frequency theorem;
the paper supplies the analytic 3-adic first-divergence argument.
"""
import math
from fractions import Fraction

COUNT = 0

def check(test, detail):
    global COUNT
    assert test, detail
    COUNT += 1

# The rational lower-bound certificate is exact.
check(Fraction(58, 225) * Fraction(77, 81) > Fraction(6, 25),
      'rational lower bound for second level')
check(6 * 2 < 3 ** 3, 'every later deviation has cosine angle in (pi/2,pi)')

# Check first-digit and second-digit residue case separations numerically.
def mask_int(m, n, j):
    denominator = 3 ** j
    return abs(1 + 2 * math.cos(2 * math.pi * (m % denominator) / denominator)
               + 2 * math.cos(2 * math.pi * (n % denominator) / denominator)) / 5

for m in range(9):
    for n in range(9):
        if m % 3 == n % 3 == 0:
            continue
        v = mask_int(m, n, 1) * mask_int(m, n, 2)
        active = (m % 3 != 0) + (n % 3 != 0)
        keep = False
        if active == 1:
            a = m if m % 3 else n
            b = n if m % 3 else m
            keep = b % 9 == 0 and min(a % 9, (-a) % 9) in (1, 2)
        if not keep:
            check(v < .24 + 1e-12, ('residue cutoff',m,n,v))
        else:
            check(v > .24 - 1e-12, ('residue survivor',m,n,v))

# Each off-path lift at level >=3 has mask strictly smaller than 3/5.
for j in range(3, 9):
    scale = 3 ** (j - 1)
    for a in (1, 2):
        for sign in (-1, 1):
            for lift_x in (-1, 0, 1):
                for lift_y in (-1, 0, 1):
                    if lift_x == lift_y == 0:
                        continue
                    x = sign * a + lift_x * scale
                    y = lift_y * scale
                    z = mask_int(x, y, j)
                    check(z < 3/5 + 1e-12,
                          ('off-path factor',j,a,sign,lift_x,lift_y,z))

# Numerical infinite-products; 50 terms yield more than enough accuracy.
def first_level(a):
    p = 2/5
    for j in range(2, 51):
        p *= (3+2*math.cos(2*math.pi*a/(3**j)))/5
    return p

A = first_level(1)
B = first_level(2)
check(A > B > .24, (A,B))
check(abs(A-0.3581726074759164) < 3e-15, A)
check(abs(B-0.25500512309614025) < 3e-15, B)

# Independent finite-frequency checks. They are not exhaustive over Z^2.
N = 120
J = 15
angles = [[math.cos(2*math.pi*x/(3**j)) for x in range(-N,N+1)]
          for j in range(1,J+1)]
threshold_margin = 2e-8  # truncation cannot affect the coarse .24 separator here
for x in range(-N,N+1):
    for y in range(-N,N+1):
        if x == y == 0:
            continue
        v = 1.0
        for cj in angles:
            v *= abs(1 + 2*cj[x+N] + 2*cj[y+N]) / 5
        def strip3(a,b):
            while a % 3 == b % 3 == 0 and (a or b):
                a //= 3
                b //= 3
            return a,b
        sx,sy=strip3(x,y)
        if (sx,sy) in {(1,0),(-1,0),(0,1),(0,-1)}:
            check(abs(v-A)<3e-8, ('first level',x,y,v,A))
        elif (sx,sy) in {(2,0),(-2,0),(0,2),(0,-2)}:
            check(abs(v-B)<3e-8, ('second level',x,y,v,B))
        else:
            check(v < .24 + threshold_margin, ('remaining gap',x,y,v))

print('VICSEK_CROSS_FOURIER_CHECK_OK', COUNT, 'finite assertions',
      'A=', format(A,'.16f'), 'B=',format(B,'.16f'))
