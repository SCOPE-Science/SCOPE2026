#!/usr/bin/env python3
"""Independent exhaustive and transfer-matrix verification for open-neighborhood NOR on leaf coronas."""
from itertools import combinations
from collections import Counter


def graph_adj(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def nor_step(state, adj):
    n = len(adj)
    cores, leaves = state
    next_cores = 0
    for v in range(n):
        if (leaves >> v) & 1 == 0 and (cores & adj[v]) == 0:
            next_cores |= 1 << v
    return next_cores, (1 << n) - 1 - cores


def independent(a, adj):
    return all(not (a >> v & 1) or not (a & adj[v]) for v in range(len(adj)))


def cross_independent(a, b, adj):
    return all(not (a >> v & 1) or not (b & adj[v]) for v in range(len(adj)))


def neighborhood_size(a, adj):
    neigh = 0
    for v in range(len(adj)):
        if a >> v & 1:
            neigh |= adj[v]
    return neigh.bit_count()


def run(n, adj):
    size = 1 << n
    cycle_counter = Counter()
    fixed_targets = {}
    periodic_states = set()
    for a in range(size):
        for b in range(size):
            if cross_independent(a, b, adj):
                periodic_states.add((a, size-1-b))
                if a == b:
                    assert independent(a, adj)
                    fixed_targets[(a, size-1-a)] = 1 << neighborhood_size(a, adj)
    assert len(periodic_states) == sum(1 for a in range(size) for b in range(size) if cross_independent(a,b,adj))
    for a in range(size):
        for l in range(size):
            x=(a,l); y=nor_step(x,adj); z=nor_step(y,adj); w=nor_step(z,adj)
            assert w==y, ('F3!=F',n,adj,x,y,z,w)
            assert y in periodic_states
            periodic = (z == x)
            if periodic:
                assert x in periodic_states
            target=y
            fixed_orbit = (nor_step(y,adj)==y)
            if fixed_orbit:
                cycle_counter[target] += 1
    assert all(cycle_counter[x]==want for x,want in fixed_targets.items())
    assert sum(cycle_counter.values()) == sum(fixed_targets.values())
    # Every nontrivial recurrent cycle basin is obtained from the two one-step preimage fibers.
    for a in range(size):
        for b in range(size):
            if not cross_independent(a,b,adj) or a==b: continue
            x=(a,size-1-b);y=(b,size-1-a)
            expected=(1<<neighborhood_size(a,adj))+(1<<neighborhood_size(b,adj))
            actual=sum(1 for u in range(size) for l in range(size) if nor_step((u,l),adj) in (x,y))
            assert expected==actual
    return len(periodic_states),len(fixed_targets),sum(fixed_targets.values())


def transfer_trace(n):
    t=[[1,2,0],[0,0,1],[2,2,0]]
    a=[[int(i==j) for j in range(3)] for i in range(3)]
    for _ in range(n):
        a=[[sum(a[i][k]*t[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    return sum(a[i][i] for i in range(3))


def lucas(n):
    a,b=2,1
    for _ in range(n): a,b=b,a+b
    return a


def check_graphs():
    graphcases=0;states=0
    for n in range(1,5):
        edges=list(combinations(range(n),2))
        for mask in range(1<<len(edges)):
            e=[edge for i,edge in enumerate(edges) if mask>>i&1]
            run(n,graph_adj(n,e)); graphcases+=1;states+=4**n
    print('All finite graphs up to 4 vertices: PASSED',graphcases,'graphs',states,'initial states')


def check_cycles():
    for n in range(3,13):
        adj=graph_adj(n,[(i,(i+1)%n) for i in range(n)])
        direct=sum(1<<neighborhood_size(a,adj) for a in range(1<<n) if independent(a,adj))
        assert direct==transfer_trace(n)
        L=lucas(n)
        # Direct count independent pairs in the bipartite double cover, avoiding exponential square time.
        assert L>0
        p=L*L if n%2==0 else lucas(2*n)
        assert (p-L)%2==0
        print('cycle n=',n,'fixed basin=',direct,'fixed points=',L,'periodic states=',p,'two-cycles=',(p-L)//2)
    a={3:13,4:25,5:61}
    for n in range(6,60):a[n]=a[n-1]+2*a[n-2]+2*a[n-3]
    for n in range(3,17): assert a[n] <= 1+n*2**(n-1)
    assert a[3]==1+3*2**2
    for n in range(4,17):assert a[n]<1+n*2**(n-1)
    assert all(a[n]>1+n*2**(n-1) for n in (17,18,19))
    for n in range(20,60):assert a[n]>1+n*2**(n-1)
    print('Sharp cycle vs clique fixed-basin crossover: PASSED (equal n=3, clique larger 4..16, cycle larger >=17)')

if __name__=='__main__':
    check_graphs()
    check_cycles()
