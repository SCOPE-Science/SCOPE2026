#!/usr/bin/env python3
from itertools import product, combinations

Q = tuple(product(range(3), repeat=3))
idx = {x:i for i,x in enumerate(Q)}

def ball_direct(x):
    out={x}
    for i,a in enumerate(x):
        if a<2:
            y=list(x); y[i]+=1; out.add(tuple(y))
    return frozenset(out)

def ball_error_words(x):
    out=set()
    for e in [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]:
        y=tuple(x[i]+e[i] for i in range(3))
        if all(v<3 for v in y):
            out.add(y)
    return frozenset(out)

balls1=[ball_direct(x) for x in Q]
balls2=[ball_error_words(x) for x in Q]
assert balls1==balls2

compat=[0]*27
for i,x in enumerate(Q):
    for j,y in enumerate(Q):
        if i!=j and balls1[i].isdisjoint(balls1[j]):
            compat[i] |= 1<<j

# Explicit nine-clique partition of the conflict graph: at most one codeword per triple.
partition=[
((0,0,0),(0,0,1),(0,1,0)),
((0,0,2),(0,1,1),(0,1,2)),
((0,2,0),(0,2,1),(1,2,0)),
((0,2,2),(1,1,2),(1,2,1)),
((1,0,0),(1,0,1),(2,0,0)),
((1,0,2),(2,0,1),(2,0,2)),
((1,1,0),(1,1,1),(2,1,0)),
((1,2,2),(2,1,2),(2,2,2)),
((2,1,1),(2,2,0),(2,2,1)),
]
assert set(sum((list(g) for g in partition),[]))==set(Q)
for g in partition:
    for x,y in combinations(g,2):
        assert not balls1[idx[x]].isdisjoint(balls1[idx[y]])

candidate=tuple(sorted([x for x in Q if all(a in (0,2) for a in x)]+[(1,1,1)]))
assert len(candidate)==9
assert all(balls1[idx[x]].isdisjoint(balls1[idx[y]]) for x,y in combinations(candidate,2))

# Enumerate every maximal compatibility clique exactly by Bron--Kerbosch.
best=0
maxima=set()
def bronk(R,P,X):
    global best,maxima
    if not P and not X:
        C=tuple(i for i in range(27) if (R>>i)&1)
        k=len(C)
        if k>best:
            best=k; maxima={C}
        elif k==best:
            maxima.add(C)
        return
    U=P|X
    if U:
        us=[u for u in range(27) if (U>>u)&1]
        pivot=max(us,key=lambda u:(P&compat[u]).bit_count())
        todo=P & ~compat[pivot]
    else:
        todo=P
    while todo:
        b=todo & -todo
        v=b.bit_length()-1
        bronk(R|b,P&compat[v],X&compat[v])
        P &= ~b; X |= b; todo &= ~b
bronk(0,(1<<27)-1,0)

assert best==9
assert len(maxima)==1
only=tuple(Q[i] for i in next(iter(maxima)))
assert only==candidate

# Independent fixed-size search: count all compatible 9-sets using ordered recursion.
count9=0
def count_k(cands, chosen, target):
    global count9
    if chosen + cands.bit_count() < target:
        return
    if chosen==target:
        count9 += 1
        return
    while cands:
        if chosen + cands.bit_count() < target:
            return
        b=cands & -cands
        v=b.bit_length()-1
        cands ^= b
        count_k(cands & compat[v], chosen+1, target)
count_k((1<<27)-1,0,9)
assert count9==1

# Verify this is exactly Construction 1A from the binary repetition code {000,111}.
lift=tuple(sorted(x for x in Q if tuple(a%2 for a in x) in {(0,0,0),(1,1,1)}))
assert lift==candidate

def word(x): return ''.join(map(str,x))
print("BALL_IMPLEMENTATIONS_AGREE=27")
print("PARTITION_CONFLICT_CLIQUES=9")
print("MAXIMUM=9")
print("LABELED_MAXIMA=1")
print("MAXIMUM_CODE="+",".join(word(x) for x in candidate))
print("CONSTRUCTION_1A_LIFT=true")
print("VERIFY_OK maximum=9 labeled_maxima=1 unique_code=corners_plus_center")
