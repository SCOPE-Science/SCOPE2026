#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

def S(i): return ("s", i)
def B(i): return ("b", i)
def T(xs): return ("t", tuple(sorted(xs)))
def vkey(v): return (v[0], v[1] if isinstance(v[1], int) else tuple(v[1]))
def fkey(f): return (len(f), tuple(sorted(f, key=vkey)))

def closure(facets):
    out=set()
    for F in facets:
        z=list(F)
        for r in range(1,len(z)+1):
            for q in combinations(z,r): out.add(frozenset(q))
    return out

def fvec(faces):
    c=Counter(map(len,faces))
    return tuple(c[i] for i in range(1,max(c)+1))

def gf2_rank(columns):
    basis={}
    for x in columns:
        y=x
        while y:
            p=y.bit_length()-1
            if p in basis: y ^= basis[p]
            else:
                basis[p]=y
                break
    return len(basis)

def betti(faces):
    dmax=max(map(len,faces))-1
    by={d:sorted((f for f in faces if len(f)==d+1),key=fkey) for d in range(dmax+1)}
    rank={}
    for d in range(1,dmax+1):
        rows={f:i for i,f in enumerate(by[d-1])}
        cols=[]
        for F in by[d]:
            x=0
            for q in combinations(F,d): x ^= 1 << rows[frozenset(q)]
            cols.append(x)
        rank[d]=gf2_rank(cols)
    b=[]
    for d in range(dmax+1): b.append(len(by[d])-rank.get(d,0)-rank.get(d+1,0))
    return tuple(b),rank

def collapse(faces):
    faces=set(faces); pairs=[]
    while True:
        found=None
        for sigma in sorted(faces,key=fkey,reverse=True):
            taus=[tau for tau in faces if len(tau)==len(sigma)+1 and sigma<tau]
            if len(taus)!=1: continue
            tau=taus[0]
            if any(tau<h for h in faces): continue
            found=(sigma,tau); break
        if found is None: break
        sigma,tau=found
        # Verify the elementary-collapse condition at the instant of deletion.
        all_cofaces=[h for h in faces if sigma<h]
        assert all(h<=tau for h in all_cofaces)
        faces.remove(sigma); faces.remove(tau); pairs.append(found)
    return faces,pairs

# Published four facet families.  The first two make the small 60-facet orbit.
A1=[]
for i in range(6):
    for j in range(6):
        if i==j: continue
        rem=[x for x in range(6) if x not in (i,j)]
        A1.append(frozenset([S(i)]+[T((i,j,l)) for l in rem]))
A2=[]
for Q in combinations(range(6),4):
    for m in [x for x in range(6) if x not in Q]:
        A2.append(frozenset([B(m)]+[T(q) for q in combinations(Q,3)]))
B1=[]
for i in range(6):
    for j in range(6):
        if j==i: continue
        for k in range(6):
            if k in (i,j): continue
            rem=[l for l in range(6) if l not in (i,j,k)]
            B1.append(frozenset([S(i),B(k)]+[T((i,j,l)) for l in rem]))
B2=[]
for i in range(6):
    for m in range(6):
        if m==i: continue
        rem=[x for x in range(6) if x not in (i,m)]
        for R in combinations(rem,3):
            B2.append(frozenset([S(i),B(m)]+[T((i,a,b)) for a,b in combinations(R,2)]))

small=set(A1+A2); full=set(A1+A2+B1+B2)
assert (len(set(A1)),len(set(A2)),len(set(B1)),len(set(B2)))==(30,30,120,120)
assert len(small)==60 and len(full)==300
FA=closure(small); FK=closure(full)
assert fvec(FK)==(32,240,660,750,300)
assert fvec(FA)==(32,210,480,270,60)
core,pairs=collapse(FA)
assert len(pairs)==270
assert fvec(core)==(32,210,270)
assert max(map(len,core))==3
b,rank=betti(core)
assert b==(1,0,91)
assert rank[1]==31 and rank[2]==179
# Cross-check the unreduced complex directly.
b0,r0=betti(FA)
assert b0==(1,0,91,0,0)
print("VERIFY_OK full_f=32,240,660,750,300 orbit_facets=60 f=32,210,480,270,60 collapses=270 core_f=32,210,270 ranks=31,179 betti=1,0,91")
