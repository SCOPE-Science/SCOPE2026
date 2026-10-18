#!/usr/bin/env python3
"""Reproducible exact verification for square-zero alternating matrices over even finite fields.
No external dependencies. All arithmetic in GF(2), GF(4), GF(8)."""
from collections import Counter
from itertools import product
from math import prod

MOD={2:0b11,4:0b111,8:0b1011}

def mul(a,b,q):
    mask=q-1; poly=MOD[q]; ans=0
    while b:
        if b&1: ans^=a
        b>>=1; a<<=1
        if a&q: a^=poly
    return ans&mask

def inv(a,q):
    assert a
    for b in range(1,q):
        if mul(a,b,q)==1: return b
    raise RuntimeError('nonfield arithmetic')

def rank(rows,q):
    n=len(rows);m=len(rows[0]);a=[list(row) for row in rows];r=0
    for j in range(m):
        pivot=next((i for i in range(r,n) if a[i][j]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        u=inv(a[r][j],q)
        for k in range(j,m): a[r][k]=mul(a[r][k],u,q)
        for i in range(r+1,n):
            b=a[i][j]
            if b:
                for k in range(j,m):a[i][k]^=mul(b,a[r][k],q)
        r+=1
        if r==n:break
    return r

def iso(m,r,q):
    if r<0 or r>m:return 0
    out=1
    for i in range(r):
        # exact integer ratio after cancelling as a whole below
        pass
    num=prod(q**(2*(m-i))-1 for i in range(r))
    den=prod(q**(r-i)-1 for i in range(r))
    assert num%den==0
    return num//den

def nondeg_alt(r,q):
    if r%2:return 0
    s=r//2
    return q**(s*(s-1))*prod(q**(2*i-1)-1 for i in range(1,s+1))

def predicted(n,q):
    out={0:1}
    for r in range(2,n+1,2):
        if n%2:
            mult=iso((n-1)//2,r,q)
        else:
            m=(n-2)//2
            mult=iso(m,r-1,q)+q**r*iso(m,r,q)
        count=mult*nondeg_alt(r,q)
        if count:out[r]=count
    return out

def brute(n,q):
    idx=[(i,j) for i in range(n) for j in range(i+1,n)]
    out=Counter(); total=q**len(idx)
    mt=[[mul(a,b,q) for b in range(q)] for a in range(q)]
    for digits in product(range(q),repeat=len(idx)):
        A=[[0]*n for _ in range(n)]
        for (i,j),v in zip(idx,digits): A[i][j]=A[j][i]=v
        if any((lambda v: v!=0)( __import__('functools').reduce(lambda a,b:a^b,(mt[A[i][k]][A[k][j]] for k in range(n)),0)) for i in range(n) for j in range(n)):
            continue
        out[rank(A,q)]+=1
    return dict(out),total

if __name__=='__main__':
    for n,q in [(2,2),(3,2),(4,2),(5,2),(6,2),(2,4),(3,4),(4,4),(2,8),(3,8)]:
        actual,total=brute(n,q);want=predicted(n,q)
        print('n=',n,'q=',q,'candidate=',total,'ranks=',actual)
        assert actual==want,(n,q,actual,want)
    for q in (2,4,8):
        for n in range(2,17):
            counts=predicted(n,q)
            assert all(r%2==0 and r<=n//2 for r in counts)
            assert max(counts)==2*(n//4)
    print('VERIFY_OK_ALTERNATING_SQUAREZERO_CHAR2')
