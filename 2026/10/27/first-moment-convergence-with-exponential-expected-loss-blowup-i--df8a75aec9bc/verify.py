#!/usr/bin/env python3
"""Exact algebraic cross-checks for a two-client scalar stochastic proximal update."""
from fractions import Fraction as Q

def mat(c):
    c=Q(c)
    return [[1/(1+c),c/(2*(1+c)),-1/(2*(1+c))],
            [Q(1),Q(0),Q(0)], [c,-c/2,Q(1,2)]]

def mv(M,v): return [sum(M[i][j]*v[j] for j in range(3)) for i in range(3)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def det(A):
    return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
def char(M,l):return det([[Q(l)*(i==j)-M[i][j] for j in range(3)] for i in range(3)])
count=0
for b in [Q(11),Q(12),Q(14),Q(18),Q(21,2),Q(37,2)]:
    A=mat(1);B=mat(b);P=mm(B,A)
    assert all(char(A,l)==l*(l-Q(1,2))*(l-Q(1,2)) for l in [Q(-5),Q(0),Q(1),Q(2)])
    for l in [Q(-5),Q(0),Q(1),Q(2)]:
        assert char(B,l)==l*(l-Q(1,2))*(l-1/(1+b))
        r=-(b-2)/4;s=b/(2*(b+1))
        assert char(P,l)==l*(l-r)*(l-s)
        mean=[[(A[i][j]+B[i][j])/2 for j in range(3)] for i in range(3)]
        alpha=(b+3)/(4*(b+1));beta=(b-1)**2/(16*(b+1))
        assert char(mean,l)==(l-Q(1,2))*(l*l-alpha*l+beta)
        count+=4
    z=[Q(1),Q(1),Q(0)]
    for n in range(1,21):
        z=mv(P,z)
        formula=-Q(2)/((b-1)*(b+2))*r**n+(b*(b+1))/((b-1)*(b+2))*s**n
        assert z[0]==formula
        count+=1
b=Q(14)
assert b>10 and b<9+4*Q(5) # coarse upper bound is not theorem; numeric check below
assert 14 < 9 + 4*(6**0.5)
assert Q(169,240)<1
for n in range(3,15):
    r=Q(-3);s=Q(7,15)
    xn=-(r**n)/104+Q(105,104)*s**n
    assert xn*xn/Q(4)**n>=Q(1,43264)*Q(9,4)**n
    count+=1
print('VERIFY_OK exact matrix characteristic identities and alternating-path moments:',count)
