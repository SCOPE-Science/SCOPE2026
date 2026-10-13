#!/usr/bin/env python3
"""Independent direct commutator enumeration and graph-partition prediction."""
from itertools import product
from collections import Counter

def parts(n, E, q, target):
    m=len(E)
    z_nonzero=[x!=0 for x in target]
    total=0
    for cols in product(range(q*q),repeat=n):
        val=1
        for a,(i,j) in enumerate(E):
            if cols[i]==cols[j]:
                if z_nonzero[a]:val=0;break
                val*=q
        total+=val
    return (q**m)*total

def direct(n,E,q):
    m=len(E)
    elements=list(product(range(q),repeat=n+m))
    cnt=Counter()
    for X in elements:
        for Y in elements:
            z=tuple(((X[i]-X[j])*Y[n+t]-(Y[i]-Y[j])*X[n+t])%q for t,(i,j) in enumerate(E))
            cnt[z]+=1
    for z in product(range(q), repeat=m):
        predicted=parts(n,E,q,z)
        assert cnt[z]==predicted,(n,E,q,z,cnt[z],predicted)
    print('EXHAUST_OK',q,n,E,'targets',q**m,'pairs',len(elements)**2)

def chrom_num(n,E):
    pairs={tuple(sorted(x)) for x in E}
    for k in range(1,n+1):
        for col in product(range(k),repeat=n):
            if all(col[i]!=col[j] for i,j in pairs):return k

def fk(n,E,q,z):
    result=0; m=len(E)
    for bits in product((0,1),repeat=m):
        parent=list(range(n))
        def find(i):
            while parent[i]!=i:i=parent[i]
            return i
        p=1
        for bit,(i,j),v in zip(bits,E,z):
            if bit:
                a,b=find(i),find(j)
                parent[a]=b
                p*=(-1 if v else q-1)
        k=len({find(v) for v in range(n)})
        result+=p*(q*q)**k
    return q**m*result

for n,E,q in [(2,[(0,1)],2),(2,[(0,1),(0,1)],2),(3,[(0,1),(1,2)],2),
              (3,[(0,1),(1,2),(2,0)],2),(2,[(0,1)],3)]:
    direct(n,E,q)
    for z in product(range(q),repeat=len(E)):
        assert parts(n,E,q,z)==fk(n,E,q,z)
print('FK_OK')
for n in (4,5,9):
    E=[(i,j) for i in range(n) for j in range(i+1,n)]
    chi=n  # A complete graph requires distinct colors at every vertex.
    width=next(r for r in range(1,4) if (2**(2*r))>=chi)
    assert chi==n
    if n<=5: assert (chrom_num(n,E)==n)
    print('COMPLETE_CHROMATIC_WIDTH_OK',n,chi,width)
print('VERIFY_OK')
