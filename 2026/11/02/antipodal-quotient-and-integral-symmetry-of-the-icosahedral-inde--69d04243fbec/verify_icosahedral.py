#!/usr/bin/env python3
"""Reproducible exact combinatorial test for icosahedral independence topology.
Standard-library combinatorics; optional networkx verifies the full group.
"""
from itertools import combinations
from collections import Counter,defaultdict
from math import factorial

# Vertices 0=T, 1=B, 2+i=u_i, 7+i=l_i, with i mod 5.
V=range(12)
def edge(a,b):return tuple(sorted((a,b)))
E=set()
for i in range(5):
 j=(i+1)%5
 for a,b in [(0,2+i),(1,7+i),(2+i,2+j),(7+i,7+j),
             (2+i,7+i),(2+i,7+(i-1)%5)]:E.add(edge(a,b))
assert len(E)==30 and all(sum(v in e for e in E)==5 for v in V)
N={v:set() for v in V}
for a,b in E:N[a].add(b);N[b].add(a)
dist={}
for s in V:
 d={s:0};q=[s]
 for u in q:
  for v in N[u]:
   if v not in d:d[v]=d[u]+1;q.append(v)
 for t,x in d.items():dist[s,t]=x
assert Counter(dist[0,t] for t in V)==Counter({0:1,1:5,2:5,3:1})
opp={v:next(w for w in V if dist[v,w]==3) for v in V}
assert all(opp[opp[v]]==v for v in V)
chords={edge(v,opp[v]) for v in V}
assert len(chords)==6
faces={k:[] for k in range(1,4)}
for k in range(1,4):
 for x in combinations(V,k):
  if all(edge(a,b) not in E for a,b in combinations(x,2)):faces[k].append(x)
assert [len(faces[k]) for k in (1,2,3)]==[12,36,20]
tri_edges=Counter(edge(a,b) for f in faces[3] for a,b in combinations(f,2))
assert Counter(tri_edges.values())=={2:30}
core=set(tri_edges)
assert core=={edge(a,b) for a,b in combinations(V,2) if dist[a,b]==2}
assert chords==set(faces[2])-core
assert all(sum(v in e for e in core)==5 for v in V)
# Triangulated orientable 2-sphere criterion: core is connected, links are 5-cycles,
# chi=2, and every edge has two cofaces.
def conn(graph_edges):
 adj={v:set() for v in V}
 for a,b in graph_edges:adj[a].add(b);adj[b].add(a)
 reached={0};pending=[0]
 for a in pending:
  for b in adj[a]:
   if b not in reached:reached.add(b);pending.append(b)
 return len(reached)==12
assert conn(core)
for v in V:
 links={edge(a,b) for f in faces[3] if v in f for a,b in [tuple(x for x in f if x!=v)]}
 ln=set(x for e in links for x in e)
 assert len(ln)==5 and len(links)==5 and all(sum(w in e for e in links)==2 for w in ln)
assert 12-30+20==2

# An orientation of core's 20 faces by propagation across each edge.
def sign_in_face(t,e):
 a,b=sorted(e)
 s=[(t[0],t[1]),(t[1],t[2]),(t[2],t[0])]
 return 1 if (a,b) in s else -1
ff=faces[3]
by_edge=defaultdict(list)
for i,f in enumerate(ff):
 for e in combinations(f,2):by_edge[edge(*e)].append(i)
o={0:1};todo=[0]
for i in todo:
 for e in combinations(ff[i],2):
  j=next(j for j in by_edge[edge(*e)] if j!=i)
  val=-o[i]*sign_in_face(ff[i],e)*sign_in_face(ff[j],e)
  if j in o:assert o[j]==val
  else:o[j]=val;todo.append(j)
assert len(o)==20
orientation={f:o[i] for i,f in enumerate(ff)}
# Exact full automorphism enumeration by adjacency-preserving backtracking.
def automorphisms():
    out=[]
    def walk(g, used):
        if len(g)==len(V):
            out.append(dict(g));return
        candidates_unmapped=[v for v in V if v not in g]
        v=max(candidates_unmapped,key=lambda z:(sum(x in g for x in N[z]),-z))
        for w in V:
            if w in used:continue
            if all(((v in N[u])==(w in N[g[u]])) for u in g):
                g[v]=w;used.add(w)
                walk(g, used)
                used.remove(w);del g[v]
    walk({},set())
    return out

def perm_parity_on_tuple(g_tuple):
    return -1 if sum(g_tuple[i]>g_tuple[j] for i in range(len(g_tuple)) for j in range(i+1,len(g_tuple)))%2 else 1

def order(g):
    seen=set(); lengths=[]
    for v in V:
        if v in seen:continue
        w=v;n=0
        while w not in seen:seen.add(w);n+=1;w=g[w]
        lengths.append(n)
    from math import lcm
    return lcm(*lengths)

autos=automorphisms()
assert len(autos)==120
assert sum(all(g[v]==opp[v] for v in V) for g in autos)==1
chars=Counter(); rot_order_chars=Counter(); all_degrees=Counter()
for g in autos:
    assert all(edge(g[a],g[b]) in E for a,b in E)
    assert {edge(g[a],g[b]) for a,b in chords}==chords
    signs=set()
    for f in ff:
        gf=[g[x] for x in f]
        sign=perm_parity_on_tuple(gf)
        signs.add(orientation[f]*sign//orientation[tuple(sorted(gf))])
    assert len(signs)==1
    degree=signs.pop();assert degree in (-1,1)
    tr1=sum((1 if g[a]==a else -1) for a,b in chords if edge(g[a],g[b])==edge(a,b))
    L=0
    for k in (1,2,3):
        for f in faces[k]:
            gf=[g[x] for x in f]
            if sorted(gf)==list(f):L+=(-1)**(k-1)*perm_parity_on_tuple(gf)
    assert L==1-tr1+degree,(L,tr1,degree)
    if all(g[v]==opp[v] for v in V):assert (tr1,degree)==(-6,-1)
    if all(g[v]==v for v in V):assert (tr1,degree)==(6,1)
    chars[(tr1,degree)]+=1
    all_degrees[degree]+=1
    if degree==1:rot_order_chars[(order(g),tr1)]+=1
assert all_degrees=={1:60,-1:60}
assert rot_order_chars=={(1,6):1,(2,-2):15,(3,0):20,(5,1):24}
assert sum(x*n for (x,y),n in chars.items())==0
assert sum(y*n for (x,y),n in chars.items())==0
print('automorphism order',len(autos),'character_pairs',sorted(chars.items()))
print('rotation order, trace',sorted(rot_order_chars.items()))
print('faces',[(k,len(faces[k])) for k in (1,2,3)])
print('opposite pairs',sorted(chords))
print('core',len(core),'incidences',len(tri_edges),'connected',conn(core),'Euler',12-30+20)
print('ICOSA_HOMOLOGY_CORE_SPHERE_PLUS_SIX_ANTIPODAL_EDGES_OK')
