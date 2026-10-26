#!/usr/bin/env python3
"""Independent incidence-model check for the Pappus feedback-set exchange graph.

Python >=3.9, standard library only. Points are 0..8; lines are 9..17.
"""
import collections,itertools,json,sys
from collections import deque
N=18
LINES=((0,1,2),(3,4,5),(0,4,6),(3,1,6),(0,5,7),
       (3,2,7),(1,5,8),(4,2,8),(6,7,8))
MAP=(0,2,8,10,6,12,4,16,14,1,11,5,3,17,9,13,7,15)
assert sorted(MAP)==list(range(N))
links=[set() for _ in range(N)]
for j,line in enumerate(LINES):
    for v in line:
        links[v].add(9+j);links[9+j].add(v)
assert all(len(v)==3 for v in links)
assert sum(len(v) for v in links)==54

# Verify the explicit isomorphism to the independent LCF description.
images={tuple(sorted((MAP[u],MAP[v]))) for u in range(N) for v in links[u] if u<v}
lcf=(5,7,-7,7,-7,-5)*3
lcfe={tuple(sorted((i,(i+1)%N))) for i in range(N)} | {tuple(sorted((i,(i+d)%N))) for i,d in enumerate(lcf)}
assert images==lcfe

def induced_acyclic(deleted):
    """Independent leaf-peeling test: a graph is a forest iff its 2-core is empty."""
    remains=set(range(N))-set(deleted)
    degree={v:len(links[v]&remains) for v in remains}
    queue=deque(v for v in remains if degree[v]<=1)
    removed=set()
    while queue:
        v=queue.popleft()
        if v in removed:continue
        removed.add(v)
        for w in links[v]:
            if w in degree and w not in removed:
                degree[w]-=1
                if degree[w]==1:queue.append(w)
    return len(removed)==len(remains)

# The incidence model is examined independently of the LCF model.
found=[c for c in itertools.combinations(range(N),5) if induced_acyclic(c)]
assert len(found)==252
sol=sorted(sum(1<<MAP[v] for v in c) for c in found)
assert len(set(sol))==252
pairs=[]
for a in range(len(found)):
    sa=set(found[a]);ma=sum(1<<MAP[v] for v in found[a])
    for b in range(a+1,len(found)):
        sb=set(found[b]);mb=sum(1<<MAP[v] for v in found[b])
        if len(sa&sb)==4:
            i=sol.index(ma);j=sol.index(mb)
            pairs.append((min(i,j),max(i,j)))
pairs=sorted(pairs)
assert len(pairs)==630 and len(set(pairs))==630
adj=[set() for _ in sol]
for a,b in pairs:adj[a].add(b);adj[b].add(a)
assert all(len(a)==5 for a in adj)

def bfs(i):
    dd={i:0};q=deque([i])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in dd:
                dd[w]=dd[v]+1;q.append(w)
    return dd

components=[];unseen=set(range(len(sol)))
while unseen:
    d=bfs(min(unseen));s=set(d);components.append(s);unseen-=s
components.sort(key=lambda a:(-len(a),min(a)))
assert [len(c) for c in components]==[216,6,6,6,6,6,6]
assert [sum(len(adj[v]&c) for v in c)//2 for c in components]==[540]+[15]*6
profiles=collections.defaultdict(set)
ecc={}
for i in range(len(sol)):
    ds=bfs(i)
    k=max(ds.values());ecc[i]=k
    profiles[str(k)].add(tuple(collections.Counter(ds.values()).get(j,0) for j in range(8)))
assert all(len(p)==1 for p in profiles.values())
assert collections.Counter(ecc.values())=={1:36,6:108,7:108}
assert {k:list(next(iter(v))) for k,v in profiles.items()}=={
'1':[1,5,0,0,0,0,0,0],
'6':[1,5,14,37,56,71,32,0],
'7':[1,5,14,36,52,69,37,2]}
# Build automorphism subgroup directly from the explicit LCF permutations.
gens=((17,0,5,4,15,16,9,8,1,2,3,10,11,6,7,14,13,12),
      (0,1,8,7,6,5,4,3,2,13,14,15,16,9,10,11,12,17))
for p in gens:
    assert sorted(p)==list(range(N))
    assert {tuple(sorted((p[u],p[v]))) for u,v in images}==images
start=tuple(range(N));group={start};q=[start]
while q:
    a=q.pop()
    for b in gens:
        c=tuple(a[b[i]] for i in range(N))
        if c not in group:group.add(c);q.append(c)
assert len(group)==216
unseen=set(sol);orbs=[]
while unseen:
    s=min(unseen)
    orb={sum(1<<p[i] for i in range(N) if s>>i&1) for p in group}
    unseen-=orb;orbs.append(orb)
assert sorted((len(o),ecc[sol.index(min(o))]) for o in orbs)==[(36,1),(108,6),(108,7)]

out={
 'graph':'Pappus LCF [5,7,-7,7,-7,-5]^3',
 'order':18,'size':27,'minimum_fvs_size':5,'minimum_fvs_count':len(sol),
 'exchange_edges':len(pairs),'exchange_degrees':{'5':252},
 'component_orders':[216,6,6,6,6,6,6],
 'component_edge_counts':[540,15,15,15,15,15,15],
 'large_component_radius':6,'large_component_diameter':7,
 'symmetry_subgroup_order':len(group),
 'orbit_size_by_eccentricity':{'1':36,'6':108,'7':108},
 'distance_profiles':{k:list(next(iter(v))) for k,v in sorted(profiles.items())},
 'diametral_unordered_pairs':108,
}
if '--check-certificate' in sys.argv:
    with open(sys.argv[sys.argv.index('--check-certificate')+1],encoding='utf-8') as f:cert=json.load(f)
    assert cert['summary']==out
    assert cert['minimum_fvs_masks']==sol
    assert cert['exchange_index_pairs']==[list(p) for p in pairs]
    assert cert['group_generators']==[list(g) for g in gens]
print(json.dumps(out,indent=2,sort_keys=True))
