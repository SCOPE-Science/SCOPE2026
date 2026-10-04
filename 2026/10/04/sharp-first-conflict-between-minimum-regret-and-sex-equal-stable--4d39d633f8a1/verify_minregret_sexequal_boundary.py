#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
import hashlib


def stable_rankmap(men, women):
    n=len(men)
    mr=[{w:i+1 for i,w in enumerate(pref)} for pref in men]
    wr=[{m:i+1 for i,m in enumerate(pref)} for pref in women]
    out=[]
    for M in permutations(range(n)):
        inv=[None]*n
        for m,w in enumerate(M): inv[w]=m
        stable=True
        for m in range(n):
            for w in range(n):
                if M[m]==w: continue
                if mr[m][w] < mr[m][M[m]] and wr[w][m] < wr[w][inv[w]]:
                    stable=False; break
            if not stable: break
        if stable:
            ranks_m=tuple(mr[m][M[m]] for m in range(n))
            ranks_w=tuple(wr[w][inv[w]] for w in range(n))
            mc=sum(ranks_m); wc=sum(ranks_w)
            out.append((tuple(M), max(ranks_m+ranks_w), abs(mc-wc), mc, wc, ranks_m+ranks_w))
    return tuple(out)


def stable_direct(men, women):
    n=len(men)
    out=[]
    for M in permutations(range(n)):
        inv=[None]*n
        for m,w in enumerate(M): inv[w]=m
        stable=True
        for m in range(n):
            assigned=M[m]
            for w in range(n):
                if w==assigned: continue
                if men[m].index(w) < men[m].index(assigned):
                    incumbent=inv[w]
                    if women[w].index(m) < women[w].index(incumbent):
                        stable=False; break
            if not stable: break
        if stable:
            rm=tuple(men[m].index(M[m])+1 for m in range(n))
            rw=tuple(women[w].index(inv[w])+1 for w in range(n))
            mc=sum(rm); wc=sum(rw)
            out.append((tuple(M),max(rm+rw),abs(mc-wc),mc,wc,rm+rw))
    return tuple(out)


def relation(st):
    r=min(x[1] for x in st)
    s=min(x[2] for x in st)
    R={x[0] for x in st if x[1]==r}
    S={x[0] for x in st if x[2]==s}
    if R==S: rel='equal'
    elif R<S: rel='regret_subset_sexequal'
    elif S<R: rel='sexequal_subset_regret'
    elif R & S: rel='overlap_nonnested'
    else: rel='disjoint'
    return r,s,R,S,rel


def transform_profile(prof, sm, sw, swap=False):
    # sm/sw are permutations giving old-label -> new-label maps on men/women.
    n=len(sm)
    men=prof[:n]; women=prof[n:]
    if not swap:
        nm=[None]*n; nw=[None]*n
        for oldm in range(n):
            newm=sm[oldm]
            nm[newm]=tuple(sw[oldw] for oldw in men[oldm])
        for oldw in range(n):
            neww=sw[oldw]
            nw[neww]=tuple(sm[oldm] for oldm in women[oldw])
        return tuple(nm+nw)
    # Side exchange: old women become new men and old men become new women.
    nm=[None]*n; nw=[None]*n
    for oldw in range(n):
        newm=sw[oldw]
        nm[newm]=tuple(sm[oldm] for oldm in women[oldw])
    for oldm in range(n):
        neww=sm[oldm]
        nw[neww]=tuple(sw[oldw] for oldw in men[oldm])
    return tuple(nm+nw)


def canonical(prof):
    n=len(prof)//2
    perms=list(permutations(range(n)))
    return min(transform_profile(prof,sm,sw,swap) for sm in perms for sw in perms for swap in (False,True))


def exhaustive(n):
    orders=list(permutations(range(n)))
    hist=Counter(); stable_hist=Counter(); detail=Counter(); lines=[]; dis=[]
    for prof in product(orders, repeat=2*n):
        men=prof[:n]; women=prof[n:]
        a=stable_rankmap(men,women); b=stable_direct(men,women)
        assert a==b and a
        r,s,R,S,rel=relation(a)
        hist[rel]+=1; stable_hist[len(a)]+=1
        detail[(len(a),rel,len(R),len(S))]+=1
        if rel=='disjoint': dis.append((prof,a,R,S))
        lines.append(repr((prof,a,r,s,tuple(sorted(R)),tuple(sorted(S)),rel)))
    dig=hashlib.sha256('\n'.join(lines).encode()).hexdigest()
    return hist,stable_hist,detail,dis,dig

r2=exhaustive(2)
assert r2[0] == Counter({'equal':16})
assert r2[1] == Counter({1:14,2:2})

r3=exhaustive(3)
assert r3[0] == Counter({
    'equal':38880,
    'sexequal_subset_regret':7488,
    'regret_subset_sexequal':144,
    'disjoint':144,
})
assert r3[0]['overlap_nonnested']==0
assert r3[1] == Counter({1:34080,2:11484,3:1092})
assert r3[2] == Counter({
    (1,'equal',1,1):34080,
    (2,'equal',1,1):2760,
    (2,'equal',2,2):1812,
    (3,'equal',1,1):228,
    (2,'sexequal_subset_regret',2,1):6624,
    (3,'sexequal_subset_regret',3,1):792,
    (3,'sexequal_subset_regret',3,2):72,
    (2,'regret_subset_sexequal',1,2):144,
    (2,'disjoint',1,1):144,
})
assert all(len(x[1])==2 for x in r3[3])

# Natural relabeling symmetries: independent renaming of men and women and side exchange.
orbits=Counter(canonical(x[0]) for x in r3[3])
assert len(orbits)==2
assert Counter(orbits.values()) == Counter({72:2})

# For every conflict, one stable matching has (regret,sex-equal)=(2,3)
# and the other has (3,2), with the aggregate burden asymmetry reversed by side exchange.
patterns=Counter()
for prof,st,R,S in r3[3]:
    q=tuple(sorted((x[1],x[2],x[3],x[4]) for x in st))
    patterns[q]+=1
expected_patterns=Counter({
    ((2,3,6,3),(3,2,4,6)):72,
    ((2,3,3,6),(3,2,6,4)):72,
})
assert patterns==expected_patterns

# Small explicit disjoint witness.
MEN=((0,1,2),(0,2,1),(1,0,2))
WOMEN=((2,0,1),(0,1,2),(1,0,2))
w=stable_rankmap(MEN,WOMEN)
assert w==stable_direct(MEN,WOMEN)
assert w == (
    ((0,2,1),3,2,4,6,(1,2,1,2,3,1)),
    ((1,2,0),2,3,6,3,(2,2,2,1,1,1)),
)
r,s,R,S,rel=relation(w)
assert (r,s,rel)==(2,2,'disjoint')
assert R=={(1,2,0)} and S=={(0,2,1)}

N=6**6
print('VERIFY_OK')
print('n2_relation_hist', dict(r2[0]))
print('n3_profiles',N)
print('n3_relation_hist',dict(r3[0]))
print('n3_probabilities',{k:str(Fraction(v,N)) for k,v in r3[0].items()})
print('n3_stable_count_hist',dict(r3[1]))
print('n3_detail',{str(k):v for k,v in sorted(r3[2].items(), key=lambda z:str(z[0]))})
print('disjoint_orbits',len(orbits))
print('disjoint_orbit_sizes',dict(Counter(orbits.values())))
print('disjoint_patterns',{str(k):v for k,v in patterns.items()})
print('canonical_disjoint_representatives',sorted(orbits))
print('witness',w)
print('n3_digest',r3[4])
