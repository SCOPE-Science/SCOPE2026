#!/usr/bin/env python3
"""Exact rational check of the interpoint-distance moment identities.

This executable is supplementary verification; the general proof is in RESULT.md.
It requires only the Python standard library.
"""
from fractions import Fraction as F
from math import factorial
from random import Random


def triangular_moment(power):
    # Difference of two independent U[-1/2,1/2] variables.
    return F(0) if power % 2 else F(2, (power + 1) * (power + 2))


def multinomial(i, j, k):
    n = i + j + k
    return factorial(n) // (factorial(i) * factorial(j) * factorial(k))


def coefficient_table(n):
    """Exact coefficients of A^i B^j C^k in E|aU+bV|^(2n)."""
    out = {}
    for i in range(n+1):
        for j in range(n-i+1):
            k = n-i-j
            v = multinomial(i,j,k) * 2**k * triangular_moment(2*i+k) * triangular_moment(2*j+k)
            if v:
                out[(i,j,k)] = v
    return out


expected = [
    {(1,0,0):F(1,6), (0,1,0):F(1,6)},
    {(2,0,0):F(1,15), (0,2,0):F(1,15),
     (1,1,0):F(1,18), (0,0,2):F(1,9)},
    {(3,0,0):F(1,28), (0,3,0):F(1,28),
     (2,1,0):F(1,30), (1,2,0):F(1,30),
     (1,0,2):F(2,15), (0,1,2):F(2,15)},
]
for n in range(1,4):
    actual = coefficient_table(n)
    assert actual == expected[n-1], (n, actual, expected[n-1])

# Linear system for P=AB and Z=C^2 from the second and third moments.
a,b,c,d = -F(7,90), F(1,9), -F(31,420), F(2,15)
assert a*d - b*c == -F(41,18900)

def moments(A,B,Z):
    S, P = A+B, A*B
    return (S/6, S*S/15-F(7,90)*P + Z/9,
            S**3/28-F(31,420)*S*P+F(2,15)*S*Z)

def invert(m):
    S = 6*m[0]
    q = m[1] - S*S/15
    r = m[2]/S - S*S/28
    P = (-2520*q+2100*r)/41
    Z = (-1395*q+1470*r)/41
    return S,P,Z

rng = Random(260802288)
for _ in range(300):
    A = F(rng.randint(1,50), rng.randint(1,50))
    B = F(rng.randint(1,50), rng.randint(1,50))
    Z = A*B*F(rng.randint(0,99),100)
    assert invert(moments(A,B,Z)) == (A+B,A*B,Z)

one = (F(1), F(1), F(1,4))
two = (F(5,4), F(3,4), F(33,160))
assert one[0]*one[1] > one[2]
assert two[0]*two[1] > two[2]
m_one, m_two = moments(*one), moments(*two)
assert m_one[:2] == m_two[:2] == (F(1,3), F(13,60))
assert m_one[2] == F(43,210)
assert m_two[2] == F(1133,5600)
assert m_one[2]-m_two[2] == F(41,16800)
print('THREE_EVEN_DISTANCE_MOMENTS_EXACT_OK')
