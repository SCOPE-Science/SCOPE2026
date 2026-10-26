#!/usr/bin/env python3
# Exact arithmetic checks for the two-delay toral observation theorem.
from itertools import product
A=((3,2),(-3,4)); B=((0,1),(-18,7))
def mul(X,Y): return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def det(X): return X[0][0]*X[1][1]-X[0][1]*X[1][0]
def tr(X): return X[0][0]+X[1][1]
def power(X,n):
 Z=((1,0),(0,1))
 for _ in range(n): Z=mul(Z,X)
 return Z
def fixed_count(X,k):
 P=power(X,k)
 return abs(det(((P[0][0]-1,P[0][1]),(P[1][0],P[1][1]-1))))
assert tr(A)==tr(B)==7 and det(A)==det(B)==18
for k in range(1,13): assert fixed_count(A,k)==fixed_count(B,k)
assert mul(B,((1,0),(0,1)))==B
for m,n in product(range(-11,12),repeat=2):
 q=2*m*m+m*n+3*n*n
 assert 8*q==(4*m+n)**2+23*n*n
 assert q!=1 and q!=-1
assert det(((1,0),(3,2)))==2
assert det(((1,0),(0,1)))==1
assert all(det(X)==18 for X in (A,B))
print('VERIFY_OK')
