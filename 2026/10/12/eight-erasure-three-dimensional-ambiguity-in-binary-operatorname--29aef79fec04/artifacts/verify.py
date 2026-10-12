#!/usr/bin/env python3
"""Independent finite checks for third-order erasure ambiguity of SPC product codes.
No external packages or file dependencies. General theorem is proved separately."""
from collections import Counter
from itertools import combinations
from math import comb


def count_formula(m,n):
    def B(a,b): return comb(m,a)*comb(n,b) if m>=a and n>=b else 0
    return B(2,4)+B(4,2)+9*B(3,3)


def cycle_nullity(edges,m,n):
    adj=[set() for _ in range(m+n)]
    for pos in edges:
        i,j=divmod(pos,n)
        adj[i].add(m+j);adj[m+j].add(i)
    active={v for v in range(m+n) if adj[v]}
    vertices=len(active);components=0
    while active:
        components+=1
        queue=[active.pop()]
        while queue:
            for w in adj[queue.pop()]:
                if w in active:
                    active.remove(w);queue.append(w)
    return len(edges)-vertices+components


def expected_kind(edges,m,n):
    rr={e//n for e in edges};cc={e%n for e in edges}
    if (len(rr),len(cc))==(2,4):return '2x4 rectangle'
    if (len(rr),len(cc))==(4,2):return '4x2 rectangle'
    if (len(rr),len(cc))==(3,3) and len(edges)==8:return '3x3 minus edge'
    return 'unclassified'


def product_basis(m,n):
    return [sum(1<<(r*n+c) for r,c in [(i,j),(i,n-1),(m-1,j),(m-1,n-1)])
            for i in range(m-1) for j in range(n-1)]


def all_rref_three(k):
    for piv in combinations(range(k),3):
        sites=[(i,j) for i in range(3) for j in range(piv[i]+1,k) if j not in piv]
        for x in range(1<<len(sites)):
            row=[1<<p for p in piv]
            for shift,(i,j) in enumerate(sites):
                if x & (1<<shift):row[i]^=1<<j
            yield tuple(row)


def check(m,n):
    k=(m-1)*(n-1)
    expected=count_formula(m,n)
    if k<3:return
    observed=Counter()
    for subset in combinations(range(m*n),8):
        nul=cycle_nullity(subset,m,n)
        if nul>=3:
            assert nul==3,(m,n,subset,nul)
            observed[expected_kind(subset,m,n)]+=1
    assert 'unclassified' not in observed
    assert sum(observed.values())==expected,(m,n,observed,expected)
    for subset in combinations(range(m*n),7):
        assert cycle_nullity(subset,m,n)<3,(m,n,subset)
    base=product_basis(m,n)
    lookup=[0]*(1<<k)
    for v in range(1,1<<k):
        t=v&-v
        lookup[v]=lookup[v^t]^base[t.bit_length()-1]
    rref_count=0
    min_count=0
    seen=set()
    for rows in all_rref_three(k):
        mask=lookup[rows[0]]|lookup[rows[1]]|lookup[rows[2]]
        rref_count+=1
        if mask.bit_count()==8:
            min_count+=1
            assert mask not in seen
            seen.add(mask)
            assert cycle_nullity([i for i in range(m*n) if mask>>i&1],m,n)==3
    assert min_count==expected and len(seen)==expected,(m,n,min_count,expected)
    print(f'CASE m={m} n={n} dim={k} 8-erasure 3-ambiguity={expected} types={dict(observed)} 3-subspaces={rref_count} minimizers={min_count}')

if __name__=='__main__':
    for m,n in [(2,4),(2,6),(3,3),(3,4),(4,4)]:check(m,n)
    print('VERIFY_OK')
