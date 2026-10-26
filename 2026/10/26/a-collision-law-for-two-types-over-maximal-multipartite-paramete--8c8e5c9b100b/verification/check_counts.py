#!/usr/bin/env python3
"""Independent finite checks of two-point extension counting for maximal multipartite parameters.
Requires Python 3 standard library only. Execution: python verify_henson.py
"""
import itertools
from math import prod

def formula(sizes):
    N=sum(sizes)
    u=(1<<N)-prod((1<<n)-1 for n in sizes)
    bad=sum(prod(4**sizes[j]-3**sizes[j] for j in range(len(sizes)) if j!=i)
            for i in range(len(sizes)))
    nonadj=u*u
    adj=u*u-bad
    return nonadj,adj

def is_K_free(adj, forbidden):
    nv=len(adj)
    for vertices in itertools.combinations(range(nv), forbidden):
        if all((v in adj[u]) for i,u in enumerate(vertices) for v in vertices[i+1:]):
            return False
    return True

def brute(sizes):
    blocks=[];cursor=0
    for n in sizes:
        blocks.append(tuple(range(cursor,cursor+n)))
        cursor+=n
    N=cursor; r=len(sizes)
    graph=[set() for _ in range(N+2)]
    for i,b in enumerate(blocks):
        for j,c in enumerate(blocks):
            if i!=j:
                for u in b:
                    graph[u].update(c)
    outcome=[0,0]
    for maskx in range(1<<N):
        for masky in range(1<<N):
            for edge in (0,1):
                g=[s.copy() for s in graph]
                for u in range(N):
                    if (maskx>>u)&1:
                        g[u].add(N);g[N].add(u)
                    if (masky>>u)&1:
                        g[u].add(N+1);g[N+1].add(u)
                if edge:
                    g[N].add(N+1);g[N+1].add(N)
                if is_K_free(g,r+1):
                    outcome[edge]+=1
    return tuple(outcome)

def main():
    count=0
    for r in range(2,5):
        for sizes in itertools.product(range(1,4),repeat=r):
            if sum(sizes)>6:continue
            actual=brute(sizes)
            expected=formula(sizes)
            assert actual==expected,(sizes,actual,expected)
            count+=1
    print('ALL_TESTS_PASS', 'full_independent_finite_graphs=',count)
    for r in (2,3,4,5):
        for n in (1,2,3,6):
            sizes=(n,)*r
            non,ad=formula(sizes)
            assert 0<=ad<=non
            print('balanced',r,n,'nonadj',non,'adj',ad,'adjacency_share',format(ad/(non+ad),'.9f'))
    print('critical_balanced_limits:')
    for r in (2,3,4,5):
        print(r,'limit',(r-1)/(2*r-1))
if __name__=='__main__':main()
