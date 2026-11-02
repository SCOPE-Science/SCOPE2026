#!/usr/bin/env python3
"""Exact arithmetic checks for the first-ascent/last-descent Dyck law.
All checks here are finite diagnostics; the all-size result rests on the proof.
"""
from math import comb
from itertools import combinations
from functools import lru_cache

count = 0

def cb(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0

def enumerate_dyck(n):
    def rec(u,d,word):
        if u==n and d==n:
            yield ''.join(word)
        else:
            if u<n:
                word.append('U');yield from rec(u+1,d,word);word.pop()
            if d<u:
                word.append('D');yield from rec(u,d+1,word);word.pop()
    yield from rec(0,0,[])

def a_b(w):
    a=len(w)-len(w.lstrip('U'))
    b=len(w)-len(w.rstrip('D'))
    return a,b

def T(n):
    hs=list(range(n%2,n+1,2))
    return [[int(a==n and h==n) if a==n else cb(n-a-1,(n-2*a+h)//2)-cb(n-a-1,(n+h)//2)
             for h in hs] for a in range(1,n+1)],hs

def joint(n):
    X,_=T(n)
    return [[sum(u*v for u,v in zip(X[a],X[b])) for b in range(n)] for a in range(n)]

def det(a):
    # Bareiss fraction-free exact determinant
    n=len(a)
    if not n:return 1
    a=[row[:] for row in a];den=1;sign=1
    for k in range(n-1):
        if not a[k][k]:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                p=a[i][j]*piv-a[i][k]*a[k][j]
                assert p%den==0
                a[i][j]=p//den
        for i in range(k+1,n):a[i][k]=0
        den=piv
    return sign*a[-1][-1]

def check():
    global count
    for n in range(1,12):
        J=joint(n);Tn,hs=T(n)
        M=[[0]*n for _ in range(n)]
        for word in enumerate_dyck(n):
            a,b=a_b(word);M[a-1][b-1]+=1
        for i in range(n):
            for j in range(n):
                assert J[i][j]==M[i][j],(n,i,j,'Gram')
                count+=1
                L=2*n-(i+1)-(j+1)-2
                direct=cb(L,n-(i+1)-1)-cb(L,n-1) if i<n-1 and j<n-1 else int(i==j==n-1)
                assert M[i][j]==direct,(n,i,j,'formula',M[i][j],direct)
                count+=1
        for a in range(1,n+1):
            rsum=a*comb(2*n-a,n-a)//(2*n-a)
            assert sum(J[a-1])==rsum,(n,a,'row sum')
            count+=1
        for a in range(n):
            for hidx,h in enumerate(hs):
                assert Tn[a][hidx]>=0
                count+=1
        if n>=3:
            assert J[0]==J[1]
            count+=1
        assert det([[Tn[a-1][j] for j in range(len(hs))] for a in range(n-len(hs)+1,n+1)])==1,(n,'rank')
        count+=1
    for n in range(1,22):
        J=joint(n);Tn,hs=T(n)
        for a in range(n):
            for b in range(n):
                assert J[a][b]>=0
                count+=1
        for aa in combinations(range(n),2):
            for bb in combinations(range(n),2):
                assert J[aa[0]][bb[0]]*J[aa[1]][bb[1]]>=J[aa[0]][bb[1]]*J[aa[1]][bb[0]],(n,aa,bb)
                count+=1
    # All-order minors for small n, including rectangular T.
    for n in range(1,9):
        J=joint(n);Tn,hs=T(n)
        for mat in (J,Tn):
            m=len(mat);p=len(mat[0]);
            for k in range(1,min(m,p)+1):
                for rr in combinations(range(m),k):
                    for cc in combinations(range(p),k):
                        d=det([[mat[i][j] for j in cc] for i in rr]);assert d>=0,(n,rr,cc,d)
                        count+=1
    print('PASSED',count,'exact checks; exhaustive Dyck paths n<=11, all minors n<=8, 2x2 n<=21')

if __name__=='__main__':check()
