#!/usr/bin/env python3
import itertools, math, json
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# Encode 0,a,b,c=a+b as (x,y) representing x*a+y*b over F2.
ELTS=((0,0),(1,0),(0,1),(1,1))
NAMES=("0","a","b","c")

def add(u,v):
    return (u[0]^v[0],u[1]^v[1])

def mul(u,v):
    # (x a + y b)(x' a + y' b) = x x' b.
    return (0,u[0]&v[0])

def dot(v,w):
    z=(0,0)
    for x,y in zip(v,w):
        z=add(z,mul(x,y))
    return z

def orbit_formula(n):
    out=Counter()
    for d in range(1,n+1):
        if d%2==0:
            t=d//2
            out[d]=t*(t+1)
        else:
            t=(d-1)//2
            out[d]=(t+1)*(t+2)
    return out

def total_formula(n):
    if n%2==0:
        m=n//2
        return 2*m*(m+1)*(m+2)//3
    m=(n-1)//2
    return (m+1)*(m+2)*(2*m+3)//3

def full_formula(n):
    if n%2==0:
        m=n//2
        return m*(m+1)
    m=(n-1)//2
    return (m+1)*(m+2)

# Ring-table anchors.
sq={NAMES[i]:NAMES[ELTS.index(mul(e,e))] for i,e in enumerate(ELTS)}
assert sq==CERT["ring"]["squares"]

for n in CERT["verified_lengths"]:
    labeled=0
    orbits=set()
    bydist=Counter()
    for idxs in itertools.product(range(4),repeat=n):
        if all(i==0 for i in idxs):
            continue
        v=tuple(ELTS[i] for i in idxs)
        selfdot=dot(v,v)
        counts=tuple(idxs.count(i) for i in range(4))
        parity=(counts[1]+counts[3])&1
        acd=(selfdot!=(0,0))
        assert acd==bool(parity)
        if not acd:
            continue
        labeled+=1
        orbits.add(counts)
    assert labeled==2**(2*n-1)

    for counts in orbits:
        n0,na,nb,nc=counts
        assert na+nc>0 and (na+nc)%2==1
        d=n-n0
        bydist[d]+=1

    expected=orbit_formula(n)
    assert bydist==expected
    assert len(orbits)==total_formula(n)
    assert bydist[n]==full_formula(n)

# Published cardinality-two row.
got=[total_formula(n) for n in range(1,6)]
assert got==CERT["source"]["published_cardinality_two_counts_n1_to_n5"]

# Algebraic cross-check of the closed sums for a wider range.
for n in range(1,101):
    direct=sum(orbit_formula(n).values())
    assert direct==total_formula(n)
    assert orbit_formula(n)[n]==full_formula(n)

print("VERIFY_OK")
