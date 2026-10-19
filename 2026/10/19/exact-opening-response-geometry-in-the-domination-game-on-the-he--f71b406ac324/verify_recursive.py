"""Exact minimax certificate for classical cubic incidence graphs.

Run: python3 verify_recursive.py
No third-party dependencies.
"""
from collections import Counter, deque
from functools import lru_cache

def heawood():
    # Points i and lines j (modulo 7); the Fano difference set is {0,1,3}.
    n=14
    adj=[set() for _ in range(n)]
    for j in range(7):
        for d in (0,1,3):
            i=(j+d)%7
            adj[i].add(7+j);adj[7+j].add(i)
    return adj

def pappus():
    # The affine 3-by-3 grid, with the vertical parallel class omitted.
    n=18
    adj=[set() for _ in range(n)]
    for x in range(3):
        for y in range(3):
            i=3*x+y
            for slope in range(3):
                b=(y-slope*x)%3
                j=9+3*slope+b
                adj[i].add(j);adj[j].add(i)
    return adj

def dist(adj,src):
    d=[-1]*len(adj)
    d[src]=0
    queue=deque([src])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if d[v]<0:d[v]=d[u]+1;queue.append(v)
    assert -1 not in d
    return d

def evaluate(name,adj,expected):
    n=len(adj); full=(1<<n)-1
    assert all(len(s)==3 for s in adj)
    assert all(i in adj[j] for j in range(n) for i in adj[j])
    neigh=[(1<<v)|sum(1<<w for w in adj[v]) for v in range(n)]
    @lru_cache(None)
    def v(mask,player):
        if mask==full:return 0
        nextvals=[1+v(mask|k,1-player) for k in neigh if k&~mask]
        assert nextvals
        return min(nextvals) if player==0 else max(nextvals)
    values=(v(0,0),v(0,1))
    assert values==expected,(name,values)
    summaries=[]
    for first_player in (0,1):
        tables=[]
        for first in range(n):
            ds=dist(adj,first)
            groups={}
            for second in range(n):
                if not (neigh[second] &~neigh[first]):continue
                score=2+v(neigh[first]|neigh[second],first_player)
                groups.setdefault(ds[second],Counter())[score]+=1
            tables.append(tuple(sorted((d,tuple(sorted(c.items()))) for d,c in groups.items())))
        assert len(set(tables))==1,(name,first_player,tables)
        table=tables[0]
        summaries.append(table)
    if name=='Heawood':
        assert summaries==[
            ((1,((7,3),)),(2,((5,6),)),(3,((5,4),))),
            ((1,((6,3),)),(2,((6,6),)),(3,((6,4),)))
        ]
    if name=='Pappus':
        assert summaries==[
            ((1,((8,3),)),(2,((7,6),)),(3,((7,6),)),(4,((7,2),))),
            ((1,((8,3),)),(2,((8,6),)),(3,((8,6),)),(4,((7,2),)))
        ]
    print(name,'order',n,'size',sum(map(len,adj))//2,'values',values,
          'states',v.cache_info().currsize)
    for label,table in zip(('D-first','S-first'),summaries):
        print(' ',label,'second-ply distance -> {score: multiplicity}',table)

if __name__=='__main__':
    evaluate('Heawood',heawood(),(7,6))
    evaluate('Pappus',pappus(),(8,7))
    print('VERIFY_OK')
