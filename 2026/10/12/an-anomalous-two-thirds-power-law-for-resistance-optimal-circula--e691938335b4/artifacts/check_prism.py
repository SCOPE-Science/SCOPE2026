#!/usr/bin/env python3
"""Exact small-instance checks for weighted prism resistance optimization.
Only the stdlib is required. This is corroboration, not a proof for all sizes.
"""
from fractions import Fraction as Q
from math import sin, pi, sqrt, acosh, tanh


def inverse(a):
    n = len(a)
    w = [[Q(z) for z in row] + [Q(i == j) for j in range(n)] for i, row in enumerate(a)]
    for k in range(n):
        p = next((i for i in range(k, n) if w[i][k]), None)
        assert p is not None
        w[k], w[p] = w[p], w[k]
        scale = w[k][k]
        w[k] = [z/scale for z in w[k]]
        for i in range(n):
            if i == k: continue
            t = w[i][k]
            if t:
                w[i] = [u-t*v for u, v in zip(w[i], w[k])]
    return [row[n:] for row in w]


def matmul(A, B):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*B)] for row in A]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def lap_cycle(n):
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j = (i+1) % n
        L[i][i] += 1; L[j][j] += 1
        L[i][j] -= 1; L[j][i] -= 1
    return L


def direct_K(n, t, x):
    a = 1/(n*(2+t*x)); b = x*a; N = 2*n
    L = [[Q(0) for _ in range(N)] for _ in range(N)]
    def edge(i,j,w):
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    for sheet in range(2):
        for i in range(n):edge(sheet*n+i,sheet*n+(i+1)%n,a)
    for i in range(n):edge(i,n+i,b)
    J = Q(1,N)
    H = [[L[i][j]+J for j in range(N)] for i in range(N)]
    return N*(trace(inverse(H))-1)


def Fourier_K(n,t,x):
    C=lap_cycle(n)
    B=[[C[i][j]+(2*x if i==j else 0) for j in range(n)] for i in range(n)]
    a=1/(n*(2+t*x)); A=Q(n*n-1,12)
    return Q(2*n,1)/a*(A+trace(inverse(B)))


def slope_threshold(n, x):
    C=lap_cycle(n)
    B=[[C[i][j]+(2*x if i==j else 0) for j in range(n)] for i in range(n)]
    Bi=inverse(B);Bi2=matmul(Bi,Bi)
    U=trace(Bi2); V=trace(matmul(C,Bi2)); A=Q(n*n-1,12)
    t = 4*U/(A+V)
    return t, U, V


def run():
    direct=0
    for n in range(3,8):
        for t in [Q(1,3),Q(1),Q(5,2),Q(8)]:
            for x in [Q(1,4),Q(3,5),Q(1),Q(5,2)]:
                k1=direct_K(n,t,x);k2=Fourier_K(n,t,x)
                assert k1 == k2, (n,t,x,k1,k2)
                direct+=1
    optimal=0
    for n in range(3,11):
        for x in [Q(1,5),Q(1,2),Q(1),Q(3),Q(7)]:
            t,U,V=slope_threshold(n,x)
            assert t>0
            A=Q(n*n-1,12)
            assert t*(A+V)==4*U
            for y in [x/4,x/2,x,2*x,4*x]:
                assert Fourier_K(n,t,y) >= Fourier_K(n,t,x)
                if y!=x:assert Fourier_K(n,t,y)>Fourier_K(n,t,x)
                optimal+=1
    hyperbolic=0
    for n in [3,4,5,8,20,100]:
        for x in [0.001,0.1,0.7,3.]:
            summation=sum(1/(4*sin(pi*k/n)**2+2*x) for k in range(n))
            close=n/(2*sqrt(x*(x+2)))/tanh(n*acosh(1+x)/2)
            assert abs(summation-close)<1e-8*max(summation,1), (n,x,summation,close)
            hyperbolic+=1
    print(f'VERIFY_OK {direct} independent exact inverse-trace identities; {optimal} exact optimal-root inequalities; {hyperbolic} hyperbolic-sum comparisons')

if __name__=='__main__':run()
