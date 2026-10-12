#!/usr/bin/env python3
"""Independent finite-field checks for endomorphism ranks of two-step alternating algebras."""
import itertools
import math
from collections import Counter


def mul(a,b,q):
    if q != 4: return a*b%q
    if not a or not b: return 0
    t=0
    for i in range(2):
        if (b>>i)&1: t ^= a<<i
    for i in (2,):
        if (t>>i)&1: t ^= 0b111 << (i-2)
    return t

def add(a,b,q):return (a^b if q==4 else (a+b)%q)
def neg(a,q):return (a if q==4 else -a%q)
def inv(a,q):
    assert a
    return next(b for b in range(1,q) if mul(a,b,q)==1)

def rank(a,q):
    a=[list(row) for row in a]
    if not a: return 0
    rows=len(a);cols=len(a[0]);i=0
    for j in range(cols):
        pivot=next((k for k in range(i,rows) if a[k][j]),None)
        if pivot is None:continue
        a[i],a[pivot]=a[pivot],a[i]
        z=inv(a[i][j],q)
        a[i]=[mul(z,t,q) for t in a[i]]
        for k in range(rows):
            if k==i:continue
            fac=a[k][j]
            if fac: a[k]=[add(a[k][t],neg(mul(fac,a[i][t],q),q),q) for t in range(cols)]
        i+=1
        if i==rows:break
    return i

def symp(a,b,m,q):
    s=0
    for k in range(m):
        s=add(s,mul(a[k],b[m+k],q),q)
        s=add(s,neg(mul(a[m+k],b[k],q),q),q)
    return s

def hom(mat,m,q):
    d=2*m
    z=[mat[i][d] for i in range(d+1)]
    vecs=[[mat[i][j] for i in range(d)] for j in range(d+1)]
    for j in range(d+1):
        for k in range(d+1):
            s=symp(vecs[j],vecs[k],m,q)
            w=symp(([1 if h==j else 0 for h in range(d)] if j<d else [0]*d),
                    ([1 if h==k else 0 for h in range(d)] if k<d else [0]*d),m,q)
            expect=[mul(w,z[i],q) for i in range(d+1)]
            actual=[0]*d+[s]
            if actual!=expect:return False
    return True

def gauss(n,k,q):
    if k<0 or k>n:return 0
    return math.prod(q**(n-i)-1 for i in range(k))//math.prod(q**(k-i)-1 for i in range(k))

def formula(m,q):
    d=2*m;res=Counter()
    for r in range(m+1):
        iso=gauss(m,r,q)*math.prod(q**(m-i)+1 for i in range(r))
        cnt=iso*math.prod(q**d-q**i for i in range(r))
        res[r]+=cnt*q**r
        res[r+1]+=cnt*(q**d-q**r)
    gsp=(q-1)*q**(m*m)*math.prod(q**(2*i)-1 for i in range(1,m+1))
    res[d+1]+=q**d*gsp
    return +res

def full_enumeration(m,q):
    d=2*m;n=d+1
    observed=Counter()
    for entries in itertools.product(range(q),repeat=n*n):
        mat=[entries[i*n:(i+1)*n] for i in range(n)]
        if hom(mat,m,q):observed[rank(mat,q)]+=1
    return +observed

def block_enumeration(m,q):
    d=2*m
    observed=Counter();Acount=Counter()
    for entries in itertools.product(range(q),repeat=d*d):
        A=[entries[i*d:(i+1)*d] for i in range(d)]
        cols=[[A[i][j] for i in range(d)] for j in range(d)]
        c=symp(cols[0],cols[m],m,q)
        if any(symp(cols[i],cols[j],m,q)!=mul(c,symp([int(x==i) for x in range(d)],
                        [int(x==j) for x in range(d)],m,q),q) for i in range(d) for j in range(d)):
            continue
        Acount[rank(A,q)]+=1
        for f in itertools.product(range(q),repeat=d):
            M=[tuple(A[i])+ (0,) for i in range(d)]+[tuple(f)+(c,)]
            observed[rank(M,q)]+=1
    return +observed,Acount

def main():
    for m,q in [(1,2),(1,3),(1,4)]:
        got=full_enumeration(m,q);want=formula(m,q)
        assert got==want,(m,q,got,want)
        print('full',m,q,dict(sorted(got.items())))
    m,q=2,2
    got,acount=block_enumeration(m,q);want=formula(m,q)
    assert got==want,(m,q,got,want)
    assert acount==Counter({0:1,1:225,2:3150,4:720}),acount
    print('block',m,q,dict(sorted(got.items())))
    print('VERIFY_OK')
if __name__=='__main__':main()
