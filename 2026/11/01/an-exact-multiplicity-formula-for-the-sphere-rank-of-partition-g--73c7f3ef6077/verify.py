#!/usr/bin/env python3
"""Reproduce the exact partition statistic and compare with direct flag Euler counts."""
from functools import lru_cache
from math import comb

@lru_cache(None)
def partitions(n, high=None):
    if high is None:
        high = n
    if n == 0:
        return ((),)
    return tuple((j,) + tail for j in range(min(n, high), 0, -1)
                 for tail in partitions(n-j, j))

def sphere_count(n):
    total = 0
    for p in partitions(n):
        multiplicities = {v:p.count(v) for v in set(p)}
        ds = sorted(multiplicities)
        s = len(ds)
        if s >= 3:
            total += comb(s-2,2) + sum(multiplicities[d]>=2 for d in ds[1:-1])
    return total

def direct_euler(n):
    import networkx as nx
    all_p = partitions(n)
    index = {p:i for i,p in enumerate(all_p)}
    g = nx.Graph()
    g.add_nodes_from(range(len(all_p)))
    for p in all_p:
        for src in range(len(p)):
            for dst in range(len(p)+1):
                if dst == src:
                    continue
                q = list(p)+[0]
                q[src]-=1
                q[dst]+=1
                q = tuple(sorted((v for v in q if v > 0), reverse=True))
                if q != p and q in index:
                    g.add_edge(index[p],index[q])
    return sum((-1)**(len(c)-1) for c in nx.enumerate_all_cliques(g))



def check_upper_link(n):
    """Compare actual rising-neighbor graph with the prescribed transfer line graph."""
    import networkx as nx
    all_p=partitions(n)
    index={p:i for i,p in enumerate(all_p)}
    G=nx.Graph(); G.add_nodes_from(range(len(all_p)))
    for p in all_p:
        for src in range(len(p)):
            for dst in range(len(p)+1):
                if src==dst:continue
                q=list(p)+[0]; q[src]-=1; q[dst]+=1
                q=tuple(sorted((z for z in q if z>0),reverse=True))
                if q!=p:G.add_edge(index[p],index[q])
    height=lambda p:sum(v*(v+1)//2 for v in p)
    for p in all_p:
        ds=sorted(set(p)); multiplicities={d:p.count(d) for d in ds}
        predicted={}
        for i,a in enumerate(ds):
            for j,b in enumerate(ds):
                if not (i<j or (i==j and multiplicities[a]>=2)):
                    continue
                q=list(p)+[0]
                source=q.index(a); q[source]-=1
                recipient=next(t for t in range(len(q)) if t!=source and q[t]==b)
                q[recipient]+=1
                q=tuple(sorted((z for z in q if z>0),reverse=True))
                predicted[(i,j)]=index[q]
        assert len(set(predicted.values()))==len(predicted)
        above={v for v in G[index[p]] if height(all_p[v])>height(p)}
        assert above==set(predicted.values()),(n,p,'neighbor mismatch')
        for (a,b),u in predicted.items():
            for (c,d),v in predicted.items():
                if (a,b)!=(c,d):
                    assert G.has_edge(u,v)==(a==c or b==d),(n,p,'line graph mismatch')

if __name__ == '__main__':
    known = (0,0,0,0,0,0,0,1,2,5,10,19,32,55,87,137,207,310,
             451,652,921,1293,1787,2453,3324)
    for n,val in enumerate(known,start=1):
        actual = sphere_count(n)
        assert actual == val,(n,actual,val)
        if n <= 15:
            direct = direct_euler(n)-1
            assert actual == direct,(n,actual,direct)
    for n in range(1,15):
        check_upper_link(n)
    assert sphere_count(26) == 4480
    print('PASS: 25 published values, 15 direct Euler checks, and 14 rising-link sizes.')
    print('Prediction: n=26 has 4480 two-sphere summands.')
