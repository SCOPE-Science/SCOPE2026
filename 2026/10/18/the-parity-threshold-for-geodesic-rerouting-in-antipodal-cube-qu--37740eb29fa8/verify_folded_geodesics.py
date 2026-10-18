#!/usr/bin/env python3
"""Finite tests of folded-cube geodesic reconfiguration (n=3..10)."""
from collections import deque,Counter
from itertools import permutations
from math import factorial,comb

def folded_graph(n):
    whole=(1<<n)-1
    canon=lambda x:min(x,x^whole)
    vertices=sorted({canon(x) for x in range(1<<n)})
    adj={v: tuple(sorted({canon(v^(1<<j)) for j in range(n)}-{v})) for v in vertices}
    for u in vertices:
        for v in adj[u]:
            assert u in adj[v]
    return vertices,adj,canon

def bfs(s,adj):
    dd={s:0}; q=deque([s])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in dd:
                dd[y]=dd[x]+1;q.append(y)
    return dd

def geodesics(a,b,adj):
    d=bfs(a,adj); L=d[b]
    paths=[]
    def visit(path):
        x=path[-1]
        if len(path)==L+1:
            if x==b:paths.append(tuple(path))
            return
        for y in adj[x]:
            if d[y]==d[x]+1:
                visit(path+[y])
    visit([a]);return paths

def components(paths):
    # Compare vertex at each layer, avoiding a generator-label assumption.
    nbr=[[] for _ in paths]
    for i,a in enumerate(paths):
        for j in range(i+1,len(paths)):
            b=paths[j]
            if sum(x!=y for x,y in zip(a,b))==1:
                nbr[i].append(j);nbr[j].append(i)
    seen=set();cc=[]
    for i in range(len(paths)):
        if i in seen:continue
        q=[i];seen.add(i)
        for v in q:
            for w in nbr[v]:
                if w not in seen:seen.add(w);q.append(w)
        cc.append(q)
    return nbr,cc

def expected(n,r):
    if r==1:return [1],0
    if n==4 and r==2:return [4],6
    if 2*r==n:return [factorial(r)]*2,factorial(r)*(r-1)
    return [factorial(r)],factorial(r)*(r-1)//2

def verify_component_metric(neighbors,cc,expected_diameter):
    for comp in cc:
        diam=0;rad=len(comp)+1
        for start in comp:
            dist={start:0};queue=deque([start])
            while queue:
                v=queue.popleft()
                for w in neighbors[v]:
                    if w not in dist:
                        dist[w]=dist[v]+1;queue.append(w)
            assert len(dist)==len(comp)
            ecc=max(dist.values());diam=max(diam,ecc);rad=min(rad,ecc)
        assert rad==diam==expected_diameter,(rad,diam,expected_diameter)

def check_n(n):
    vertices,adj,canon=folded_graph(n)
    assert len(vertices)==2**(n-1)
    da=bfs(0,adj)
    assert len(da)==len(vertices)
    assert max(da.values())==n//2
    for r in range(1,n//2+1):
        targets=[v for v in vertices if da[v]==r]
        for t in targets:
            pp=geodesics(0,t,adj)
            nb,cc=components(pp)
            sizes=sorted(map(len,cc))
            exp,edges=expected(n,r)
            assert sizes==sorted(exp),(n,r,t,sizes,exp)
            assert sum(map(len,nb))//2==edges,(n,r,t,'edge count')
            if t == targets[0]:
                expected_diameter = (1 if n==4 and r==2 else comb(r,2))
                verify_component_metric(nb,cc,expected_diameter)
            if len(cc)>1:
                assert n%2==0 and r==n//2 and n>=6
            # Degree matches the respective permutahedron or K4.
            target_degree = 3 if n==4 and r==2 else r-1
            assert set(map(len,nb))=={target_degree},(n,r,t,'degree')
        print(f'n={n} distance={r} target_count={len(targets)} paths_each={len(pp)} component_sizes={sorted(exp)} edges={edges}')

if __name__=='__main__':
    for n in range(3,11):check_n(n)
    print('VERIFY_OK')
