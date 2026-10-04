#!/usr/bin/env python3
import itertools, math, collections
from fractions import Fraction

N=5
VERT=range(N)
RANKINGS=list(itertools.permutations(VERT))
PAIRS=[(i,j) for i in VERT for j in VERT if i<j]
PIDX={p:k for k,p in enumerate(PAIRS)}
RELABELS=list(itertools.permutations(VERT))

def ranking_bits(order):
    pos=[0]*N
    for k,v in enumerate(order): pos[v]=k
    bits=0
    for k,(i,j) in enumerate(PAIRS):
        if pos[i]<pos[j]: bits |= 1<<k
    return bits

RBITS=[ranking_bits(p) for p in RANKINGS]

def relabel(bits,sigma):
    out=0
    for k,(i,j) in enumerate(PAIRS):
        if (bits>>k)&1: u,v=i,j
        else: u,v=j,i
        nu,nv=sigma[u],sigma[v]
        a,b=(nu,nv) if nu<nv else (nv,nu)
        kk=PIDX[(a,b)]
        if nu<nv: out |= 1<<kk
    return out

# Exhaustive tournament quotient under candidate relabeling.
CANON={}
AUT={}
for bits in range(1<<len(PAIRS)):
    imgs=[relabel(bits,s) for s in RELABELS]
    c=min(imgs)
    CANON[bits]=c
    if bits==c:
        AUT[c]=sum(x==c for x in imgs)
CLASSES=sorted(set(CANON.values()))
assert len(CLASSES)==12

def majority3(a,b,c):
    return (a&b) | (c & (a|b))

# Route A: all ordered voter triples.
A=collections.Counter()
for a in RBITS:
    for b in RBITS:
        ab=a&b; aorb=a|b
        for c in RBITS:
            A[CANON[ab | (c&aorb)]] += 1
assert sum(A.values())==120**3

# Route B: anonymous profile types, restored with exact multinomial weights.
B=collections.Counter()
for i in range(120):
    a=RBITS[i]
    for j in range(i,120):
        b=RBITS[j]
        ab=a&b; aorb=a|b
        for k in range(j,120):
            c=RBITS[k]
            t=CANON[ab | (c&aorb)]
            if i==j==k: w=1
            elif i==j or j==k: w=3
            else: w=6
            B[t]+=w
assert A==B

# Human-readable isomorphism signature: sorted (outdegree, number of cyclic triangles through vertex).
def edge(bits,u,v):
    a,b=(u,v) if u<v else (v,u)
    bit=(bits>>PIDX[(a,b)])&1
    return bit if u<v else 1-bit

def signature(bits):
    out=[sum(edge(bits,v,w) for w in VERT if w!=v) for v in VERT]
    tri=[0]*N
    tcount=0
    for T in itertools.combinations(VERT,3):
        d={v:0 for v in T}
        for u,v in itertools.combinations(T,2):
            if edge(bits,u,v): d[u]+=1
            else: d[v]+=1
        if sorted(d.values())==[1,1,1]:
            tcount+=1
            for v in T: tri[v]+=1
    sig=tuple(sorted(zip(out,tri), reverse=True))
    return tuple(sorted(out,reverse=True)), tcount, sig

SIGS={c:signature(c) for c in CLASSES}
assert len(set(SIGS.values()))==12

EXPECTED={
    76:720, 12:17280, 40:2160, 41:8640, 8:32400, 10:28080,
    9:95760, 11:91440, 4:95760, 5:96720, 2:91440, 0:1167600,
}
assert dict(A)==EXPECTED
assert all(A[c]>0 for c in CLASSES)

# Orbit-size/per-labeled-fiber audit.
for c in CLASSES:
    orbit=math.factorial(N)//AUT[c]
    assert A[c] % orbit == 0

print('VERIFY_OK')
print('ordered_profiles',120**3)
print('anonymous_profile_types',math.comb(122,3))
print('unlabeled_tournament_classes',len(CLASSES))
print('transitive_profiles',A[0], 'probability', Fraction(A[0],120**3))
print('regular_C5_profiles',A[76], 'probability', Fraction(A[76],120**3))
for c in sorted(CLASSES, key=lambda x:(SIGS[x][0],SIGS[x][1],SIGS[x][2])):
    degrees,tcount,sig=SIGS[c]
    orbit=120//AUT[c]
    perlab=A[c]//orbit
    print(c, degrees, tcount, sig, 'aut',AUT[c], 'orbit',orbit, 'profiles',A[c], 'per_labeled',perlab, 'prob',Fraction(A[c],120**3))
