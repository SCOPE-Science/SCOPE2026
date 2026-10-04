#!/usr/bin/env python3
from fractions import Fraction

# Polynomials in ascending powers of t.
def add(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return out

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def power(a,n):
    out=[1]
    for _ in range(n): out=mul(out,a)
    return out

def sub(a,b): return add(a,[-x for x in b])
def scale(c,a): return [c*x for x in a]

def val(a,t):
    s=Fraction(0); q=Fraction(1)
    for x in a:
        s += x*q; q *= t
    return s

# 0 <= t <= 1/2.
U0=add(power([1,2],3), power([2,-1],3))
V0=add(power([1,-2],3), power([2,1],3))
W=add(power([1,1],3), power([1,-1],3))
assert U0 == [9,-6,18,7]
assert V0 == [9,6,18,-7]
assert W == [2,0,6,0]
D0=sub(scale(9,W),add(U0,V0))
assert D0 == [0,0,18,0]

# 1/2 <= t <= 1: |1-2t| = 2t-1.
V1=add(power([-1,2],3), power([2,1],3))
assert V1 == [7,18,-6,9]
D1=sub(scale(9,W),add(U0,V1))
assert D1 == [2,-12,42,-16]

# D1/2 = 1 + t h(t), h(t)=-8t^2+21t-6.
h=[-6,21,-8]
assert val(h,Fraction(1,2)) == Fraction(5,2)
# h'(t)=21-16t >= 5 on [1/2,1].
assert 21-16*1 == 5

# Reciprocal symmetry checked at exact positive rational points directly from cubes.
def cube_abs(q): return abs(q)**3
def UVW(t):
    U=cube_abs(1+2*t)+cube_abs(2-t)
    V=cube_abs(1-2*t)+cube_abs(2+t)
    Wv=cube_abs(1+t)+cube_abs(1-t)
    return U,V,Wv
for t in [Fraction(1,5),Fraction(1,2),Fraction(2,3),Fraction(3,2),Fraction(5,1)]:
    U,V,Wv=UVW(t); Ui,Vi,Wi=UVW(1/t)
    assert Ui*t**3 == V
    assert Vi*t**3 == U
    assert Wi*t**3 == Wv

# Equality-point algebra: Omega^3 = 162/125.
assert Fraction(2,5)**3 * Fraction(9,2)**2 == Fraction(162,125)
print('VERIFY_OK')
