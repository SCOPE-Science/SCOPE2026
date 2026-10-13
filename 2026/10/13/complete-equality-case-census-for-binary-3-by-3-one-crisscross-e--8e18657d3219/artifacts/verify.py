#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter

def cw(x):
    if x==0:return 0
    for p in permutations(range(3)):
        if all((x>>(3*r+p[r]))&1 for r in range(3)): return 3
    for rs in combinations(range(3),2):
        for cs in combinations(range(3),2):
            if (((x>>(3*rs[0]+cs[0]))&1) and ((x>>(3*rs[1]+cs[1]))&1)) or (((x>>(3*rs[0]+cs[1]))&1) and ((x>>(3*rs[1]+cs[0]))&1)): return 2
    return 1
W=[cw(x) for x in range(512)]
assert Counter(W)=={0:1,1:33,2:231,3:247}
V=[x for x in range(1,512) if W[x]==3]
adj=[]
for i,a in enumerate(V):
    m=0
    for j,b in enumerate(V):
        if i!=j and W[a^b]==3:m|=1<<j
    adj.append(m)
# enumerate all 7-cliques among V; adjoining 0 gives all normalized size-8 codes
codes=[]
def rec(pref,P,left):
    if left==0:
        codes.append(frozenset([0]+[V[i] for i in pref]));return
    if P.bit_count()<left:return
    while P:
        bit=P & -P; i=bit.bit_length()-1; P^=bit
        rec(pref+[i],P & adj[i],left-1)
rec([], (1<<len(V))-1, 7)
assert len(codes)==7622 and len(set(codes))==7622
# projection bound: d_C>=3 implies each fixed row projection injective, hence |C|<=8.
# Validate equality rigidity for every enumerated maximum.
for C in codes:
    for r in range(3):
        vals={ (x>>(3*r))&7 for x in C }
        assert len(vals)==8
    for c in range(3):
        vals={sum(((x>>(3*r+c))&1)<<r for r in range(3)) for x in C}
        assert len(vals)==8

def linear(C):return all((a^b) in C for a in C for b in C)
aff=sum(linear(C) for C in codes)
assert aff==1718
# Count labeled maxima by pointed-translation incidence: N*8 = 7622*512.
total=7622*512//8; aff_total=aff*512//8
assert total==487808 and aff_total==109952 and total-aff_total==377856
# Natural isometries: translations, S3 row perms, S3 column perms, transpose.
def pb(x,m):
    y=0
    for old,new in enumerate(m):
        if (x>>old)&1:y|=1<<new
    return y
def rm(p):return [p[r]*3+c for r in range(3) for c in range(3)]
def cm(p):return [r*3+p[c] for r in range(3) for c in range(3)]
tm=[c*3+r for r in range(3) for c in range(3)]
gens=[rm((1,0,2)),rm((1,2,0)),cm((1,0,2)),cm((1,2,0)),tm]
S=set(codes); unseen=set(S); os=[]
while unseen:
    seed=unseen.pop(); O={seed}; stack=[seed]
    while stack:
        C=stack.pop(); N=[]
        for m in gens:N.append(frozenset(pb(x,m) for x in C))
        N += [frozenset(x^a for x in C) for a in C]
        for D in N:
            assert D in S
            if D not in O:
                O.add(D); unseen.discard(D); stack.append(D)
    os.append(O)
dist=Counter(len(O)*64 for O in os)
expect={128:1,768:2,1152:2,2304:8,3072:1,4608:21,6144:1,9216:9,18432:13,36864:1}
assert len(os)==59 and dict(sorted(dist.items()))==expect
print('VERIFY_OK cover_weight_hist=0:1,1:33,2:231,3:247 normalized_maxima=7622 maximum=8 labeled_maxima=487808 affine_maxima=109952 nonlinear_maxima=377856 natural_group_size=36864 orbits=59 orbit_sizes='+','.join(f'{k}x{v}' for k,v in sorted(dist.items())))
