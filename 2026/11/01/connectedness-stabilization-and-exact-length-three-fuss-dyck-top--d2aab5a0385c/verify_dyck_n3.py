#!/usr/bin/env python3
"""Independent exhaustive enumeration of (1,b)-Dyck words of length three.
Uses actual valley positions (word index and height), not the proposed edge rule.
"""
from itertools import combinations
from collections import defaultdict, deque
from math import comb

def enumerate_faces(b):
    N=3*b+3
    faces={frozenset()}
    count=0
    for d_pos in combinations(range(N),3):
        dset=set(d_pos)
        path=['D' if t in dset else 'U' for t in range(N)]
        u=d=0
        v=[]
        good=True
        for t,z in enumerate(path):
            if z=='U':u+=1
            else:d+=1
            if u<b*d:
                good=False; break
            if z=='D' and t+1<N and path[t+1]=='U':
                v.append((t+1,u-d))
        if not good:continue
        count+=1
        for sz in range(len(v)+1):
            for face in combinations(v,sz):faces.add(frozenset(face))
    return faces,count

def validate(b):
    faces,path_count=enumerate_faces(b)
    verts={next(iter(f)) for f in faces if len(f)==1}
    edges={tuple(sorted(f)) for f in faces if len(f)==2}
    assert not any(len(f)>2 for f in faces)
    assert len(verts)==3*b, (b,len(verts))
    assert len(edges)==b*(3*b-1)//2, (b,len(edges))
    adj={v:set() for v in verts}
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    components=[]
    unseen=set(verts)
    while unseen:
        x=unseen.pop();visited={x};stack=[x]
        while stack:
            for nxt in adj[stack.pop()]:
                if nxt not in visited:
                    visited.add(nxt); unseen.remove(nxt);stack.append(nxt)
        components.append(visited)
    assert sorted(map(len,components))==[1,3*b-1]
    one_faces=sum(len(adj[v])==0 for v in verts)
    h1=len(edges)-len(verts)+len(components)
    assert h1==(3*b-4)*(b-1)//2
    assert one_faces==1
    assert len(edges)+(3*b-1)+1+1==len(faces)
    return b,path_count,len(verts),len(edges),sorted(map(len,components)),h1

if __name__=='__main__':
    for b in range(1,11):print(validate(b))

def check_components(n,b):
    total_u=n*b
    total=total_u+n
    verts=set(); edge_set=set()
    paths=0
    for ds in combinations(range(total),n):
        dset=set(ds); path=['D' if x in dset else 'U' for x in range(total)]
        u=d=0;vals=[];valid=True
        for t,x in enumerate(path):
            if x=='U': u+=1
            else: d+=1
            if u < b*d: valid=False;break
            if x=='D' and t+1<total and path[t+1]=='U':vals.append((d,u))
        if not valid:continue
        paths+=1
        verts.update(vals)
        edge_set.update(tuple(sorted(pair)) for pair in combinations(vals,2))
    adj={v:set() for v in verts}
    for u,v in edge_set:adj[u].add(v);adj[v].add(u)
    unseen=set(verts); cc=[]
    while unseen:
        v=unseen.pop(); comp={v};stack=[v]
        while stack:
            for w in adj[stack.pop()]:
                if w not in comp:comp.add(w);unseen.remove(w);stack.append(w)
        cc.append(comp)
    assert len(cc)==2,(n,b,len(cc),sorted(map(len,cc)))
    assert sorted(map(len,cc))==[1,len(verts)-1]
    assert {v for v in verts if not adj[v]}=={(1,n*b-1)}
    return n,b,paths,len(verts),len(edge_set),tuple(sorted(map(len,cc)))

if __name__=='__main__':
    for n,b in [(4,1),(4,2),(4,3),(4,4),(5,1),(5,2),(5,3),(6,1),(6,2)]:
        print('connectivity',check_components(n,b))
