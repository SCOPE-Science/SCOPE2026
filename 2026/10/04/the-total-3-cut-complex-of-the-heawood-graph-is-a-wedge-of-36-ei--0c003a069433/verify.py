#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict, deque

N=14
POINTS=range(7)
LINES=range(7,14)
# Heawood graph as Levi graph of the Fano plane: line i contains i,i+1,i+3 mod 7.
EDGES=set()
for i in range(7):
    for p in (i,(i+1)%7,(i+3)%7):
        EDGES.add(tuple(sorted((p,7+i))))
assert len(EDGES)==21
assert all(sum(v in e for e in EDGES)==3 for v in range(N))

def mask(xs):
    z=0
    for x in xs: z|=1<<x
    return z

ind3=[]
for c in combinations(range(N),3):
    if all(tuple(sorted(e)) not in EDGES for e in combinations(c,2)):
        ind3.append(mask(c))
assert len(ind3)==154
FULL=(1<<N)-1
faces=[]
for s in range(1<<N):
    comp=FULL^s
    if any((t & comp)==t for t in ind3):
        faces.append(s)
F=set(faces)
by=defaultdict(list)
for s in faces: by[s.bit_count()-1].append(s)
expected=[14,91,364,1001,2002,3003,3432,3003,2002,833,154]
assert [len(by[d]) for d in range(11)]==expected
assert len(faces)==1+sum(expected)==15900

# Sequential element matching with vertex order 0,1,...,13.
unmatched=set(faces)
pairs=[]
for v in range(N):
    b=1<<v
    for s in sorted(tuple(unmatched), key=lambda x:(x.bit_count(),x)):
        if s not in unmatched or s&b: continue
        t=s|b
        if t in unmatched and t in F:
            unmatched.remove(s); unmatched.remove(t); pairs.append((s,t))
assert len(pairs)==7932
assert len(unmatched)==36
assert Counter(s.bit_count()-1 for s in unmatched)==Counter({8:36})
assert 0 not in unmatched

# Direct acyclicity check on the complete Hasse diagram: unmatched cover edges point down,
# matched edges are reversed. A topological sort must visit every face.
pairset=set(pairs)
adj={s:[] for s in faces}; indeg={s:0 for s in faces}; covers=0
for hi in faces:
    if hi==0: continue
    t=hi
    while t:
        b=t & -t
        lo=hi^b
        if lo in F:
            covers += 1
            if (lo,hi) in pairset: u,v=lo,hi
            else: u,v=hi,lo
            adj[u].append(v); indeg[v]+=1
        t-=b
q=deque([s for s in faces if indeg[s]==0]); seen=0
while q:
    u=q.popleft(); seen+=1
    for v in adj[u]:
        indeg[v]-=1
        if indeg[v]==0:q.append(v)
assert seen==len(faces)
assert covers==109410

# Independent mod-2 chain-rank check.
def rank2(cols):
    piv={}; r=0
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x; r+=1; break
    return r
ranks={0:1}
for d in range(1,11):
    ridx={s:i for i,s in enumerate(by[d-1])}
    cols=[]
    for s in by[d]:
        z=0; t=s
        while t:
            b=t&-t; z ^= 1<<ridx[s^b]; t-=b
        cols.append(z)
    ranks[d]=rank2(cols)
expected_ranks={0:1,1:13,2:78,3:286,4:715,5:1287,6:1716,7:1716,8:1287,9:679,10:154}
assert ranks==expected_ranks
betti={d:len(by[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(11)}
assert {d:b for d,b in betti.items() if b}=={8:36}
# Reduced Euler characteristic is +36 for an even-dimensional wedge of 36 spheres.
red_euler=sum(((-1)**d)*len(by[d]) for d in range(11))-1
assert red_euler==36
print('HEAWOOD_TOTAL3_VERIFY_OK')
print('independent_triples=154 faces=15900 hasse_covers=109410 matching_pairs=7932 critical_8=36')
print('f_vector='+repr(expected))
print('boundary_ranks_mod2='+repr([ranks[d] for d in range(11)]))
