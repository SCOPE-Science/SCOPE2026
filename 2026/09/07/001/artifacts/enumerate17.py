"""Enumerate ALL max (17) families containing 1234; classify up to S8; test ball property.
Self-checks: solver must FIND 17s (ball) here; verifier re-checks each."""
import itertools, time, sys
ALL=list(itertools.combinations(range(1,9),4))
N=70
idx={A:i for i,A in enumerate(ALL)}
inter=lambda a,b: len(set(a)&set(b))
ADJ=[0]*N
for i in range(N):
    Ai=set(ALL[i]); m=0
    for j in range(N):
        if j!=i and len(Ai&set(ALL[j]))==1: m|=1<<j
    ADJ[i]=m
v0=idx[(1,2,3,4)]
P=[j for j in range(N) if j!=v0 and not (ADJ[v0]>>j & 1)]
pidx={v:k for k,v in enumerate(P)}
M=len(P)
adj=[0]*M
for k,v in enumerate(P):
    m=0
    for w in P:
        if (ADJ[v]>>w)&1: m|=1<<pidx[w]
    adj[k]=m
def popcount(x): return bin(x).count("1")
def cover_ub(mask):
    n=0
    while mask:
        lsb=mask&-mask; v=lsb.bit_length()-1
        C=1<<v
        cand=adj[v]&mask&~C
        while cand:
            l=cand&-cand; u=l.bit_length()-1
            C|=1<<u
            cand&=adj[u]; cand&=mask
        mask&=~C; n+=1
    return n
sols=[]; nodes=[0]; CAP=20000
t0=time.time()
def search(mask, cur, target, chosen):
    nodes[0]+=1
    if len(sols)>=CAP: return True
    if cur+popcount(mask)<target: return False
    while True:
        m=mask; iso=-1
        while m:
            l=m&-m; v=l.bit_length()-1; m^=l
            if (adj[v]&mask)==0: iso=v; break
        if iso<0: break
        mask^=(1<<iso); cur+=1; chosen=chosen+(iso,)
        if cur>=target:
            sols.append(chosen); return False
    if mask==0: return False
    if cur+popcount(mask)<target: return False
    if cur+cover_ub(mask)<target: return False
    bestv=-1; bestd=-1; m=mask
    while m:
        l=m&-m; v=l.bit_length()-1; m^=l
        d=popcount(adj[v]&mask)
        if d>bestd: bestd=d; bestv=v
    v=bestv
    search(mask&~(adj[v]|(1<<v)), cur+1, target, chosen+(v,))
    search(mask&~(1<<v), cur, target, chosen)
    return False
full=(1<<M)-1
search(full,0,16,())
print(f"found {len(sols)} 17-families containing 1234 (nodes={nodes[0]}, {time.time()-t0:.1f}s), cap={CAP}")
# verify each
for s in sols:
    F=[v0]+[P[k] for k in s]
    assert len(F)==17
    for a in range(17):
        for b in range(a+1,17):
            assert not (ADJ[F[a]]>>F[b]&1), "solution invalid!"
print("all solutions verified 1-free")
# canonicalize under S8
import math
perms=list(itertools.permutations(range(1,9)))
print("perms:",len(perms))
def canon(F):
    best=None
    sets=[set(ALL[v]) for v in F]
    for p in perms:
        img=tuple(sorted(tuple(sorted(p[x-1] for x in A)) for A in sets))
        if best is None or img<best: best=img
    return best
from collections import Counter
c=Counter()
for s in sols:
    F=[v0]+[P[k] for k in s]
    c[canon(F)]+=1
print("distinct S8-orbits among 17-families containing 1234:",len(c))
for k,v in c.items(): print(" orbit size:",v, "example:",k[:4],"...")
# ball test: F == {A:|A cap S|>=3} for some 4-set S?
def is_ball(F):
    S=set(F)
    for C in ALL:
        CC=set(C)
        if set(A for A in ALL if len(set(A)&CC)>=3)==set(ALL[v] for v in F):
            return C
    return None
for k,v in c.items():
    Fidx=[idx[A] for A in k]
    print("orbit count",v,"ball-center:",is_ball(Fidx))
