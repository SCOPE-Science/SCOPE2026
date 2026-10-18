#!/usr/bin/env python3
"""Exact finite certificate for three-atom convolution on the binary octahedral group.

Requires Python >=3.9 and SymPy >=1.10. No floating-point linear algebra.
Each quaternion coordinate is (a+b*sqrt(2))/2, encoded by integer pair (a,b).
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from sympy import Matrix
import numpy as np

Z = (0, 0)

def mult_quaternion(x, y):
    def mul(a,b):
        return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
    def total(pieces):
        a = sum(z[0] for z in pieces)
        b = sum(z[1] for z in pieces)
        assert a % 2 == b % 2 == 0
        return (a//2, b//2)
    def opposite(a):
        return (-a[0],-a[1])
    a,b,c,d=x
    e,f,g,h=y
    return (
      total([mul(a,e),opposite(mul(b,f)),opposite(mul(c,g)),opposite(mul(d,h))]),
      total([mul(a,f),mul(b,e),mul(c,h),opposite(mul(d,g))]),
      total([mul(a,g),opposite(mul(b,h)),mul(c,e),mul(d,f)]),
      total([mul(a,h),mul(b,g),opposite(mul(c,f)),mul(d,e)]),
    )

G=[]
for index in range(4):
    for sign in [-2,2]:
        v=[Z]*4
        v[index]=(sign,0)
        G.append(tuple(v))
for signs in product([-1,1],repeat=4):
    G.append(tuple((s,0) for s in signs))
for i,j in combinations(range(4),2):
    for x,y in product([-1,1],repeat=2):
        v=[Z]*4
        v[i]=(0,x)
        v[j]=(0,y)
        G.append(tuple(v))
assert len(G)==len(set(G))==48
ids={v:i for i,v in enumerate(G)}
e=ids[((2,0),Z,Z,Z)]
mult=[[ids[mult_quaternion(x,y)] for y in G] for x in G]
assert all(mult[e][x]==x==mult[x][e] for x in range(48))
assert all(set(row)==set(range(48)) for row in mult)
inv=[next(y for y in range(48) if mult[x][y]==e) for x in range(48)]
assert all(mult[inv[x]][x]==e for x in range(48))
assert all(mult[mult[a][b]][c]==mult[a][mult[b][c]]
           for a in range(48) for b in range(48) for c in range(48))


def order(a):
    x=e
    for i in range(1,49):
        x=mult[x][a]
        if x==e: return i
    raise AssertionError('order not found')
orders=[order(a) for a in range(48)]


def pair_order_signature(a,b):
    return tuple(sorted((orders[a],orders[b],orders[mult[inv[a]][b]])))


def matrix_rank(a,b):
    # T_{1,a,b} f(x) = f(x)+f(a^{-1}x)+f(b^{-1}x).
    rows=[[0]*48 for _ in range(48)]
    for x in range(48):
        for s in (e,a,b):
            rows[x][mult[inv[s]][x]]+=1
    return Matrix(rows).rank()

# Orbits under left translation and inner conjugation. All have invariant complex nullity.
conj=[[mult[mult[k][x]][inv[k]] for x in range(48)] for k in range(48)]
def transforms(pair):
    s=(e,)+pair
    for a in s:
        yield tuple(sorted(mult[inv[a]][b] for b in s if b!=a))
    for k in range(48):
        yield tuple(sorted((conj[k][pair[0]],conj[k][pair[1]])))

unused=set(combinations((x for x in range(48) if x!=e),2))
orbit_table=[]
while unused:
    seed=min(unused)
    reached={seed}
    queue=[seed]
    for pair in queue:
        for nxt in transforms(pair):
            if nxt not in reached:
                reached.add(nxt)
                queue.append(nxt)
    assert reached<=unused
    unused-=reached
    null=48-matrix_rank(*seed)
    assert all(pair_order_signature(*q)==pair_order_signature(*seed) for q in reached)
    orbit_table.append((seed,len(reached),null,pair_order_signature(*seed)))
assert len(orbit_table)==28
assert sum(x[1] for x in orbit_table)==1081

by_signature=defaultdict(lambda:[0,set()])
by_null=Counter()
for seed,size,null,signature in orbit_table:
    num_supports=16*size # 48 translations, three choices for identity-normalization
    by_signature[signature][0]+=num_supports
    by_signature[signature][1].add(null)
    by_null[null]+=num_supports
assert all(len(v[1])==1 for v in by_signature.values())
assert sum(by_null.values())==17296
assert len(by_signature)==19
EXPECTED_COUNTS={0:7056,2:4608,4:576,5:2304,8:2304,12:192,16:192,32:64}
assert dict(by_null)==EXPECTED_COUNTS

EXPECTED_SIGNATURES={
 (2,3,6):(384,0), (2,4,4):(432,0), (2,8,8):(288,0),
 (3,3,3):(64,32), (3,3,4):(576,0), (3,3,6):(576,4),
 (3,4,4):(1152,8), (3,4,6):(1152,0), (3,4,8):(2304,2),
 (3,6,6):(192,16), (3,8,8):(1152,5), (4,4,4):(768,0),
 (4,4,6):(1152,8), (4,4,8):(2304,0), (4,6,6):(576,0),
 (4,6,8):(2304,2), (4,8,8):(576,0), (6,6,6):(192,12),
 (6,8,8):(1152,5),
}
assert {k:(v[0],next(iter(v[1]))) for k,v in by_signature.items()}==EXPECTED_SIGNATURES

# Independent modular ranks for every normalized triple. Modular rank cannot
# exceed rational rank; equality here supplies an additional cross-check.
def matrix_rank_mod(a,b,prime):
    rows=np.zeros((48,48),dtype=np.int64)
    for x in range(48):
        for s in (e,a,b):
            rows[x,mult[inv[s]][x]]+=1
    rank=0
    for col in range(48):
        piv=next((r for r in range(rank,48) if rows[r,col]%prime),None)
        if piv is None:continue
        if piv != rank: rows[[rank,piv]]=rows[[piv,rank]]
        unit=pow(int(rows[rank,col]),-1,prime)
        rows[rank,col:]=(rows[rank,col:]*unit)%prime
        ii=np.nonzero(rows[rank+1:,col])[0]+rank+1
        if len(ii):
            rows[ii,col:]=(rows[ii,col:]-rows[ii,col,None]*rows[rank,None,col:])%prime
        rank+=1
        if rank==48:break
    return rank

for a,b in combinations((x for x in range(48) if x!=e),2):
    sig=pair_order_signature(a,b)
    assert 48-matrix_rank_mod(a,b,1009)==EXPECTED_SIGNATURES[sig][1]
    assert 48-matrix_rank_mod(a,b,10007)==EXPECTED_SIGNATURES[sig][1]

# Check full-support subdivisions by normal index-two Hurwitz subgroup.
H={i for i,g in enumerate(G) if all(coef[1]==0 for coef in g)}
assert len(H)==24
assert all(mult[x][y] in H for x in H for y in H)
assert all(conj[g][x] in H for g in range(48) for x in H)
order3_subgroups={frozenset((e,g,mult[g][g])) for g in range(48) if orders[g]==3}
assert len(order3_subgroups)==4
order3_cosets={frozenset(mult[x][y] for y in B) for B in order3_subgroups for x in range(48)}
assert len(order3_cosets)==64
assert all(pair_order_signature(*(sorted(B-{e})))==(3,3,3) if e in B else
           tuple(sorted((orders[mult[inv[a]][b]] for a,b in combinations(sorted(B),2))))==(3,3,3)
           for B in order3_cosets)
within=Counter(); across=Counter()
for a,b in combinations((x for x in range(48) if x!=e),2):
    sig=pair_order_signature(a,b)
    (within if a in H and b in H else across)[EXPECTED_SIGNATURES[sig][1]]+=16
assert within=={0:3024,4:576,12:192,16:192,32:64}
assert across=={0:4032,2:4608,5:2304,8:2304}

print('PASS: 48 elements, 28 action orbits, 1081 normalized triples, 17296 unordered supports')
print('PASS: exact rational ranks for 28 orbit representatives; two modular cross-checks for all 1081 normalized triples (19 order signatures)')
print('all nullities',dict(sorted(by_null.items())))
print('mixed cosets',dict(sorted(across.items())))
print('all signatures (signature: count, nullity):')
for k in sorted(EXPECTED_SIGNATURES):print(' ',k,EXPECTED_SIGNATURES[k])
