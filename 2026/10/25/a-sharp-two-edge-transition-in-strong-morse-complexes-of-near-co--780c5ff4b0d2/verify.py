#!/usr/bin/env python3
"""Standalone finite checks for strong-Morse complexes of near-cliques.

For the one-dimensional graph obtained from a clique by deleting edges
{0,1} and {0,2}, the strong gradient of a vertex order contains v->u
exactly when u is the unique previously seen neighbor of v.
"""
from itertools import permutations
from collections import Counter, deque


def edgekey(x, y):
    return frozenset((x, y))


def expected(n):
    U = range(3, n)
    arcs = {(x,y) for x in range(n) for y in range(n)
            if x != y and edgekey(x,y) not in ({frozenset((0,1)),frozenset((0,2))})}
    p, q = (1,2), (2,1)
    E = set()
    for u in U:
        a,b,c,d,e,f = (0,u),(1,u),(2,u),(u,0),(u,1),(u,2)
        for x,y in ((a,e),(a,f),(a,p),(a,q),(a,b),(a,c),(b,d),(c,d)):
            E.add(edgekey(x,y))
    return arcs, E


def generated(n, full=False):
    no_edges = {edgekey(0,1),edgekey(0,2)}
    V, E, tri = set(), set(), set()
    all_arcs=set()
    for order in permutations(range(n), n if full else min(n,4)):
        prev=[]; selected=[]
        for v in order:
            neighbors=[u for u in prev if edgekey(v,u) not in no_edges]
            if len(neighbors)==1:
                selected.append((v,neighbors[0]))
            prev.append(v)
        if selected:
            all_arcs.update(selected)
            if len(selected)>=2:
                for i in range(len(selected)):
                    for j in range(i+1,len(selected)):
                        E.add(edgekey(selected[i],selected[j]))
            if len(selected)>=3:
                tri.add(frozenset(selected))
    return all_arcs,E,tri


def component_sizes(V,E):
    adj={v:set() for v in V}
    for e in E:
        a,b=tuple(e)
        adj[a].add(b);adj[b].add(a)
    seen=set();sizes=[]
    for start in V:
        if start in seen:continue
        seen.add(start);stack=[start];size=0
        while stack:
            x=stack.pop();size+=1
            for y in adj[x]:
                if y not in seen:seen.add(y);stack.append(y)
        sizes.append(size)
    return sorted(sizes,reverse=True)


def trace_checks(n, V, E):
    U=list(range(3,n));k=len(U)
    perms=[tuple(U)]
    if k>1:perms.append(tuple(U[::-1]))
    if k>2:perms.append(tuple(U[1:]+U[:1]))
    for perm in perms:
        trans={u:v for u,v in zip(U,perm)}
        f=sum(u==trans[u] for u in U)
        for swap in (0,1):
            def g(x):
                if x in trans:return trans[x]
                if swap and x in (1,2):return 3-x
                return x
            def actarc(x):return (g(x[0]),g(x[1]))
            vtrace=sum(actarc(v)==v for v in V)
            etrace=0
            for e in E:
                a,b=tuple(e)
                ga,gb=actarc(a),actarc(b)
                if edgekey(ga,gb)==e:
                    etrace+= 1 if (ga,gb)==(a,b) else -1
            # One connected core plus isolated directed edges among U.
            h0trace=1+f*(f-1)
            h1trace=etrace-vtrace+h0trace
            proposed=(-1 if swap else 1)*(2*f-1)
            assert h1trace==proposed,(n,perm,swap,h1trace,proposed)


def main():
    for n in range(4,12):
        V,E=expected(n)
        observed,edges,tri=generated(n)
        assert observed==V,('vertices',n)
        assert edges==E,('edges',n,edges^E)
        assert not tri,('three matched pairs',n)
        k=n-3
        assert len(V)==n*(n-1)-4
        assert len(E)==8*k
        assert component_sizes(V,E)==[6*k+2]+[1]*(k*(k-1))
        assert len(E)-(6*k+2)+1==2*k-1
        trace_checks(n,V,E)
        if n<=8:
            observed_full,edges_full,tri_full=generated(n,full=True)
            assert observed_full==V and edges_full==E and not tri_full,n
        print('n=%d k=%d directed_vertices=%d one_simplices=%d core_cycles=%d isolated=%d OK'%
              (n,k,len(V),len(E),2*k-1,k*(k-1)))
    print('VERIFY_OK')


if __name__=='__main__':main()
