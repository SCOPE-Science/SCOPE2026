#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from collections import defaultdict

def recursive_partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for x in range(cap, 0, -1):
        for rest in recursive_partitions(n-x, x):
            yield (x,) + rest

def independent_partitions(n):
    out=set()
    for k in range(1,n+1):
        for a in combinations_with_replacement(range(1,n+1),k):
            if sum(a)==n:
                out.add(tuple(sorted(a, reverse=True)))
    return out

def lt(profile):
    N=sum(profile)
    return Fraction(N*N, sum(x*x for x in profile))

def golosov(profile):
    N=sum(profile)
    leader=profile[0]
    return sum((Fraction(x*N, x*N + leader*leader - x*x) for x in profile), Fraction(0,1))

def sign(z):
    return (z>0)-(z<0)

expected_profiles={2:1,3:2,4:4,5:6,6:10,7:14,8:21,9:29,10:41}
expected_pairs={2:0,3:0,4:0,5:0,6:0,7:1,8:2,9:5,10:11}
weak_counts={}
strict_counts={}
strict_layer={}

for N in range(2,11):
    p1={p for p in recursive_partitions(N) if len(p)>=2}
    p2={p for p in independent_partitions(N) if len(p)>=2}
    assert p1==p2
    assert len(p1)==expected_profiles[N]
    groups=defaultdict(list)
    for p in sorted(p1, reverse=True):
        groups[(len(p),p[0])].append(p)
    pair_count=sum(len(v)*(len(v)-1)//2 for v in groups.values())
    assert pair_count==expected_pairs[N]
    weak=[]; strict=[]
    for key,arr in groups.items():
        for a,b in combinations(arr,2):
            dl=sign(lt(a)-lt(b)); dg=sign(golosov(a)-golosov(b))
            if dl != dg:
                weak.append((key,a,b))
            if dl*dg < 0:
                strict.append((key,a,b))
    weak_counts[N]=len(weak)
    strict_counts[N]=len(strict)
    strict_layer[N]=strict

for N in range(2,10):
    assert weak_counts[N]==0
    assert strict_counts[N]==0
assert weak_counts[10]==1
assert strict_counts[10]==1
assert strict_layer[10]==[((3,4),(4,4,2),(4,3,3))]

A=(4,4,2); B=(4,3,3)
assert lt(A)==Fraction(25,9)
assert lt(B)==Fraction(50,17)
assert golosov(A)==Fraction(21,8)
assert golosov(B)==Fraction(97,37)
assert lt(A) < lt(B)
assert golosov(A) > golosov(B)
assert golosov(A)-golosov(B)==Fraction(1,296)

# Common scaling preserves both share-based indices.
for q in range(1,9):
    Aq=tuple(q*x for x in A); Bq=tuple(q*x for x in B)
    assert lt(Aq)==lt(A) and lt(Bq)==lt(B)
    assert golosov(Aq)==golosov(A) and golosov(Bq)==golosov(B)

print('VERIFY_OK')
print('profile_counts', expected_profiles)
print('comparable_pair_counts', expected_pairs)
print('first_strict_total', 10)
print('unique_first_pair', A, B)
print('LT_values', lt(A), lt(B))
print('Golosov_values', golosov(A), golosov(B))
print('Golosov_gap', golosov(A)-golosov(B))
