"""Independent finite checks for leap groups of prisms.

Requires Python 3 and SymPy. Execute: python verify_leap_prisms.py
This program enumerates graph-admissible vertex permutations directly, before
computing the generated group; the mathematical theorem is not based on these
finite tests.
"""
from itertools import combinations
from math import factorial
from sympy.combinatorics import Permutation, PermutationGroup


def connected(n, edges):
    todo={0}; seen=set()
    while todo:
        u=todo.pop()
        if u in seen: continue
        seen.add(u)
        todo.update(v for e in edges if u in e for v in e if v!=u)
    return len(seen)==n


def bipartite(n, edges):
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    col={}
    for root in range(n):
        if root in col:continue
        col[root]=0;queue=[root]
        for u in queue:
            for v in adj[u]:
                if v in col and col[v]==col[u]:return False
                if v not in col:col[v]=1-col[u];queue.append(v)
    return True


def prism_neighbors(n, edges):
    N=2*n
    adj=[set() for _ in range(N)]
    for u,v in edges:
        for j in range(2):
            a,b=2*u+j,2*v+j
            adj[a].add(b);adj[b].add(a)
    for u in range(n):
        a,b=2*u,2*u+1
        adj[a].add(b);adj[b].add(a)
    return adj


def enumerate_hops(adj):
    N=len(adj);f=[0]*N;found=[]
    def visit(i, used):
        if i==N:
            found.append(Permutation(f[:],size=N));return
        for j in adj[i]:
            if not (used>>j)&1:
                f[i]=j;visit(i+1,used|(1<<j))
    visit(0,0)
    return found


def verify_one(n, edges):
    adj=prism_neighbors(n,edges)
    hops=enumerate_hops(adj)
    assert hops
    for p in hops:
        assert sorted(p.array_form)==list(range(2*n))
        assert all(p(i) in adj[i] for i in range(2*n))
    actual=PermutationGroup(hops).order()
    predicted=2*factorial(n)**2 if bipartite(n,edges) else factorial(2*n)
    assert actual==predicted,(n,edges,actual,predicted)
    # Verify each elementary square produces exactly its two diagonal transpositions.
    vert=[2*u+(1-j) for u in range(n) for j in range(2)]
    matching=Permutation(vert)
    assert matching in hops
    for u,v in edges:
        for orientation in (0,1):
            cyc=([2*u,2*v,2*v+1,2*u+1] if orientation==0
                 else [2*u,2*u+1,2*v+1,2*v])
            perm=vert[:]
            for a,b in zip(cyc,cyc[1:]+cyc[:1]):perm[a]=b
            q=Permutation(perm)
            assert q in hops
            difference=q*matching
            supp=[k for k in range(2*n) if difference(k)!=k]
            assert len(supp)==2 and difference(supp[0])==supp[1]
            assert set(supp) in ({2*u,2*v+1},{2*v,2*u+1})
    return len(hops)


def all_connected_small():
    checks=0;total_hops=0
    for n in range(1,5):
        pairs=list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            edges=[e for i,e in enumerate(pairs) if mask>>i&1]
            if not connected(n,edges):continue
            total_hops+=verify_one(n,edges);checks+=1
    return checks,total_hops


def circle(n):
    return sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)})


def cube(d):
    return [(x,x^(1<<i)) for x in range(1<<d) for i in range(d)
            if x < (x^(1<<i))]


if __name__=='__main__':
    checks,hops=all_connected_small()
    more=[(5,circle(5)),(5,[(i,i+1) for i in range(4)]),
          (6,circle(6)),(7,circle(7)),
          (8,cube(3))]
    for n,es in more:
        hops+=verify_one(n,es);checks+=1
    print(f'VERIFY_OK connected_base_graphs={checks} enumerated_hops={hops}')
