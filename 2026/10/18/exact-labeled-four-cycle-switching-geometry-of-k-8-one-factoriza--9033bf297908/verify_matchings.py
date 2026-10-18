#!/usr/bin/env python3
"""Exhaustive enumeration of fixed-vertex 1-factorization four-cycle moves.
Use: python verify_matchings.py [output_dir]. Python standard library only.
"""
from itertools import combinations
from collections import Counter
import hashlib, json, os, sys

N=8
EDGES=list(combinations(range(N),2))
EI={e:i for i,e in enumerate(EDGES)}
FULL=(1<<len(EDGES))-1

def perfect_matchings(vertices):
    if not vertices:
        yield ()
        return
    u=vertices[0]
    for v in vertices[1:]:
        others=tuple(w for w in vertices[1:] if w!=v)
        for tail in perfect_matchings(others):
            yield ((u,v),)+tail

masks=[]
for M in perfect_matchings(tuple(range(N))):
    masks.append(sum(1<<EI[e] for e in M))
assert len(masks)==105 and len(set(masks))==105
byedge={i:[m for m in masks if m>>i & 1] for i in range(28)}

factorizations=[]
def extend(used,matched):
    if used==FULL:
        assert len(matched)==7
        factorizations.append(tuple(sorted(matched)))
        return
    free=FULL^used
    i=(free&-free).bit_length()-1
    for m in byedge[i]:
        if not used&m:
            extend(used|m,matched+[m])
extend(0,[])
factorizations.sort()
assert len(factorizations)==6240 and len(set(factorizations))==6240
index={f:i for i,f in enumerate(factorizations)}
maskset=set(masks)

adj=[set() for _ in factorizations]
for i,ff in enumerate(factorizations):
    for a,b in combinations(ff,2):
        two=a|b
        rem=set(range(N)); parts=[]
        while rem:
            root=min(rem)
            component={root}
            q=[root]
            for x in q:
                for y in range(N):
                    if y!=x and (two>>EI[(min(x,y),max(x,y))]&1) and y not in component:
                        component.add(y);q.append(y)
            rem-=component
            parts.append(component)
        if sorted(map(len,parts))!=[4,4]:
            continue
        block=parts[0]
        sub=sum(1<<EI[e] for e in combinations(sorted(block),2) if two>>EI[e]&1)
        aa=a^sub; bb=b^sub
        assert aa in maskset and bb in maskset
        nxt=tuple(sorted((set(ff)-{a,b})|{aa,bb}))
        j=index[nxt]
        assert i!=j
        adj[i].add(j)
assert all(i in adj[j] for i,A in enumerate(adj) for j in A)

deg=Counter(map(len,adj))
seen=set();components=[]
for s in range(len(adj)):
    if s in seen:continue
    q=[s];seen.add(s)
    for u in q:
        for v in adj[u]:
            if v not in seen:
                seen.add(v);q.append(v)
    components.append(q)
comps=Counter(map(len,components))
assert comps=={1:960,5280:1}
giant=next(c for c in components if len(c)>1)
ecc=Counter()
for s in giant:
    d={s:0};q=[s]
    for u in q:
        for v in adj[u]:
            if v not in d:
                d[v]=d[u]+1;q.append(v)
    assert len(d)==len(giant)
    ecc[max(d.values())]+=1
assert ecc=={9:30,10:3570,11:1680}

state_lines=[' '.join(f'{m:07x}' for m in ff)+'\n' for ff in factorizations]
state_bytes=''.join(state_lines).encode('ascii')
lines=[f'{i} {j}\n' for i,A in enumerate(adj) for j in sorted(A) if j>i]
assert len(lines)==17640
payload=''.join(lines).encode('ascii')
summary={'vertices':len(factorizations),'perfect_matchings':len(masks),
         'edges':len(lines),'degree_distribution':dict(sorted(deg.items())),
         'component_sizes':dict(sorted(comps.items())),
         'eccentricities_nontrivial':dict(sorted(ecc.items())),
         'radius_nontrivial':min(ecc),'diameter_nontrivial':max(ecc),
         'ordered_edge_list_sha256':hashlib.sha256(payload).hexdigest(),
         'ordered_states_sha256':hashlib.sha256(state_bytes).hexdigest()}
print(json.dumps(summary,sort_keys=True))
if len(sys.argv)>1:
    dest=sys.argv[1]
    os.makedirs(dest,exist_ok=True)
    with open(os.path.join(dest,'fourcycle_edges.txt'),'wb') as out:out.write(payload)
    with open(os.path.join(dest,'factorization_states.txt'),'wb') as out:out.write(state_bytes)
    with open(os.path.join(dest,'enumeration_summary.json'),'w') as out:json.dump(summary,out,indent=2,sort_keys=True);out.write('\n')
