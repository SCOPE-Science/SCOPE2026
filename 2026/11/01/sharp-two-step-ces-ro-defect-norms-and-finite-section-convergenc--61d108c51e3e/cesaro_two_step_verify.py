#!/usr/bin/env python3
"""Independent exact-rational finite-section tests of a two-step Cesaro defect theorem."""
from fractions import Fraction as Q
from math import exp

def cf(n):
    return [[Q(1,i+1) if j <= i else Q(0) for j in range(n)] for i in range(n)]

def mm(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),Q(0)) for j in range(n)] for i in range(n)]

def row_formula(i):
    H=[Q(0)]
    for t in range(1,i+1): H.append(H[-1]+Q(1,t))
    k=sum(H[i]-H[j-1]>2 for j in range(1,i))
    return Q(2)*(1-Q(1,i))**2+Q(2*k,i)*(H[i]-H[k]-1),k

def test():
    total=0
    for n in range(1,29):
        C=cf(n)
        CC=mm(C,C)
        T=[[ (Q(int(i==j))-C[i][j])*2+CC[i][j]-Q(int(i==j)) for j in range(n)] for i in range(n)]
        # above equals I-2C+C^2
        sums=[sum((abs(v) for v in row),Q(0)) for row in T]
        for i,row in enumerate(T):
            for j,v in enumerate(row):
                expect=(Q(1)-Q(1,i+1))**2 if j==i else (sum((Q(1,h) for h in range(j+1,i+2)),Q(0))-2)/Q(i+1) if j<i else Q(0)
                assert v==expect,(n,i,j,v,expect)
                total+=1
            expected,k=row_formula(i+1)
            assert sums[i]==expected,(n,i,sums[i],expected,k)
            total+=1
        assert all(sums[t+1]>sums[t] for t in range(n-1)),(n,sums)
        total+=n-1
    for n in (128,256,512,1024,2048,4096,8192):
        H=[0.0]
        for j in range(1,n+1):H.append(H[-1]+1.0/j)
        k=sum(H[n]-H[j-1]>2.0 for j in range(1,n))
        v=2*(1-1/n)**2+2*k/n*(H[n]-H[k]-1)
        q=exp(-2)
        assert abs(n*(2+2*q-v)-(5-q))<20/n,(n,k,v,n*(2+2*q-v))
        total+=1
    print('PASSED exact-rational kernel entries, row sums, strict row monotonicity, and 7 asymptotic profiles:',total)
if __name__=='__main__':test()
