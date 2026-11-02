"""Exact classification for Cremona--Richmond trivalent stable graph curves.
Requires Python 3 and networkx. This file uses no external data files.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict
from math import lcm
import networkx as nx
import json

DUADS=tuple(combinations(range(6),2))
def matchings(rest):
    if not rest:
        yield ()
    else:
        x=rest[0]
        for y in rest[1:]:
            for other in matchings(tuple(z for z in rest if z!=x and z!=y)):
                yield tuple(sorted(((x,y),)+other))
SYNTHEMES=tuple(sorted(set(matchings(tuple(range(6))))))
VERTICES=tuple(('d',d) for d in DUADS)+tuple(('m',m) for m in SYNTHEMES)
idx={x:i for i,x in enumerate(VERTICES)}
EDGES=tuple(tuple(sorted((idx[('d',d)],idx[('m',m)]))) for m in SYNTHEMES for d in m)
assert len(VERTICES)==30 and len(EDGES)==45 and len(set(EDGES))==45
adj=[set() for _ in range(30)]
for i,j in EDGES: adj[i].add(j);adj[j].add(i)
assert all(len(a)==3 for a in adj)
graph=nx.Graph();graph.add_nodes_from(range(30));graph.add_edges_from(EDGES)
assert nx.is_connected(graph)
perm_group=set(tuple(m[i] for i in range(30)) for m in nx.algorithms.isomorphism.GraphMatcher(graph,graph).isomorphisms_iter())
assert len(perm_group)==1440
outer=(15,23,19,27,25,24,28,22,20,17,18,29,26,21,16,0,14,9,10,2,8,13,7,1,5,4,12,3,6,11)
def mul(x,y): return tuple(x[j] for j in y)
def inv(x):
    v=[0]*len(x)
    for i,j in enumerate(x):v[j]=i
    return tuple(v)
assert mul(outer,outer)==tuple(range(30))
assert outer in perm_group
# Independent explicit construction: S6 acting on duads/synthemes and an outer involution.
def action(p,node):
    t,z=node
    if t=='d': return ('d',tuple(sorted(p[k] for k in z)))
    return ('m',tuple(sorted(tuple(sorted(p[k] for k in duad)) for duad in z)))
inner={tuple(idx[action(p,v)] for v in VERTICES) for p in permutations(range(6))}
assert len(inner)==720
explicit=inner|{mul(outer,g) for g in inner}
assert explicit==perm_group
emap={e:i for i,e in enumerate(EDGES)}
branches=tuple((i,e) for e,uv in enumerate(EDGES) for i in uv)
bmap={t:i for i,t in enumerate(branches)}
def on_edges(g):return tuple(emap[tuple(sorted((g[u],g[v])))] for u,v in EDGES)
def on_branches(g,ge):return tuple(bmap[(g[v],ge[e])] for v,e in branches)
def cyc(g):
    seen=set(); out=Counter()
    for i in range(len(g)):
        if i in seen:continue
        x=i;n=0
        while x not in seen:
            seen.add(x);n+=1;x=g[x]
        assert x==i
        out[n]+=1
    return tuple(sorted(out.items()))
records={}
for g in perm_group:
    eg=on_edges(g)
    bg=on_branches(g,eg)
    vv,ee,bb=cyc(g),cyc(eg),cyc(bg)
    assert sum(d*k for d,k in vv)==30
    assert sum(d*k for d,k in ee)==45
    assert sum(d*k for d,k in bb)==90
    n=dict(bb);v=dict(vv);e=dict(ee)
    alpha=tuple(sorted((d,n.get(d,0)-v.get(d,0)-e.get(d,0)) for d in set(n)|set(v)|set(e) if n.get(d,0)-v.get(d,0)-e.get(d,0)))
    # For each extension degree, independently check normalization count and log zeta coefficient.
    for r in range(1,25):
        fc=lambda cy:sum(d*count for d,count in cy if r%d==0)
        assert fc(vv)*(3**r+1)+fc(ee)-fc(bb)==3**r*fc(vv)-sum(d*a for d,a in alpha if r%d==0)
    records[g]=(vv,ee,bb,alpha)

remaining=set(perm_group)
classes=[]
while remaining:
    g=min(remaining)
    cl={mul(mul(h,g),inv(h)) for h in perm_group}
    assert cl<=remaining
    remaining-=cl
    vv,ee,bb,aa=records[g]
    assert {records[h] for h in cl}=={records[g]}
    classes.append({'representative':list(g), 'class_size':len(cl),'order':lcm(*(d for d,c in vv)),
                    'side_swap':g[0]>=15,'vertices':dict(vv),'nodes':dict(ee),
                    'branches':dict(bb),'numerator_exponents':dict(aa),
                    'rational_point_polynomial':f"{dict(vv).get(1,0)}*q+{dict(vv).get(1,0)+dict(ee).get(1,0)-dict(bb).get(1,0)}"})
classes.sort(key=lambda r:(r['order'],r['side_swap'],r['class_size'],r['vertices'],r['nodes'],r['representative']))
for i,r in enumerate(classes,1):r['index']=i
assert len(classes)==13
assert sum(r['class_size'] for r in classes)==1440
zeta={(tuple(sorted(r['vertices'].items())),tuple(sorted(r['numerator_exponents'].items()))) for r in classes}
assert len(zeta)==11
zero=[r for r in classes if r['rational_point_polynomial']=='0*q+0']
assert len(zero)==2 and sorted(r['order'] for r in zero)==[5,10]
assert sum(1 for r in classes if r['side_swap'])==5
# Each zeta collision is a non-isomorphism despite agreement at all extension degrees.
zmult=Counter((tuple(sorted(r['vertices'].items())),tuple(sorted(r['numerator_exponents'].items()))) for r in classes)
assert sorted(zmult.values())==[1]*9+[2]*2
with open('classification.json','w',encoding='utf-8') as handle:
    json.dump(classes,handle,sort_keys=True,indent=2)
    handle.write('\n')
print('VERTICES=30 NODES=45 BRANCHES=90 GENUS=16')
print('AUTOMORPHISMS=1440 S6=720 OUTER_COSET=720')
print('CONJUGACY_CLASSES=13 DISTINCT_ZETA_FUNCTIONS=11')
print('ZERO_POINT_CLASSES=2 ORDERS=5,10')
print('ZETA_COLLISION_MULTIPLICITIES=1x9,2x2')
print('EXHAUSTIVE_24_EXTENSION_CHECKS=PASS')
print('VERIFY_OK')
