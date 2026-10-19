#!/usr/bin/env python3
"""Exact finite graph checks for sparse primitive shifts: finite consistency tests.
The general result is proved by directed-path decomposition and Möbius inversion,
not by the finite enumeration in this script.
"""
from itertools import combinations, permutations
from math import gcd

CHECKS=0

def assert_eq(a,b):
    global CHECKS
    assert a==b,(a,b)
    CHECKS+=1

def strongly_connected(out,n):
    for src in range(n):
        seen={src}; todo=[src]
        for v in todo:
            for w in out[v]:
                if w not in seen:
                    seen.add(w);todo.append(w)
        if len(seen)!=n:return False
    return True

def determinant_poly(edges,n):
    # det(I-zA) by Leibniz expansion, all integer coefficients.
    rows = [[0]*n for _ in range(n)]
    for i,j in edges:rows[i][j]=1
    poly=[0]*(n+1)
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        sign=(-1)**inversions
        terms=[1]
        for i,j in enumerate(perm):
            # diagonal contributes 1-z*A_ii, offdiagonal -z*A_ij.
            factor=[int(i==j),-rows[i][j]]
            conv=[0]*(len(terms)+1)
            for k,c in enumerate(terms):
                conv[k]+=c*factor[0]
                conv[k+1]+=c*factor[1]
            terms=conv
        for k,c in enumerate(terms):poly[k]+=sign*c
    return tuple(poly)

def totient(n):
    return sum(gcd(j,n)==1 for j in range(1,n+1))

def expected_polys(n):
    s=set()
    for a in range(1,n+1):
        for b in range(a,n+1):
            if a+b>=n+1 and (a<b or a<n) and gcd(a,b)==1:
                p=[0]*(n+1)
                p[0]=1;p[a]-=1;p[b]-=1
                s.add(tuple(p))
    return s

def primitive_from_poly(poly,n):
    if poly[0]!=1 or sum(-c for c in poly[1:])!=2: return False
    lengths=[i for i,c in enumerate(poly) if c<0]
    return gcd(*lengths)==1

for n in range(2,5):
    got=set()
    for subset in combinations([(i,j) for i in range(n) for j in range(n)],n+1):
        out=[[] for _ in range(n)]
        for i,j in subset:out[i].append(j)
        if not strongly_connected(out,n):continue
        p=determinant_poly(subset,n)
        assert_eq(p[0],1)
        assert_eq(sum(-t for t in p[1:] if t<0),2)
        # The cycles have lengths gcd=period, so this checks primitivity.
        if primitive_from_poly(p,n): got.add(p)
        # The Bowen-Franks determinant in the strongly-connected bicyclic class.
        assert_eq(sum(p),-1)
    assert_eq(got,expected_polys(n))
    print(f'n={n}, distinct primitive zeta denominators: {len(got)}')

def witness(n,a,b):
    assert 1<=a<=b<=n and a+b>=n+1 and (a<b or a<n)
    c=a+b-(n+1)
    edges=[];next_vertex=1
    if c==0:
        for length in (a,b):
            prior=0
            for _ in range(length-1):
                edges.append((prior,next_vertex))
                prior=next_vertex;next_vertex+=1
            edges.append((prior,0))
    else:
        # Shared return path q -> ... -> p, with p=0 and q=c.
        q=c
        for v in range(1,c+1): edges.append((v,v-1))
        next_vertex=c+1
        for length in (a-c,b-c):
            prior=0
            for _ in range(length-1):
                edges.append((prior,next_vertex))
                prior=next_vertex;next_vertex+=1
            edges.append((prior,q))
    assert_eq(next_vertex,n)
    assert_eq(len(edges),n+1)
    assert_eq(len(set(edges)),len(edges))
    out=[[] for _ in range(n)]
    for i,j in edges:out[i].append(j)
    assert_eq(strongly_connected(out,n),True)
    return edges

for n in range(2,8):
    for a in range(1,n+1):
        for b in range(a,n+1):
            if a+b>=n+1 and (a<b or a<n) and gcd(a,b)==1:
                E=witness(n,a,b)
                p=determinant_poly(E,n)
                target=[0]*(n+1);target[0]=1;target[a]-=1;target[b]-=1
                assert_eq(p,tuple(target))
                assert_eq(sum(p),-1)

for n in range(2,151):
    spectrum={(a,b) for a in range(1,n+1) for b in range(a,n+1)
              if a+b>=n+1 and (a<b or a<n)}
    by_period={d:sum(1 for a,b in spectrum if gcd(a,b)==d)
               for d in range(1,n+1)}
    for d in range(1,n+1):
        m=n//d
        coprime_count=(sum(totient(k) for k in range(1,m+1))//2) if m>=2 else 0
        expected=coprime_count+int(d<n<2*d)
        assert_eq(by_period[d],expected)
    assert_eq(by_period[1]*2,sum(totient(k) for k in range(1,n+1)))
print(f'PASS {CHECKS} exact finite assertions')
