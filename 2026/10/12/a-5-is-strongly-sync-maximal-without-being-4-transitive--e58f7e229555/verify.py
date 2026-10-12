#!/usr/bin/env python3
from itertools import permutations, product, combinations
from pathlib import Path
import json

N=5
Q=range(N)

def parity(p):
    inv=0
    for i in range(N):
        for j in range(i+1,N):
            inv += p[i] > p[j]
    return inv % 2

A5=[tuple(p) for p in permutations(Q) if parity(p)==0]
assert len(A5)==60

twos=[frozenset(c) for c in combinations(Q,2)]

def image(S,t):
    return frozenset(t[x] for x in S)

# A_5 is 3-transitive: every prescribed bijection on three distinct
# points has two extensions to S_5, and exactly one extension is even.
for xs in permutations(Q,3):
    for ys in permutations(Q,3):
        assert any(all(g[xs[i]]==ys[i] for i in range(3)) for g in A5)

# It is also transitive on ordered pairs of disjoint 2-subsets.
def orbit(seed):
    X,Y=seed
    return {(image(X,g),image(Y,g)) for g in A5}

inter_seed=(frozenset((0,1)),frozenset((0,2)))
disj_seed=(frozenset((0,1)),frozenset((2,3)))
inter_configs={(X,Y) for X in twos for Y in twos if X!=Y and len(X&Y)==1}
disj_configs={(X,Y) for X in twos for Y in twos if X.isdisjoint(Y)}
assert orbit(inter_seed)==inter_configs
assert orbit(disj_seed)==disj_configs
assert len(inter_configs)==60
assert len(disj_configs)==30

def rank(t):
    return len(set(t))

# Constructive witness lemma used in the proof.
def local_witnesses(f):
    fibers={}
    for x,y in enumerate(f):
        fibers.setdefault(y,[]).append(x)

    # Intersecting: a collapsed pair and a pair sharing one point
    # whose two images differ.
    C=None
    I=None
    for F in fibers.values():
        if len(F)>=2:
            x,y=F[0],F[1]
            for z in Q:
                if f[z]!=f[x]:
                    C=frozenset((x,y))
                    I=frozenset((x,z))
                    break
        if C is not None:
            break
    assert C is not None and I is not None
    assert len(C&I)==1
    assert len(image(C,f))==1 and len(image(I,f))==2

    # Disjoint: first use a fiber of size at least 3 if available.
    D1=D2=None
    big=next((F for F in fibers.values() if len(F)>=3),None)
    if big is not None:
        x,y,w=big[:3]
        z=next(z for z in Q if f[z]!=f[x])
        D1=frozenset((x,y))
        D2=frozenset((w,z))
    else:
        # Then every nontrivial fiber has size 2. Since f is
        # non-injective and has rank at least 2 on five points, choose
        # such a fiber and two complement points with distinct images.
        F=next(F for F in fibers.values() if len(F)==2)
        comp=[z for z in Q if z not in F]
        z=w=None
        for a,b in combinations(comp,2):
            if f[a]!=f[b]:
                z,w=a,b
                break
        assert z is not None
        D1=frozenset(F)
        D2=frozenset((z,w))
    assert D1.isdisjoint(D2)
    assert len(image(D1,f))==1 and len(image(D2,f))==2
    return C,I,D1,D2

counts={2:0,3:0,4:0}
for f in product(Q, repeat=N):
    r=rank(f)
    if r not in counts:
        continue
    f=tuple(f)
    counts[r]+=1
    C,I,D1,D2=local_witnesses(f)

    # Directly check the stronger one-group-element property for every
    # ordered pair of distinct 2-subsets.
    for S in twos:
        for T in twos:
            if S==T:
                continue
            ok=False
            for g in A5:
                a=len(image(image(S,g),f))==1
                b=len(image(image(T,g),f))==1
                if a != b:
                    ok=True
                    break
            assert ok,(f,S,T)

assert counts=={2:300,3:1500,4:1200}

# A_5 cannot be 4-transitive on five points because a 4-transitive
# degree-five group has order divisible by the number 5*4*3*2=120
# of ordered 4-tuples of distinct points.
assert len(A5)==60 and 60 < 120

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["strongly_sync_maximal"] is True
assert cert["four_transitive"] is False
assert cert["nonpermutation_transformations_checked"]["total"]==3000

print("VERIFY_OK A5_order=60 three_transitive=1 pair_orbits=intersecting+disjoint "
      "rank2=300 rank3=1500 rank4=1200 transformations=3000 "
      "all_ordered_pair_tests=270000 one_group_element_then_f=1 "
      "four_transitive=0 strongly_sync_maximal=1")
