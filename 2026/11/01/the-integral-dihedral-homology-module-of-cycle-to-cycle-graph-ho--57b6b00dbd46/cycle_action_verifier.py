#!/usr/bin/env python3
"""Exact finite cubical traces for cycle-to-cycle Hom complexes.
Neutral implementation using integer tuple cell labels and no external packages.
"""
from itertools import product,combinations
from collections import deque
from math import gcd

def build(m,n):
    maps=[]
    for start in range(n):
      for steps in product((-1,1),repeat=m):
        if sum(steps)%n: continue
        y=[start]
        for z in steps[:-1]: y.append((y[-1]+z)%n)
        maps.append(tuple(y))
    ids={f:i for i,f in enumerate(maps)}
    adj=[{} for _ in maps]
    faces=set()
    for idx,f in enumerate(maps):
        flippable=[]
        for i in range(m):
            if f[(i-1)%m]!=f[(i+1)%m]: continue
            alt=(2*f[(i-1)%m]-f[i])%n
            if alt==f[i]:continue
            flippable.append((i,alt))
            ff=list(f);ff[i]=alt;ff=tuple(ff)
            j=ids[ff]
            delta=(alt-f[i])%n
            d=0 if i!=0 else (2 if delta==2 else -2)
            adj[idx][j]=d
        faces.add(tuple((a,) for a in f))
        for r in range(1,len(flippable)+1):
            for chosen in combinations(flippable,r):
                indices=[i for i,_ in chosen]
                if any((indices[t]+1)%m in indices for t in range(r)): continue
                cells=[(a,) for a in f]
                for i,a in chosen:cells[i]=tuple(sorted((f[i],a)))
                faces.add(tuple(cells))
    comps=[];compid={}
    for u in range(len(maps)):
        if u in compid:continue
        j=len(comps); q=deque([u]);compid[u]=j; members=[]
        while q:
            v=q.popleft();members.append(v)
            for z in adj[v]:
                if z not in compid:compid[z]=j;q.append(z)
        comps.append(members)
    comp_tags=[]
    for members in comps:
        f=maps[members[0]]
        s=sum(1 if (f[(i+1)%m]-f[i])%n==1 else -1 for i in range(m))
        tag=(s//n,f[0]%2 if n%2==0 else None)
        comp_tags.append(tag)
    return maps,ids,adj,faces,comps,compid,comp_tags

def operation(f,s,k,t,l,m,n):
    return tuple((t*f[s*((j-k)%m)%m]+l)%n for j in range(m))

def cell_operation(face,s,k,t,l,m,n):
    out=[None]*m
    for i,x in enumerate(face):out[(s*i+k)%m]=tuple(sorted((t*z+l)%n for z in x))
    return tuple(out)

def oriented_cell_sign(face,s,k,t,l,m,n):
    old=[i for i,x in enumerate(face) if len(x)==2]
    new=[(s*i+k)%m for i in old]
    inv=sum(new[i]>new[j] for i in range(len(new)) for j in range(i+1,len(new)))
    z=-1 if inv%2 else 1
    for i in old:
        a,b=face[i]
        u=(t*a+l)%n;v=(t*b+l)%n
        if u>v:z=-z
    return z

def compute(m,n,ops):
    maps,ids,adj,faces,comps,compid,tags=build(m,n)
    by_dim={d:sum(sum(len(x)==2 for x in face)==d for face in faces) for d in range(m+1)}
    by_dim={d:c for d,c in by_dim.items() if c}
    print(f'CASE m={m} n={n} vertices={len(maps)} cells={len(faces)} f-vector={by_dim} components={len(comps)}',flush=True)
    maxdegree=m//2
    for s,k,t,l in ops:
        fixed0=0
        for comp in comps:
            f=maps[comp[0]];j=ids[operation(f,s,k,t,l,m,n)]
            if compid[j]==compid[comp[0]]:fixed0+=1
        lev=0
        for face in faces:
            if cell_operation(face,s,k,t,l,m,n)==face:
                d=sum(len(x)==2 for x in face)
                lev+=(-1)**d*oriented_cell_sign(face,s,k,t,l,m,n)
        observed=fixed0-lev
        count=0
        for tag in sorted(set(tags)):
            w,p=tag
            if abs(w)*n>=m: continue # isolated
            newtag=(s*t*w, None if n%2 else (p+k+l)%2)
            if tag==newtag:count+=1
        predicted=t*count
        assert observed==predicted,(m,n,(s,k,t,l),observed,predicted)
        print(f'  op={(s,k,t,l)} H0trace={fixed0} Lefschetz={lev} H1trace={observed}',flush=True)

if __name__=='__main__':
    compute(6,5,[(1,0,1,0),(1,1,1,0),(-1,0,1,0),(1,0,-1,0),(-1,0,-1,0)])
    compute(7,5,[(1,0,1,0),(1,1,1,0),(-1,0,1,0),(1,0,-1,0),(-1,1,-1,1)])
    compute(8,6,[(1,0,1,0),(1,1,1,0),(-1,0,1,0),(1,0,1,1),(1,0,-1,0),(-1,0,-1,0),(-1,1,-1,1),(1,2,-1,2)])
    print('ALL_CHECKS_PASS')
