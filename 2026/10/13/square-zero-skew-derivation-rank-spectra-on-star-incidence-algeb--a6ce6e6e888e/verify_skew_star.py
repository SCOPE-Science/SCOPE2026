#!/usr/bin/env python3
"""Independent modular-linear derivation-space and square-zero rank checks.
Usage: python verify_skew_star.py; requires only Python standard library.
"""
from itertools import product
from collections import Counter
from math import comb

def gf_rank(rows,p):
    A=[list(map(lambda x:x%p,row)) for row in rows]
    if not A:return 0
    r=0; n=len(A[0]); m=len(A)
    for col in range(n):
        k=next((i for i in range(r,m) if A[i][col]), None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        z=pow(A[r][col],-1,p)
        A[r]=[(z*t)%p for t in A[r]]
        for i in range(r+1,m):
            t=A[i][col]
            if t:
                A[i]=[(a-t*b)%p for a,b in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

def star(m,swaps):
    n=1+2*m; sigma=list(range(m))
    for i in range(0,2*swaps,2):sigma[i],sigma[i+1]=i+1,i
    # index 0 is source, i+1 leaf diagonal, m+i+1 arrow
    mult={}
    for x in range(n):
        for y in range(n):
            z=None
            if x==y and x<=m:z=x
            elif x==0 and y>m:z=y
            elif m<x and y==x-m:z=x
            if z is not None:mult[x,y]=z
    phi=[0]+[sigma[i]+1 for i in range(m)]+[m+sigma[i]+1 for i in range(m)]
    return n,sigma,mult,phi

def derivation_nullity(m,s,p):
    n,sigma,mult,phi=star(m,s)
    eq=[]
    for x in range(n):
      for y in range(n):
       z=mult.get((x,y))
       for k in range(n):
        row=[0]*(n*n)
        if z is not None:row[k*n+z]+=1
        for t in range(n):
            if mult.get((t,y))==k:row[t*n+x]-=1
            if mult.get((phi[x],t))==k:row[t*n+y]-=1
        if any(a%p for a in row):eq.append(row)
    return n*n-gf_rank(eq,p)

def operator(m,s,p,pars):
    n,sg,mult,phi=star(m,s)
    alpha,delta,beta=pars
    M=[[0]*n for _ in range(n)]
    for i in range(m):
        di=i+1;ri=m+i+1
        M[ri][0]-=beta[i]
        M[ri][di]+=beta[i]
        M[ri][ri]+=delta[i]
        if sg[i]!=i:
            M[di][di]+=alpha[i]
            M[sg[i]+1][di]-=alpha[sg[i]]
            M[m+sg[i]+1][ri]-=alpha[sg[i]]
    return [[x%p for x in row] for row in M]

def square_zero(M,p):
    n=len(M)
    for i in range(n):
     for j in range(n):
      if sum(M[i][k]*M[k][j] for k in range(n))%p:return False
    return True

def predicted(m,s,p):
    f=m-2*s
    pair=Counter({0:1,1:2*(p-1),2:(p-1)**2+(p-1)*(p if p%2==0 else p+1)})
    pol=Counter({0:1})
    for _ in range(s):
     nex=Counter()
     for i,a in pol.items():
      for j,b in pair.items():nex[i+j]+=a*b
     pol=nex
    for _ in range(f):
     nex=Counter()
     for i,a in pol.items():nex[i]+=a;nex[i+1]+=a*(p-1)
     pol=nex
    return pol

def verify_basis_derivations(m,s,p):
    n,sg,mult,phi=star(m,s)
    dim=2*m+2*s
    for j in range(dim):
        vals=[0]*dim; vals[j]=1
        alpha=[0]*m
        for i in range(2*s):alpha[i]=vals[i]
        D=operator(m,s,p,(alpha, vals[2*s:2*s+m], vals[2*s+m:]))
        for x in range(n):
          for y in range(n):
            xy=mult.get((x,y))
            for k in range(n):
                lhs=D[k][xy] if xy is not None else 0
                rhs=sum(D[t][x] for t in range(n) if mult.get((t,y))==k)
                rhs+=sum(D[t][y] for t in range(n) if mult.get((phi[x],t))==k)
                assert (lhs-rhs)%p==0,(m,s,p,j,x,y,k,lhs,rhs)

def gf4mul(x,y):
    z=0
    for i in range(2):
      for j in range(2):
        if (x>>i&1) and (y>>j&1): z^=1<<(i+j)
    if z&4:z^=7  # t^2+t+1=0
    return z

def gf4rank(M):
    A=[row[:] for row in M]; m=len(A); n=len(A[0]);r=0
    for j in range(n):
        i=next((k for k in range(r,m) if A[k][j]), None)
        if i is None: continue
        A[r],A[i]=A[i],A[r]
        inv=gf4mul(A[r][j],A[r][j])
        A[r]=[gf4mul(inv,x) for x in A[r]]
        for k in range(r+1,m):
            c=A[k][j]
            if c:A[k]=[a^gf4mul(c,b) for a,b in zip(A[k],A[r])]
        r+=1
        if r==m:break
    return r

def _xor4(seq):
    z=0
    for x in seq:z^=x
    return z

def verify_gf4():
    cnt=Counter()
    for a,b,di,dj,t,u in product(range(4),repeat=6):
      M=[[0]*5 for _ in range(5)]
      for k,x in enumerate((t,u)):
        M[3+k][0]^=x
      M[1][1]^=a;M[2][1]^=b;M[3][1]^=t
      M[2][2]^=b;M[1][2]^=a;M[4][2]^=u
      M[3][3]^=di;M[4][3]^=b
      M[4][4]^=dj;M[3][4]^=a
      if any(any(_xor4(gf4mul(M[i][k],M[k][j]) for k in range(5)) for j in range(5)) for i in range(5)):continue
      cnt[gf4rank(M)]+=1
    assert cnt==predicted(2,1,4),(cnt,predicted(2,1,4))
    print('PASS',dict(m=2,transpositions=1,q=4,rank_counts=sorted(cnt.items()),total=sum(cnt.values())))

def exhaust(m,s,p):
    n,sg,mult,phi=star(m,s)
    assert derivation_nullity(m,s,p)==2*m+2*s
    verify_basis_derivations(m,s,p)
    result=Counter()
    for vals in product(range(p),repeat=2*m+2*s):
        alpha=[0]*m
        for i in range(2*s):alpha[i]=vals[i]
        delta=vals[2*s:2*s+m];beta=vals[2*s+m:]
        M=operator(m,s,p,(alpha,delta,beta))
        if square_zero(M,p):result[gf_rank(M,p)]+=1
    expect=predicted(m,s,p)
    assert result==expect, (m,s,p,result,expect)
    print('PASS',dict(m=m,transpositions=s,p=p,rank_counts=sorted(result.items()),total=sum(result.values())))

if __name__=='__main__':
    for data in [(2,1,2),(2,1,3),(2,1,5),(3,1,2),(4,2,2),(2,0,3)]:exhaust(*data)
    verify_gf4()
    print('VERIFY_OK')
