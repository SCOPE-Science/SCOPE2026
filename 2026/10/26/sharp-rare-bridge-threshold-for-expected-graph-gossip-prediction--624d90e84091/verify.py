#!/usr/bin/env python3
"""Exact rational checks for a rare-shortcut harmonic-gossip benchmark.
Run with Python 3 standard library only: python verify.py
"""
from fractions import Fraction as F

checks = 0

def ck(condition, msg):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)

def endpoint(L,H,t):
    e=F(L,H)
    return (e+L*t)/(1+2*e+2*L*t)

def predicted(L,H,t):
    a=endpoint(L,H,t)
    N=2*L+H
    return [F(j,L)*a if j<=L else
            a+F(j-L,H)*(1-2*a) if j<=L+H else
            1-a+F(j-L-H,L)*a for j in range(N+1)]

def harmonic(L,H,t):
    N=2*L+H
    A=[[F(0) for _ in range(N)] for i in range(N-1)]
    for i in range(1,N):
        for j,w in ((i-1,F(1)),(i+1,F(1)),
                    (L+H,t) if i==L else (L,t) if i==L+H else (i,F(0))):
            if not w: continue
            A[i-1][i-1]+=w
            if j==N: A[i-1][N-1]+=w
            elif j!=0: A[i-1][j-1]-=w
    # RREF on the grounded Laplacian. All graph realizations are connected.
    for k in range(N-1):
        pivot=next(i for i in range(k,N-1) if A[i][k])
        A[k],A[pivot]=A[pivot],A[k]
        a=A[k][k]
        A[k]=[z/a for z in A[k]]
        for i in range(N-1):
            if i!=k and A[i][k]:
                b=A[i][k]
                A[i]=[x-b*y for x,y in zip(A[i],A[k])]
    return [F(0)]+[row[-1] for row in A]+[F(1)]

def bsum(H):
    return F(H,2)+1+(F(1,2*H) if H%2 else 0)

for L in range(1,5):
    for H in range(2,9):
        for t in (F(0),F(1),F(1,5),F(1,2),F(4,5)):
            direct=harmonic(L,H,t)
            model=predicted(L,H,t)
            ck(direct==model,('harmonic',L,H,t))
            ck(direct[0]==0 and direct[-1]==1,('boundary',L,H,t))
        for p in (F(1,6),F(1,3),F(1,2),F(2,3),F(5,6)):
            q=[(1-p)*x+p*y for x,y in zip(predicted(L,H,F(0)),predicted(L,H,F(1)))]
            annealed=predicted(L,H,p)
            d=endpoint(L,H,p)-((1-p)*endpoint(L,H,F(0))+p*endpoint(L,H,F(1)))
            C=1+F(2*L,H)
            ck(d==F(2*L*L)*p*(1-p)/(C*(C+2*L)*(C+2*L*p)),('Jensen gap',L,H,p))
            ck(d>0,('strict positivity',L,H,p))
            ck(all(0<=x<=1 for x in annealed),('range',L,H,p))
            ck(sum(abs(x-y) for x,y in zip(annealed,q))==d*(L-1+bsum(H)),('L1',L,H,p))
            ck(sum(abs(1-F(2*k,H)) for k in range(H+1))==bsum(H),('bridge sum',L,H,p))
            ck(all((x-y)==-((annealed[-1-j]-q[-1-j])) for j,(x,y) in enumerate(zip(annealed,q))),('antisymmetry',L,H,p))

# Exact finite instances in the critical regime and the stronger-bridge regime.
L,H,p=100,10000,F(1,100)
a=endpoint(L,H,p); q=(1-p)*endpoint(L,H,0)+p*endpoint(L,H,1)
ck(abs(a-F(1,3))<F(1,50),('critical scale',a))
ck(q<F(1,50),('quenched critical',q))
L,H,p=10000,100000000,F(1,100)
a=endpoint(L,H,p); q=(1-p)*endpoint(L,H,0)+p*endpoint(L,H,1)
ck(a>F(49,100),('annealed near neutral',a))
ck(q<F(1,100),('quenched near polar',q))
print(f'VERIFY_OK exact_assertions={checks}')
