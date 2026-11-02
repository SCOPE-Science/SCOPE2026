#!/usr/bin/env python3
"""Finite numerical checks for the beta-symbol/Hilbert-matrix theorem.

Only Python standard library is needed. The mathematical proof, not this
finite test, establishes the Fredholm statement and all infinite quantifiers.
"""
import math
import cmath

COUNT = 0

def check(condition, explanation):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(explanation)

def approx(x, y, atol=1e-11, rtol=1e-10):
    return abs(x-y) <= atol + rtol * max(abs(x), abs(y))

def matrix_entry(b, j, k):
    return math.exp(math.lgamma(j+b+1)-math.lgamma(j+1)
                    +math.lgamma(j+k+1)-math.lgamma(j+k+b+2))

def integer_symbol(m, x):
    z = complex(math.pi / (math.factorial(m)*math.cosh(math.pi*x)))
    for j in range(m):
        z *= complex(j+0.5, -x)
    return z

def phase(m, x):
    return -sum(math.atan(x/(j+0.5)) for j in range(m))

def positive_phase_crossing(m, ell):
    left, right = 0.0, 1.0
    while phase(m, right) > -ell*math.pi:
        right *= 2
        if right > 1e7:
            raise AssertionError('Failed to bracket a predicted crossing')
    for _ in range(90):
        mid = (left+right)/2
        if phase(m, mid) > -ell*math.pi:
            left = mid
        else:
            right = mid
    return (left+right)/2

# Coefficient formula: gamma ratio and its elementary integral for integer b.
for b in (1, 2, 3, 4):
    for j in range(12):
        for k in range(12):
            val = matrix_entry(b, j, k)
            exact = math.comb(j+b, j) * math.factorial(j+k)*math.factorial(b) / math.factorial(j+k+b+1)
            check(approx(val, exact), f'matrix coefficient b={b}, j={j}, k={k}')

# Exact Fourier-transform beta value at zero and reflection for integer b.
for m in range(1, 11):
    beta0 = math.gamma(m+0.5)*math.gamma(0.5)/math.gamma(m+1)
    check(approx(integer_symbol(m, 0), beta0), f'beta value m={m}')
    last = abs(integer_symbol(m, 0))
    for ix in range(1, 201):
        x = ix * 0.045
        symbol = integer_symbol(m, x)
        check(approx(symbol, integer_symbol(m, -x).conjugate()), 'reflection')
        mag = abs(symbol)
        check(mag < last, 'strictly decreasing radial profile')
        last = mag
        check(approx(math.atan2(symbol.imag, symbol.real),
                     math.atan2(math.sin(phase(m, x)), math.cos(phase(m, x))),
                     atol=3e-11), 'phase formula')

# Exact predicted count of distinct nonzero real double points.
for m in range(1, 16):
    expected = (m-1)//2
    check(len([ell for ell in range(1, m+1) if 2*ell<m]) == expected,
          'number of crossings')
    for ell in range(1, expected+1):
        x = positive_phase_crossing(m, ell)
        value = integer_symbol(m, x)
        check(approx(value, integer_symbol(m, -x), atol=1e-10), 'double point')
        check(approx(value.imag, 0, atol=1e-10), 'real crossing')
        check(value.real*((-1)**ell)>0, 'alternating sign')
        # Derivative radial and argument slopes are nonzero: transverse crossing.
        delta = max(1e-6, x*1e-5)
        radder = (abs(integer_symbol(m, x+delta))-
                  abs(integer_symbol(m, x-delta)))/(2*delta)
        argder = (phase(m, x+delta)-phase(m, x-delta))/(2*delta)
        check(radder < 0 and argder < 0, 'transversality')

# Compare the exact coefficient against homogeneous model away from the origin.
for b in (0.25, 0.5, 1.0, 2.0, 3.5):
    for n in (50, 100, 300, 600):
        for factor in (0.2, 0.5, 1.0, 2.0, 4.0):
            j = n
            k = int(n*factor)
            h = matrix_entry(b, j, k)
            homog = (j+1)**b / (j+k+2)**(b+1)
            check(abs(h-homog) <= 50*(1+b)**3*homog/(j+1), 'gamma ratio model')

# Test finite-column weak-null estimate using exact coefficients (not an infinite proof).
for b in (0.5, 1.0, 2.0, 4.0):
    for n in (30, 70, 150):
        col2 = sum(matrix_entry(b, j, n)**2 for j in range(10*n+500))
        check(col2 < 100/(n+1), 'weakly-null columns')

print('PASS:', COUNT, 'finite deterministic assertions; analytical proof is separate.')
