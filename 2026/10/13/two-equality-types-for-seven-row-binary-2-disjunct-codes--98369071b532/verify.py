#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter
import hashlib

V = list(range(1, 1<<7))

def good3(a,b,c):
    return ((a & ~(b|c)) != 0 and (b & ~(a|c)) != 0 and (c & ~(a|b)) != 0)

def enum_target(k):
    sols=[]
    nodes=0
    def rec(chosen,cands):
        nonlocal nodes
        nodes += 1
        if len(chosen)==k:
            sols.append(tuple(chosen)); return
        need=k-len(chosen)
        if len(cands)<need: return
        for idx,s in enumerate(cands):
            if len(cands)-idx<need: break
            if len(chosen)<2 or all(good3(u,v,s) for u,v in combinations(chosen,2)):
                nc=[]
                for t in cands[idx+1:]:
                    if all(good3(u,s,t) for u in chosen): nc.append(t)
                rec(chosen+[s],nc)
    rec([],V)
    return sols,nodes

sol8,n8=enum_target(8)
assert not sol8
sol7,n7=enum_target(7)
assert len(sol7)==31

def wt(x): return x.bit_count()
single=[s for s in sol7 if all(wt(x)==1 for x in s)]
assert len(single)==1 and set(single[0])=={1,2,4,8,16,32,64}
fano=[s for s in sol7 if s not in single]
assert len(fano)==30
for fam in fano:
    assert all(wt(x)==3 for x in fam)
    pairct=Counter()
    for b in fam:
        pts=[i for i in range(7) if b>>i & 1]
        for p in combinations(pts,2): pairct[p]+=1
    assert len(pairct)==21 and set(pairct.values())=={1}

canon_sets=[(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
canon=tuple(sorted(sum(1<<i for i in B) for B in canon_sets))

def perm_mask(x,p):
    y=0
    for i in range(7):
        if x>>i & 1: y |= 1<<p[i]
    return y

def act(fam,p): return tuple(sorted(perm_mask(x,p) for x in fam))
orb=set()
stab=0
for p in permutations(range(7)):
    im=act(canon,p); orb.add(im)
    if im==canon: stab+=1
assert len(orb)==30 and stab==168 and orb==set(fano)
assert 5040//len(orb)==168
# singleton invariant under every row permutation
assert all(act(single[0],p)==single[0] for p in permutations(range(7)))

def fmt(fam):
    return ','.join(format(x,'07b') for x in fam)
blob=('\n'.join(fmt(s) for s in sorted(sol7))+'\n').encode()
sha=hashlib.sha256(blob).hexdigest()
print(f"VERIFY_OK target8={len(sol8)} nodes8={n8} maximum=7 maxima={len(sol7)} singleton=1 fano=30 row_group=5040 orbits=2 orbit_sizes=1,30 stabilizers=5040,168 nodes7={n7} census_sha256={sha}")
