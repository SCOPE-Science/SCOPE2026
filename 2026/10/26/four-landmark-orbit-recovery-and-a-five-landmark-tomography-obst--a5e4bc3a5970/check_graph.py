#!/usr/bin/env python3
"""Direct small-graph check of the four-landmark orbit-recovery implication."""
from collections import Counter
from itertools import combinations,product
from random import Random
from math import factorial

Q=4

def signature(anchors,x):
    # For each coordinate the ordered marker-equality partition and selected status.
    local=[]
    for i in range(len(x)):
        partition=[]; table={}
        for a in anchors:
            sym=a[i]
            if sym not in table:table[sym]=len(table)
            partition.append(table[sym])
        status=table.get(x[i],len(table))
        local.append((tuple(partition),status))
    return tuple(sorted(Counter(local).items()))

def check(d,r,anchors,vs,neis):
    source={v:i for i,v in enumerate(vs)}
    colors=[1+anchors.index(x) if x in anchors else 0 for x in vs]
    for t in range(d+1):
        z=[(colors[i],tuple(sorted(Counter(colors[j] for j in neis[i]).items()))) for i in range(len(vs))]
        labs={w:j for j,w in enumerate(sorted(set(z)))}
        colors=[labs[w] for w in z]
    orbit=[signature(anchors,x) for x in vs]
    groups={}
    for x,y in zip(orbit,colors):
        if x in groups:assert groups[x]==y
        else:groups[x]=y
    assert len(groups)==len(set(colors))
    counts=Counter(orbit)
    for profile,actual in counts.items():
        bypat={}
        for (pi,status),ct in profile:
            if pi not in bypat:bypat[pi]={}
            bypat[pi][status]=ct
        expected=1
        for pi,st_counts in bypat.items():
            k=max(pi)+1
            n=sum(st_counts.values())
            val=factorial(n)
            for ct in st_counts.values():val//=factorial(ct)
            if k<4:val*= (4-k)**st_counts.get(k,0)
            expected*=val
        assert actual==expected

rng=Random(70033)
count=0
for d in (1,2,3,4):
    vs=list(product(range(Q),repeat=d))
    ids={v:i for i,v in enumerate(vs)}
    neis=[]
    for v in vs:
        neis.append([ids[v[:i]+(a,)+v[i+1:]] for i in range(d) for a in range(Q) if a!=v[i]])
    for r in range(1,5):
        if len(vs)<r: continue
        if d<=2:
            cases=list(combinations(vs,r))
        else:
            cases=[tuple(rng.sample(vs,r)) for _ in range(110 if d==3 else 40)]
        for anchors in cases:
            check(d,r,anchors,vs,neis)
            count+=1
print('CASES',count,'ALL_TESTS_PASS')
