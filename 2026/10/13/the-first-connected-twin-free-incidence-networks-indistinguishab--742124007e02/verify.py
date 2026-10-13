#!/usr/bin/env python3
"""Exact incidence-richness-law finite classification; no external files."""
from itertools import combinations, permutations

def connected(rows,n):
    r=len(rows); seen_r={0}; seen_c=set()
    while True:
        c=seen_c | {j for i in seen_r for j in range(n) if (rows[i]>>j)&1}
        s=seen_r | {i for i in range(r) if any((rows[i]>>j)&1 for j in c)}
        if s==seen_r and c==seen_c: break
        seen_r,seen_c=s,c
    return len(seen_r)==r and len(seen_c)==n

def eligible(rows,n):
    if len(set(rows))!=len(rows) or not all(rows):return False
    cols=[sum(((m>>j)&1)<<i for i,m in enumerate(rows)) for j in range(n)]
    return len(set(cols))==n and all(cols) and connected(rows,n)

def law(rows,n):
    cnt=[[0]*(len(rows)+1) for _ in range(n+1)]
    for subset in range(1<<n):
        cnt[subset.bit_count()][sum(bool(row&subset) for row in rows)]+=1
    return tuple(map(tuple,cnt))

def same_guild_iso(a,b,n):
    for p in permutations(range(n)):
        mapped=sorted(sum(((m>>j)&1)<<p[j] for j in range(n)) for m in a)
        if mapped==sorted(b): return True
    return False

def classify(n,r):
    types=range(1,1<<n)
    buckets={};valid=0;orbits=0
    for rows in combinations(types,r):
        if not eligible(rows,n):continue
        valid+=1; key=law(rows,n); lst=buckets.setdefault(key,[])
        if any(same_guild_iso(rows,old,n) for old in lst):continue
        if lst:raise AssertionError(('unanticipated collision',n,r,rows,lst[0]))
        lst.append(rows);orbits+=1
    return valid,orbits

counts=[]
# No twins means r <= 2^n-1 and n <= 2^r-1; every permissible small-guild dimension is tested.
for n in range(1,4):
    for r in range(1,(1<<n)):
        counts.append((n,r,*classify(n,r)))
for r in range(1,4):
    for n in range(4,(1<<r)):
        counts.append((n,r,*classify(n,r)))

A=(1,3,6,14); B=(1,3,6,13)
assert eligible(A,4) and eligible(B,4)
assert not same_guild_iso(A,B,4)
assert law(A,4)==law(B,4)
assert sorted(m.bit_count() for m in A)==sorted(m.bit_count() for m in B)==[1,2,2,3]
assert sorted(sum((m>>j)&1 for m in A) for j in range(4))==sorted(sum((m>>j)&1 for m in B) for j in range(4))==[1,2,2,3]
# Their incidence graphs have different shortest cycle length: A has a 4-cycle and B does not.
def four_cycle(rows):
    return any(((rows[i]&rows[j]).bit_count()>=2) for i in range(len(rows)) for j in range(i+1,len(rows)))
assert four_cycle(A) and not four_cycle(B)
print('VERIFY_OK small_dimension_cases=',counts)
print('WITNESS_LAW=',law(A,4))
