#!/usr/bin/env python3
"""Independent combination/linear-algebra/Lefschetz checks for Chvatal Ind_2.
Does not import the discrete-Morse certificate. Pure Python standard library.
"""
from collections import Counter
from itertools import combinations
N=12
ADJ=((1,4,6,9),(0,2,5,7),(1,3,6,8),(2,4,7,9),
     (0,3,5,8),(1,4,10,11),(0,2,10,11),(1,3,8,11),
     (2,4,7,10),(0,3,10,11),(5,6,8,9),(5,6,7,9))
assert all(i in ADJ[j] for i in range(N) for j in ADJ[i])

def faces(mode=None,vertex=None):
    allowed=[]
    for k in range(1,N+1):
        for seq in combinations(range(N),k):
            s=frozenset(seq)
            if any(sum(t in s for t in ADJ[v])>1 for v in seq):continue
            if mode=='delete' and vertex in s:continue
            if mode=='link':
                if vertex not in s:continue
                s=s-{vertex}
                if not s:continue
            allowed.append(tuple(sorted(s)))
    return tuple(sorted(set(allowed),key=lambda t:(len(t),t)))

def gf2_rank(columns):
    pivots={}
    for col in columns:
        while col:
            r=col.bit_length()-1
            if r in pivots:col ^= pivots[r]
            else:pivots[r]=col;break
    return len(pivots)

def betti(fs):
    bydim={k:[] for k in range(N)}
    for f in fs:bydim[len(f)-1].append(f)
    rank={-1:0,0:0}
    for k in range(1,N):
        lower={f:i for i,f in enumerate(bydim[k-1])}
        columns=[]
        for f in bydim[k]:
            bits=0
            for omit in f:
                face=tuple(x for x in f if x!=omit)
                bits ^= 1<<lower[face]
            columns.append(bits)
        rank[k]=gf2_rank(columns)
    b={k:len(bydim[k])-rank[k]-rank[k+1] for k in range(N-1)}
    b[0]-=1
    return {k:v for k,v in b.items() if v}

def compose(g,h):return tuple(g[h[i]] for i in range(N))
identity=tuple(range(N))
r=(1,5,11,6,0,4,7,10,9,2,3,8)
s=(0,4,3,2,1,5,9,8,7,6,11,10)
r2=compose(r,r)
r3=compose(r,r2)
assert compose(r,r3)==identity and compose(s,s)==identity
assert compose(s,compose(r,s))==r3
G={compose(q,t) for q in (identity,r,r2,r3) for t in (identity,s)}
assert len(G)==8
for g in G:
    assert all(set(g[j] for j in ADJ[i])==set(ADJ[g[i]]) for i in range(N))

def signed_fixed_face_lefschetz(g,fs):
    L=0
    for f in fs:
        perm=[g[i] for i in f]
        if set(perm)!=set(f):continue
        inversions=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
        L+=(-1)**(len(f)-1+inversions)
    return L

allfaces=faces()
assert len(allfaces)==424
for name,mode,v,expected in (
    ('K',None,None,{3:1}),('D0','delete',0,{3:1}),('L0','link',0,{}),
    ('D2','delete',2,{}),('L2','link',2,{2:1})):
    f=allfaces if mode is None else faces(mode,v)
    b=betti(f)
    assert b==expected,(name,b)
    print(name,'GF2_REDUCED_BETTI',b,'FACES',len(f))
characters={g:1-signed_fixed_face_lefschetz(g,allfaces) for g in G}
assert characters[identity]==1
assert characters[r]==-1,characters[s]==1
assert all(characters[compose(a,b)]==characters[a]*characters[b] for a in G for b in G)
assert sum(characters.values())==0
assert Counter(characters.values())=={1:4,-1:4}
print('D4_ORDER',len(G),'CHARACTER_R',characters[r],'CHARACTER_S',characters[s])
print('CHARACTER_DISTRIBUTION',dict(sorted(Counter(characters.values()).items())))
print('H3_GROUP_INVARIANTS',sum(characters.values())//len(G))
print('INDEPENDENT_CHECKS_OK')
