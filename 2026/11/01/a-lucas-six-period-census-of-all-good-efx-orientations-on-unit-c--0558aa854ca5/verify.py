#!/usr/bin/env python3
"""Exact exhaustive cross-check of EFX orientations for unit-valued cycle goods.
No probabilistic tests; for n=3..14 enumerate every labeled orientation.
"""
from math import comb

def direct_efx(bits):
    n=len(bits)
    bundles=[set() for _ in range(n)]
    for edge,bit in enumerate(bits):
        head=(edge+bit)%n # bit=0 gives vertex edge; bit=1 gives edge+1
        bundles[head].add(edge)
    for v in range(n):
        own=len(bundles[v] & {(v-1)%n,v})
        for w in range(n):
            for e in bundles[w]:
                other=len((bundles[w]-{e}) & {(v-1)%n,v})
                if own<other:return False
    return True

def transitions_ok(bits):
    n=len(bits)
    return all(not ((bits[i]!=bits[(i+1)%n]) and (bits[(i+1)%n]!=bits[(i+2)%n])) for i in range(n))

def independent_cycle(n,k):
    if k==0:return 1
    if k>n//2:return 0
    return n*comb(n-k,k)//(n-k)

def lucas(n):
    a,b=2,1
    for _ in range(n):a,b=b,a+b
    return a
period=(2,1,-1,-2,-1,1)
for n in range(3,15):
    by_transitions={}
    count=0
    for mask in range(1<<n):
        bits=tuple((mask>>j)&1 for j in range(n))
        a=direct_efx(bits)
        b=transitions_ok(bits)
        assert a==b, (n,mask,a,b)
        if a:
            count+=1
            k=sum(bits[j]!=bits[(j+1)%n] for j in range(n))
            by_transitions[k]=by_transitions.get(k,0)+1
    expected=lucas(n)+period[n%6]
    assert count==expected, (n,count,expected)
    assert sum(2*independent_cycle(n,k) for k in range(0,n//2+1,2))==expected
    for k,val in by_transitions.items():assert val==2*independent_cycle(n,k)
    print(f'n={n} total={1<<n} efx={count} by_transitions={by_transitions}')
print('VERIFY_OK n=3..14')
