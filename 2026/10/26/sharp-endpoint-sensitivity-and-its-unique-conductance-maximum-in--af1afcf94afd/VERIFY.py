"""Exact-rational independent finite checks of two-community edge-flow projection.
Run with Python 3 and the standard library: python VERIFY.py.
Finite checks supplement, and do not substitute for, the algebraic proof.
"""
from fractions import Fraction as F

def inverse(A):
    n=len(A)
    T=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        l=next(i for i in range(k,n) if T[i][k])
        T[k],T[l]=T[l],T[k]
        a=T[k][k]
        T[k]=[z/a for z in T[k]]
        for j in range(n):
            if j!=k and T[j][k]:
                a=T[j][k];T[j]=[u-a*v for u,v in zip(T[j],T[k])]
    return [r[n:] for r in T]

def rows(m,y):
    n=2*m;t=y*y
    edges=[(i,j,t if (i<m)==(j<m) else F(1), y if (i<m)==(j<m) else F(1)) for i in range(n) for j in range(i+1,n)]
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for u,v,c,_ in edges:
        L[u][u]+=c;L[v][v]+=c;L[u][v]-=c;L[v][u]-=c
    J=inverse([v[:-1] for v in L[:-1]])
    B=[[F(i==u)-F(i==v) for i in range(n-1)] for u,v,_,_ in edges]
    R=[]
    for e,(u,v,c,s) in enumerate(edges):
        S=F(0)
        for f,(_,_,d,h) in enumerate(edges):
            S+=abs(s*h*sum(B[e][i]*J[i][j]*B[f][j] for i in range(n-1) for j in range(n-1)))
        R.append((S,(u<m)==(v<m)))
    return R

def claim(m,y):
    h=F(m-1,m);t=y*y
    within=(2*h*t+2*y)/(1+t)
    if y<=1:
        cross=(1+2*h*h+(1-2*h*h)*t+2*h*y)/(1+t)
    else:
        cross=1+2*h*y/(1+t)
    return within,cross

def main():
    z=0
    for m in range(2,6):
        for y in [F(1,10),F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(2),F(3)]:
            expected=claim(m,y)
            for x,within in rows(m,y):
                assert x==expected[0 if within else 1],(m,y,x,expected,within)
                z+=1
    print('PASS exact rational weighted two-clique projection checks:',z)
if __name__=='__main__':main()
