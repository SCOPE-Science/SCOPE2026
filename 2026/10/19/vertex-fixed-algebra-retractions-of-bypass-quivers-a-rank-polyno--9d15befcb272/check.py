"""Finite-field verification for vertex-fixed retractions of three-vertex path algebras.

Usage: python check.py
This is an independent finite-case check, not an infinite proof.
"""
from itertools import product
from collections import Counter
from math import prod


def field(q):
    if q in (2, 3):
        return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q
    if q == 4:
        def mul(a,b):
            z=0
            for i in range(2):
                if (b>>i)&1: z ^= a<<i
            if z&8: z ^= 0b1100  # x^3 = x^2+x, mod x^2+x+1
            if z&4: z ^= 0b111   # x^2 = x+1
            return z
        return lambda a,b:a^b, mul
    raise ValueError(q)

def gauss_rank(M,q):
    add,mul=field(q)
    A=[row[:] for row in M]; rows=len(A); cols=len(A[0]); piv=0
    for c in range(cols):
        k=next((i for i in range(piv,rows) if A[i][c]),None)
        if k is None:continue
        A[piv],A[k]=A[k],A[piv]
        inv=next(z for z in range(1,q) if mul(z,A[piv][c])==1)
        A[piv]=[mul(inv,x) for x in A[piv]]
        for i in range(rows):
            if i!=piv and A[i][c]:
                z=A[i][c]
                A[i]=[add(a,mul(z,b)) for a,b in zip(A[i],A[piv])]
        piv+=1
        if piv==rows:break
    return piv

def gb(q,n,k):
    # Division only after complete products.
    numerator=prod(q**(n-j)-1 for j in range(k))
    denominator=prod(q**(k-j)-1 for j in range(k))
    return numerator//denominator

def predicted(q,r,s,t):
    C=Counter();m=r*s
    for a in range(r+1):
        for b in range(s+1):
            for d in range(t+1):
                z=a*b
                count=(gb(q,r,a)*q**(a*(r-a))*gb(q,s,b)*q**(b*(s-b))
                       *gb(q,t,d)*q**(d*(t-d))
                       *q**(d*(m-z)+(t-d)*z))
                C[3+a+b+d+z]+=count
    return C

def test(q,r,s,t):
    add,mul=field(q)
    # Basis order: vertices; arrows 1->2, 2->3, 1->3; length-two paths 1->2->3.
    x=list(range(3,3+r)); y=list(range(3+r,3+r+s));
    w=list(range(3+r+s,3+r+s+t));
    paths=list(range(3+r+s+t,3+r+s+t+r*s));
    n=3+r+s+t+r*s
    endpts=[(i,i) for i in range(3)]+[(0,1)]*r+[(1,2)]*s+[(0,2)]*(t+r*s)
    table=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if endpts[i][1]!=endpts[j][0]:continue
            if i<3: table[i][j]=j
            elif j<3: table[i][j]=i
            elif i in x and j in y:
                table[i][j]=paths[x.index(i)*s+y.index(j)]
    def vproduct(A,B):
        out=[0]*n
        for i,ai in enumerate(A):
            if ai:
                for j,bj in enumerate(B):
                    if bj and table[i][j] is not None:
                        k=table[i][j];out[k]=add(out[k],mul(ai,bj))
        return out
    def mapping(M,V):
        z=[0]*n
        for j,c in enumerate(V):
            if c:
                for i in range(n):z[i]=add(z[i],mul(M[i][j],c))
        return z
    actual=Counter();n_maps=0
    for entries in product(range(q),repeat=r*r+s*s+t*t+r*s*t):
        ptr=0
        def matrix(rows,cols):
            nonlocal ptr
            out=[list(entries[ptr+i*cols:ptr+(i+1)*cols]) for i in range(rows)]
            ptr+=rows*cols
            return out
        S=matrix(r,r);T=matrix(s,s);D=matrix(t,t);B=matrix(r*s,t)
        M=[[0]*n for _ in range(n)]
        for i in range(3):M[i][i]=1
        for out_cols,in_cols,F in [(x,x,S),(y,y,T),(w,w,D),(paths,w,B)]:
            for i,oi in enumerate(out_cols):
                for j,ij in enumerate(in_cols):M[oi][ij]=F[i][j]
        for ai,xi in enumerate(x):
            for bj,yj in enumerate(y):
                out=paths[ai*s+bj]
                P=vproduct([M[i][xi] for i in range(n)],[M[i][yj] for i in range(n)])
                for i in range(n):M[i][out]=P[i]
        # Independent multiplication check on every ordered basis pair.
        for i in range(n):
            for j in range(n):
                e=vproduct([M[k][i] for k in range(n)],[M[k][j] for k in range(n)])
                m=table[i][j]
                rhs=[M[k][m] for k in range(n)] if m is not None else [0]*n
                assert e==rhs,(q,r,s,t,i,j)
        n_maps+=1
        if all(mapping(M,[M[k][j] for k in range(n)]) == [M[k][j] for k in range(n)] for j in range(n)):
            actual[gauss_rank(M,q)]+=1
    expected=predicted(q,r,s,t)
    assert actual==expected,(q,r,s,t,actual,expected)
    print('PASS',q,r,s,t,'homomorphisms',n_maps,'idempotents',sum(actual.values()),'ranks',dict(sorted(actual.items())))

if __name__=='__main__':
    for args in [(2,1,1,1),(3,1,1,1),(4,1,1,1),(2,2,1,1),(2,1,2,1),(2,2,2,1)]:
        test(*args)
    print('ALL_EXACT_CHECKS_PASSED')
