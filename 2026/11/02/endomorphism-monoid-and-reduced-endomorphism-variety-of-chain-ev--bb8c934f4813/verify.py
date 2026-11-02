#!/usr/bin/env python3
"""Direct exhaustive checks for homomorphisms of chain evolution algebras."""
from itertools import product
from collections import Counter

def mul(a,b,q):
    if q != 4: return (a*b)%q
    z=0
    while b:
        if b&1: z ^= a
        a <<= 1
        if a&4: a ^= 7
        b >>= 1
    return z

def add(a,b,q):
    return ((a+b)%q) if q!=4 else (a^b)

def sq_vector(v,q):
    n=len(v)
    return (0,)+tuple(mul(x,x,q) for x in v[:-1])

def product_vec(v,w,q):
    n=len(v)
    return (0,)+tuple(mul(x,y,q) for x,y in zip(v[:-1],w[:-1]))

def hom(cols,q):
    n=len(cols)
    for i in range(n-1):
        if cols[i+1]!=sq_vector(cols[i],q):return False
    if any(sq_vector(cols[-1],q)):return False
    for i in range(n):
        for j in range(i+1,n):
            if any(product_vec(cols[i],cols[j],q)):return False
    return True

def rank(cols,q):
    v=[list(row) for row in zip(*cols)]
    n=len(cols); d=0
    for c in range(n):
        piv=next((i for i in range(d,n) if v[i][c]),None)
        if piv is None: continue
        v[d],v[piv]=v[piv],v[d]
        # work over GF4 using exhaustive scalar elimination
        inv=next(x for x in range(1,q) if mul(v[d][c],x,q)==1)
        v[d]=[mul(x,inv,q) for x in v[d]]
        for i in range(n):
            if i!=d and v[i][c]:
                t=v[i][c]
                v[i]=[add(x,mul(t,y,q) if q==4 else -mul(t,y,q),q) for x,y in zip(v[i],v[d])]
        d+=1
    return d

def classify_first(v):
    return sum(x!=0 for x in v[:-1])<=1

def columns_for(first,q):
    n=len(first); cols=[first]
    for _ in range(1,n): cols.append(sq_vector(cols[-1],q))
    return cols

def compose(f,g,q):
    n=len(f); h=[]
    for col in g:
        out=[0]*n
        for i,coeff in enumerate(col):
            for j in range(n): out[j]=add(out[j],mul(coeff,f[i][j],q),q)
        h.append(tuple(out))
    return h

def check_composition_index(first,q):
    n=len(first); f=columns_for(first,q)
    if first[0]:
        assert rank(f,q)==n
        return
    s=next((i+1 for i,a in enumerate(first[:-1]) if a),None)
    expected=(n-1)//(s-1)+1 if s is not None else (2 if first[-1] else 1)
    z=[(0,)*n for _ in range(n)]
    p=f
    for t in range(1,expected):
        assert p!=z,(n,q,first,t,expected)
        p=compose(f,p,q)
    assert p==z,(n,q,first,expected)

def test(n,q,full):
    expected={0:1,1:q-1}
    for r in range(2,n+1): expected[r]=q*(q-1)
    if full:
        cells=product(range(q), repeat=n*n)
        actual=Counter(); count=0
        for cell in cells:
            cols=[cell[n*i:n*(i+1)] for i in range(n)]
            if hom(cols,q):
                actual[rank(cols,q)]+=1
                check_composition_index(cols[0],q)
                assert classify_first(cols[0])
                count+=1
    else:
        actual=Counter(); count=0
        for first in product(range(q),repeat=n):
            cols=[first]
            for _ in range(1,n): cols.append(sq_vector(cols[-1],q))
            if hom(cols,q):
                actual[rank(cols,q)]+=1
                check_composition_index(first,q)
                assert classify_first(first)
                count+=1
    assert all(actual[r]==expected[r] for r in range(n+1)),(n,q,actual,expected)
    assert count==(n-1)*q*q-(n-2)*q
    print(f'n={n} q={q} exhaustive_{"all_linear_maps" if full else "generator_images"} count={count} ranks={dict(sorted(actual.items()))}')

for n,q,full in [(2,2,True),(2,3,True),(2,4,True),(3,2,True),(3,3,True),(3,4,True),(4,2,True),(4,3,False),(5,2,False),(5,4,False),(7,2,False)]:
    test(n,q,full)
print('EVOLUTION_CHAIN_ENDOMORPHISM_OK')
