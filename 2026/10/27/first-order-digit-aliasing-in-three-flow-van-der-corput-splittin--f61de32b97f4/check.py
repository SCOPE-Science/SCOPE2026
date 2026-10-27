#!/usr/bin/env python3
"""Exact-rational checks for a three-flow binary radical-inverse ordering law."""
from fractions import Fraction
from math import exp

def radical_inverse(n):
    result = Fraction(0)
    weight = Fraction(1,2)
    while n:
        if n & 1:
            result += weight
        weight /= 2
        n >>= 1
    return result

def ordering(n):
    q1 = radical_inverse(2*n+1)
    q2 = radical_inverse(2*n+2)
    perm = [1,2,3]
    j3 = 1 + (3*q1).numerator // (3*q1).denominator
    perm[2],perm[j3-1] = perm[j3-1],perm[2]
    j2 = 1 + (2*q2).numerator // (2*q2).denominator
    perm[1],perm[j2-1] = perm[j2-1],perm[1]
    return tuple(perm)

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def identity():
    return [[Fraction(i==j) for j in range(3)] for i in range(3)]

def poly_step(h,typ):
    p=identity()
    p[0][1]+=h
    p[1][2]+=h
    if typ==(2,1,3): p[0][2]+=h*h
    return p

def check_one(N):
    h=Fraction(1,N)
    u=identity(); c=0
    for n in range(N):
        z=ordering(n)
        assert z in ((3,1,2),(2,1,3))
        assert (z==(3,1,2))==(radical_inverse(n)<Fraction(1,3))
        c += (z==(2,1,3))
        u=mm(poly_step(h,z),u)
    ex=identity();ex[0][1]=ex[1][2]=Fraction(1);ex[0][2]=Fraction(1,2)
    for i in range(3):
        for j in range(3):
            expected=h*h*(Fraction(c)-Fraction(N,2)) if (i,j)==(0,2) else Fraction(0)
            assert u[i][j]-ex[i][j]==expected,(N,i,j,u[i][j],ex[i][j])
    return c

if __name__=='__main__':
    for n in range(1,129):check_one(n)
    print('Exact rational matrix products: all N=1..128 passed')
    for n in [256,1024,4096]:
        count=sum(ordering(j)==(2,1,3) for j in range(n))
        # T=1: error/h = e * (count/n - 1/2).
        print('N=',n,'reverse-order frequency=',count/n,
              'witness error/h=',exp(1)*(count/n-0.5))
    print('limiting error/h=',exp(1)/6)
