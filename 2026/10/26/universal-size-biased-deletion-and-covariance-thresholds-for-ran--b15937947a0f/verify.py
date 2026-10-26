#!/usr/bin/env python3
"""Independent finite-state checks for size-biased component deletion in binomial uniform hypergraphs."""
from itertools import combinations
from fractions import Fraction
from math import comb


def bc(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def comp_data(n, edges, mask):
    parent=list(range(n))
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for j,e in enumerate(edges):
        if mask >> j & 1:
            z=e[0]
            for v in e[1:]:
                a,b=root(z),root(v)
                parent[b]=a
    vertices={}
    for v in range(n):
        vertices.setdefault(root(v),[]).append(v)
    numedges={key:0 for key in vertices}
    for j,e in enumerate(edges):
        if mask >> j & 1:
            numedges[root(e[0])]+=1
    x=sum(len(vs)==1 for vs in vertices.values())
    stat={}
    for key,vs in vertices.items():
        s=len(vs); j=numedges[key]
        if j:
            stat[(s,j)]=stat.get((s,j),0)+1
    return x,stat


def one_case(n,r,p):
    edges=list(combinations(range(n),r))
    assert len(edges)<=15
    M=len(edges); q=1-p
    mass=[p**j*q**(M-j) for j in range(M+1)]
    ex=sum(bc(n-1,r-1) for _ in range(0)) # no reliance on assertions about moments
    ex=Fraction(n)*q**bc(n-1,r-1)
    total={}; cross={}; factorial={}
    for mask in range(1<<M):
        x,bytype=comp_data(n,edges,mask)
        w=mass[mask.bit_count()]
        for (s,j),y in bytype.items():
            if s>=n: continue
            key=(s,j)
            total[key]=total.get(key,Fraction(0))+w*y
            cross[key]=cross.get(key,Fraction(0))+w*x*y
            factorial[key]=factorial.get(key,Fraction(0))+w*x*(x-1)*y
    checked=0
    for (s,j),ey in total.items():
        assert ey>0
        outside=n-s
        y1=outside*q**bc(outside-1,r-1)
        y2=outside*(outside-1)*q**(bc(outside,r)-bc(outside-2,r))
        assert cross[(s,j)]==ey*y1, (n,r,p,s,j,'first',cross[(s,j)],ey*y1)
        assert factorial[(s,j)]==ey*y2, (n,r,p,s,j,'second')
        cov=cross[(s,j)]-ex*ey
        assert cov==ey*(y1-ex)
        checked+=1
    assert checked
    return checked, 1<<M


def threshold_checks():
    from decimal import Decimal, getcontext
    getcontext().prec=70
    for n in range(5,51):
        for r in range(2,min(n,8)):
            arr=[]
            for s in range(r,n):
                delta=bc(n-1,r-1)-bc(n-s-1,r-1)
                root=(Decimal(1)-Decimal(s)/Decimal(n))**(Decimal(1)/Decimal(delta))
                arr.append(Decimal(1)-root)
            assert all(a<b for a,b in zip(arr,arr[1:])), (n,r)
    print('THRESHOLD_STRICT_ORDER_PASS')

if __name__=='__main__':
    strata=0; states=0
    for n,r in [(3,2),(4,2),(5,2),(4,3),(5,3),(5,4),(6,4)]:
        for p in [Fraction(1,4),Fraction(2,3)]:
            k,z=one_case(n,r,p)
            strata+=k;states+=z
            print('EXACT_COMPONENT_PALM_PASS',n,r,str(p),k,z)
    threshold_checks()
    print('VERIFY_OK',strata,'component-shape strata',states,'hypergraph states')
