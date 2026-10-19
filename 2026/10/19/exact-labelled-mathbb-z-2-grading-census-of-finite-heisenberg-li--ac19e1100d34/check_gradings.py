#!/usr/bin/env python3
"""Independent exhaustive checks for labelled Z/2-gradings of Heisenberg Lie algebras.

A grading is an ordered pair (H_0,H_1), including H_1=0. The program
enumerates reduced-row-echelon subspace bases and tests the bracket axiom.
No computer algebra system is required.
"""
from itertools import combinations, product
from math import prod

class Field:
    def __init__(self, q):
        self.q=q
        if q==4:
            self.add=lambda a,b:a^b
            self.mul=lambda a,b: (((a&1)&(b&1)) ^ (((a>>1)&(b>>1)))) | (((((a&1)&(b>>1)) ^ ((a>>1)&(b&1)) ^ ((a>>1)&(b>>1)))&1)<<1)
        else:
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
        self.inv={a:next(b for b in range(1,q) if self.mul(a,b)==1) for a in range(1,q)}
    def sub(self,a,b):
        return self.add(a, self.additive_inverse(b))
    def additive_inverse(self,b):
        return b if self.q==4 else (-b)%self.q

def rowrank(rows,d,F):
    m=[list(row) for row in rows]
    rank=0
    for c in range(d):
        pivot=next((j for j in range(rank,len(m)) if m[j][c]!=0),None)
        if pivot is None:continue
        m[rank],m[pivot]=m[pivot],m[rank]
        inv=F.inv[m[rank][c]]
        m[rank]=[F.mul(inv,v) for v in m[rank]]
        for j in range(len(m)):
            if j!=rank and m[j][c]:
                f=m[j][c]
                m[j]=[F.sub(u,F.mul(f,v)) for u,v in zip(m[j],m[rank])]
        rank+=1
        if rank==len(m):break
    return rank

def subspaces(d,F):
    out=[[] for _ in range(d+1)]
    for k in range(d+1):
        for pivots in combinations(range(d),k):
            slots=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,d) if j not in pivots]
            for values in product(range(F.q),repeat=len(slots)):
                basis=[[0]*d for _ in range(k)]
                for i,p in enumerate(pivots):basis[i][p]=1
                for (i,j),v in zip(slots,values):basis[i][j]=v
                out[k].append(tuple(tuple(r) for r in basis))
    return out

def bracket(x,y,n,F):
    acc=0
    for i in range(n):
        acc=F.add(acc,F.sub(F.mul(x[2*i],y[2*i+1]),F.mul(x[2*i+1],y[2*i])))
    return tuple([0]*(2*n)+[acc])

def closed_pair(B0,B1,n,F):
    d=2*n+1
    for left,right,dest in ((B0,B0,B0),(B0,B1,B1),(B1,B1,B0)):
        for u in left:
            for v in right:
                w=bracket(u,v,n,F)
                if w[-1] and rowrank(tuple(dest)+(w,),d,F)>len(dest):return False
    return True

def sp_order(n,q):
    return q**(n*n)*prod(q**(2*i)-1 for i in range(1,n+1))

def predicted(n,q):
    even={r:q**(2*(n-r))*sp_order(n,q)//(sp_order(r,q)*sp_order(n-r,q)) for r in range(n+1)}
    odd=q**(n*(n+3)//2)*prod(q**i+1 for i in range(1,n+1))
    return even,odd

def verify(n,q):
    F=Field(q); d=2*n+1
    subs=subspaces(d,F)
    z=tuple([0]*(d-1)+[1])
    even={r:0 for r in range(n+1)};odd=0; total=0
    for k in range(d+1):
        for B0 in subs[k]:
            for B1 in subs[d-k]:
                if rowrank(B0+B1,d,F)!=d:continue
                if not closed_pair(B0,B1,n,F):continue
                total+=1
                z0=rowrank(B0+(z,),d,F)==len(B0)
                z1=rowrank(B1+(z,),d,F)==len(B1)
                assert z0!=z1
                if z0:
                    r=(len(B0)-1)//2
                    assert 2*r+1==len(B0)
                    even[r]+=1
                else:odd+=1
    expected_even,expected_odd=predicted(n,q)
    assert even==expected_even,(n,q,even,expected_even)
    assert odd==expected_odd,(n,q,odd,expected_odd)
    assert total==sum(expected_even.values())+expected_odd
    print(f"PASS n={n} q={q}: even={even} odd={odd} total={total}",flush=True)

if __name__=='__main__':
    for n,q in [(1,2),(1,3),(1,4),(1,5),(2,2)]:
        verify(n,q)
    print('ALL_GRADING_COUNTS_PASSED 5',flush=True)
