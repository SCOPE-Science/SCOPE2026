#!/usr/bin/env python3
"""Exact integer-arithmetic verification of cyclic inverse-Cremona degree identities."""
from math import comb


def qinv_coeffs(s):
    qforward = [(-1)**j * comb(2*s-j, j) for j in range(s+1)]
    return [(-1)**s * qforward[s-j] for j in range(s+1)]


def sequences(n, max_r):
    s = (n-1)//2
    L = s+1
    a = [0]*n
    a[0]=1
    sequence=[]
    for r in range(max_r+1):
        k = (r*s+n)//2 % n
        m = min(a)
        d = L**r - n*m
        assert a[k] == m, (n,r,a,k)
        assert sum(a)==L**r
        sequence.append(d)
        if r==max_r: break
        b=[0]*n
        for j in range(s+1):
            for i,x in enumerate(a):
                b[(i+j)%n]+=x
        a=b
    return sequence


def matrix_matmul(A,B):
    n=len(A)
    out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,v in enumerate(A[i]):
            if v:
                for j,w in enumerate(B[k]):out[i][j]+=v*w
    return out


def check():
    count=0
    for n in range(3,102,2):
        s=(n-1)//2
        max_r=35 if n>50 else 90
        D=sequences(n,max_r)
        q=qinv_coeffs(s)
        assert q[0]==1 and len(q)==s+1
        for r in range(max_r-2*s+1):
            assert sum(q[j]*D[r+2*(s-j)] for j in range(s+1))==0,(n,r)
            count+=1
        # Direct exponent-matrix calculation, independent of cyclic convolution implementation.
        if n<=19:
            H=[[int(any(col==(row+2*j)%n for j in range(s+1))) for col in range(n)] for row in range(n)]
            P=[[int(i==j) for j in range(n)] for i in range(n)]
            for r in range(0,9):
                mins=[min(P[i][j] for i in range(n)) for j in range(n)]
                assert len(set(mins))==1,(n,r,mins)
                assert sum(P[0])-sum(mins)==D[r],(n,r)
                P=matrix_matmul(P,H)
    print('VERIFY_OK: 50 odd dimensions; cyclic antipodal minima to degree 90/35; %d recurrence cases; 81 independent exponent-matrix comparisons.'%count)


if __name__=='__main__':check()
