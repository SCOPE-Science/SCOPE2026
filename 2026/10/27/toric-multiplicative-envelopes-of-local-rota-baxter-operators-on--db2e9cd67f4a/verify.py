#!/usr/bin/env python3
"""Exact rational checks for the multiplicative envelope of local Rota--Baxter maps.
No numerical tolerance or finite enumeration is used as a substitute for the proof.
"""
from fractions import Fraction
from itertools import product


def mm(A,B):
    n=len(A)
    return [[sum(A[i][h]*B[h][j] for h in range(n)) for j in range(n)] for i in range(n)]

def T(n,k,alpha,row):
    M=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    if k is not None:
        for i in range(k-1,n-1):
            M[i][i]=Fraction(alpha)*2**(n-1-i)
    for j in range(n):
        M[-1][j]=Fraction(row[j])
    return M

def diag_profile(n,k,ell,a):
    return [Fraction(a)*2**(ell*(n-1-i)) if k<=i+1<n else Fraction(0) for i in range(n-1)]

def toric_check(diagonal,k):
    n=len(diagonal)+1
    assert all(diagonal[i]==0 for i in range(k-1))
    y=list(reversed(diagonal[k-1:]))
    for i in range(len(y)-2):
        for j in range(i+1,len(y)-1):
            assert y[i]*y[j+1]==y[i+1]*y[j]

cases=0
for n in range(3,8):
  for i0 in range(n-2):
    for length in range(1,6):
      for thresholds in product(range(i0+1,n),repeat=min(length,3)):
        if len(thresholds)<length: thresholds=thresholds+(thresholds[-1],)*(length-len(thresholds))
        # Variable last rows; nontrivial last-column entries are tested exactly.
        A=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
        alphas=[]
        for step,k in enumerate(thresholds):
          alpha=[Fraction(2,3),Fraction(-3,5),Fraction(7,2),Fraction(1,6),Fraction(-4,3)][step]
          alphas.append(alpha)
          row=[Fraction(((step+2)*(j+3))%9-4,step+j+2) for j in range(n)]
          A=mm(A,T(n,k,alpha,row))
        K=max(thresholds)
        a=Fraction(1)
        for alpha in alphas:a*=alpha
        expected=diag_profile(n,K,length,a)
        assert [A[i][i] for i in range(n-1)]==expected,(n,thresholds,length,expected)
        assert all(A[i][j]==0 for i in range(n-1) for j in range(n) if i!=j)
        toric_check(expected,K)
        cases+=1

# Explicit witness: product of two local maps leaves the local locus.
n=3
A=T(n,1,1,[0]*n)
B=mm(A,A)
assert [B[i][i] for i in range(2)] == [16,4]
assert B[0][0]!=2*B[1][1]

# Last row is freely prescribeable for each fixed product length/threshold.
for n in range(3,9):
  for length in range(1,6):
    for k in range(1,n):
      a=Fraction(7,11)
      desired=[Fraction(i+1,i+2) for i in range(n)]
      prod=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
      for step in range(length):
        alpha=a if step==0 else Fraction(1)
        row=desired if step==length-1 else [0]*(n-1)+[1]
        prod=mm(prod,T(n,k,alpha,row))
      assert prod[-1]==desired
      assert [prod[i][i] for i in range(n-1)]==diag_profile(n,k,length,a)

print('VERIFY_OK product_cases=',cases,' toric_minors=checked','free_last_rows=checked','nonclosure_witness=checked')
