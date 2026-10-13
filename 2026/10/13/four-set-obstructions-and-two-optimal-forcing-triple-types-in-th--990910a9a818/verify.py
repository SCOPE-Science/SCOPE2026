#!/usr/bin/env python3
"""Exact independent checks of matching-forcing structures on the Heawood graph.
Python 3 standard library only. Run: python3 verify.py
"""
from itertools import combinations, permutations, product
from collections import Counter

N=7
D={0,2,3}
identity=tuple(range(N))
cyclic_matchings={p for p in permutations(range(N)) if all((p[i]-i)%N in D for i in range(N))}
assert len(cyclic_matchings)==24
# Ryser inclusion-exclusion, evaluated independently of permutation enumeration.
perm=0
for S in range(1<<N):
    prod=1
    for i in range(N):
        prod*=sum(((j-i)%N in D) for j in range(N) if S>>j&1)
    perm+=(-1)**(N-S.bit_count())*prod
assert perm==24

# Independent Fano-plane model with seven nonzero vectors of F_2^3.
points=[1,2,7,3,5,4,6]
lines=[2,1,6,4,5,3,7]
incidence=lambda p,l: (p&l).bit_count()%2 == 0
assert all(incidence(points[i],lines[j]) == ((j-i)%N in D)
           for i in range(N) for j in range(N))
geo_matchings=[]
def geo_dfs(i,used,matching):
    if i==N:
        geo_matchings.append(tuple(matching));return
    for j in range(N):
        if not (used>>j)&1 and incidence(points[i],lines[j]):
            geo_dfs(i+1,used|(1<<j),matching+[j])
geo_dfs(0,0,[])
assert set(geo_matchings)==cyclic_matchings

# Forcing decisions by direct unique perfect-matching extension,
# not by using the seven-four-set structural description.
def extension_count(p,S):
    return sum(all(q[i]==p[i] for i in S) for q in cyclic_matchings)

def force_profile(p):
    return Counter(k for k in range(N+1) for S in combinations(range(N),k)
                   if extension_count(p,S)==1)
assert all(force_profile(p)=={3:14,4:28,5:21,6:7,7:1}
           for p in cyclic_matchings)
assert Counter(sum(q[i]==i for i in range(N)) for q in cyclic_matchings)=={7:1,4:7,2:7,1:7,0:2}

blocks={frozenset((t+j)%N for j in (0,1,3,5)) for t in range(N)}
assert {frozenset(i for i in range(N) if p[i]==i)
        for p in cyclic_matchings if sum(p[i]==i for i in range(N))==4}==blocks
assert all(any({i for i in range(N) if p[i]==i}<=b for b in blocks)
           for p in cyclic_matchings if p!=identity)
for k in range(N+1):
    for S in combinations(range(N),k):
        assert (extension_count(identity,S)==1)==(all(not set(S)<=b for b in blocks))

minsets={frozenset(S) for S in combinations(range(N),3)
         if extension_count(identity,S)==1}
A={frozenset((t+j)%N for j in (0,1,4)) for t in range(N)}
B={frozenset((t+j)%N for j in (0,1,6)) for t in range(N)}
assert len(A)==len(B)==7 and A.isdisjoint(B) and minsets==A|B
assert {frozenset((t-j)%N for j in S) for t in range(N) for S in A}==A
assert {frozenset((t-j)%N for j in S) for t in range(N) for S in B}==B

# Compute all 168 invertible binary linear maps, with dual maps on lines.
matrices=[]
for cols in product(range(1,8),repeat=3):
    def lin(v):
        return (cols[0] if v&1 else 0) ^ (cols[1] if v&2 else 0) ^ (cols[2] if v&4 else 0)
    mapped={v:lin(v) for v in range(1,8)}
    if len(set(mapped.values()))<7:continue
    dual={l: next(n for n in range(1,8) if
                   {mapped[p] for p in range(1,8) if incidence(p,l)} ==
                   {p for p in range(1,8) if incidence(p,n)})
          for l in range(1,8)}
    pi=tuple(points.index(mapped[p]) for p in points)
    lam=tuple(lines.index(dual[l]) for l in lines)
    assert all(((j-i)%N in D)==((lam[j]-pi[i])%N in D)
               for i in range(N) for j in range(N))
    matrices.append((pi,lam))
assert len(matrices)==168

# Bipartition-swap polarity p_i <-> l_{-i} doubles the group.
# An unordered graph automorphism either preserves or swaps its two sides,
# and there are precisely 168 point-line preserving ones.
autos=[]
for pi,lam in matrices:
    autos.append((pi,lam,False))
    autos.append((pi,lam,True))
assert len(autos)==336

def image_edge(e,aut):
    i,j=e
    pi,lam,swapped=aut
    return (pi[i],lam[j]) if not swapped else ((-lam[j])%N,(-pi[i])%N)

def image_matching(m,aut):
    return frozenset(image_edge((i,m[i]),aut) for i in range(N))

M0=frozenset((i,i) for i in range(N))
orbit_M={image_matching(identity,a) for a in autos}
assert len(orbit_M)==24
stabilizer=[a for a in autos if image_matching(identity,a)==M0]
assert len(stabilizer)==14
assert set(len({frozenset(image_edge((i,i),a) for i in S) for a in stabilizer})
               for S in [next(iter(A)),next(iter(B))])=={7}
assert {frozenset(image_edge((i,i),a) for i in next(iter(A))) for a in stabilizer}=={
    frozenset((i,i) for i in S) for S in A}
assert {frozenset(image_edge((i,i),a) for i in next(iter(B))) for a in stabilizer}=={
    frozenset((i,i) for i in S) for S in B}

# Every optimal determining triple belongs to exactly one perfect matching;
# the full automorphism orbits are disjoint and each of size 168.
all_forcing_triples={frozenset((i,p[i]) for i in S)
                     for p in cyclic_matchings
                     for S in combinations(range(N),3)
                     if extension_count(p,S)==1}
assert len(all_forcing_triples)==24*14==336
fullA={frozenset(image_edge((i,i),a) for i in next(iter(A))) for a in autos}
fullB={frozenset(image_edge((i,i),a) for i in next(iter(B))) for a in autos}
assert len(fullA)==len(fullB)==168 and fullA.isdisjoint(fullB)
assert fullA|fullB==all_forcing_triples

print('VERIFY_OK fano_incidence=7points_7lines heawood_edges=21')
print('VERIFY_OK matchings_permutation=24 ryser_permanent=24 geometric_matchings=24')
print('VERIFY_OK overlap_histogram=0:2,1:7,2:7,4:7,7:1')
print('VERIFY_OK seven_maximal_nonforcing_4sets=rotations_of_{0,1,3,5}')
print('VERIFY_OK all_128_subsets_per_matching=24_matching_checks')
print('VERIFY_OK per_matching_forcing_polynomial=14z3+28z4+21z5+7z6+z7')
print('VERIFY_OK minimum_local_forcing_sets=14 cyclic_types=7+7')
print('VERIFY_OK automorphisms=336 matching_orbit=24 stabilizer=14')
print('VERIFY_OK across_matchings_minimum_triplets=336 orbit_sizes=168+168')
