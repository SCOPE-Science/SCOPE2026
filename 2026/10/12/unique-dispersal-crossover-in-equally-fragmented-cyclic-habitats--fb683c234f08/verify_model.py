#!/usr/bin/env python3
"""Exact continuant and Rayleigh checks for two cyclic binary-growth profiles.
No external dependencies. Run: python3 verify_model.py
"""
from fractions import Fraction
from math import cos, pi

A = (0, 0, 0, 1, 0, 0, 1, 1, 1)
B = (0, 0, 0, 0, 1, 1, 0, 1, 1)

# A polynomial is a dict mapping (power_of_z, power_of_d) to integer.
def add(p, q, sign=1):
    o = dict(p)
    for monomial, coeff in q.items():
        o[monomial] = o.get(monomial, 0) + sign * coeff
        if not o[monomial]:
            del o[monomial]
    return o

def mul(p, q):
    o = {}
    for (i,j), a in p.items():
        for (k,l), b in q.items():
            index = (i+k,j+l)
            o[index] = o.get(index,0) + a*b
    return {k:v for k,v in o.items() if v}

def scalar(i):
    return {(0,0):i} if i else {}

Z = {(1,0):1}
D = {(0,1):1}
D2 = {(0,2):1}

def path_det(pattern):
    if not pattern:
        return scalar(1)
    diagonal0 = add(add(Z, {(0,1):2}), scalar(-pattern[0]))
    prev2,prev1=scalar(1),diagonal0
    for v in pattern[1:]:
        diagonal=add(add(Z,{(0,1):2}),scalar(-v))
        nxt=add(mul(diagonal,prev1),mul(D2,prev2),-1)
        prev2,prev1=prev1,nxt
    return prev1

def ring_det(pattern):
    n=len(pattern)
    assert n>=3
    return add(add(path_det(pattern),mul(D2,path_det(pattern[1:-1])),-1),{(0,n):2},-1)

observed = add(ring_det(A),ring_det(B),-1)
# d^4 (2d+z)(d^2-4d-2z+1)
expected = mul({(0,4):1},mul(add(mul(scalar(2),D),Z),
    add(add(add(D2,mul(scalar(-4),D)),mul(scalar(-2),Z)),scalar(1))))
assert observed == expected, (observed,expected)

# Independent finite sanity checks via integer Bareiss elimination on actual
# cyclic matrices, without using the continuant code.
def bareiss(a):
    a=[list(row) for row in a]
    n=len(a); sign=1; previous=1
    for k in range(n-1):
        if not a[k][k]:
            pivot_row=next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot_row is None:return 0
            a[k],a[pivot_row]=a[pivot_row],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%previous==0
                a[i][j]=numerator//previous
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

def evaluate(poly,z,d):
    return sum(c*z**i*d**j for (i,j),c in poly.items())

for pattern in (A,B):
    for t in (1,2,5):
        for z0 in (-2,0,1,3):
            matrix=[[(-t if (i-j)%9 in (1,8) else
                     (z0+2*t-pattern[i] if i==j else 0))
                     for j in range(9)] for i in range(9)]
            assert evaluate(ring_det(pattern),z0,t)==bareiss(matrix)

def rayleigh(pattern,vector,d):
    num=sum(v*vector[i]**2 for i,v in enumerate(pattern))
    num-=d*sum((vector[i]-vector[(i+1)%len(vector)])**2 for i in range(len(vector)))
    den=sum(x*x for x in vector)
    return Fraction(num,den)

assert rayleigh(B,(2,1,1,2,4,5,3,5,4),1)==Fraction(62,101)
assert rayleigh(B,(9,8,8,9,11,12,11,12,11),4)==Fraction(474,941)
assert Fraction(62,101)>Fraction(3,5)
assert Fraction(474,941)>Fraction(1,2)
assert 2-2*cos(2*pi/9)>2/5
assert sum(A)==sum(B)==4
assert sum(A[i]!=A[(i+1)%9] for i in range(9))==4
assert sum(B[i]!=B[(i+1)%9] for i in range(9))==4

# Independent numerical sanity check. Does not replace the analytic proof.
def top_eigen(pattern,d,steps=10000):
    n=len(pattern); x=[1.0/n**0.5]*n
    # Shift M by 2d+1 to obtain a primitive nonnegative matrix.
    for _ in range(steps):
        y=[(pattern[i]+1)*x[i]+d*(x[(i-1)%n]+x[(i+1)%n]) for i in range(n)]
        norm=sum(v*v for v in y)**0.5
        y=[v/norm for v in y]
        if max(abs(y[i]-x[i]) for i in range(n))<3e-15:
            x=y
            break
        x=y
    return (sum(pattern[i]*x[i]**2 for i in range(n))-
            d*sum((x[i]-x[(i+1)%n])**2 for i in range(n)))

def q(d): return (d*d-4*d+1)/2
for d in (1,2,4,5,10):
    la,lb=top_eigen(A,d),top_eigen(B,d)
    if d<=4: assert la>lb
    else: assert la<lb

lo,hi=4.0,5.0
for _ in range(70):
    mid=(lo+hi)/2
    if q(mid)<top_eigen(B,mid):lo=mid
    else: hi=mid
assert 4.0025<lo<4.0026

for repeat in (2,3):
    for d in (1,5):
        for pat in (A,B):
            difference=abs(top_eigen(pat*repeat,d)-top_eigen(pat,d))
            assert difference<5e-11,(repeat,d,pat,difference)
print('VERIFY_OK exact_determinant_identity=1 direct_bareiss_checks=24 rayleigh_witnesses=2 edge_counts=2 periods=1,2,3 unique_root_bracket=(4.0025,4.0026)')
