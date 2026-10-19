"""Exact exhaustive Hamilton-cycle reconfiguration check on the icosahedral graph.
Python 3 standard library only. Run: python verify_flips.py certificate.json
"""
import collections
import itertools
import json
import sys
from collections import Counter

def graph():
    edges=set()
    for i in range(5):
        a=1+i; b=6+i
        for x,y in ((0,a),(11,b),(a,1+(i+1)%5),(b,6+(i+1)%5),(a,b),(a,6+(i+4)%5)):
            edges.add(tuple(sorted((x,y))))
    return tuple(sorted(edges))

def compute():
    E=graph(); assert len(E)==30
    adj=[set() for _ in range(12)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    assert all(len(a)==5 for a in adj)
    edge_no={p:i for i,p in enumerate(E)}
    masks=set()
    def dfs(path,used):
        if len(path)==12:
            if path[-1] in adj[0] and path[1]<path[-1]:
                m=0
                for i in range(12):
                    a,b=path[i],path[(i+1)%12]
                    m|=1<<edge_no[tuple(sorted((a,b)))]
                masks.add(m)
            return
        for u in adj[path[-1]]:
            if not (used>>u&1):dfs(path+[u],used|(1<<u))
    dfs([0],1)
    assert len(masks)==1280
    masks=sorted(masks);idx={m:i for i,m in enumerate(masks)}
    squares=set()
    for a,b,c,d in itertools.combinations(range(12),4):
        for v in ((a,b,c,d),(a,c,b,d),(a,b,d,c)):
            if all(tuple(sorted((v[i],v[(i+1)%4]))) in edge_no for i in range(4)):
                squares.add(sum(1<<edge_no[tuple(sorted((v[i],v[(i+1)%4])))] for i in range(4)))
    assert len(squares)==30
    switch_pairs=set()
    for i,m in enumerate(masks):
        for sq in squares:
            j=idx.get(m^sq)
            if j is not None and i<j:switch_pairs.add((i,j))
    switch_pairs=sorted(switch_pairs)
    assert len(switch_pairs)==1800
    nbr=[set() for _ in masks]
    for i,j in switch_pairs:nbr[i].add(j);nbr[j].add(i)
    seen=set(); comps=[];membership={}
    for v in range(len(masks)):
        if v in seen:continue
        todo=[v];seen.add(v);component=[]
        while todo:
            u=todo.pop();component.append(u)
            for w in nbr[u]-seen:seen.add(w);todo.append(w)
        component=set(component);k=len(comps);comps.append(component)
        for u in component:membership[u]=k
    assert Counter(map(len,comps))==Counter({1:80,2:60,36:30})
    assert Counter(map(len,nbr))==Counter({0:80,1:180,2:330,3:240,4:240,5:180,6:30})
    def distances(v):
        dist={v:0};queue=collections.deque([v])
        while queue:
            u=queue.popleft()
            for w in nbr[u]:
                if w not in dist:dist[w]=dist[u]+1;queue.append(w)
        return dist
    for c in comps:
        if len(c)==36:
            assert sum(len(nbr[i]) for i in c)//2==58
            assert Counter(len(nbr[v]) for v in c)==Counter({1:2,2:11,3:8,4:8,5:6,6:1})
            assert max(max(distances(v).values()) for v in c)==8
    return E,masks,switch_pairs,comps,membership

def group_orbits(E,masks,comps,membership):
    adj=[set() for _ in range(12)]
    for a,b in E:adj[a].add(b);adj[b].add(a)
    bijections=[]
    def rec(mapping,unused):
        if not unused:
            bijections.append(tuple(mapping));return
        unmapped=[v for v in range(12) if mapping[v]<0]
        x=max(unmapped,key=lambda v: sum(mapping[t]>=0 for t in adj[v]))
        for y in range(12):
            if y not in unused:continue
            if all(((t in adj[x])==(mapping[t] in adj[y])) for t in range(12) if mapping[t]>=0):
                mapping[x]=y;rec(mapping,unused-{y});mapping[x]=-1
    rec([-1]*12,set(range(12)))
    assert len(bijections)==120
    edge_index={e:i for i,e in enumerate(E)}
    lookup={m:i for i,m in enumerate(masks)}
    left=set(range(len(comps))); types=[]
    while left:
        k=min(left);sample=masks[next(iter(comps[k]))];reachable=set()
        for perm in bijections:
            image=0
            for j,(a,b) in enumerate(E):
                if sample>>j&1:
                    image|=1<<edge_index[tuple(sorted((perm[a],perm[b])))]
            reachable.add(membership[lookup[image]])
        assert reachable<=left
        left-=reachable
        types.append((len(comps[k]),len(reachable)))
    assert sorted(types)==[(1,20),(1,60),(2,60),(36,30)]
    return types

def main():
    E,masks,pairs,comps,membership=compute()
    if len(sys.argv)>1:
        cert=json.load(open(sys.argv[1],encoding='utf-8'))
        assert cert['icosahedron_edges']==[list(e) for e in E]
        assert cert['undirected_cycle_edge_masks']==masks
        assert cert['switch_edges_indexed']==[list(e) for e in pairs]
    types=group_orbits(E,masks,comps,membership)
    print('VERIFY_FLIPS_OK edges=30 undirected_Hamilton_cycles=1280 4cycles=30 switch_edges=1800')
    print('VERIFY_FLIPS_OK components=30x36+60x2+80x1 nontrivial_large_components_each_58edges_diameter8')
    print('VERIFY_SYMMETRY_OK automorphism_order=120 component_orbits='+repr(sorted(types)))
if __name__=='__main__':main()
