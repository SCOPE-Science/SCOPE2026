#!/usr/bin/env python3
"""Full independent finite certificate replay for GP(12,5) matchings."""
import json, collections, hashlib
from pathlib import Path
root = Path(__file__).parent
certpath = root/'certificate.json'
cert = json.loads(certpath.read_text(encoding='utf-8'))
E = [tuple(x) for x in cert['edges']]
assert len(E)==len(set(E))==36
assert E == sorted(E)
ref = set()
for i in range(12):
    for a,b in ((i,(i+1)%12),(i,12+i),(12+i,12+(i+5)%12)):
        ref.add(tuple(sorted((a,b))))
assert set(E)==ref
M = [tuple(row) for row in cert['minimum_maximal_matchings']]
assert len(M)==len(set(M))==90
assert M==sorted(M)
rows = [tuple(int(x) for x in line.split()) for line in (root/'matchings_cpp.txt').read_text().splitlines()]
assert rows==M

for row in M:
    assert len(row)==len(set(row))==8 and list(row)==sorted(row)
    vertices=set()
    for ei in row:
        assert 0<=ei<len(E)
        u,v=E[ei]
        assert u not in vertices and v not in vertices
        vertices|={u,v}
    leftovers=set(range(24))-vertices
    assert len(leftovers)==8
    assert all(not (u in leftovers and v in leftovers) for u,v in E)

adj={}
for t in (1,2,3,4):
    links=[]
    A=[set() for _ in M]
    for i in range(len(M)):
        a=set(M[i])
        for j in range(i+1,len(M)):
            if len(a-set(M[j]))<=t:
                links.append([i,j])
                A[i].add(j);A[j].add(i)
    assert links==cert['exchange_edges'][str(t)]
    adj[t]=A

def sizes(A):
    visited=set()
    comps=[]
    for i in range(len(A)):
        if i in visited:continue
        discovered={i}
        stack=[i]
        while stack:
            u=stack.pop()
            for v in A[u]:
                if v not in discovered:
                    discovered.add(v);stack.append(v)
        visited |= discovered
        comps.append(sorted(discovered))
    return sorted(comps,key=lambda x:x[0])

assert [len(x) for x in sizes(adj[1])]==[1]*90
assert sizes(adj[2])==cert['components_t2']
assert sizes(adj[3])==sizes(adj[2])
assert sorted(map(len,sizes(adj[2])))==[30,30,30]
assert [len(q) for q in cert['exchange_edges'].values()]==[0,180,180,522]
assert len(sizes(adj[4]))==1
assert collections.Counter(map(len,adj[2]))=={4:90}
assert collections.Counter(map(len,adj[4]))=={11:72,14:18}

def ecc(A, vertex):
    D={vertex:0};todo=collections.deque([vertex])
    while todo:
        u=todo.popleft()
        for v in A[u]:
            if v not in D:
                D[v]=D[u]+1;todo.append(v)
    return max(D.values()), len(D)
E2=[ecc(adj[2],i) for i in range(90)]
E4=[ecc(adj[4],i) for i in range(90)]
assert all(n==30 and d==5 for d,n in E2)
assert collections.Counter(E4)=={(3,90):18,(4,90):72}
assert [d for d,_ in E2]==cert['eccentricities_t2']
assert [d for d,_ in E4]==cert['eccentricities_t4']

# Verify that vertex permutations preserve all 36 edges and induce the
# recorded permutations of connected components.
idx={m:i for i,m in enumerate(M)}
edge_index={e:i for i,e in enumerate(E)}
comp=sizes(adj[2]); label={v:i for i,q in enumerate(comp) for v in q}
for kind,transform,expected in (
    ('rotation',lambda i: (i+1)%12 if i<12 else 12+(i-12+1)%12, cert['component_action_rotation']),
    ('reflection',lambda i: (-i)%12 if i<12 else 12+(-(i-12))%12, cert['component_action_reflection'])
):
    image = [transform(i) for i in range(24)]
    assert set(image)==set(range(24))
    assert {tuple(sorted((image[u],image[v]))) for u,v in E}==set(E)
    def image_idx(i):
        return idx[tuple(sorted(edge_index[tuple(sorted((image[E[e][0]],image[E[e][1]])))] for e in M[i]))]
    p=[label[image_idx(q[0])] for q in comp]
    assert p==expected
    for component in comp:
        assert {label[image_idx(i)] for i in component}=={p[label[component[0]]]}
    for i in range(90):
        assert {image_idx(j) for j in adj[2][i]} == adj[2][image_idx(i)]
print('CERTIFICATE_OK minimum=8 matchings=90 R2=3x30 R4=connected')
print('R2_edges=180 R4_edges=522 R2_ecc=5 R4_ecc_distribution=3:18,4:72')
print('rotation_component_action='+str(cert['component_action_rotation']))
print('reflection_component_action='+str(cert['component_action_reflection']))
print('sha256='+hashlib.sha256(certpath.read_bytes()).hexdigest())
