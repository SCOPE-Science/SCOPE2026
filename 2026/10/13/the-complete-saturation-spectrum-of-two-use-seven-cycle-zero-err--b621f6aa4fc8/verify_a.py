#!/usr/bin/env python3
"""Enumerate maximal two-use zero-error codes for the 7-cycle channel."""
from collections import Counter, defaultdict
import hashlib

N=7
vertices=list(range(N*N))
def apart(x,y):
    d=(x-y)%N
    return d not in (0,1,N-1)

# G is the nonconfusability graph, and its maximal cliques are terminal codebooks.
adj=[0]*(N*N)
for v in vertices:
    i,j=divmod(v,N)
    for w in vertices:
        if v==w: continue
        k,l=divmod(w,N)
        if apart(i,k) or apart(j,l): adj[v]|=1<<w

masks=[]
def maximal_cliques(R,P,X):
    if not (P|X):
        masks.append(R)
        return
    px=P|X
    pivot=max((u for u in vertices if px>>u&1),key=lambda u:(P&adj[u]).bit_count())
    choices=P&~adj[pivot]
    while choices:
        bit=choices&-choices; v=bit.bit_length()-1
        maximal_cliques(R|bit,P&adj[v],X&adj[v])
        P^=bit; X|=bit; choices^=bit
maximal_cliques(0,(1<<(N*N))-1,0)
assert len(masks)==len(set(masks))
ms=set(masks)
counter=Counter(m.bit_count() for m in ms)
print('spectrum',sorted(counter.items()),'total',len(ms))
# All elements pairwise separated, but no further symbol can be added.
for m in ms:
    for v in vertices:
        if m>>v&1: assert (m&~adj[v])==1<<v  # v alone is incompatible with itself
        else: assert m&~adj[v]

def moved(mask,which):
    out=0
    for v in vertices:
        if mask>>v&1:
            x,y=divmod(v,N)
            if which==0:x=(x+1)%N
            elif which==1:y=(y+1)%N
            elif which==2:x=(-x)%N
            elif which==3:y=(-y)%N
            else:x,y=y,x
            out|=1<<(x*N+y)
    return out
rest=set(ms); orbit_size=Counter(); orbit_count=Counter(); representatives=[]
while rest:
    root=min(rest)
    orb={root};pending=[root]
    for m in pending:
        for g in range(5):
            z=moved(m,g)
            if z not in orb:
                orb.add(z);pending.append(z)
    assert orb<=rest
    rest-=orb
    k=root.bit_count()
    orbit_count[k]+=1; orbit_size[(k,len(orb))]+=1
    representatives.append((k,len(orb),root))
print('orbit_count',sorted(orbit_count.items()))
print('orbit_sizes',sorted(orbit_size.items()))
print('representatives_minimal',[(k,z,hex(m)) for k,z,m in representatives if k==7])
canonical=''.join(f'{m:013x}\n' for m in sorted(ms)).encode('ascii')
print('canonical_sha256',hashlib.sha256(canonical).hexdigest())
if __name__=='__main__':
    with open('catalogue.txt','wb') as f:
        f.write(canonical)
    print('all checks passed')
