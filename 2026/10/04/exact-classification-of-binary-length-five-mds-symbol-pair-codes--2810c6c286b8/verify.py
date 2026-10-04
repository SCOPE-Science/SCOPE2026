#!/usr/bin/env python3
import itertools

N=5
WORDS=[tuple((x>>i)&1 for i in range(N-1,-1,-1)) for x in range(1<<N)]
INDEX={w:i for i,w in enumerate(WORDS)}

def pdist(a,b):
    return sum((a[i],a[(i+1)%N]) != (b[i],b[(i+1)%N]) for i in range(N))

ADJ=[set() for _ in WORDS]
for i in range(len(WORDS)):
    for j in range(i+1,len(WORDS)):
        if pdist(WORDS[i],WORDS[j]) >= 4:
            ADJ[i].add(j); ADJ[j].add(i)

max_size=0
maxima=[]
maximal_count=0

def bronk(R,P,X):
    global max_size,maxima,maximal_count
    if not P and not X:
        maximal_count += 1
        t=tuple(sorted(R))
        if len(R)>max_size:
            max_size=len(R); maxima=[t]
        elif len(R)==max_size:
            maxima.append(t)
        return
    if len(R)+len(P)<max_size:
        return
    U=P|X
    u=max(U,key=lambda z:len(P&ADJ[z])) if U else None
    cand=list(P-(ADJ[u] if u is not None else set()))
    for v in cand:
        bronk(R+[v],P&ADJ[v],X&ADJ[v])
        P.remove(v); X.add(v)

bronk([],set(range(len(WORDS))),set())
maxima=sorted(set(maxima))
assert max_size==8
assert len(maxima)==20
assert maximal_count==118

ZERO=(0,)*N

def xor(a,b): return tuple(x^y for x,y in zip(a,b))

def affine_direction(C):
    S={WORDS[i] for i in C}
    a=min(S)
    D={xor(x,a) for x in S}
    if ZERO not in D: return None
    if any(xor(x,y) not in D for x in D for y in D): return None
    return frozenset(D)

dirs=[]
for C in maxima:
    D=affine_direction(C)
    assert D is not None and len(D)==8
    dirs.append(D)
UD=set(dirs)
assert len(UD)==5
assert all(dirs.count(D)==4 for D in UD)

BASE=frozenset(tuple(map(int,s)) for s in [
    '00000','00101','01011','01110','10010','10111','11001','11100'])
assert BASE in UD

def rot(w,r): return tuple(w[(j+r)%N] for j in range(N))
assert {frozenset(rot(w,r) for w in BASE) for r in range(N)} == UD

MAXSETS={frozenset(WORDS[i] for i in C) for C in maxima}

def transform_word(w,r,rev,mask):
    idx=list(range(N))
    if rev: idx=idx[::-1]
    idx=idx[r:]+idx[:r]
    return tuple(w[idx[j]] ^ ((mask>>j)&1) for j in range(N))

rep=min(MAXSETS,key=lambda C:sorted(C))
orbit=set()
stab=0
for r in range(N):
    for rev in (0,1):
        for mask in range(1<<N):
            T=frozenset(transform_word(w,r,rev,mask) for w in rep)
            orbit.add(T)
            if T==rep: stab += 1
assert len(orbit)==20
assert orbit==MAXSETS
assert stab==16

# Recheck each code directly from the definition.
for C in MAXSETS:
    assert len(C)==8
    assert min(pdist(a,b) for a,b in itertools.combinations(C,2))>=4

print('VERIFY_OK maximum=8 labeled_maxima=20 maximal_cliques=118 affine_maxima=20 direction_subspaces=5 cosets_per_direction=4 orbit_size=20 stabilizer=16 group_size=320')
