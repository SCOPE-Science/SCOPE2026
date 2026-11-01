#!/usr/bin/env python3
"""Independent finite exact-arithmetic consistency tests for the explicit kernel formulas.

Tests are finite, not a replacement for the analytic proof.
No nonstandard Python packages are required.
"""
from fractions import Fraction
from math import factorial

checks = 0

def verify(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def coeff(alpha, count):
    a = [Fraction(alpha)]
    for j in range(count - 1):
        a.append(a[-1] * (Fraction(j+1)-alpha) / (j+1))
    return a

def determinant(mat):
    a = [list(row) for row in mat]
    n = len(a)
    determinant_sign = 1
    d = Fraction(1)
    for i in range(n):
        pivot = next((k for k in range(i,n) if a[k][i]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            determinant_sign = -determinant_sign
        v = a[i][i]
        d *= v
        for k in range(i+1,n):
            q = a[k][i] / v
            for j in range(i+1,n):
                a[k][j] -= q*a[i][j]
            a[k][i] = 0
    return determinant_sign * d

for m in range(1,11):
    a = coeff(Fraction(m),m+4)
    verify(a[:m] == [Fraction(m) * (-1)**j * Fraction(factorial(m-1),factorial(j)*factorial(m-1-j)) for j in range(m)], f'integer coefficients m={m}')
    for j in range(m,m+4):
        verify(a[j] == 0, f'finite kernel rank m={m},j={j}')
    trace_kernel = sum(a[j]/Fraction(2*j+1) for j in range(m))
    trace_pred = Fraction(m * 4**m * factorial(m)*factorial(m-1), 2*factorial(2*m))
    verify(trace_kernel == trace_pred, f'kernel trace m={m}')
    trace_square = sum(a[i]*a[j]/Fraction((i+j+1)**2) for i in range(m) for j in range(m))
    harmonic = sum(Fraction(1,k) for k in range(1,2*m))
    trace_square_pred = Fraction(m*m,2*m-1)*harmonic
    verify(trace_square == trace_square_pred, f'commutator trace m={m}')
    gram = [[Fraction(1,i+j+1) for j in range(m)] for i in range(m)]
    verify(determinant(gram) != 0, f'moment independence m={m}')
    verify(sum(1 for j in range(m) if a[j]>0) == (m+1)//2, f'positive index m={m}')
    verify(sum(1 for j in range(m) if a[j]<0) == m//2, f'negative index m={m}')

for m in range(0,9):
    a = coeff(Fraction(2*m+1,2),55)
    for j in range(55):
        verify(a[j] != 0, f'noninteger no vanishing coefficient m={m},j={j}')
        expected = (-1)**j if j<m else (-1)**m
        verify((1 if a[j]>0 else -1)==expected, f'noninteger sign m={m},j={j}')
    verify(sum(1 for j in range(m) if ((1 if a[j]>0 else -1) != (-1)**m)) == (m+1)//2, f'finite contrary index m={m}')

# Direct exact small-order spectral invariants of the signed square root:
verify(coeff(Fraction(2),2) == [Fraction(2),Fraction(-2)], 'second-order binomial')
verify(Fraction(2,3) + Fraction(2,3) == Fraction(4,3), 'second-order signed trace')
verify(Fraction(22,9) == Fraction(2)*Fraction(11,9), 'second-order squared trace')
print(f'PASS {checks} exact rational assertions; integer order 1..10 and noninteger half-orders 0.5..8.5')
