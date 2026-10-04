#!/usr/bin/env python3
from fractions import Fraction
import math

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def check(n):
    G=[[Fraction(1,1) if i==j else Fraction(-1,n) for j in range(3)] for i in range(3)]
    H=[[Fraction(n,n+1)*(1 if i==j else 0)+Fraction(n,(n+1)*(n-2)) for j in range(3)] for i in range(3)]
    P=mm(G,H)
    for i in range(3):
        for j in range(3):
            assert P[i][j] == (1 if i==j else 0)
    det=Fraction((n+1)**2*(n-2),n**3)
    assert det == Fraction(n+1,n)**2*Fraction(n-2,n)
    c3sq=Fraction(n-2,3*n)
    assert c3sq*Fraction(3*n,n-2)==1
    c4sq=Fraction(n-3,4*n)
    assert 4*c4sq==Fraction(n-3,n)
    if n>=5:
        assert Fraction(3,1)+Fraction(n-5,2)==Fraction(n+1,2)
        a=(n-5)/2.0
        lhs=3.0**(a+3.0)*math.gamma(a+1.0)/math.gamma(a+4.0)
        rhs=3.0**((n+1)/2.0)*math.gamma((n-3)/2.0)/math.gamma((n+3)/2.0)
        assert abs(lhs-rhs) <= 1e-12*max(1.0,abs(rhs))

for n in range(4,41):
    check(n)
print('VERIFY_OK')
