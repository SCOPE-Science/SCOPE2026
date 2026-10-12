#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import combinations

N=6
WORDS=tuple(range(1<<N))

def bit(x,i): return (x>>i)&1

def d3(x,y):
    return sum(((bit(x,i),bit(x,(i+1)%N),bit(x,(i+2)%N)) !=
                (bit(y,i),bit(y,(i+1)%N),bit(y,(i+2)%N))) for i in range(N))

adj=[0]*(1<<N)
edges=0
for x in WORDS:
    for y in range(x+1,1<<N):
        if d3(x,y)>=5:
            adj[x]|=1<<y; adj[y]|=1<<x; edges+=1

# Bron-Kerbosch with pivot: enumerate every maximal clique exactly once.
maximal_hist=Counter(); maxima=[]; bk_nodes=0

def choose_pivot(PX,P):
    best=-1; score=-1; z=PX
    while z:
        lb=z & -z; u=lb.bit_length()-1; z-=lb
        s=(P & adj[u]).bit_count()
        if s>score: best,score=u,s
    return best

def bronk(R,P,X):
    global bk_nodes
    bk_nodes += 1
    if not P and not X:
        k=len(R); maximal_hist[k]+=1
        if k==16: maxima.append(tuple(R))
        return
    u=choose_pivot(P|X,P)
    cand=P if u<0 else P & ~adj[u]
    while cand:
        lb=cand & -cand; v=lb.bit_length()-1; cand-=lb
        bronk(R+(v,), P & adj[v], X & adj[v])
        P &= ~lb; X |= lb

bronk((), (1<<64)-1, 0)
maxima=sorted(set(tuple(sorted(c)) for c in maxima))
assert max(maximal_hist)==16
assert len(maxima)==76

# Independent fixed-cardinality increasing search for all 16-cliques.
ind=[]
def enum16(prefix, candidates, need):
    if need==0:
        ind.append(tuple(prefix)); return
    if candidates.bit_count()<need: return
    while candidates:
        lb=candidates & -candidates; v=lb.bit_length()-1; candidates-=lb
        if candidates.bit_count()+1 < need: break
        enum16(prefix+[v], candidates & adj[v], need-1)
enum16([], (1<<64)-1, 16)
ind=sorted(ind)
assert ind==maxima

# Direct Singleton bound for this parameter: agreement on any fixed block of
# four consecutive coordinates forces at least two equal cyclic 3-windows,
# so a d_3>=5 code projects injectively onto those 4 bits. Hence |C|<=16.
proj={x: tuple(bit(x,i) for i in range(4)) for x in WORDS}
for C in maxima:
    assert len({proj[x] for x in C})==16
    for a,b in combinations(C,2): assert d3(a,b)>=5

# 12 coordinate symmetries of a 6-cycle, then all 64 binary translations.
def permute_word(x,p):
    y=0
    for newpos,oldpos in enumerate(p): y |= bit(x,oldpos)<<newpos
    return y
coord=[]
for r in range(N):
    coord.append(tuple((i+r)%N for i in range(N)))
for r in range(N):
    coord.append(tuple((r-i)%N for i in range(N)))
coord=list(dict.fromkeys(coord)); assert len(coord)==12
transforms=[]
for p in coord:
    for t in WORDS:
        transforms.append(tuple(permute_word(x,p)^t for x in WORDS))
assert len(transforms)==768
assert len(set(transforms))==768
# Check every declared map preserves d_3 on every unordered pair.
for T in transforms:
    for x in WORDS:
        for y in range(x+1,64): assert d3(x,y)==d3(T[x],T[y])

M=set(maxima)
def image(C,T): return tuple(sorted(T[x] for x in C))
unseen=set(maxima); orbits=[]
while unseen:
    C=min(unseen)
    orb={image(C,T) for T in transforms}
    assert orb<=M
    orbits.append(sorted(orb)); unseen-=orb
orbits=sorted(orbits,key=lambda o:(len(o),o[0]))
assert [len(o) for o in orbits]==[4,4,12,24,32]

def affine(C):
    base=C[0]
    S={x^base for x in C}
    return 0 in S and all((a^b) in S for a in S for b in S)
aff=[affine(C) for C in maxima]
assert sum(aff)==44
for o in orbits:
    vals={affine(C) for C in o}; assert len(vals)==1
assert [len(o) for o in orbits if not affine(o[0])]==[32]

# Orbit invariants: ordinary Hamming pair-distance profiles.
def dh(x,y): return (x^y).bit_count()
def hprof(C): return tuple(sorted(Counter(dh(a,b) for a,b in combinations(C,2)).items()))
prof_counts=Counter(hprof(C) for C in maxima)
assert prof_counts == Counter({
    ((2,36),(3,36),(4,36),(5,12)):32,
    ((2,32),(3,48),(4,24),(5,16)):24,
    ((2,24),(3,64),(4,24),(6,8)):16,
    ((2,48),(4,72)):4,
})
print('VERIFY_OK vertices=64 edges=%d bk_nodes=%d maximal_cliques=%d maximal_hist=%s maximum=16 labeled_maxima=76 independent_16_cliques=76 group_size=768 orbits=5 orbit_sizes=4,4,12,24,32 affine_maxima=44 nonlinear_maxima=32 nonlinear_orbit=32' % (
    edges,bk_nodes,sum(maximal_hist.values()),','.join(f'{k}:{maximal_hist[k]}' for k in sorted(maximal_hist))))
