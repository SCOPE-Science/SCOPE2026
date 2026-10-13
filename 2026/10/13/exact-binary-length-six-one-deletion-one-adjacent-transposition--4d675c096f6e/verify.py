#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter

N=6
WORDS=list(product((0,1), repeat=N))
INDEX={w:i for i,w in enumerate(WORDS)}

def transposition_variants(x):
    out={x}
    for i in range(N-1):
        if x[i] != x[i+1]:
            y=list(x); y[i],y[i+1]=y[i+1],y[i]
            out.add(tuple(y))
    return out

def deletion_variants(y):
    out={y}
    for i in range(len(y)):
        out.add(y[:i]+y[i+1:])
    return out

def ball(x):
    out=set()
    for y in transposition_variants(x):
        out.update(deletion_variants(y))
    return out

BALLS=[ball(w) for w in WORDS]
ADJ=[0]*len(WORDS)
edges=0
for i,j in combinations(range(len(WORDS)),2):
    if BALLS[i].isdisjoint(BALLS[j]):
        ADJ[i] |= 1<<j; ADJ[j] |= 1<<i; edges += 1

maximal=[]
nodes=0
def bronk(R,P,X):
    global nodes
    nodes += 1
    if not P and not X:
        maximal.append(R); return
    U=P|X
    if U:
        z=U; best=-1; bestc=-1
        while z:
            b=z & -z; u=b.bit_length()-1; z-=b
            c=(P & ADJ[u]).bit_count()
            if c>bestc: best,bestc=u,c
        cand=P & ~ADJ[best]
    else:
        cand=P
    while cand:
        b=cand & -cand; v=b.bit_length()-1
        bronk(R|b, P & ADJ[v], X & ADJ[v])
        P &= ~b; X |= b; cand &= ~b

bronk(0,(1<<len(WORDS))-1,0)
hist=Counter(m.bit_count() for m in maximal)
maximum=max(hist)
MAXIMA=[m for m in maximal if m.bit_count()==maximum]
assert maximum==6 and len(MAXIMA)==26
assert hist==Counter({3:218,4:1861,5:816,6:26})
assert edges==928

core=(1<<64)-1
for m in MAXIMA: core &= m
core_words=tuple(''.join(map(str,WORDS[i])) for i in range(64) if (core>>i)&1)
assert core_words==('000000','111111')

def map_index(i,rev,comp):
    w=WORDS[i]
    if rev: w=w[::-1]
    if comp: w=tuple(1-b for b in w)
    return INDEX[w]
MAPS=[]
for rev in (False,True):
    for comp in (False,True):
        MAPS.append([map_index(i,rev,comp) for i in range(64)])

def map_mask(m,mp):
    out=0
    z=m
    while z:
        b=z & -z; i=b.bit_length()-1; z-=b
        out |= 1<<mp[i]
    return out
MSET=set(MAXIMA); seen=set(); orbit_sizes=[]
for m in MAXIMA:
    if m in seen: continue
    orb={map_mask(m,mp) for mp in MAPS}
    assert orb <= MSET
    seen |= orb; orbit_sizes.append(len(orb))
assert sorted(orbit_sizes)==[1,1,2,2,2,2,4,4,4,4]
coverage=Counter()
for m in MAXIMA:
    inds=[i for i in range(64) if (m>>i)&1]
    for i,j in combinations(inds,2):
        assert BALLS[i].isdisjoint(BALLS[j])
    coverage[len(set().union(*(BALLS[i] for i in inds)))] += 1
assert coverage==Counter({28:1,32:4,33:4,36:5,37:8,38:4})

witness=next(m for m in MAXIMA if len(set().union(*(BALLS[i] for i in range(64) if (m>>i)&1)))==28)
witness_words=[''.join(map(str,WORDS[i])) for i in range(64) if (witness>>i)&1]
print('VERIFY_OK vertices=64 edges=928 maximal_cliques=2921 histogram=3:218,4:1861,5:816,6:26 maximum=6 labeled_maxima=26 core=000000,111111 group_size=4 orbits=10 orbit_sizes=1x2,2x4,4x4 coverage=28x1,32x4,33x4,36x5,37x8,38x4 nodes=%d witness=%s' % (nodes,','.join(witness_words)))
