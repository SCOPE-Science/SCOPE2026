#!/usr/bin/env python3
"""Exact rational boundary tests and independent matrix/Fourier checks.

Python 3 standard library only. Finite tests support but do not replace
uniform-in-order trigonometric and convexity arguments in the theorem.
"""
from fractions import Fraction as F
from math import cos, pi, isclose


def mat_mul(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def mat_inv(a):
    n=len(a)
    z=[list(row)+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        k=next((i for i in range(j,n) if z[i][j]),None)
        assert k is not None, 'matrix singular'
        z[j],z[k]=z[k],z[j]
        scale=z[j][j]
        z[j]=[e/scale for e in z[j]]
        for i in range(n):
            if i!=j:
                d=z[i][j]
                if d: z[i]=[u-d*v for u,v in zip(z[i],z[j])]
    return [row[n:] for row in z]


def ring_lap(n,step):
    out=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        j=(i+step)%n
        assert i!=j
        out[i][i]+=1;out[j][j]+=1
        out[i][j]-=1;out[j][i]-=1
    return out


def matrix(n,a,b):
    l1=ring_lap(n,1); l2=ring_lap(n,2)
    return [[a*l1[i][j]+b*l2[i][j]+F(1,n) for j in range(n)] for i in range(n)]


def derivative(n,t,b):
    c=F(1,n)
    a=c-t*b
    inv=mat_inv(matrix(n,a,b))
    l1=ring_lap(n,1);l2=ring_lap(n,2)
    d=[[l2[i][j]-t*l1[i][j] for j in range(n)] for i in range(n)]
    return -tr(mat_mul(mat_mul(inv,d),inv))


def objective(n,a,b):
    return tr(mat_inv(matrix(n,a,b)))-1


def fourier(n,a,b):
    return sum(1/(a*(2-2*cos(2*pi*k/n))+b*(2-2*cos(4*pi*k/n))) for k in range(1,n))

count=0
for n in range(5,12):
    thigh=F(4*(n-2),n+1)
    assert derivative(n,thigh,F(0))==0
    assert derivative(n,thigh+F(1,7),F(0))>0
    assert derivative(n,thigh-F(1,7),F(0))<0
    count+=3
    if n%2:
        tlow=F(16,n*n+7)
        assert derivative(n,tlow,F(1,n)/tlow)==0
        assert derivative(n,tlow-F(1,100),F(1,n)/(tlow-F(1,100)))<0
        assert derivative(n,tlow+F(1,100),F(1,n)/(tlow+F(1,100)))>0
        count+=3
    for t in (F(1,2),F(1),F(3,2)):
        b=F(1,3*n)/t
        a=F(1,n)-t*b
        exact=objective(n,a,b)
        approx=fourier(n,float(a),float(b))
        assert isclose(float(exact),approx,rel_tol=2e-10,abs_tol=1e-10), (n,t,exact,approx)
        count+=1
    # Numerically demonstrate strict-positive Hessian along feasible segment
    for t in (F(1),F(2)):
        b=F(1,3*n)/t
        eps=F(1,900*n)/t
        f_minus=objective(n,F(1,n)-t*(b-eps),b-eps)
        f_center=objective(n,F(1,n)-t*b,b)
        f_plus=objective(n,F(1,n)-t*(b+eps),b+eps)
        assert f_minus-2*f_center+f_plus>0
        count+=1
print(f'OK: {count} independent exact-rational boundary, trace/Fourier, and convexity checks; n=5..11')
