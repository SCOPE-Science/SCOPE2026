#!/usr/bin/env python3
"""Independent finite checks for maximal-geodesic packing on Q2 Cartesian K_n."""
from functools import lru_cache
from itertools import product

def graph(n):
    vv=list(product(range(2),range(2),range(n)))
    index={v:i for i,v in enumerate(vv)}
    adj=[]
    for u in vv:
        adj.append({index[v] for v in vv if sum(a!=b for a,b in zip(u,v))==1})
    return vv,adj

def distance_from(adj,source):
    dist=[-1]*len(adj);dist[source]=0;todo=[source]
    for i in todo:
        for j in adj[i]:
            if dist[j]<0:dist[j]=dist[i]+1;todo.append(j)
    return dist

def paths(n):
    vv,adj=graph(n)
    ds=[distance_from(adj,i) for i in range(len(vv))]
    assert max(max(x) for x in ds)==3
    found=set()
    for a in range(len(vv)):
        for b in adj[a]:
            for c in adj[b]-{a}:
                for d in adj[c]-{b,a}:
                    if ds[a][d]==3:
                        p=(a,b,c,d)
                        found.add(min(p,p[::-1]))
    assert all(len({vv[v][2] for v in p})==2 for p in found)
    return vv,ds,found

def check_witness(pairs):
    n=max(max(a,b) for a,b in pairs)+1
    vv,ds,gs=paths(n)
    index={v:i for i,v in enumerate(vv)}
    allpaths=[]
    for i,j in pairs:
        allpaths.append(((0,0,i),(1,0,i),(1,0,j),(1,1,j)))
        allpaths.append(((1,1,i),(0,1,i),(0,1,j),(0,0,j)))
    used=[]
    for path in allpaths:
        ids=tuple(index[v] for v in path)
        assert all(ds[ids[k]][ids[k+1]]==1 for k in range(3))
        assert ds[ids[0]][ids[3]]==3
        assert min(ids,ids[::-1]) in gs
        used.extend(ids)
    assert len(used)==len(set(used))
    return len(allpaths),len(used)

def exact_max(n):
    vv,ds,gs=paths(n)
    masks=[sum(1<<v for v in p) for p in gs]
    containing=[[] for _ in vv]
    for mask in masks:
        for i in range(len(vv)):
            if mask>>i&1:containing[i].append(mask)
    @lru_cache(None)
    def best(free):
        if not free:return 0
        bit=free&-free;v=bit.bit_length()-1
        res=best(free^bit)
        for pm in containing[v]:
            if free&pm==pm:
                res=max(res,1+best(free^pm))
        return res
    ans=best((1<<len(vv))-1)
    return ans,best.cache_info().currsize

def edge(kind,side):
    # kind=0 varies first bit, kind=1 varies second bit
    if kind==0:return {(0,side),(1,side)}
    return {(side,0),(side,1)}

def cycle_packing(cycle):
    assert len(cycle)%2==0 and len(set(cycle))==len(cycle)
    columns={v:i for i,v in enumerate(cycle)}
    n=len(cycle)
    paths_out=[]
    for i in range(n):
        j=(i+1)%n
        ei=edge(i%2,1)  # outgoing
        ej=edge(j%2,0)  # incoming
        intersection=ei & ej
        assert len(intersection)==1
        x=next(iter(intersection))
        y=next(iter(ei-{x}));z=next(iter(ej-{x}))
        paths_out.append(((*y,i),(*x,i),(*x,j),(*z,j)))
    vv,ds,gs=paths(n)
    ids={v:i for i,v in enumerate(vv)}
    seen=[]
    for p in paths_out:
        u=tuple(ids[v] for v in p)
        assert min(u,u[::-1]) in gs
        seen.extend(u)
    assert len(seen)==4*n and len(set(seen))==4*n
    return len(paths_out)

if __name__=='__main__':
    for n in range(2,5):
        v,ds,ps=paths(n)
        optimum,states=exact_max(n)
        assert optimum==2*(n//2),(n,optimum)
        print('EXACT',n,optimum,'states',states,'paths',len(ps))
    for n in range(2,13,2):
        c=check_witness([(i,i+1) for i in range(0,n,2)])
        assert c==(n,4*n)
        assert cycle_packing(tuple(range(n)))==n
        print('CONSTRUCT',n,c)
    print('VERIFY_OK')
