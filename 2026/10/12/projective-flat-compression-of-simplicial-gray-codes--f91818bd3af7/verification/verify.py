#!/usr/bin/env python3
"""Exact small-field tests for the Gray-image projective-core theorem.
Independent finite-field construction, projective normalization, weight-two
rank-two checks, and exhaustive core generalized-weight census.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

class F:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
    def plus(self,x,y): return (x^y) if self.q==4 else ((x+y)%self.q)
    def neg(self,x): return x if self.q==4 else (-x)%self.q
    def mul(self,x,y):
        if self.q!=4:return (x*y)%self.q
        z=0
        for i in range(2):
            if y & (1<<i):z^=x<<i
        if z&4:z^=7
        return z
    def inv(self,x):
        assert x
        return next(y for y in range(1,self.q) if self.mul(x,y)==1)
    def scale(self,c,v):return tuple(self.mul(c,z) for z in v)
    def vecsum(self,a,b):return tuple(self.plus(x,y) for x,y in zip(a,b))
    def norm(self,v):
        p=next(z for z in v if z)
        return self.scale(self.inv(p),v)

# Generate exactly one reduced echelon basis for each d-dimensional subspace.
def spaces(field,k,d):
    for piv in combinations(range(k),d):
        pos=[(i,j) for i in range(d) for j in range(piv[i]+1,k) if j not in piv]
        for values in product(range(field.q),repeat=len(pos)):
            rows=[[0]*k for _ in range(d)]
            for i,p in enumerate(piv):rows[i][p]=1
            for (i,j),v in zip(pos,values):rows[i][j]=v
            yield tuple(map(tuple,rows))

def span_projective(field,basis,k):
    d=len(basis)
    seen=set()
    for coeff in product(range(field.q),repeat=d):
        if not any(coeff):continue
        v=[0]*k
        for c,row in zip(coeff,basis):
            for j,z in enumerate(row):v[j]=field.plus(v[j],field.mul(c,z))
        seen.add(field.norm(v))
    return seen

def check(q,m,A,B,check_all_weights=True):
    field=F(q); k=2*m; a=len(A);b=len(B);c=len(set(A)&set(B));t=b+c
    V=list(product(range(q),repeat=m))
    dA={v for v in V if all(v[j]==0 for j in range(m) if j not in A)}
    dB={v for v in V if all(v[j]==0 for j in range(m) if j not in B)}
    raw=Counter()
    for d in V:
        for x in V:
            if d in dA and x in dB:continue
            raw[field.norm(x+d)]+=1
            raw[field.norm(field.vecsum(x,d)+d)]+=1
    n=2*(q**(2*m)-q**(a+b))
    assert sum(raw.values())==n
    H=(q**(2*m)-2*q**(a+b)+q**t)//(q-1)
    L=2*(q**(a+b)-q**t)//(q-1)
    counts=Counter(raw.values())
    expected=Counter()
    if H:expected[2*(q-1)]+=H
    if L:expected[q-1]+=L
    assert counts==expected,(q,m,A,B,counts,expected)
    N=(q**(2*m)-q**t)//(q-1)
    assert len(raw)==N
    # Explicit identify the missing projective flat.
    I=set(A)&set(B)
    for v in product(range(q),repeat=k):
        if not any(v):continue
        x,d=v[:m],v[m:]
        is_missing=(all(d[j]==0 for j in range(m) if j not in I)
            and all(x[j]==0 for j in range(m) if j not in B))
        assert (field.norm(v) not in raw)==is_missing
    dual_two=(q-1)*sum(comb(v,2) for v in raw.values())
    assert dual_two==(q-1)*(H*comb(2*(q-1),2)+L*comb(q-1,2))
    if check_all_weights:
        projective=set(raw)
        max_inside=[]
        for r in range(1,k+1):
            largest=-1
            for base in spaces(field,k,k-r):
                inside=len(span_projective(field,base,k)&projective)
                largest=max(largest,inside)
            ideal=(q**(k-r)-q**max(0,t-r))//(q-1)
            assert largest==ideal,(q,m,A,B,r,largest,ideal)
            max_inside.append(N-largest)
        print(f'q={q} m={m} A={A} B={B}: n={n}; projective_core={N}; heavy={H} light={L}; A2_dual={dual_two}; GHW={max_inside}; PASS')
    else:
        print(f'q={q} m={m} A={A} B={B}: n={n}; projective_core={N}; heavy={H} light={L}; A2_dual={dual_two}; PASS')

for p in [(2,2,(0,),(1,)),(2,2,(0,),(0,)),(2,3,(0,1),(1,2)),(2,3,(0,1),(0,1)),(3,2,(0,),(1,)),(3,2,(0,),(0,)),(4,2,(0,),(1,))]:
    check(*p)
print('VERIFY_OK')
