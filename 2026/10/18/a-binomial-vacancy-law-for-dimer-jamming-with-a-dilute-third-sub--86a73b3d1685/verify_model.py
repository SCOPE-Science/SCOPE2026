#!/usr/bin/env python3
"""Alternative finite-state checks for irreversible dimer deposition on a tripartite graph."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import comb

def aggregate(n,r):
    @lru_cache(None)
    def rec(a,b,c):
        rates=((a*b,(a-1,b-1,c)),(a*c,(a-1,b,c-1)),(b*c,(a,b-1,c-1)))
        total=sum(w for w,_ in rates)
        if not total:
            return {a+b+c:F(1)}
        out={}
        for w,st in rates:
            if w:
                for u,p in rec(*st).items(): out[u]=out.get(u,F(0))+F(w,total)*p
        return out
    return rec(n,n,r)

def labelled(n,r):
    nn=2*n+r
    kinds=[0]*n+[1]*n+[2]*r
    edges=[(i,j) for i in range(nn) for j in range(i+1,nn) if kinds[i]!=kinds[j]]
    @lru_cache(None)
    def rec(mask):
        avail=[(i,j) for i,j in edges if (mask>>i)&1 and (mask>>j)&1]
        if not avail: return {mask.bit_count():F(1)}
        out={}
        for i,j in avail:
            for u,p in rec(mask&~(1<<i)&~(1<<j)).items():
                out[u]=out.get(u,F(0))+p/F(len(avail))
        return out
    return rec((1<<nn)-1)

def target(r):
    o={}
    for k in range(r+1):
        u=abs(2*k-r)
        o[u]=o.get(u,F(0))+F(comb(r,k),2**r)
    return o

def tv(a,b):
    return sum(abs(a.get(i,0)-b.get(i,0)) for i in set(a)|set(b))/2

def test():
    a_ct=0
    for n in range(1,5):
        for r in range(1,5):
            a=aggregate(n,r)
            b=labelled(n,r)
            assert a==b,(n,r,a,b)
            assert sum(a.values())==1
            assert all(u <=r and (u-r)%2==0 for u in a)
            a_ct+=1
    perms_ct=0
    for n,r in [(1,1),(1,2),(2,1)]:
        kinds=[0]*n+[1]*n+[2]*r
        edges=[(i,j) for i in range(2*n+r) for j in range(i+1,2*n+r) if kinds[i]!=kinds[j]]
        assert len(edges)<=8
        freq={}
        for perm in permutations(edges):
            occupied=set()
            for i,j in perm:
                if i not in occupied and j not in occupied: occupied.update([i,j])
            u=2*n+r-len(occupied)
            freq[u]=freq.get(u,0)+1
            perms_ct+=1
        denominator=sum(freq.values())
        assert {u:F(cnt,denominator) for u,cnt in freq.items()}==aggregate(n,r)
    b_ct=0
    for n in range(1,19):
        for r in range(1,6):
            got=aggregate(n,r)
            assert sum(got.values())==1
            for h in range(1,n+1):
                bound=F(r*(h+r),n+r)+F(r*r,4*h)
                assert tv(got,target(r))<=bound,(n,r,h,got,target(r),bound)
                b_ct+=1
    print(f'PASS: {a_ct} exact labeled-vs-class recurrences; {perms_ct} exhaustive edge orders; {b_ct} rational TV-bound comparisons.')
    for n in [1,2,3,5,10,20,40,80]:
        g=aggregate(n,2)
        print('n',n,'r2', {k: str(v) if n<=3 else f'{float(v):.9f}' for k,v in sorted(g.items())})
if __name__=='__main__':test()
