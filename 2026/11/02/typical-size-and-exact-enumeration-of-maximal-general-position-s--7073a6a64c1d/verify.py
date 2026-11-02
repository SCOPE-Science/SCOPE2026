"""Reproducible finite checks for maximal general-position sets in triangular graphs."""
from itertools import combinations
from collections import Counter,deque
from functools import lru_cache
from math import factorial,comb

def formula(n):
    # Exponential formula: each block is an edge, triangle or labeled star.
    @lru_cache(None)
    def f(m):
        if m==0: return {0:1}
        ans=Counter()
        for s in range(2,m+1):
            w=1 if s in (2,3) else s
            value=1 if s==2 else (3 if s==3 else s-1)
            for a,count in f(m-s).items():ans[a+value]+=comb(m-1,s-1)*w*count
        return ans
    d=Counter(f(n))
    if n%3==1:
        k=(n-1)//3
        d[n-1]+=factorial(n)//(6**k*factorial(k))
    return dict(sorted(d.items()))

def graph(n):
    edges=list(combinations(range(n),2))
    neigh=[[] for _ in edges]
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if i!=j and (e[0] in f or e[1] in f):neigh[i].append(j)
    dist=[]
    for i in range(len(edges)):
        d=[10**9]*len(edges);d[i]=0;q=deque([i])
        while q:
            x=q.popleft()
            for y in neigh[x]:
                if d[y]==10**9:d[y]=d[x]+1;q.append(y)
        dist.append(d)
    return edges,dist

def exhaustive_original(n):
    edges,dist=graph(n);h=len(edges);counts=Counter();gp=[False]*(1<<h)
    for mask in range(1<<h):
        vs=[i for i in range(h) if mask>>i&1];ok=True
        for a,b,c in combinations(vs,3):
            if any(dist[x][y]+dist[y][z]==dist[x][z] for x,y,z in ((a,b,c),(a,c,b),(b,a,c))):
                ok=False;break
        gp[mask]=ok
    for mask in range(1<<h):
        if gp[mask] and not any(gp[mask|(1<<i)] for i in range(h) if not(mask>>i&1)):
            counts[mask.bit_count()]+=1
    return dict(sorted(counts.items()))

if __name__=='__main__':
    checks=0
    for n in range(4,7):
        a=exhaustive_original(n);b=formula(n)
        assert a==b,(n,a,b)
        checks+=2**comb(n,2)
        print('PASS original shortest-path predicate vs structural formula',n,a)
    for n in range(7,12):
        a=formula(n); assert sum(a.values())>0
        print('Formula',n,a)
    print('TOTAL original graph subsets examined:',checks)
