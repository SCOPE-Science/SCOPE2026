#!/usr/bin/env python3
"""Finite definition and construction checks for rectangular cycle-product MEG sets.

Only the standard library is used. Proof for all dimensions is in RESULT.md;
these finite calculations test definitions and exceptional constructions.
"""
from collections import deque
from itertools import combinations


def cycle_gap_ok(vertices, order):
    s = sorted(vertices)
    if len(s) < 2 or len(s) != len(set(s)):
        return False
    steps = [s[i + 1] - s[i] for i in range(len(s)-1)]
    steps.append(s[0] + order - s[-1])
    return all(2*step < order for step in steps)


def direct_cycle_meg(vertices, order):
    """Test edge monitoring via actual uniquely shortest arcs, not gap sizes."""
    covered = set()
    for a,b in combinations(sorted(vertices), 2):
        clockwise = b-a
        other = order-clockwise
        if clockwise < other:
            covered.update(range(a,b))
        elif other < clockwise:
            covered.update(k % order for k in range(b,a+order))
    return len(covered) == order


def columns(m,n):
    assert 5 <= m <= n
    if (m,n)==(5,6):
        return [set(range(5)) - ({0,2} if j%2 == 0 else {1,3})
                for j in range(n)]
    if (m,n)==(7,8):
        # The eight columns are written out because the balanced-floor
        # construction needs two local replacements at this boundary.
        return [set(v) for v in ((0,2,4),(2,4,6),(1,3,5),(0,2,5),
                                 (1,4,6),(0,3,5),(2,4,6),(1,3,5))]
    t=(0,m//3,(2*m)//3)
    return [{(x - (m*j//n)) % m for x in t} for j in range(n)]


def fiber_certificate(m,n,col):
    if len(col)!=n or any(len(c)!=3 or not cycle_gap_ok(c,m) for c in col):
        return False
    return all(cycle_gap_ok([j for j in range(n) if i in col[j]],n)
               for i in range(m))


def make_graph(m,n):
    N=m*n
    graph=[set() for _ in range(N)]
    for i in range(m):
        for j in range(n):
            u=i*n+j
            for v in [((i+1)%m)*n+j,i*n+(j+1)%n]:
                graph[u].add(v)
                graph[v].add(u)
    return graph


def bfs(adj, src, excluded=None):
    distances=[-1]*len(adj)
    distances[src]=0
    queue=deque([src])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if excluded and ((u,v)==excluded or (v,u)==excluded):
                continue
            if distances[v]<0:
                distances[v]=distances[u]+1
                queue.append(v)
    return distances


def direct_product_meg(m,n,col):
    """For each edge, delete it and compare distances between probe pairs."""
    graph=make_graph(m,n)
    chosen=[i*n+j for j in range(n) for i in sorted(col[j])]
    baseline={s:bfs(graph,s) for s in chosen}
    edges={(min(u,v),max(u,v)) for u in range(m*n) for v in graph[u]}
    for edge in sorted(edges):
        monitored=False
        for s in chosen:
            after=bfs(graph,s,edge)
            if any(after[t]>baseline[s][t] for t in chosen):
                monitored=True
                break
        if not monitored:
            return False, edge
    return True, len(edges)


def main():
    subset_count=0
    for k in range(5,13):
        for mask in range(1 << k):
            group=[i for i in range(k) if (mask>>i)&1]
            assert cycle_gap_ok(group,k)==direct_cycle_meg(group,k),(k,mask)
            subset_count+=1
    print('Cycle gap criterion independently checked on',subset_count,'subsets (orders 5..12).')

    bad=[]
    for m in range(5,12):
        for n in range(m,12):
            g=(m+2)//3
            bound=1+((g-1)*n+m-1)//m
            if 2*bound>=n:
                bad.append((m,n))
    assert bad==[(5,6),(7,8)],bad
    print('All small arithmetic exceptions are exactly',bad)

    count=0
    for m in range(5,71):
        for n in range(m, min(3*m+1,211)):
            col=columns(m,n)
            assert fiber_certificate(m,n,col),(m,n)
            assert sum(map(len,col))==3*n
            count+=1
    print('Fiber certificates verified for',count,'pairs: 5<=m<=70, m<=n<min(3m+1,211).')

    for m,n in [(5,5),(5,6),(5,7),(6,7),(7,8),(7,9),(8,11),(9,12)]:
        col=columns(m,n)
        yes,count_edges=direct_product_meg(m,n,col)
        assert yes,(m,n,count_edges)
        print('Direct edge-deletion distance test passed for (%d,%d): %d edges, %d probes.' %
              (m,n,count_edges,3*n))
    print('All checks passed (finite verification is not an infinite proof).')

if __name__=='__main__':
    main()
