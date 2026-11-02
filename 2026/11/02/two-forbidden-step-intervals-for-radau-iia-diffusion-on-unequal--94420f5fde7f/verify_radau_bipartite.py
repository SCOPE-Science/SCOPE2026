#!/usr/bin/env python3
"""Exact-rational checks for two-stage Radau IIA on unequal complete bipartite graphs.

Requires only Python 3's standard library. Infinite-family statements are proved
separately in RESULT.md; this script supplies independent finite arithmetic checks.
"""
from fractions import Fraction as F

COUNT = 0


def chk(v, desc):
    global COUNT
    COUNT += 1
    if not v:
        raise AssertionError(desc)


def radau(z):
    z = F(z)
    return (6 - 2*z)/(z*z + 4*z + 6)


def poly(p,q,h):
    n=p+q
    return (q*q*n*h**4 -2*q*(n*n-3*p-6*q)*h**3
            +(6*p*p+4*p*q-2*q*q+18*q)*h*h
            +(24*p+12*q)*h+36)


def den(z):
    return z*z+4*z+6


def entries(p,q,h):
    n=p+q
    a,b,c=radau(q*h),radau(p*h),radau(n*h)
    return ((p+q*c+n*(p-1)*a)/(p*n),
            (q+p*c+n*(q-1)*b)/(q*n),
            (p+q*c-n*a)/(p*n),
            (q+p*c-n*b)/(q*n),
            (1-c)/n)


def matrix(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0))
             for j in range(n)] for i in range(n)]


def inv(A):
    n=len(A)
    G=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next((k for k in range(j,n) if G[k][j]),None)
        if k is None: raise ArithmeticError('singular')
        G[k],G[j]=G[j],G[k]
        z=G[j][j]
        G[j]=[x/z for x in G[j]]
        for i in range(n):
            if i!=j and G[i][j]:
                z=G[i][j]
                G[i]=[u-z*v for u,v in zip(G[i],G[j])]
    return [row[n:] for row in G]


def actual(p,q,h):
    n=p+q
    L=[[F(q if i==j and i<p else p if i==j else
          -1 if ((i<p)!=(j<p)) else 0)
         for j in range(n)] for i in range(n)]
    H=[[h*v for v in row] for row in L]
    H2=matrix(H,H)
    D=[[H2[i][j]+4*H[i][j]+(6 if i==j else 0)
        for j in range(n)] for i in range(n)]
    T=[[(6 if i==j else 0)-2*H[i][j]
        for j in range(n)] for i in range(n)]
    return matrix(T,inv(D))


def bracket(p,q,part,lo,hi):
    f=lambda h:poly(p,q,h) if part=='A' else poly(q,p,h)
    chk(f(lo)*f(hi)<0,'certified rational root isolating bracket')


def main():
    for p in range(2,31):
        for q in range(2,31):
            if p==q: continue
            n=p+q
            for h in (F(1,37),F(1,5),F(1),F(8,q),F(8,p),F(17)):
                dA,dB,wA,wB,cross=entries(p,q,h)
                chk(dA==poly(p,q,h)/(den(n*h)*den(q*h)), 'A diagonal quartic')
                chk(dB==poly(q,p,h)/(den(n*h)*den(p*h)), 'B diagonal quartic')
                chk(wA>0 and wB>0 and cross>0,'all off-diagonal classes positive')
                chk(dA+(p-1)*wA+q*cross==1,'A row stochastic')
                chk(dB+(q-1)*wB+p*cross==1,'B row stochastic')
                if n>=12 and h==F(8,q):chk(dA<0,'A negative diagonal witness')
                if n>=12 and h==F(8,p):chk(dB<0,'B negative diagonal witness')
                if n<=11:chk(dA>0 and dB>0,'small-order positivity')
    cases=((2,3),(2,5),(2,10),(3,4),(3,9),(4,8),(5,7))
    steps=(F(1,10),F(2,3),F(1),F(7,6),F(4),F(20))
    for p,q in cases:
        for h in steps:
            P=actual(p,q,h)
            dA,dB,wA,wB,cross=entries(p,q,h)
            n=p+q
            for i in range(n):
                chk(sum(P[i])==1,'full rational row sum')
                for j in range(n):
                    x=(dA if i==j and i<p else dB if i==j else
                       wA if i<p and j<p else wB if i>=p and j>=p else cross)
                    chk(P[i][j]==x,'independent full rational matrix entry')
    # Disjoint unsafe intervals on K_(2,10), with all endpoints separated.
    for part,intervals in [('A',[(F(561,1000),F(562,1000)),
                                  (F(1097,1000),F(1098,1000))]),
                           ('B',[(F(3053,1000),F(3054,1000)),
                                  (F(5779,1000),F(5780,1000))])]:
        for lo,hi in intervals:bracket(2,10,part,lo,hi)
    # Overlapping unsafe intervals on K_(5,7).
    for part,intervals in [('A',[(F(845,1000),F(846,1000)),
                                  (F(1570,1000),F(1571,1000))]),
                           ('B',[(F(1212,1000),F(1213,1000)),
                                  (F(2225,1000),F(2227,1000))])]:
        for lo,hi in intervals:bracket(5,7,part,lo,hi)
    print('VERIFY_OK',COUNT,'exact-rational assertions')


if __name__=='__main__':
    main()
