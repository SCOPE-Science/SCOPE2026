#!/usr/bin/env python3
"""Exact combinatorial tests for the degree-bounded induced-subgraph complex.
All numbers are obtained from fresh simplicial-face enumeration, not typed-in homology tables.
No nonstandard Python dependencies.
"""
from itertools import combinations, permutations, product
from collections import Counter
from math import comb


def faces(m,n,r):
    V=range(m+n)
    out=[]
    for k in range(1,m+n+1):
        for tup in combinations(V,k):
            a=sum(i<m for i in tup);b=k-a
            if a==0 or b==0 or (a<=r and b<=r):out.append(tup)
    return out


def rank_mod_p(rows,p):
    if not rows:return 0
    A=[[int(v)%p for v in row] for row in rows]
    nr,nc=len(A),len(A[0]);rank=0
    for c in range(nc):
        ix=next((i for i in range(rank,nr) if A[i][c]),None)
        if ix is None:continue
        A[rank],A[ix]=A[ix],A[rank]
        z=pow(A[rank][c],-1,p)
        for k in range(c,nc):A[rank][k]=(A[rank][k]*z)%p
        for i in range(rank+1,nr):
            q=A[i][c]
            if q:
                for k in range(c,nc):A[i][k]=(A[i][k]-q*A[rank][k])%p
        rank+=1
        if rank==nr:break
    return rank


def homology(m,n,r,prime):
    fs=faces(m,n,r)
    bydim={d:sorted(f for f in fs if len(f)==d+1) for d in range(max(map(len,fs)))}
    boundary={-1:0}
    for d in range(1,max(bydim)+1):
        A=bydim[d-1];B=bydim[d]
        pos={a:i for i,a in enumerate(A)}
        rows=[[0]*len(B) for _ in A]
        for col,b in enumerate(B):
            for j in range(len(b)):
                i=pos[b[:j]+b[j+1:]]
                rows[i][col]=(-1)**j
        boundary[d]=rank_mod_p(rows,prime)
    boundary[max(bydim)+1]=0
    # reduced C_0 --> C_-1 has rank one for nonempty K
    boundary[0]=1
    betti={d:len(bydim[d])-boundary[d]-boundary[d+1] for d in bydim}
    expected={r:comb(m-1,r)+comb(n-1,r),2*r-1:comb(m-1,r)*comb(n-1,r)}
    for d in betti:
        assert betti[d]==expected.get(d,0),(m,n,r,prime,d,betti,expected)
    return betti,len(fs)


def sign(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1


def chain_trace(fs,perm):
    tr=0
    for s in fs:
        out=[perm[v] for v in s]
        if set(out)==set(s):
            pos={v:i for i,v in enumerate(s)}
            tr+=(-1)**(len(s)-1)*sign([pos[v] for v in out])
    return tr-1 # reduced Euler trace


def wedge_char(p,r):
    cycles=[];seen=set()
    for i in range(len(p)):
        if i not in seen:
            j=i;count=0
            while j not in seen:
                seen.add(j);count+=1;j=p[j]
            cycles.append(count)
    A=[1]+[0]*r
    for ell in cycles:
        for k in range(r,ell-1,-1):A[k]-=(-1)**ell*A[k-ell]
    # divide by (1+t) to remove trivial summand
    B=[0]*(r+1)
    for k in range(r+1):B[k]=A[k]-(B[k-1] if k else 0)
    return B[r]


def check_char(m,n,r,swap=False):
    fs=faces(m,n,r)
    P=list(permutations(range(m)));Q=list(permutations(range(n)))
    for p in P:
        for q in Q:
            f=tuple(p)+tuple(m+x for x in q)
            ap,bq=wedge_char(p,r),wedge_char(q,r)
            pred=(-1)**r*(ap+bq)-ap*bq
            actual=chain_trace(fs,f)
            assert actual==pred,(m,n,r,p,q,actual,pred)
            if swap:
                # first swap, then apply (p,q)
                sw=tuple(m+i for i in range(m))+tuple(i for i in range(m))
                g=tuple(f[sw[i]] for i in range(2*m))
                # tr of wedge^r(p*q) = tr of wedge^r(q*p)
                pq=tuple(p[q[i]] for i in range(m))
                pred=(-1)**(r+1)*wedge_char(pq,r)
                actual=chain_trace(fs,g)
                assert actual==pred,(m,n,r,p,q,'swap',actual,pred)
    print('character_checks',m,n,r,len(P)*len(Q),('plus swap' if swap else ''),'OK')


if __name__=='__main__':
    for m,n,r in [(3,3,2),(4,4,2),(4,5,2),(5,5,3)]:
        d2,fc=homology(m,n,r,2)
        d3,_=homology(m,n,r,3)
        assert d2==d3
        print(f'm={m},n={n},r={r}: faces={fc}, beta={d2}, p=2,3 OK')
    for m,n,r,s in [(3,3,2,True),(4,4,2,True),(4,5,2,False),(4,4,3,True)]:
        check_char(m,n,r,s)
    print('VERIFY_OK')
