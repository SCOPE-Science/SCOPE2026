#!/usr/bin/env python3
"""Exact finite simplicial-collapse certificate for the shortest-path Rips complex of GP(7,2)."""
import json
from collections import Counter,deque
from pathlib import Path

V=14
E=set()
for i in range(7):
    for x,y in ((i,(i+1)%7),(i,i+7),(i+7,((i+2)%7)+7)):
        E.add(tuple(sorted((x,y))))
assert len(E)==21
adj=[set() for _ in range(V)]
for x,y in E:
    adj[x].add(y);adj[y].add(x)
assert all(len(s)==3 for s in adj)
D=[]
for root in range(V):
    d=[99]*V;d[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if d[v]==99:d[v]=d[u]+1;q.append(v)
    D.append(d)
assert max(max(d) for d in D)==3
assert all(not set((x,y)).issubset(adj[z]) for z in range(V) for x,y in E if z not in (x,y))
faces=set()
for m in range(1,1<<V):
    v=[j for j in range(V) if m>>j&1]
    if all(D[x][y]<=2 for i,x in enumerate(v) for y in v[i+1:]):faces.add(m)
fvec=lambda F:dict(sorted(Counter(m.bit_count()-1 for m in F).items()))
assert fvec(faces)=={0:14,1:63,2:105,3:56,4:7}
cert=json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
assert len(cert['collapse_pairs'])==68
for small,big in cert['collapse_pairs']:
    assert small in faces and big in faces
    assert small&big==small and big.bit_count()==small.bit_count()+1
    bigger_small=[m for m in faces if m!=small and m&small==small and m.bit_count()==small.bit_count()+1]
    assert bigger_small==[big],(small,big,bigger_small)
    assert not any(m!=big and m&big==big for m in faces)
    faces.remove(small);faces.remove(big)
assert fvec(faces)=={int(k):v for k,v in cert['remaining_face_counts'].items()}
assert max(m.bit_count() for m in faces)==3
assert all((m & ~(1<<i)) in faces for m in faces for i in range(V) if m&(1<<i) and m.bit_count()>1)
assert sum((-1)**(k) * val for k,val in fvec(faces).items())==7
# Check full spanning tree and eight fundamental cycles; each has length 5 or 6.
tree={tuple(sorted(t)) for t in cert['tree_edges']}
assert tree<=E and len(tree)==V-1
T=[set() for _ in range(V)]
for x,y in tree:T[x].add(y);T[y].add(x)
seen={7};Q=deque([7])
while Q:
    x=Q.popleft()
    for y in T[x]:
        if y not in seen:seen.add(y);Q.append(y)
assert len(seen)==V
chords=E-tree
assert len(chords)==8==len(cert['fundamental_cycles'])
lengths=[]
for item in cert['fundamental_cycles']:
    x,y=item['edge'];path=item['cycle_path'];l=item['cycle_length']
    assert tuple(sorted((x,y))) in chords and path[0]==x and path[-1]==y
    assert len(set(path))==len(path) and len(path)==l and l in (5,6)
    assert all(tuple(sorted((a,b))) in tree for a,b in zip(path,path[1:]))
    lengths.append(l)
assert sorted(lengths)==[5]*4+[6]*4
# Independent binary boundary ranks for reduced 2-complex.
levels=[[m for m in sorted(faces) if m.bit_count()==k] for k in (1,2,3)]
def rank_mod2(columns):
    pivots={}
    for col in columns:
        while col:
            p=col.bit_length()-1
            if p not in pivots:pivots[p]=col;break
            col^=pivots[p]
    return len(pivots)
vertices={m:i for i,m in enumerate(levels[0])}
edges={m:i for i,m in enumerate(levels[1])}
cols1=[sum(1<<vertices[1<<i] for i in range(V) if e>>i&1) for e in levels[1]]
cols2=[]
for t in levels[2]:
    edges_in_t=[t & ~(1<<i) for i in range(V) if t>>i&1]
    cols2.append(sum(1<<edges[e] for e in edges_in_t))
assert rank_mod2(cols1)==13 and rank_mod2(cols2)==38
assert len(levels[2])-38==6 and len(levels[1])-13-38==0
print('G72_RIPS_CERTIFICATE_OK: 245 faces, 68 collapses, 6 second-homology generators, 8 fundamental cycles')
