#!/usr/bin/env python3
"""Independent finite-field and rank checks for the elementary-symmetric cubic.
Pure Python, no nonstandard dependencies. These tests supplement a general proof.
"""
from itertools import product, combinations
from math import comb

def mul(a,b):
    x=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:
                x ^= 1 << (i+j)
    if x & 8: x ^= 0b1001  # t^3 = 1 mod (t^2+t+1)
    if x & 4: x ^= 0b111  # t^2=t+1
    return x

def rank2(matrix):
    b=[sum((a&1)<<j for j,a in enumerate(row)) for row in matrix]
    rank=0
    for j in range(len(matrix[0])):
        i=next((i for i in range(rank,len(b)) if (b[i]>>j)&1),None)
        if i is None:continue
        b[rank],b[i]=b[i],b[rank]
        for k in range(len(b)):
            if k!=rank and (b[k]>>j)&1:b[k]^=b[rank]
        rank+=1
    return rank

INV={a:next(b for b in (1,2,3) if mul(a,b)==1) for a in (1,2,3)}
assert INV=={1:1,2:3,3:2}

def normalize(x):
    v=next(v for v in x if v)
    return tuple(mul(a,INV[v]) for a in x)

def critical(x):
    s1=0;s2=0
    for a in x:
        s2^=mul(s1,a);s1^=a
    return all((mul(a,a)^mul(s1,a)^s2)==0 for a in x)

def points(n):
    for pivot in range(n):
        for tail in product(range(4),repeat=n-pivot-1):
            yield (0,)*pivot+(1,)+tail

def indicator(n,S):
    return tuple(int(i in S) for i in range(n))

def predicted(n):
    if n%4!=2:
        return {indicator(n,S) for r in range(1,n+1,4) for S in combinations(range(n),r)}
    val=set()
    for r in range(1,n,4):
        for S in combinations(range(n),r):
            mask=set(S)
            for u in range(4):
                for v in range(4):
                    vec=tuple(u if i in mask else v for i in range(n))
                    if any(vec): val.add(normalize(vec))
    return val

for n in (5,6,7,8,9):
    actual={x for x in points(n) if critical(x)}
    exp=predicted(n)
    assert actual==exp,(n,len(actual),len(exp),list(actual-exp)[:2],list(exp-actual)[:2])
    if n%4!=2:
        expect=sum(comb(n,j) for j in range(1,n+1,4))
        assert len(exp)==expect
        if n%4==0: assert expect==2**(n-2)
        ranktarget=n-1 if n%2 else n-2
        for x in exp:
            total=0
            for a in x:total^=a
            matrix=[[(total^x[i]^x[j]) if i!=j else 0 for j in range(n)] for i in range(n)]
            assert rank2(matrix)==ranktarget,(n,x,rank2(matrix))
            # Smoothness of projectivized quadratic tangent cone is a separate
            # condition from Hessian invertibility in characteristic two.
            pivot=x.index(1)
            active=[j for j in range(n) if j!=pivot and x[j]==1]
            outside=[j for j in range(n) if x[j]==0]
            def q(v):
                def e2(block):
                    return sum(v[i]*v[j] for i,j in combinations(block,2))&1
                return e2(active)^e2(outside)
            def polar_gradient(v):
                return [sum(v[j] for j in block if j!=i)&1
                        for block in (active,outside) for i in block]
            assert all(q({j:(mask>>(j-(j>pivot)))&1 for j in range(n) if j!=pivot}) or
                       any(polar_gradient({j:(mask>>(j-(j>pivot)))&1 for j in range(n) if j!=pivot}))
                       for mask in range(1,1<<(n-1))),('singular quadratic cone',n,x)
    print('F4-projective-critical',n,'actual',len(actual),'predicted',len(exp),'Hessian ranks checked', n%4!=2)
for n in (8,12,16,20):
    k=sum(comb(n,j) for j in range(1,n+1,4))
    assert k==2**(n-2)
    print('complete-intersection degree check',n,'support',k,'double-length',2*k,'Bezout',2**(n-1))
print('VERIFY_OK')
