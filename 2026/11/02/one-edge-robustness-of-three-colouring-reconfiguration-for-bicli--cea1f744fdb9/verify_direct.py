"""Finite cross-check for three-colouring reconfiguration after one bipartite edge deletion.
Python standard library only; no external data.
"""
from itertools import product
from collections import deque, Counter


def graph(m, n, deleted):
    edges = [(i, m+j) for i in range(m) for j in range(n)
             if not deleted or (i,j)!=(0,0)]
    states = [p for p in product(range(3),repeat=m+n)
              if all(p[i] != p[j] for i,j in edges)]
    ids={v:i for i,v in enumerate(states)}
    adj=[set() for _ in states]
    for i,s in enumerate(states):
        for k in range(m+n):
            for c in range(3):
                if c == s[k]: continue
                v=s[:k]+(c,)+s[k+1:]
                j=ids.get(v)
                if j is not None: adj[i].add(j)
    return states,adj


def distances(adj,i):
    ds=[-1]*len(adj);ds[i]=0;q=deque([i])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if ds[v]<0:ds[v]=ds[u]+1;q.append(v)
    assert all(d>=0 for d in ds)
    return ds


def odd_girth(adj):
    g=None
    for i in range(len(adj)):
        ds={(i,0):0};q=deque([(i,0)])
        while q:
            u,b=q.popleft()
            if (u,b)==(i,1):break
            for v in adj[u]:
                z=(v,1-b)
                if z not in ds:ds[z]=ds[u,b]+1;q.append(z)
        if (i,1) in ds:g=min(g,ds[i,1]) if g else ds[i,1]
    return g


def main():
    for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)]:
        old,oa=graph(m,n,False)
        new,na=graph(m,n,True)
        D=3*(m+n)//2
        assert len(old)==3*(2**m+2**n)-6
        assert len(new)==3*(2**m+2**n)
        assert sum(map(len,oa))//2 == 3*(m*2**(m-1)+n*2**(n-1))
        assert sum(map(len,na))//2 == 3*(m*2**(m-1)+n*2**(n-1))+12
        old_idx={x:i for i,x in enumerate(old)}
        new_idx={x:i for i,x in enumerate(new)}
        for i,x in enumerate(old):
            dold=distances(oa,i)
            dnew=distances(na,new_idx[x])
            assert max(dold)==D and max(dnew)==D
            assert all(dold[j]==dnew[new_idx[y]] for j,y in enumerate(old))
        assert all(max(distances(na,i))==D for i,x in enumerate(new) if x not in old_idx)
        assert sum(1 for x in new if x not in old_idx)==6
        assert odd_girth(na)==(3*(m+n) if (m+n)%2 else None)
        print('DIRECT_PASS',m,n,len(new),sum(map(len,na))//2,D)
    print('DIRECT_EXHAUSTIVE_PASS')

if __name__=='__main__':main()
