#!/usr/bin/env python3
from fractions import Fraction
from math import cos, pi


def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def eye(n):
    return [[Fraction(int(i==j),1) for j in range(n)] for i in range(n)]

def scale(A,c):
    return [[c*x for x in row] for row in A]

def cyclic_matrix(weights):
    n=len(weights)
    J=[[Fraction(0,1) for _ in range(n)] for __ in range(n)]
    for i,a in enumerate(weights):
        J[i][(i-1)%n]=a
    return J

def mpow(A,n):
    R=eye(len(A))
    B=A
    while n:
        if n&1: R=matmul(R,B)
        B=matmul(B,B); n//=2
    return R

# Exact weighted-cycle identity J^N=(prod a_i)I, sampled over many dimensions
for n in range(2,21):
    w=[Fraction(i+2,i+3) for i in range(n)]
    if n%2: w[0]*=-1
    P=Fraction(1,1)
    for a in w: P*=a
    assert mpow(cyclic_matrix(w),n)==scale(eye(n),P)

# Exact count of roots of lambda^N=P having positive real part
for n in range(2,41):
    roots_even=[cos(2*pi*k/n) for k in range(n)]
    got_even=sum(x>1e-12 for x in roots_even)
    want_even=2*((n-1)//4)+1
    assert got_even==want_even
    roots_odd=[cos((2*k+1)*pi/n) for k in range(n)]
    got_odd=sum(x>1e-12 for x in roots_odd)
    want_odd=2*((n+1)//4)
    assert got_odd==want_odd

# Exact cancellation in the N=2 conserved-quantity derivative.
b1=Fraction(7,3); b2=Fraction(-5,4)
p1=Fraction(2,5); p2=Fraction(3,7); q1=Fraction(1,3); q2=Fraction(4,9)
common=(p1-q1)*(p2-q2)
dK=abs(b2)*b1*common + abs(b1)*b2*common
assert dK==0

print('VERIFY_OK')
