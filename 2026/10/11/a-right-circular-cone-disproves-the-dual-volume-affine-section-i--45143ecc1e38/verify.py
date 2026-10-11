#!/usr/bin/env python3
from fractions import Fraction as F
from math import isqrt

def sqrt_interval_rat(n, d=1, digits=40):
    T = 10**digits
    k = isqrt((n*T*T)//d)
    lo = F(k, T)
    hi = F(k+1, T)
    assert lo*lo <= F(n,d) <= hi*hi
    return lo, hi

def atanh_log_unit_interval(y, N=80):
    # y in [1,2); z in [0,1/3).
    assert F(1) <= y <= F(2)
    z = (y-F(1))/(y+F(1))
    s = F(0)
    zpow = z
    for k in range(N):
        s += zpow/F(2*k+1)
        zpow *= z*z
    lo = 2*s
    # First omitted exponent is 2N+1.
    rem = 2 * (z**(2*N+1)) / (F(2*N+1) * (F(1)-z*z))
    hi = lo + rem
    return lo, hi

def log_interval_pos(x, N=80):
    assert x > 0
    if x < 1:
        lo, hi = log_interval_pos(1/x, N)
        return -hi, -lo
    k = 0
    y = x
    while y >= 2:
        y /= 2
        k += 1
    ly_lo, ly_hi = atanh_log_unit_interval(y, N)
    l2_lo, l2_hi = atanh_log_unit_interval(F(2), N)
    return ly_lo + k*l2_lo, ly_hi + k*l2_hi

def log_interval(lo_x, hi_x, N=80):
    assert 0 < lo_x <= hi_x
    lo, _ = log_interval_pos(lo_x, N)
    _, hi = log_interval_pos(hi_x, N)
    return lo, hi

def atan_interval(x, N=80):
    # Alternating series, 0 <= x <= 1.
    assert F(0) <= x <= F(1)
    s = F(0)
    xpow = x
    for k in range(N):
        term = xpow/F(2*k+1)
        s = s + term if k % 2 == 0 else s - term
        xpow *= x*x
    err = x**(2*N+1)/F(2*N+1)
    return s-err, s+err

def add_int(a,b):
    return (a[0]+b[0], a[1]+b[1])

def mul_pos(a,b):
    assert a[0] >= 0 and b[0] >= 0
    return (a[0]*b[0], a[1]*b[1])

# Exact rational geometry identities.
assert F(1) + F(12,35)**2 == F(37,35)**2
assert F(1) + F(17,50)**2 == F(2789,2500)

# Sectional sign certificate.
s2_lo, s2_hi = sqrt_interval_rat(2)
B_lo = (F(121) + F(84)*s2_lo)/F(23)
B_hi = (F(121) + F(84)*s2_hi)/F(23)
logB = log_interval(B_lo, B_hi, 100)
log6 = log_interval(F(6), F(6), 100)
inv_s2 = (F(1,1)/s2_hi, F(1,1)/s2_lo)
prod = mul_pos(inv_s2, logB)
Jp = (-log6[1] + prod[0], -log6[0] + prod[1])
assert Jp[1] < 0

# Global sign certificate.
atan17 = atan_interval(F(17,50), 100)
atan1_5 = atan_interval(F(1,5), 100)
atan1_239 = atan_interval(F(1,239), 100)
pi_int = (16*atan1_5[0] - 4*atan1_239[1],
          16*atan1_5[1] - 4*atan1_239[0])
ratio = F(17**4, 33**2 * 2789)
logr = log_interval(ratio, ratio, 120)
Kp = (pi_int[0]/4 + atan17[0]/2 + logr[0]/4,
      pi_int[1]/4 + atan17[1]/2 + logr[1]/4)
assert Kp[0] > 0

def dec(fr, places=12):
    scale = 10**places
    n = fr.numerator*scale // fr.denominator
    return f"{n/scale:.{places}f}"

print("VERIFY_OK")
print("section_derivative_interval =", dec(Jp[0]), dec(Jp[1]))
print("global_derivative_interval =", dec(Kp[0]), dec(Kp[1]))
print("section_upper_negative =", Jp[1] < 0)
print("global_lower_positive =", Kp[0] > 0)
