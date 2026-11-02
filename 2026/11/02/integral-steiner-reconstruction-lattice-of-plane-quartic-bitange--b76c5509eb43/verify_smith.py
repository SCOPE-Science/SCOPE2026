#!/usr/bin/env python3
"""Exact integral Smith certificate for odd theta/Steiner incidence, standalone Python 3."""
from collections import Counter
from math import gcd

def dot(a,b):return (a&b).bit_count()%2
def q(a,b,v):
    x=v&7; y=v>>3
    return dot(x,y)^dot(a,x)^dot(b,y)
odd=[(a,b) for a in range(8) for b in range(8) if dot(a,b)]
vec=list(range(1,64))
A0=[[1-q(a,b,v) for v in vec] for a,b in odd]
assert len(odd)==28 and len(vec)==63

def sm_cert(A):
    m=len(A); n=len(A[0]);A=[row[:] for row in A]
    U=[[int(i==j) for j in range(m)] for i in range(m)]
    V=[[int(i==j) for j in range(n)] for i in range(n)]
    def rowswap(i,j):
        A[i],A[j]=A[j],A[i];U[i],U[j]=U[j],U[i]
    def colswap(i,j):
        for H in (A,V):
            for row in H:row[i],row[j]=row[j],row[i]
    def rowadd(i,j,a):
        for H in (A,U):
            for c in range(len(H[0])):H[i][c]+=a*H[j][c]
    def coladd(i,j,a):
        for H in (A,V):
            for row in H: row[i]+=a*row[j]
    for k in range(m):
        cands=[(abs(A[i][j]),i,j) for i in range(k,m) for j in range(k,n) if A[i][j]]
        assert cands
        _,i,j=min(cands)
        rowswap(k,i);colswap(k,j)
        count=0
        while True:
            count+=1
            assert count<2000,(k,count)
            changed=False
            for i in range(k+1,m):
                if A[i][k]:
                    t,r=divmod(A[i][k],A[k][k]);rowadd(i,k,-t)
                    if r:rowswap(i,k)
                    changed=True
                    break
            if changed:continue
            for j in range(k+1,n):
                if A[k][j]:
                    t,r=divmod(A[k][j],A[k][k]);coladd(j,k,-t)
                    if r:colswap(j,k)
                    changed=True
                    break
            if changed:continue
            bad=next(((i,j) for i in range(k+1,m) for j in range(k+1,n) if A[i][j]%A[k][k]),None)
            if bad:
                rowadd(k,bad[0],1)
                continue
            break
        if A[k][k]<0:rowadd(k,k,-2)
        print('PIVOT',k,A[k][k], 'steps',count)
    return A,U,V

def mul(X,Y):
    assert len(X[0])==len(Y)
    nz=[[ (j,v) for j,v in enumerate(row) if v] for row in Y]
    out=[[0]*len(Y[0]) for i in X]
    for i,row in enumerate(X):
        for k,a in enumerate(row):
            if a:
                for j,b in nz[k]:out[i][j]+=a*b
    return out

if __name__=='__main__':
    B,U,V=sm_cert(A0)
    ds=[B[i][i] for i in range(28)]
    assert all(B[i][j]==(ds[i] if i==j else 0) for i in range(28) for j in range(63))
    assert all(ds[i+1]%ds[i]==0 for i in range(27))
    assert mul(mul(U,A0),V)==B
    assert sum(A0[i][j] for i in range(28) for j in range(63))==63*12
    assert all(sum(A0[i][j] for j in range(63))==27 for i in range(28))
    assert all(sum(A0[i][j] for i in range(28))==12 for j in range(63))
    gram=mul(A0,list(map(list,zip(*A0))))
    assert all(gram[i][j]==(27 if i==j else 11) for i in range(28) for j in range(28))
    print('SNF:',Counter(ds))
    print('VERIFY_OK: all 28 diagonal entries and unimodular row/column certificate, incidence counts, Gram identity')
