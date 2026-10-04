#!/usr/bin/env python3
import itertools
from collections import Counter

perms=list(itertools.permutations(range(1,6)))
idx={p:i for i,p in enumerate(perms)}
n=len(perms)

def dist(a,b):
    return max(abs(x-y) for x,y in zip(a,b))

adj=[0]*n
edges=0
for i in range(n):
    for j in range(i+1,n):
        if dist(perms[i],perms[j])>=3:
            adj[i]|=1<<j
            adj[j]|=1<<i
            edges+=1

maximum=0
maxima=[]
maximal_count=0

def bk(R,P,X):
    global maximum,maxima,maximal_count
    if P==0 and X==0:
        maximal_count+=1
        s=R.bit_count()
        if s>maximum:
            maximum=s
            maxima=[R]
        elif s==maximum:
            maxima.append(R)
        return
    U=P|X
    if U:
        u=max((i for i in range(n) if (U>>i)&1), key=lambda i:(P&adj[i]).bit_count())
        cand=P & ~adj[u]
    else:
        cand=P
    while cand:
        bit=cand & -cand
        v=bit.bit_length()-1
        bk(R|bit, P&adj[v], X&adj[v])
        P &= ~bit
        X |= bit
        cand &= ~bit

bk(0,(1<<n)-1,0)
assert maximum==10
assert len(maxima)==192
maxsets={frozenset(i for i in range(n) if (m>>i)&1) for m in maxima}
assert len(maxsets)==192

coords=list(itertools.permutations(range(5)))
def transform(p,c,rev):
    q=tuple(p[c[i]] for i in range(5))
    if rev:
        q=tuple(6-x for x in q)
    return q

seen=set(); orbit_data=[]
for C in maxsets:
    if C in seen:
        continue
    orb=set()
    for c in coords:
        for rev in (0,1):
            D=frozenset(idx[transform(perms[i],c,rev)] for i in C)
            assert D in maxsets
            orb.add(D)
    seen |= orb
    rep=next(iter(orb))
    L=sorted(rep)
    spectrum=Counter(dist(perms[L[a]],perms[L[b]]) for a in range(10) for b in range(a+1,10))
    orbit_data.append((len(orb),240//len(orb),dict(sorted(spectrum.items()))))

orbit_data.sort()
assert orbit_data==[
    (24,10,{3:30,4:15}),
    (48,5,{3:25,4:20}),
    (120,2,{3:28,4:17}),
]
assert len(seen)==192

print('VERIFY_OK maximum=10 labeled_maxima=192 orbits=3 orbit_sizes=24,48,120 stabilizers=10,5,2 maximal_cliques=%d edges=%d' % (maximal_count,edges))
