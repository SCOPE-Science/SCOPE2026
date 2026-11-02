#!/usr/bin/env python3
"""Exact, dependency-free finite checks for the qubit mixing-bound theorem.

The general theorem is proved analytically in RESULT.md; this script checks
matrix identities and one rigorous fixed-parameter witness using rationals.
"""
from fractions import Fraction as F
from math import factorial

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def matsum(A, B):
    return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]

def scale(A, s):
    return [[s*A[i][j] for j in range(3)] for i in range(3)]

def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]

I = [[F(int(i==j)) for j in range(3)] for i in range(3)]
zeros = [[F(0) for j in range(3)] for i in range(3)]
count = 0
for a in range(4):
    for b in range(4):
        for g in range(1,5):
            M = [[F(0),F(-2*b),F(0)],
                 [F(2*b),F(-2*g),F(-2*a)],
                 [F(0),F(2*a),F(-2*g)]]
            M2=matmul(M,M);M3=matmul(M2,M)
            CH=matsum(matsum(matsum(M3,scale(M2,4*g)),
                              scale(M,4*(g*g+a*a+b*b))),scale(I,8*g*b*b))
            assert CH==zeros,('Cayley-Hamilton',a,b,g)
            count+=9

# Check the Laplace numerator via an exact 3x3 adjugate calculation.
for a in range(4):
    for b in range(4):
        for g in range(1,5):
            for s in [F(1,3),F(2),F(9,2)]:
                M=[[F(0),F(-2*b),F(0)],[F(2*b),F(-2*g),F(-2*a)],
                   [F(0),F(2*a),F(-2*g)]]
                A=matsum(scale(I,s),scale(M,-1))
                determinant=(A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
                            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
                            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
                minor=A[0][0]*A[1][1]-A[0][1]*A[1][0]
                P=s*((s+2*g)**2+4*a*a)+4*b*b*(s+2*g)
                Q=s*(s+2*g)+4*b*b
                assert determinant==P and minor==Q
                count+=2

# Certified witness: a=b=gamma=1 and t=2.  If A=2M,
# ||A||_infty=12.  Remainder is bounded by 3^12*12^(K+1)/(K+1)!.
K=100
M=[[F(0),F(-2),F(0)],
   [F(2),F(-2),F(-2)],
   [F(0),F(2),F(-2)]]
A=scale(M,2)
v=[F(0),F(0),F(1)]
zsum=F(0)
for k in range(K+1):
    zsum += v[2]
    v=[u/F(k+1) for u in mv(A,v)]
refsum=F(0);term=F(1)
for k in range(K+1):
    refsum+=term
    term*=F(-4,k+1)
err_z=F(3**12 *12**(K+1),factorial(K+1))
err_ref=F(3**4 *4**(K+1),factorial(K+1))
assert zsum-refsum > err_z+err_ref
count+=1
print('PASS: exact rational assertions:',count)
print('Certified: z(2)-exp(-4) >',float(zsum-refsum-err_z-err_ref))
print('Certified bound on matrix Taylor remainder:',float(err_z))
