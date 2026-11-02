#!/usr/bin/env python3
"""Exact finite arithmetic for a phenotype-switching Fourier example.
This checker corroborates algebra in the proof; it is not an infinite proof.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from math import isqrt

b=[F(1),F(-13),F(15)]
c=[F(7),F(2),F(2)]
L=[[F(-1),F(1),F(0)], [F(1),F(-2),F(1)], [F(0),F(1),F(-1)]]

def det(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
          - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
          + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def coeffs(m):
    tr=sum(m[i][i] for i in range(3))
    minors=sum(m[i][i]*m[j][j]-m[i][j]*m[j][i] for i in range(3) for j in range(i+1,3))
    return (F(1), -tr, minors, -det(m))

def matrices(n):
    assert n>=1
    a=F(2*n*n, 2**(n*n))
    return a, [[-F(n*n)*(i==j)+L[i][j]+a*b[i]*c[j] for j in range(3)] for i in range(3)]

# Source's normalized separable kernel: sum_ij Aij / 9 == 1.
B=[F(3,11)*x for x in b]
assert sum(B)*sum(c)/9 == 1
assert all(x>0 for x in c) and B[1]<0 and sum(B)>0
assert F(88,3)*F(1,2)*F(1,2)*F(1,2)*F(3,11) == 1

_,m1=matrices(1)
assert m1==[[F(5),F(3),F(2)], [F(-90),F(-29),F(-25)], [F(105),F(31),F(28)]]
assert [[m1[i][j]+(i==j) for j in range(3)] for i in range(3)] == [[F(6),F(3),F(2)], [F(-90),F(-28),F(-25)], [F(105),F(31),F(29)]]
assert coeffs(m1)==(1,-4,18,-10)
q=[[m1[i][j]+(i==j) for j in range(3)] for i in range(3)]
assert coeffs(q)==(1,-7,29,-33)
A,B1,C,D=coeffs(q)
disc=B1*B1*C*C-4*A*C*C*C-4*B1*B1*B1*D-27*A*A*D*D+18*A*B1*C*D
assert disc == -10444
assert 1-7+29-33 == -10
assert 8-28+58-33 == 5

for n, want in [(2,(1,F(21,2),52,F(175,2))),(3,(1,F(7837,256),F(19965,64),F(135135,128)))]:
    _,m=matrices(n)
    co=coeffs(m)
    assert co==want,(n,co,want)
    _,aa,bb,cc=co
    assert aa>0 and bb>0 and cc>0 and aa*bb>cc
# For n>=4, symmetric L has maximal eigenvalue zero. The rank-one
# perturbation has Euclidean operator norm a_n sqrt(395*57).
assert sum(x*x for x in b)==395
assert sum(x*x for x in c)==57
assert 151*151>395*57
assert 302<2**16
# Since n^2>=16, 2*n^2*sqrt(395*57)/2^(n^2) < n^2.
print('PASS: normalized positive-net interaction, exact n=1 cubic and discriminant,')
print('      n=2,3 Routh-Hurwitz polynomials, and all-n>=4 norm inequality.')
