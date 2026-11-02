#!/usr/bin/env python3
"""Independent exact checker: dualize pentagonal faces of GP(10,2),
enumerate all matchings, and toggle alternating simple cycles.
Pure Python standard library; no use of primal construction or pair-difference test.
"""
from collections import Counter,deque
from itertools import combinations
n=20
p_edges=set()
def p_add(a,b):p_edges.add(tuple(sorted((a,b))))
for i in range(10):
    p_add(i,(i+1)%10)
    p_add(i,10+i)
    p_add(10+i,10+((i+2)%10))
assert len(p_edges)==30
p_adj=[set() for _ in range(n)]
for a,b in p_edges:p_adj[a].add(b);p_adj[b].add(a)
def canonical(c):
    t=tuple(c)
    rot=[t[i:]+t[:i] for i in range(len(t))]
    inv=t[::-1];rot += [inv[i:]+inv[:i] for i in range(len(t))]
    return min(rot)
faces=set()
for first in range(n):
    def visit(path):
        if len(path)==5:
            if first in p_adj[path[-1]]:faces.add(canonical(path))
            return
        for w in p_adj[path[-1]]:
            if w not in path:visit(path+[w])
    visit([first])
faces=sorted(faces)
assert len(faces)==12
face_edges=[]
for face in faces:
    face_edges.append({tuple(sorted((face[k],face[(k+1)%5]))) for k in range(5)})
assert Counter(e for f in face_edges for e in f)=={e:2 for e in p_edges}
edges=[]
for i,j in combinations(range(12),2):
    if len(face_edges[i]&face_edges[j])==1:edges.append((i,j))
assert len(edges)==30
neighbors=[set() for _ in range(12)]
for u,v in edges:neighbors[u].add(v);neighbors[v].add(u)
assert all(len(x)==5 for x in neighbors)
e_index={e:i for i,e in enumerate(edges)}
match=[]
def scan(remaining,selected):
    if not remaining:
        match.append(selected);return
    v=remaining[0]
    for w in neighbors[v]:
        if w in remaining:
            scan(tuple(x for x in remaining if x!=v and x!=w),selected|{e_index[tuple(sorted((v,w)))]})
scan(tuple(range(12)),frozenset())
assert len(match)==125
by_mask={frozenset(m):i for i,m in enumerate(match)}
# Direct cycle enumeration, not the symmetric-difference classification.
cycles={4:set(),6:set()}
def canon_seq(path):
    q=tuple(path)
    shifts=[]
    for vec in (q,q[::-1]):
        shifts.extend(vec[i:]+vec[:i] for i in range(len(q)))
    return min(shifts)
for L in (4,6):
    for src in range(12):
        def grow(p):
            if len(p)==L:
                if src in neighbors[p[-1]]:cycles[L].add(canon_seq(p))
                return
            for v in neighbors[p[-1]]:
                if v not in p:grow(p+[v])
        grow([src])
adj4=[set() for _ in match];adj6=[set() for _ in match]
for L in (4,6):
    for cyc in cycles[L]:
        cycidx=[e_index[tuple(sorted((cyc[k],cyc[(k+1)%L])))] for k in range(L)]
        cset=frozenset(cycidx)
        for i,m in enumerate(match):
            if len(m & cset)!=L//2:continue
            # every other edge must be occupied (cyclically)
            occup=[int(e in m) for e in cycidx]
            if any(occup[k]==occup[(k+1)%L] for k in range(L)):continue
            new=frozenset(m.symmetric_difference(cset))
            j=by_mask[new]
            (adj4 if L==4 else adj6)[i].add(j)
assert sum(map(len,adj4))//2==300
assert sum(map(len,adj6))//2==580
isolated={i for i in range(125) if len(adj4[i])==0}
assert len(isolated)==5
assert Counter(e for i in isolated for e in match[i])=={e:1 for e in range(30)}
alladj=[adj4[i]|adj6[i] for i in range(125)]
assert sum(map(len,alladj))//2==880
assert Counter(map(len,alladj))=={8:5,11:20,14:30,15:60,18:10}
comp=[];seen=set()
for s in range(125):
    if s in seen:continue
    q=[s];seen.add(s);part=[]
    while q:
        v=q.pop();part.append(v)
        for w in adj4[v]:
            if w not in seen:seen.add(w);q.append(w)
    comp.append(len(part))
assert sorted(comp)==[1]*5+[120]
allpairs=Counter()
for s in range(125):
    d={s:0};q=deque([s])
    while q:
        v=q.popleft()
        for w in alladj[v]:
            if w not in d:d[w]=d[v]+1;q.append(w)
    assert len(d)==125 and max(d.values())==3
    allpairs.update(d[j] for j in range(s))
assert allpairs=={1:880,2:4250,3:2620}
for s in isolated:
    d={s:0};q=deque([s])
    while q:
        v=q.popleft()
        for w in alladj[v]:
            if w not in d:d[w]=d[v]+1;q.append(w)
    assert all(d[t]==2 for t in isolated if t!=s)
print('ICOSAHEDRAL_DODECAHEDRAL_DUAL_CYCLE_TOGGLES_PASS')
print('dual_faces=12, dual_edges=30, perfect_matchings=125')
print('simple_cycles_4='+str(len(cycles[4]))+', simple_cycles_6='+str(len(cycles[6])))
print('four_flip_edges=300, six_flip_edges=580; five_frozen_partition_edge_set')
print('radius=diameter=3; distances='+str(dict(sorted(allpairs.items()))))
