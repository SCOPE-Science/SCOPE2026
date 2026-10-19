#!/usr/bin/env python3
"""Exact, self-contained Heawood torus face-flip census. Python stdlib only."""
import collections, itertools, json, pathlib, sys
P=range(1,8)
L=sorted(set(tuple(sorted((a,b,a^b))) for a in P for b in P if a<b))
assert len(L)==7
E=sorted((p,j) for p in P for j,line in enumerate(L) if p in line)
assert len(E)==21
PM=[]
def enumerate_matchings(p,used,now):
    if p==8:
        PM.append(frozenset(now)); return
    for e in E:
        if e[0]==p and e[1] not in used:
            enumerate_matchings(p+1,used|{e[1]},now+[e])
enumerate_matchings(1,set(),[])
PM.sort(key=lambda m: tuple(sorted(m)))
assert len(PM)==24
idx={m:i for i,m in enumerate(PM)}
C=[]
for x in itertools.combinations(E,6):
    a=collections.Counter(p for p,j in x)
    b=collections.Counter(j for p,j in x)
    if sorted(a.values())==[2]*3 and sorted(b.values())==[2]*3:
        C.append(frozenset(x))
C.sort(key=lambda c:tuple(sorted(c)))
assert len(C)==28
# Each selected 6-cycle turns at six distinct vertex angles. The angular
# exact cover criterion is equivalent to having seven hexagonal disc faces.
def vertices_of(e): return (e[0],e[1]+8)
def walk(c):
    neigh=collections.defaultdict(list)
    for e in c:
        a,b=vertices_of(e);neigh[a].append(b);neigh[b].append(a)
    assert len(neigh)==6 and all(len(v)==2 for v in neigh.values())
    s=min(neigh);prev=None;curr=s;out=[]
    while True:
        out.append(curr)
        nbs=sorted(neigh[curr]); nxt=nbs[0] if nbs[0]!=prev else nbs[1]
        prev,curr=curr,nxt
        if curr==s:break
        assert len(out)<7
    assert len(out)==6
    return out
walks=[walk(c) for c in C]
angles=[];directions=[]
for w in walks:
    A=set(); D={}
    for j,v in enumerate(w):
        a,b=w[(j-1)%6],w[(j+1)%6]
        A.add((v,min(a,b),max(a,b)))
        lo,hi=sorted((v,b));D[(lo,hi)]=1 if v==lo else -1
    angles.append(frozenset(A));directions.append(D)
A=frozenset.union(*angles)
assert len(A)==42
lookup={a:[i for i,ang in enumerate(angles) if a in ang] for a in A}
FACE=[]
def cover(rem,selected):
    if not rem:
        assert len(selected)==7
        FACE.append(tuple(sorted(selected)));return
    pivot=min(rem,key=lambda a:sum(angles[i]<=rem for i in lookup[a]))
    for i in lookup[pivot]:
        if angles[i]<=rem:cover(rem-angles[i],selected+[i])
cover(A,[])
FACE=sorted(set(FACE))
assert len(FACE)==8
FACTOR=sorted(t for t in itertools.combinations(range(24),3)
             if all(PM[a].isdisjoint(PM[b]) for a,b in itertools.combinations(t,2)))
assert len(FACTOR)==8
# Every edge pair occurs once; face coorientations globally consistent -> torus.
def orientable(F):
    attached=collections.defaultdict(list)
    for i in F:
        for e,sgn in directions[i].items():attached[e].append((i,sgn))
    assert len(attached)==21 and all(len(x)==2 for x in attached.values())
    val={F[0]:1};queue=[F[0]]
    while queue:
        i=queue.pop()
        for e,s in directions[i].items():
            j,t=next((j,t) for j,t in attached[e] if j!=i)
            desired=-val[i]*s*t
            if j in val:
                if val[j]!=desired:return False
            else:val[j]=desired;queue.append(j)
    return len(val)==7
certificate=[]
all_full_edges=set(); face_edge_counter=collections.Counter();cycle_freq=collections.Counter()
for f in FACE:
    assert orientable(f)
    assert collections.Counter(len(C[i]&C[j]) for i,j in itertools.combinations(f,2))=={1:21}
    flip_edges=set()
    for i,m in enumerate(PM):
        for fid in f:
            if len(m&C[fid])==3:
                mm=m^C[fid]; assert mm in idx
                j=idx[mm]
                flip_edges.add(tuple(sorted((i,j))))
    assert len(flip_edges)==21
    # Every face supports three reversible flips; on each C7 all seven
    # facial labels occur once (a homological odd-parity phenomenon).
    face_edge_label={}
    for fid in f:
        incident={tuple(sorted((i,idx[m^C[fid]]))) for i,m in enumerate(PM)
                  if len(m&C[fid])==3}
        assert len(incident)==3
        for e in incident:
            assert e not in face_edge_label
            face_edge_label[e]=fid
    assert set(face_edge_label)==flip_edges
    neighbours=[set() for _ in PM]
    for i,j in flip_edges:neighbours[i].add(j);neighbours[j].add(i)
    assert collections.Counter(map(len,neighbours))=={2:21,0:3}
    comps=[];seen=set()
    for i in range(24):
        if i in seen:continue
        todo=[i];seen.add(i);comp=[]
        while todo:
            j=todo.pop();comp.append(j)
            for k in neighbours[j]:
                if k not in seen:seen.add(k);todo.append(k)
        comps.append(comp)
    assert collections.Counter(map(len,comps))=={7:3,1:3}
    assert all(all(len(neighbours[i])==2 for i in comp) for comp in comps if len(comp)==7)
    for comp in comps:
        if len(comp)==7:
            compedges={tuple(sorted((a,b))) for a in comp for b in neighbours[a] if a<b}
            assert len(compedges)==7
            assert {face_edge_label[e] for e in compedges}==set(f)
    frozen=tuple(i for i in range(24) if not neighbours[i])
    assert frozen in FACTOR
    certificate.append({'faces':list(f),'frozen':list(frozen),'flips':[list(x) for x in sorted(flip_edges)]})
    face_edge_counter.update(flip_edges);cycle_freq.update(f)
    all_full_edges.update(flip_edges)
assert len(all_full_edges)==84
assert set(face_edge_counter.values())=={2}
assert len(cycle_freq)==28 and set(cycle_freq.values())=={2}
assert {tuple(item['frozen']) for item in certificate}==set(FACTOR)
# Matchings are partitioned into eight disjoint one-factorizations.
assert set(range(24))==set.union(*(set(f) for f in FACTOR))
assert sum(map(len,FACTOR))==24
# Each flip in full hexagon graph is realized by exactly one hexagon.
full_edges=collections.Counter()
for f in C:
    for i,m in enumerate(PM):
        if len(m&f)==3:
            j=idx[m^f]
            full_edges[tuple(sorted((i,j)))]+=1
assert len(full_edges)==84 and set(full_edges.values())=={2}
assert set(full_edges)==all_full_edges
# Frozen triples characterize faces without brute-force graph isomorphism.
for item in certificate:
    fr=item['frozen']
    Fset=set(item['faces'])
    admissible={i for i,c in enumerate(C) if all(len(c&PM[j])!=3 for j in fr)}
    assert admissible==Fset
# The certificate indexes explicitly defined points, lines, cycles, matchings.
cert={'fano_lines':[list(x) for x in L],'point_line_edges':[list(e) for e in E],
      'matching_edges':[[list(e) for e in sorted(m)] for m in PM],
      'six_cycle_edges':[[list(e) for e in sorted(c)] for c in C],
      'facial_tori':certificate}
if len(sys.argv)>1:
    path=pathlib.Path(sys.argv[1])
    if path.exists():
        expected=json.loads(path.read_text('utf-8'))
        assert expected==cert
        print('CERTIFICATE_REPLAY_OK all_exact_entries=true')
    else:path.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('VERIFY_MAIN_OK points=7 lines=7 incidences=21 matchings=24 hexagons=28 angle_sites=42')
print('VERIFY_MAIN_OK torus_face_systems=8 each_7_hexagons_orientable=true pairwise_face_intersection=1')
print('VERIFY_MAIN_OK factorisations=8 frozen_triples_are_factorisations=true bijection=true')
print('VERIFY_MAIN_OK each_torus_flip_graph=3C7+3K1 edges=21 each_cycle_uses_seven_faces_once=true')
print('VERIFY_MAIN_OK every_full_hexagon_flip_in_2_tori=true distinct_full_flips=84 every_hexagon_in_2_tori=true')
