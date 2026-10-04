#!/usr/bin/env python3
from itertools import combinations


def integer_partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n + 1):
        for rest in integer_partitions(n - x, x):
            yield (x,) + rest


def graph(parts):
    part_of=[]
    local=[]
    for p,n in enumerate(parts):
        for i in range(n):
            part_of.append(p); local.append(i)
    edges=[]
    for u in range(len(part_of)):
        for v in range(u+1,len(part_of)):
            if part_of[u] != part_of[v]:
                edges.append((u,v))
    return part_of, local, edges


def conflict_graph(parts):
    part_of,local,edges=graph(parts)
    E=set(edges)
    def has(u,v):
        if u>v: u,v=v,u
        return (u,v) in E
    adj=[set() for _ in edges]
    structural=0
    for a in range(len(edges)):
        u,v=edges[a]
        for b in range(a+1,len(edges)):
            w,x=edges[b]
            if len({u,v,w,x})<4:
                conf=True
            else:
                connectors=sum(has(*z) for z in ((u,w),(u,x),(v,w),(v,x)))
                conf=connectors>=3
                # For complete multipartite graphs, nonconflict for disjoint edges
                # is equivalent to using exactly the same two parts.
                same_pair={part_of[u],part_of[v]}=={part_of[w],part_of[x]}
                assert conf == (not same_pair)
                structural += 1
            if conf:
                adj[a].add(b); adj[b].add(a)
    return part_of,local,edges,adj,structural


def exact_chromatic(adj):
    n=len(adj)
    if n==0: return 0
    colors=[-1]*n
    best=n
    def rec(done,used):
        nonlocal best
        if used>=best: return
        if done==n:
            best=used; return
        un=[v for v in range(n) if colors[v]<0]
        v=max(un,key=lambda z:(len({colors[w] for w in adj[z] if colors[w]>=0}),len(adj[z])))
        forbidden={colors[w] for w in adj[v] if colors[w]>=0}
        for c in range(used):
            if c not in forbidden:
                colors[v]=c; rec(done+1,used); colors[v]=-1
        colors[v]=used; rec(done+1,used+1); colors[v]=-1
    rec(0,0)
    return best


def formula(parts):
    return sum(max(parts[i],parts[j]) for i in range(len(parts)) for j in range(i+1,len(parts)))


def explicit_colors(parts):
    part_of,local,edges=graph(parts)
    offsets={}
    off=0
    for i in range(len(parts)):
        for j in range(i+1,len(parts)):
            offsets[(i,j)]=(off,max(parts[i],parts[j])); off += max(parts[i],parts[j])
    col=[]
    for u,v in edges:
        i,j=part_of[u],part_of[v]
        if i>j: i,j=j,i
        base,q=offsets[(i,j)]
        col.append(base+(local[u]+local[v])%q)
    return edges,col,off


def verify_coloring(parts):
    _,_,edges,adj,_=conflict_graph(parts)
    e2,c,k=explicit_colors(parts)
    assert e2==edges and k==formula(parts)
    for u in range(len(edges)):
        for v in adj[u]:
            assert c[u]!=c[v]
    return len(edges),len(adj)

exact_types=0
exact_edges=0
structural_pairs=0
for N in range(2,8):
    for p in integer_partitions(N):
        if len(p)<2: continue
        _,_,edges,adj,s=conflict_graph(p)
        got=exact_chromatic(adj)
        want=formula(p)
        assert got==want,(p,got,want)
        verify_coloring(p)
        exact_types += 1
        exact_edges += len(edges)
        structural_pairs += s

constructive_types=0
constructive_edges=0
for N in range(2,11):
    for p in integer_partitions(N):
        if len(p)<2: continue
        e,_=verify_coloring(p)
        constructive_types += 1
        constructive_edges += e

# Directly verify the conjectured bound and equality characterization
# for a broader finite parameter box.
bound_cases=0
for r in range(2,7):
    def rec(prefix,last):
        global bound_cases
        if len(prefix)==r:
            parts=tuple(prefix)  # nonincreasing
            D=sum(parts[:-1])
            F=formula(parts)
            assert F <= D*(D+1)//2
            assert (F==D*(D+1)//2) == all(x==1 for x in parts)
            bound_cases += 1
            return
        for x in range(last,0,-1):
            rec(prefix+[x],x)
    rec([],5)

print(f"ALL CHECKS PASSED; exact_types={exact_types}; exact_edges={exact_edges}; structural_disjoint_pairs={structural_pairs}; constructive_types={constructive_types}; constructive_edges={constructive_edges}; bound_cases={bound_cases}")
