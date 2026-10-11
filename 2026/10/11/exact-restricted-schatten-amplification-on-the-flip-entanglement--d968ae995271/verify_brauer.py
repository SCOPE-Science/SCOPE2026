#!/usr/bin/env python3
"""Standalone finite consistency checks for the flip–entanglement calculation.

Finite tests cannot certify universal Schatten norm or originality claims.
"""
import math


def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def flip(n):
    m=n*n
    a=[[0]*m for _ in range(m)]
    for i in range(n):
        for j in range(n):
            a[i*n+j][j*n+i]=1
    return a


def bell(n):
    m=n*n
    a=[[0]*m for _ in range(m)]
    for i in range(n):
        for j in range(n):
            a[i*n+i][j*n+j]=1
    return a


def partial_transpose(a,n):
    m=n*n
    b=[[0]*m for _ in range(m)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                for l in range(n):
                    b[i*n+j][k*n+l]=a[i*n+l][k*n+j]
    return b


def mm(a,b):
    m=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(m)) for j in range(m)] for i in range(m)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def c_formula(p,n):
    return (((n+1)**p+n*n-1)**(1/p) / (2*n)
            * (1+((n-1)**p/(n*n-1))**(1/(p-1)))**((p-1)/p))


def test():
    for n in range(2,6):
        f,b=flip(n),bell(n)
        assert partial_transpose(f,n)==b
        assert partial_transpose(b,n)==f
        assert mm(f,f)==eye(n*n)
        assert mm(b,b)==[[n*v for v in row] for row in b]
        assert mm(f,b)==b and mm(b,f)==b
        for a,c in [(0,1),(1,0),(2,3),(-3,1)]:
            x=[[a*f[i][j]+c*b[i][j] for j in range(n*n)] for i in range(n*n)]
            lhs=trace(mm(mm(mm(x,x),x),x))
            rhs=(a+n*c)**4 + (n*n-1)*a**4
            assert lhs==rhs,(n,a,c,lhs,rhs)
            s=a+c
            output=[[(x[i][j]+partial_transpose(x,n)[i][j])/2 for j in range(n*n)] for i in range(n*n)]
            out4=trace(mm(mm(mm(output,output),output),output))
            expected=s**4*((n+1)**4+n*n-1)/16
            assert abs(out4-expected)<1.e-8
        for p in (1.1,1.3,1.5,2.,3.,4.,8.,20.):
            cval=c_formula(p,n)
            assert cval>=1-1.e-10,(p,n,cval)
            if p!=2: assert cval>1+1.e-6,(p,n,cval)
            else: assert abs(cval-1)<1.e-10
            y=1.
            x=(n+1)**(1/(p-1))*y
            a=y;bb=(x-y)/n
            witness=((n+1)**p+n*n-1)**(1/p)*abs(a+bb)/2 / ((abs(a+n*bb)**p+(n*n-1)*abs(a)**p)**(1/p))
            assert abs(witness-cval)<1.e-10,(p,n,cval,witness)
    cubic=(7*(1+3**(1/3))**3/64)**.25
    assert abs(cubic-c_formula(4,2))<1.e-12
    print('BRAUER_SCHATTEN_EXACT_BLOCK_CHECK_OK')


if __name__ == '__main__':
    test()
