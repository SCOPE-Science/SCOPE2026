#!/usr/bin/env python3
"""Independent GF(2) row-reduction and codeword enumeration for two-token biclique parity kernels."""
from itertools import combinations
from math import comb
from collections import Counter

def polyprod(a,b):
    r=Counter()
    for i,x in a.items():
        for j,y in b.items():r[i+j]+=x*y
    return +r

def mult_bin(a,z):
    # polynomial (1+z)^a times (1-z)^z
    p=[1]
    for _ in range(a):
        q=[0]*(len(p)+1)
        for i,v in enumerate(p):q[i]+=v;q[i+1]+=v
        p=q
    for _ in range(z):
        q=[0]*(len(p)+1)
        for i,v in enumerate(p):q[i]+=v;q[i+1]-=v
        p=q
    return p

def closed(m,n):
    L=m*n
    cx=[0]*(L+1)
    for p in range(0,m+1,2):
        for q in range(0,n+1,2):
            w=p*(n-q)+(m-p)*q
            f=comb(m,p)*comb(n,q)
            terms=mult_bin(L-w,w)
            for j,v in enumerate(terms):cx[j]+=f*v
    d=2**(m+n-2)
    assert all(x%d==0 for x in cx)
    X=Counter({i:x//d for i,x in enumerate(cx) if x})
    def euler(q,odd):
        N=comb(q,2)
        cc=[0]*(N+1)
        for p in range(q+1):
            w=p*(q-p)
            f=(-1 if odd and p%2 else 1)*comb(q,p)
            terms=mult_bin(N-w,w)
            for j,v in enumerate(terms):cc[j]+=f*v
        den=2**q
        assert all(x%den==0 for x in cc)
        return Counter({i:x//den for i,x in enumerate(cc) if x})
    Y=polyprod(euler(m,False),euler(n,False))
    if m%2==0 and n%2==0:
        plus=polyprod(euler(m,True),euler(n,True))
        for i,v in plus.items():Y[i]+=v
    assert min(X.values())>=0 and min(Y.values())>=0
    return polyprod(X,Y),X,Y

def graph(m,n):
    v=list(combinations(range(m+n),2)); N=len(v)
    adj=[]
    for x in v:
        row=0
        for j,y in enumerate(v):
            d=list(set(x)^set(y))
            if len(d)==2 and ((d[0]<m)!=(d[1]<m)):
                row|=1<<j
        adj.append(row)
    return adj

def nullspace(rows):
    a=rows[:];n=len(a);pivs=[];r=0
    for j in range(n):
        k=next((i for i in range(r,n) if a[i]&(1<<j)),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k]
        for i in range(n):
            if i!=r and (a[i]>>j)&1:a[i]^=a[r]
        pivs.append(j);r+=1
    free=[j for j in range(n) if j not in pivs]
    basis=[]
    for j in free:
        v=1<<j
        for i,p in enumerate(pivs):
            if (a[i]>>j)&1:v|=1<<p
        assert all((row&v).bit_count()%2==0 for row in rows)
        basis.append(v)
    return basis,r

def enumerate_code(b):
    c=Counter({0:1});prev=0
    for g in range(1,1<<len(b)):
        diff=g^(g>>1) ^((g-1)^((g-1)>>1))
        prev^=b[(diff&-diff).bit_length()-1]
        c[prev.bit_count()]+=1
    return c

for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
    rows=graph(m,n);b,r=nullspace(rows)
    actual=enumerate_code(b)
    formula,X,Y=closed(m,n)
    delta=int(m%2==0 and n%2==0)
    expected_rank=m+n-2-delta
    assert r==2*expected_rank,(m,n,r,expected_rank)
    assert len(b)==len(rows)-2*expected_rank
    assert actual==formula,(m,n,actual,formula)
    print('INDEPENDENT_GF2_KERNEL_OK',m,n,'nullity',len(b),'kernel_words',sum(actual.values()),'min_nonzero',min(k for k in actual if k>0),'weights',sorted(actual.items())[:13])
for m in range(2,10):
 for n in range(m,11):
    formula,X,Y=closed(m,n)
    delta=int(m%2==0 and n%2==0)
    nullity=comb(m+n,2)-2*(m+n-2-delta)
    assert sum(formula.values())==2**nullity,(m,n,sum(formula.values()),nullity)
    assert formula[0]==1
print('VERIFY_OK')
