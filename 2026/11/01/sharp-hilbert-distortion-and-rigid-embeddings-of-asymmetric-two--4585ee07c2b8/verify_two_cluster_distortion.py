#!/usr/bin/env python3
"""Exact finite diagnostics for the two-equilateral-cluster Hilbert distortion theorem."""
from fractions import Fraction as Q
import itertools

def rank(M):
    A=[list(row) for row in M]
    r=0
    for col in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][col]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        t=A[r][col]
        A[r]=[a/t for a in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][col]:
                x=A[i][col]
                A[i]=[a-x*b for a,b in zip(A[i],A[r])]
        r+=1
        if r==len(A):break
    return r

def gram(m,n,u2,v2):
    L=Q(m-1,2*m)*u2+Q(n-1,2*n)*v2
    q=max(Q(1),L)
    size=m+n
    D=[[Q(0)]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i!=j: D[i][j]=u2 if i<m and j<m else (v2 if i>=m and j>=m else q)
    G=[[(D[i][0]+D[j][0]-D[i][j])/2 for j in range(1,size)] for i in range(1,size)]
    return L,D,G

def verify():
    cases=0;phase={"subcritical":0,"critical":0,"supercritical":0}; var=0; split=0
    options=[Q(1,4),Q(1,2),Q(1),Q(3,2),Q(2),Q(5,2),Q(3),Q(4)]
    for m in range(2,7):
      for n in range(2,7):
       for u2 in options:
        for v2 in options:
         L,D,G=gram(m,n,u2,v2)
         predicted=m+n-1 if L<1 else m+n-2
         assert rank(G)==predicted,(m,n,u2,v2,L,rank(G),predicted)
         assert all(D[i][j]==(u2 if i<m and j<m else (v2 if i>=m and j>=m else max(Q(1),L))) for i in range(m+n) for j in range(m+n) if i!=j)
         phase['subcritical' if L<1 else ('critical' if L==1 else 'supercritical')]+=1
         cases+=1
         # Rational test of centroid and variance formulas using reconstructed Gram.
         alpha=[Q((j*7+3)%11-5) for j in range(m)]
         alpha[-1]=-sum(alpha[:-1]);
         qdist=sum(alpha[i]*alpha[j]*D[i][j] for i in range(m) for j in range(m))
         assert qdist==-u2*sum(x*x for x in alpha)
         var+=1
    print('EXACT_GRAM_RANK_AND_PHASES_OK',cases,phase)
    print('EXACT_HILBERT_ZERO_SUM_VARIANCE_OK',var)
    for m in range(2,12):
      for n in range(2,12):
       L,D,G=gram(m,n,Q(4),Q(1))
       assert L==Q(5,2)-Q(2,m)-Q(1,2*n)
       assert L>1
       assert rank(G)==m+n-2
       split+=1
    print('EXACT_COMPLETE_SPLIT_GRAPH_CASES_OK',split)
    assert all(phase.values())
    print('ALL_TWO_CLUSTER_DISTORTION_CHECKS_OK')

if __name__=='__main__':verify()
