"""Exact checks for random fixed-block partition tree-edge covariance."""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from collections import defaultdict
from math import comb

@lru_cache(None)
def stirling(n,k):
    if n==k==0:return 1
    if n<0 or k<0 or k>n or not n or not k:return 0
    return k*stirling(n-1,k)+stirling(n-1,k-1)

def partitions(n):
    def rec(a,m):
        if len(a)==n:
            yield tuple(a);return
        for k in range(m+2):
            yield from rec(a+[k],max(m,k))
    yield from rec([0],0)

def tree(n,seq):
    deg=[1]*n
    for x in seq:deg[x]+=1
    edges=[]
    for x in seq:
        v=min(i for i in range(n) if deg[i]==1)
        edges.append(tuple(sorted((v,x))))
        deg[v]-=1;deg[x]-=1
    i,j=[v for v in range(n) if deg[v]==1]
    edges.append((i,j))
    return frozenset(edges)

assert sum(stirling(6,k) for k in range(1,7))==203
assert sum(1 for _ in partitions(6))==203
checks=0
for n in range(3,8):
    for k in range(2,n):
        a,b,d=stirling(n,k),stirling(n-1,k),stirling(n-2,k)
        p,q=Fraction(b,a),Fraction(d,a)
        assert q < p*p
        N=comb(n,2)
        assert (n-1)**2*(p*p-q)/(p-q) <= Fraction((n-1)**2,N)
        for overlap in range(n):
            c=overlap*(p-q)-(n-1)**2*(p*p-q)
            if overlap==0:assert c<0
            if overlap>=2:assert c>0
            checks+=1
    if n>6:continue
    baseline=frozenset((i,i+1) for i in range(n-1))
    representatives={}
    for seq in product(range(n),repeat=n-2):
        other=tree(n,seq)
        t=len(baseline&other)
        representatives.setdefault(t,other)
        if len(representatives)==n:break
    for k in range(2,n):
        ps=[part for part in partitions(n) if max(part)+1==k]
        a=stirling(n,k)
        assert len(ps)==a
        p,q=Fraction(stirling(n-1,k),a),Fraction(stirling(n-2,k),a)
        for t,other in representatives.items():
            aval=bval=abval=0
            for part in ps:
                x=sum(part[u]==part[v] for u,v in baseline)
                y=sum(part[u]==part[v] for u,v in other)
                aval+=x;bval+=y;abval+=x*y
            observed=Fraction(abval,a)-Fraction(aval*bval,a*a)
            predicted=t*(p-q)-(n-1)**2*(p*p-q)
            assert observed==predicted,(n,k,t,observed,predicted)
            checks+=1
    print('n',n,'checked overlap classes',sorted(representatives))
for n in range(4,35):
    k=n-1
    a,b,d=stirling(n,k),stirling(n-1,k),stirling(n-2,k)
    tau=Fraction((n-1)**2*(b*b-a*d),a*(b-d))
    assert tau==Fraction(2*(n-1),n)
for n in range(3,35):
    k=2
    a,b,d=stirling(n,k),stirling(n-1,k),stirling(n-2,k)
    tau=Fraction((n-1)**2*(b*b-a*d),a*(b-d))
    assert tau==Fraction((n-1)**2,2**(n-1)-1)
print('ALL EXACT CHECKS PASSED',checks)
