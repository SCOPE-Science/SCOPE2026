#!/usr/bin/env python3
"""Finite exact certificate for threshold-two three-colour CCA on tripartite graphs.

All finite arithmetic is integer-only. The 3^9 capped population system and
its reachable tagged-vertex states are enumerated without size assumptions.
"""
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import permutations
from math import factorial,lcm

N=3**9
POW=[3**j for j in range(9)]
def decode(n):
    v=[]
    for _ in range(9):v.append(n%3);n//=3
    return tuple(v)
def encode(v):return sum(v[j]*POW[j] for j in range(9))
def good(v):return all(sum(v[3*i:3*i+3])>0 for i in range(3))
def advance(v):
    dest=[0]*9
    for i in range(3):
        for c in range(3):
            mass=v[3*i+c]
            if not mass:continue
            successor=(c+1)%3
            cnt=sum(v[3*j+successor] for j in range(3) if j!=i)
            new=successor if cnt>=2 else c
            dest[3*i+new]=min(2,dest[3*i+new]+mass)
    return tuple(dest)

def orbit_invariants(next_map):
    """Return (entrance time, least cycle period) for a total finite map."""
    out={}
    for root in next_map:
        if root in out:continue
        line=[];seen={};u=root
        while u not in out and u not in seen:
            seen[u]=len(line);line.append(u);u=next_map[u]
        if u in out:
            t,cycle=out[u]
            for x in reversed(line):
                t+=1;out[x]=(t,cycle)
        else:
            position=seen[u];cycle=len(line)-position
            for x in line[position:]:out[x]=(0,cycle)
            t=0
            for x in reversed(line[:position]):
                t+=1;out[x]=(t,cycle)
    return out

def canonical(v):
    candidates=[]
    for perm in permutations(range(3)):
        for rot in range(3):
            candidates.append(tuple(tuple(v[3*i+(c-rot)%3] for c in range(3)) for i in perm))
    return min(candidates)

V=[decode(j) for j in range(N)]
S=[s for s in range(N) if good(V[s])]
F={s:encode(advance(V[s])) for s in S}
assert len(S)==17576 and all(F[s] in F for s in S)
T={}
for s in S:
    v=V[s]
    for i in range(3):
        for c in range(3):
            if not v[3*i+c]:continue
            nextc=(c+1)%3
            neighbor_count=sum(v[3*j+nextc] for j in range(3) if j!=i)
            T[s,i,c]=(F[s],i,nextc if neighbor_count>=2 else c)
assert len(T)==109512 and all(y in T for y in T.values())
INV=orbit_invariants(T)
Q={}
for s in S:
    inv=[INV[s,i,c] for i in range(3) for c in range(3) if V[s][3*i+c]>0]
    Q[s]=(max(x[0] for x in inv),lcm(*(x[1] for x in inv)))

# The eventual period of the whole labelled colouring is the lcm of the
# eventual tagged periods, and its first periodic time their maximum.
periods=Counter(p for t,p in Q.values() if t==0)
assert periods=={1:174,3:1826,4:18,6:6,12:126},periods
assert max(t for t,p in Q.values())==9
assert {p for t,p in Q.values()}=={1,3,4,6,12}

# This direct power identity checks every reachable tagged state, independent
# of the graph sizes represented by its truncated occupancy labels.
for q in T:
    t=q
    for _ in range(9):t=T[t]
    target=t
    for _ in range(12):t=T[t]
    assert t==target,(q,target,t)

canonical_expected={
    4:{
        ((0,1,1),(0,1,1),(2,2,0)),
        ((0,1,1),(0,1,1),(2,0,2)),
    },
    6:{
        ((0,1,1),(1,0,1),(1,1,0)),
    },
    12:{
        ((0,0,1),(0,2,2),(2,0,2)),
        ((0,0,1),(2,0,2),(2,2,0)),
        ((0,0,1),(0,2,2),(2,2,0)),
        ((0,1,1),(0,2,2),(2,2,0)),
        ((0,1,1),(0,2,2),(2,0,2)),
        ((0,1,1),(2,0,2),(2,2,0)),
        ((0,2,2),(1,1,1),(2,0,2)),
    },
}
for p,expected in canonical_expected.items():
    members=[s for s in S if Q[s]==(0,p)]
    got={canonical(V[s]) for s in members}
    assert got==expected,(p,got^expected)
    # Each canonical profile generates a single orbit under part permutations
    # and simultaneous colour rotations, tested by the actual cardinality.
    assert len(members)=={4:18,6:6,12:126}[p]

@lru_cache(None)
def weight(n,signature):
    if n<sum(signature):return 0
    tot=0
    for i in range(n+1):
        for j in range(n-i+1):
            k=n-i-j
            if tuple(min(2,z) for z in (i,j,k))==signature:
                tot+=factorial(n)//(factorial(i)*factorial(j)*factorial(k))
    return tot

def weighted_census(sizes):
    out=Counter()
    for s in S:
        w=1
        for i,n in enumerate(sizes):
            w*=weight(n,V[s][3*i:3*i+3])
            if not w:break
        if w:out[Q[s]]+=w
    assert sum(out.values())==3**sum(sizes)
    return out

def B(n):return 2**n-2*n-2 if n>=4 else 0
def J(n):return {1:1,2:2,3:2}.get(n,0)
def expected_high_periods(a,b,c):
    x=(a,b,c)
    r4=sum(24*B(x[k]) if x[(k+1)%3]==x[(k+2)%3]==2 else 0 for k in range(3))
    r6=48 if x==(2,2,2) else 0
    r12=18*sum(J(x[k])*B(x[(k+1)%3])*B(x[(k+2)%3]) for k in range(3))
    return {4:r4,6:r6,12:r12}

for sizes in [(1,1,1),(1,4,4),(2,4,4),(3,4,4),(2,2,2),(2,2,4),
              (2,2,5),(1,5,6),(3,4,7),(4,4,4),(6,6,2),(7,7,7)]:
    census=weighted_census(sizes)
    rec=Counter()
    for (t,p),w in census.items():
        if t==0:rec[p]+=w
    ex=expected_high_periods(*sizes)
    assert all(rec[p]==ex[p] for p in (4,6,12)),(sizes,rec,ex)
    assert max(t for t,p in census)<=9
    print('PARAM',sizes,'recurrent',dict(sorted(rec.items())), 'maxpre',max(t for t,p in census))
print('FINITE_CERTIFICATE_OK', 'profiles',len(S),'tag_states',len(T),
      'maxpre',max(t for t,p in Q.values()),'recurrent_profiles',dict(sorted(periods.items())))
