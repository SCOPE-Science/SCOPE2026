#!/usr/bin/env python3
from itertools import product, combinations

def bits(x,n): return tuple((x>>i)&1 for i in range(n))
def wt(x): return x.bit_count()
def xor_sum(vals):
    z=0
    for v in vals: z ^= v
    return z

def gf2_rank(cols,n):
    a=list(cols); r=0
    for bit in range(n):
        p=next((k for k in range(r,len(a)) if (a[k]>>bit)&1),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for k in range(len(a)):
            if k!=r and ((a[k]>>bit)&1): a[k]^=a[r]
        r+=1
    return r

def coords_from_basis(x,basis,n):
    # brute-force enough for n<=8 verification
    for mask in range(1<<n):
        if xor_sum(basis[i] for i in range(n) if (mask>>i)&1)==x:
            return mask
    raise ValueError('not a basis')

def canonical_generators(n):
    # target Cayley generating set after basis change
    if n%2==0:
        return set([1<<i for i in range(n)] + [(1<<n)-1]), 'FQ_%d'%(n+1)
    else:
        # coordinate 0 is K2; coordinates 1..n-1 form FQ_n
        return set([1] + [1<<i for i in range(1,n)] + [sum(1<<i for i in range(1,n))]), 'K2xFQ_%d'%n

def verify(n):
    j=(1<<n)-1
    S=set([j]+[j^(1<<i) for i in range(n)])
    assert all(wt(s) in (n-1,n) for s in S)
    if n%2==0:
        basis=[j^(1<<i) for i in range(n)]
    else:
        basis=[j]+[j^(1<<i) for i in range(n-1)]
    assert gf2_rank(basis,n)==n
    mapped={coords_from_basis(s,basis,n) for s in S}
    target,name=canonical_generators(n)
    assert mapped==target, (n,mapped,target)
    # exhaustive adjacency check under coordinate map
    image=[coords_from_basis(x,basis,n) for x in range(1<<n)]
    assert len(set(image))==(1<<n)
    for x in range(1<<n):
        for y in range(x+1,1<<n):
            far=(wt(x^y)>=n-1)
            target_edge=((image[x]^image[y]) in target)
            assert far==target_edge
    return name, basis, sorted(mapped)

for n in range(3,9):
    name,basis,mapped=verify(n)
    print(f'n={n}: far graph is {name}; basis={basis}; mapped_generators={mapped}')
print('VERIFY_OK')
