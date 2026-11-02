"""Exact finite checks for geodesic second-order many-searcher cover asymptotics.

Python 3, standard library only. Infinite asymptotic theorem is established
analytically in RESULT.md, not by these finite checks.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from random import Random
from collections import deque


def graph_generator(n, weighted_edges):
    Q = [[F(0) for _ in range(n)] for __ in range(n)]
    for a, b, wab, wba in weighted_edges:
        Q[a][b] += F(wab)
        Q[b][a] += F(wba)
    for i in range(n):
        Q[i][i] = -sum(Q[i][j] for j in range(n) if i != j)
    return Q


def matvec(M, v):
    return [sum(x*y for x, y in zip(row,v)) for row in M]


def killed_coeff(Q, start, targets, d):
    out = [i for i in range(len(Q)) if i not in targets]
    R = [[Q[i][j] for j in out] for i in out]
    u = [F(1) for _ in out]
    series = []
    for k in range(1,d+2):
        u = matvec(R,u)
        if k >= d:
            series.append(-u[out.index(start)]/factorial(k))
    return tuple(series)


def shortest_distance(Q,start,targets):
    dist={start:0}; q=deque([start])
    while q:
        u=q.popleft()
        if u in targets: return dist[u]
        for v in range(len(Q)):
            if v!=u and Q[u][v]>0 and v not in dist:
                dist[v]=dist[u]+1; q.append(v)
    raise AssertionError('unreachable')


def path_coeff(Q,start,targets,d):
    n=len(Q)
    weights=[F(0),F(0)]
    waiting=F(0)
    def rec(path,w,k):
        nonlocal waiting
        if k==0:
            if path[-1] in targets:
                if len(path)-1==d:
                    weights[0]+=w
                    waiting+=w*sum(-Q[v][v] for v in path[:-1])
                else:
                    weights[1]+=w
            return
        if path[-1] in targets:return
        i=path[-1]
        for j in range(n):
            if i!=j and Q[i][j]>0:
                rec(path+[j],w*Q[i][j],k-1)
    rec([start],F(1),d)
    rec([start],F(1),d+1)
    return weights[0]/factorial(d),(weights[1]-waiting)/factorial(d+1)


def connected(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    seen={0}; q=[0]
    for x in q:
        for y in adj[x]:
            if y not in seen:seen.add(y);q.append(y)
    return len(seen)==n


def run():
    tests=0
    # Fully enumerate connected simple graphs up to five vertices;
    # test all source/target pairs with graph distance at least two.
    for n in range(3,6):
        possible=list(combinations(range(n),2))
        for bits in range(1,1<<len(possible)):
            edges=[p for k,p in enumerate(possible) if bits>>k &1]
            if not connected(n,edges):continue
            Q=graph_generator(n,[(a,b,1,1) for a,b in edges])
            for st in range(n):
                for tg in range(n):
                    if st==tg:continue
                    d=shortest_distance(Q,st,{tg})
                    if d<2:continue
                    assert killed_coeff(Q,st,{tg},d)==path_coeff(Q,st,{tg},d)
                    tests+=1
    # Weighted asymmetric edges, with multiple equal-distance targets.
    rng=Random(42)
    for _ in range(140):
        n=rng.randint(4,7)
        edges=[(i,i+1) for i in range(n-1)]
        for a,b in combinations(range(n),2):
            if (a,b) not in edges and rng.random()<.17:edges.append((a,b))
        weighted=[(a,b,rng.randint(1,4),rng.randint(1,4)) for a,b in edges]
        Q=graph_generator(n,weighted)
        st=rng.randrange(n)
        dist={j:shortest_distance(Q,st,{j}) for j in range(n) if j!=st}
        d=max(dist.values())
        if d<2:continue
        far=[j for j,k in dist.items() if k==d]
        for r in range(1,min(len(far),3)+1):
            for T in combinations(far,r):
                assert killed_coeff(Q,st,set(T),d)==path_coeff(Q,st,set(T),d)
                tests+=1
    # Four- and five-vertex example with a genuine near target b.
    edges0=[(0,1,1,1),(0,2,1,1),(1,3,1,1)]
    edges1=edges0+[(1,4,1,1)]
    for edges,B in [(edges0,F(-2,3)),(edges1,F(-5,6))]:
        Q=graph_generator(1+max(max(e[:2]) for e in edges),edges)
        A, b=killed_coeff(Q,0,{3},2)
        assert A==F(1,2) and b==B
        assert -b/(2*A*A) == (-2*B)
        tests+=3
    print('PASS:',tests,'exact rational assertions')

if __name__=='__main__':run()
