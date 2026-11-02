#!/usr/bin/env python3
"""Independent exact branch-partition test for twisted baker coordinate covariance."""
from fractions import Fraction as Q
from itertools import product
from math import isclose

def split(lo,hi,expr,left):
    j,a,b=expr
    L=list(lo); H=list(hi)
    if a==0:
        ok=(b<0) if left else (b>=0)
        return (L,H) if ok else None
    c=-b/a
    if left:
        if a>0: H[j]=min(H[j],c)
        else: L[j]=max(L[j],c)
    else:
        if a>0: L[j]=max(L[j],c)
        else: H[j]=min(H[j],c)
    if H[j]<=L[j]:return None
    return L,H

def check_partition(M,N):
    exprs=[(j,Q(1),Q(0)) for j in range(M)]
    states=[([Q(-1)]+[Q(0)]*(M-1),[Q(1)]*M,exprs)]
    out=[]
    for n in range(N+1):
        total=Q(0)
        for L,H,E in states:
            j,a,b=E[0]
            v=Q(1,2)
            for l,h in zip(L,H):v*=h-l
            means=[(l+h)/2 for l,h in zip(L,H)]
            means2=[(l*l+l*h+h*h)/3 for l,h in zip(L,H)]
            moment=means2[0] if j==0 else means[0]*means[j]
            total +=v*(a*moment+b*means[0])
        out.append(total)
        if n==N:break
        new=[]
        for L,H,E in states:
            for left in (True,False):
                clip=split(L,H,E[0],left)
                if clip is None:continue
                X,Y=clip
                if left:
                    j,a,b=E[0]
                    Enew=[(j,2*a,1+2*b)]+E[1:]
                else:
                    j,a,b=E[-1]
                    Enew=[(j,-2*a,1-2*b)]+E[:-1]
                new.append((X,Y,Enew))
        states=new
    return out

def matrix_prediction(M,N):
    B=[[Q(0) for _ in range(M)] for _ in range(M)]
    B[0][0]=Q(1,4);B[0][1]=Q(1,2)
    for j in range(1,M-1):B[j][j]=Q(1,2);B[j][j+1]=Q(1,2)
    B[-1][0]=Q(-1,4);B[-1][-1]=Q(1,2)
    r=[Q(0)]*M;r[0]=Q(1)
    out=[]
    for n in range(N+1):
        out.append(r[0]/3)
        r=[sum(r[j]*B[j][i] for j in range(M)) for i in range(M)]
    return out

def run():
    num=0
    for M in (2,3,4,5):
        for N in range(0,10):
            actual=check_partition(M,N)
            predicted=matrix_prediction(M,N)
            assert actual==predicted,(M,N,actual,predicted)
            num+=N+1
    for M in range(2,20):
        # Direct pointwise coboundary identity on both branches.
        for x1 in (Q(-7,8),Q(-1,4),Q(1,8),Q(7,8)):
            x=[x1]+[Q((3*j+1)%(j+5),j+5) for j in range(2,M+1)]
            fx=([1+2*x[0]]+x[1:]) if x1<0 else ([1-2*x[-1]]+x[:-1])
            h=lambda y:sum((y[j]-Q(1,2)) for j in range(1,M))
            d=x1 if x1<0 else x[-1]
            assert x1==d+h(fx)-h(x)
            num+=1
    for M in range(2,20):
        # Adjoint preimages both defined on all of X, with equal weights 1/2.
        for t in (Q(-3,5),Q(0),Q(4,5)):
            x=[t]+[Q((j+1),2*j+3) for j in range(1,M)]
            yl=[(x[0]-1)/2]+x[1:]
            yr=x[1:]+[(1-x[0])/2]
            d=lambda y: y[0] if y[0]<0 else y[-1]
            assert (d(yl)+d(yr))/2==0
            num+=1
    print('PASSED',num,'independent exact partition/coboundary/adjoint identities')
    for M in (2,3,4,5):
        print('M=',M,'covariance:', [str(x) for x in matrix_prediction(M,8)])

if __name__=='__main__':run()

# Additional analytic consequences can be verified with exact arithmetic directly.
