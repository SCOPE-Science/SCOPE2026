#!/usr/bin/env python3
"""Exact-rational finite checks of the stated stationary coordinate covariance law."""
from fractions import Fraction as F

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def matvec(A,v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]

def series(a,N):
    # N(a,z)/D(a,z) coefficient-by-coefficient, using exact rational arithmetic.
    polyN=[8*a*a-128*a+128,-10*a**3+132*a*a-128*a,3*a**4-22*a**3+20*a*a]
    f1=[F(2),-a];f2=[F(4),-(3*a+2),a]
    d=[F(0)]*4
    for i,x in enumerate(f1):
        for j,y in enumerate(f2): d[i+j]+=48*(2-a)**2*x*y
    out=[]
    for n in range(N+1):
        c=((polyN[n] if n<3 else 0)-sum(d[k]*out[n-k] for k in range(1,min(n,3)+1)))/d[0]
        out.append(c)
    return out

def check(a,limit=36):
    a=F(a)
    P=[[(1+a)/2,F(1,2),F(0),F(1,4)],[(1-a)/2,F(1,2),F(0),F(1,4)],
       [F(0),F(0),(1+3*a)/4,F(1,4)], [F(0),F(0),(1-a)/4,F(1,4)]]
    h0=2/(2-a); h1=2*(1-a)/(2-a)
    v=[F(0),F(0),h0,h1]
    mean=(4-3*a)/(4*(2-a))
    L=[F(1,8),F(3,8),F(1,24),F(7,24)]
    expected=series(a,limit)
    for n in range(limit+1):
        exact=sum(x*y for x,y in zip(L,v))-mean**2
        assert exact==expected[n],(a,n,exact,expected[n])
        v=matvec(P,v)
    return limit+1

if __name__=='__main__':
    total=sum(check(q) for q in [F(0),F(1,6),F(1,3),F(1,2),F(3,4),F(9,10),F(99,100)])
    print(f'PASS: {total} exact-rational covariance coefficients across seven parameters.')
