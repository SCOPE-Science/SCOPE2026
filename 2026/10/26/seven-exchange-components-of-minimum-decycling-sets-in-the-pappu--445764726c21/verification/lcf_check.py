#!/usr/bin/env python3
"""Complete finite certificate for induced-tree feedback sets in the Pappus graph.

Python >=3.9, standard library only. Label convention: LCF [5,7,-7,7,-7,-5]^3.
"""
import collections
import itertools
import json
import sys
from collections import deque

N = 18
LCF = (5, 7, -7, 7, -7, -5) * 3
GEN = (
    (17,0,5,4,15,16,9,8,1,2,3,10,11,6,7,14,13,12),
    (0,1,8,7,6,5,4,3,2,13,14,15,16,9,10,11,12,17),
)
EDGES = sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)} |
               {tuple(sorted((i,(i+d)%N))) for i,d in enumerate(LCF)})
assert len(EDGES)==27

def forest(s):
    """Check whether deleting bitset s leaves a forest using exact DSU."""
    parent=list(range(N))
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for u,v in EDGES:
        if not ((s>>u)&1 or (s>>v)&1):
            a,b=find(u),find(v)
            if a==b:
                return False
            parent[a]=b
    return True

# Bound: every size-k FVS in a cubic 18-vertex 27-edge graph
# has 2k >= 27-18+1=10; hence enumerate all k=5 only.
SOL=sorted(sum(1<<v for v in c) for c in itertools.combinations(range(N),5)
           if forest(sum(1<<v for v in c)))
assert len(SOL)==252
IDX={x:i for i,x in enumerate(SOL)}
assert all(not any((s>>u)&1 and (s>>v)&1 for u,v in EDGES) for s in SOL)
ADJ=[set() for _ in SOL]
for i,s in enumerate(SOL):
    for v in range(N):
        if not (s>>v)&1:
            continue
        for w in range(N):
            if (s>>w)&1:
                continue
            t=s^(1<<v)^(1<<w)
            j=IDX.get(t)
            if j is not None:
                ADJ[i].add(j)
assert all(i in ADJ[j] for i,row in enumerate(ADJ) for j in row)
PAIRS=sorted((i,j) for i,row in enumerate(ADJ) for j in row if i<j)
assert len(PAIRS)==630

def bfs(root):
    depth={root:0};queue=deque([root])
    while queue:
        i=queue.popleft()
        for j in ADJ[i]:
            if j not in depth:
                depth[j]=depth[i]+1;queue.append(j)
    return depth

# Do not rely on graph-library component routines.
UNSEEN=set(range(len(SOL))); COMPONENTS=[]
while UNSEEN:
    p=min(UNSEEN);c=set(bfs(p));COMPONENTS.append(c);UNSEEN-=c
COMPONENTS.sort(key=lambda c:(-len(c),min(c)))
assert sorted(len(c) for c in COMPONENTS)==[6]*6+[216]
assert all(len(ADJ[i])==5 for i in range(252))
assert all(len(PAIRS)==sum(len(r) for r in ADJ)//2 for _ in [0])
DIST={i:bfs(i) for i in range(len(SOL))}
ECC={i:max(DIST[i].values()) for i in DIST}
assert collections.Counter(ECC.values())=={1:36,6:108,7:108}
assert all(len(DIST[i])==216 for i in COMPONENTS[0])
assert all(len(DIST[i])==6 for c in COMPONENTS[1:] for i in c)

# Generated subgroup witnesses symmetry between states in each distance class.
edge_set=set(EDGES)
for gen in GEN:
    assert sorted(gen)==list(range(N))
    assert {tuple(sorted((gen[u],gen[v]))) for u,v in EDGES}==edge_set
idp=tuple(range(N));gr={idp};queue=[idp]
while queue:
    a=queue.pop()
    for b in GEN:
        p=tuple(a[b[i]] for i in range(N))
        if p not in gr:
            gr.add(p);queue.append(p)
assert len(gr)==216
orbits=[];unseen=set(SOL)
while unseen:
    seed=min(unseen)
    orb={sum(1<<p[v] for v in range(N) if (seed>>v)&1) for p in gr}
    orbits.append(orb);unseen-=orb
orbits.sort(key=lambda c:(len(c),ECC[IDX[min(c)]]))
assert [(len(o),ECC[IDX[min(o)]]) for o in orbits]==[(36,1),(108,6),(108,7)]
DIST_PROFILE={}
for o in orbits:
    i=IDX[min(o)]
    profile=tuple(collections.Counter(DIST[i].values()).get(k,0) for k in range(8))
    assert all(tuple(collections.Counter(DIST[IDX[s]].values()).get(k,0) for k in range(8))==profile for s in o)
    DIST_PROFILE[str(ECC[i])]=list(profile)
assert DIST_PROFILE=={'1':[1,5,0,0,0,0,0,0],
    '6':[1,5,14,37,56,71,32,0], '7':[1,5,14,36,52,69,37,2]}

out={
 'graph':'Pappus LCF [5,7,-7,7,-7,-5]^3',
 'order':18,'size':27,'minimum_fvs_size':5,'minimum_fvs_count':len(SOL),
 'exchange_edges':len(PAIRS),'exchange_degrees':{'5':252},
 'component_orders':[216,6,6,6,6,6,6],
 'component_edge_counts':[540,15,15,15,15,15,15],
 'large_component_radius':6,'large_component_diameter':7,
 'symmetry_subgroup_order':len(gr),
 'orbit_size_by_eccentricity':{'1':36,'6':108,'7':108},
 'distance_profiles':DIST_PROFILE,
 'diametral_unordered_pairs':108,
}
if '--certificate' in sys.argv:
    cert={'n':N,'edges':EDGES,'minimum_fvs_masks':SOL,'exchange_index_pairs':[list(p) for p in PAIRS],
          'group_generators':[list(g) for g in GEN], 'summary':out}
    p=sys.argv[sys.argv.index('--certificate')+1]
    with open(p,'w',encoding='utf-8') as f:json.dump(cert,f,sort_keys=True,separators=(',',':'));f.write('\n')
if '--check-certificate' in sys.argv:
    p=sys.argv[sys.argv.index('--check-certificate')+1]
    with open(p,encoding='utf-8') as f:cert=json.load(f)
    assert cert['n']==18 and cert['edges']==[list(e) for e in EDGES]
    assert cert['minimum_fvs_masks']==SOL
    assert cert['exchange_index_pairs']==[list(p) for p in PAIRS]
    assert cert['group_generators']==[list(g) for g in GEN]
    assert cert['summary']==out
print(json.dumps(out,indent=2,sort_keys=True))
