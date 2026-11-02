#!/usr/bin/env python3
"""Finite falsification checks for pair-equality shattering by partitions into triples.
Pure Python standard library; all symbols are mathematical, no dependency on external files.
"""
from itertools import combinations
from math import factorial


def partitions_into_triples(vs):
    if not vs:
        yield ()
        return
    a, rest = vs[0], vs[1:]
    for bc in combinations(rest, 2):
        remaining = tuple(x for x in rest if x not in bc)
        for other in partitions_into_triples(remaining):
            yield ((a,)+bc,) + other


def predicted(n, edges):
    adj = [set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    visited = set(); p = q = 0
    for v in range(n):
        if v in visited: continue
        stack = [v]; visited.add(v); verts=[]
        while stack:
            u=stack.pop(); verts.append(u)
            for w in adj[u]:
                if w not in visited: visited.add(w); stack.append(w)
        edge_count = sum(len(adj[u]) for u in verts)//2
        if len(verts)==3 and edge_count==2: p+=1
        elif len(verts)==2 and edge_count==1: q+=1
        elif len(verts)==1:pass
        else:return False
    m=n//3
    return p+q<=m and not (p==m and q==0) and not (p==m-1 and q==1)


def mask_list(n,edges):
    found=set()
    for part in partitions_into_triples(tuple(range(n))):
        blockidx = [0]*n
        for j,block in enumerate(part):
            for x in block:blockidx[x]=j
        found.add(sum((1<<i) for i,(a,b) in enumerate(edges) if blockidx[a]==blockidx[b]))
        if len(found)==1<<len(edges):return len(found)
    return len(found)


def canonical(n,p,q):
    s=[]
    for i in range(p):
        j=3*i; s.extend(((j,j+1),(j,j+2)))
    offset=3*p
    for i in range(q):
        j=offset+2*i; s.append((j,j+1))
    return s


def coefficient(m,j):
    n=3*m; total=0
    for p in range(m+1):
        for q in range(m-p+1):
            if 2*p+q != j:continue
            if (p,q) in ((m,0),(m-1,1)): continue
            total+=factorial(n)//(2**(p+q)*factorial(p)*factorial(q)*factorial(n-3*p-2*q))
    return total


def run():
    representative=0; equalities=0
    for m in range(1,5):
        n=3*m
        for p in range(m+1):
            for q in range(m-p+1):
                es=canonical(n,p,q)
                got=mask_list(n,es)==(1<<len(es))
                expected=predicted(n,es)
                if got!=expected:raise AssertionError((m,p,q,got,expected))
                representative+=1
        assert max(j for j in range(2*m+1) if coefficient(m,j)>0)==max(0,2*m-2)
        equalities+=1

    for m in (1,2):
        n=3*m
        pairs=list(combinations(range(n),2))
        actual=[0]*(len(pairs)+1)
        for s in range(1<<len(pairs)):
            edges=[pair for i,pair in enumerate(pairs) if s>>i&1]
            expected=predicted(n,edges)
            num_concepts=factorial(n)//(factorial(3)**m*factorial(m))
            # More binary traces than concepts is a rigorous cardinality obstruction.
            got = False if (1<<len(edges))>num_concepts else mask_list(n,edges)==(1<<len(edges))
            if got!=expected:raise AssertionError((m,edges,expected,got))
            actual[len(edges)]+=got
        theo=[coefficient(m,j) for j in range(len(pairs)+1)]
        if actual!=theo:raise AssertionError((m,actual,theo))
        print(f'FULL_SUPPORT_CENSUS n={n} supports={1<<len(pairs)} coeffs={[(j,a) for j,a in enumerate(actual) if a]}')
    print(f'CANONICAL_PROFILE_CHECKS_PASS {representative} profiles m=1..4')
    print(f'ALL_TRIPLE_PARTITION_SHATTERING_CHECKS_PASS')

if __name__=='__main__': run()
