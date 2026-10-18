#!/usr/bin/env python3
"""Independent direct edge-monitoring verification on GP(10,3), standard library only."""
from itertools import combinations
from collections import Counter,deque

V=range(20)
E=set()
for i in range(10):
    E.add(tuple(sorted((i,(i+1)%10))))
    E.add(tuple(sorted((i,10+i))))
    E.add(tuple(sorted((10+i,10+(i+3)%10))))
E=tuple(sorted(E)); assert len(E)==30
N=[set() for _ in V]; Inc=[set() for _ in V]
for e,(u,v) in enumerate(E):
    N[u].add(v);N[v].add(u);Inc[u].add(e);Inc[v].add(e)
assert all(len(n)==3 for n in N)

def monitored(start):
    observed=set(start)
    measured={i for i,(u,v) in enumerate(E) if u in start or v in start}
    while True:
        newobs=observed | {w for i in measured for w in E[i]}
        newedges=measured|{i for i,(u,v) in enumerate(E) if u in newobs and v in newobs}
        for v in V:
            remaining=Inc[v]-measured
            if len(remaining)==1:newedges |= remaining
        if newobs==observed and newedges==measured:break
        observed,measured=newobs,newedges
    return len(observed)==20 and len(measured)==30

for k in (0,1,2):assert all(not monitored(s) for s in combinations(V,k))
mins={frozenset(s) for s in combinations(V,3) if monitored(s)}
assert len(mins)==240

# Explicit checked graph isomorphism from GP(10,3) to the 2/3-subset
# incidence model of the Desargues graph; no graph-isomorphism package.
labels=(3,7,6,14,12,28,24,25,17,19,11,5,22,10,13,20,26,9,21,18)
assert len(set(labels))==20
assert set(labels)=={a for a in range(32) if a.bit_count() in (2,3)}
assert all(((labels[u]&labels[v])==labels[u] if labels[u].bit_count()==2 else (labels[u]&labels[v])==labels[v]) for u,v in E)

D=[]
for root in V:
    d={root:0};q=deque([root])
    while q:
        x=q.popleft()
        for y in N[x]:
            if y not in d:d[y]=d[x]+1;q.append(y)
    assert len(d)==20;D.append(d)

def sig(s):return tuple(sorted(D[a][b] for a,b in combinations(sorted(s),2)))
assert Counter(sig(s) for s in mins)==Counter({(2,3,5):120,(3,3,4):120})

def graph(sliding):
    R={s:set() for s in mins}
    for s in mins:
        for u in s:
            for v in V:
                if v not in s and (not sliding or v in N[u]):
                    nxt=(s-{u})|{v}
                    if nxt in mins:R[s].add(nxt)
    assert all(s in R[t] for s in R for t in R[s])
    return R

def distances(R,root):
    d={root:0};q=deque([root])
    while q:
        x=q.popleft()
        for y in R[x]:
            if y not in d:d[y]=d[x]+1;q.append(y)
    assert len(d)==240
    return d

for label,is_slide in [('TJ',False),('TS',True)]:
    R=graph(is_slide)
    assert Counter(len(z) for z in R.values())==(Counter({4:240}) if is_slide else Counter({13:120,17:120}))
    assert sum(len(z) for z in R.values())//2==(480 if is_slide else 1800)
    ecc=Counter();type_ecc={}
    for s in R:
        e=max(distances(R,s).values())
        ecc[e]+=1
        type_ecc.setdefault(sig(s),set()).add(e)
    assert type_ecc==({(2,3,5):{7},(3,3,4):{8}} if is_slide else {(2,3,5):{4},(3,3,4):{4}})
    print(label,'edges',sum(map(len,R.values()))//2,'eccentricities',sorted(ecc.items()),'distance profiles',sorted((k,sorted(v)) for k,v in type_ecc.items()))
print('INDEPENDENT_VERIFY_OK')
