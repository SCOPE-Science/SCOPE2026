#!/usr/bin/env python3
"""Exact-rational independent check of para-line adjacency-inertia formulas.

Python 3.9+ standard library only. The theorem is proved separately; these
finite calculations are checks, not a proof of the unbounded statement.
"""
from fractions import Fraction
from itertools import combinations
from random import Random

def components_and_bipartite(n, edges):
    nbr = [[] for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < v < n
        nbr[u].append(v)
        nbr[v].append(u)
    color = [None] * n
    components = 0
    for root in range(n):
        if color[root] is not None:
            continue
        components += 1
        color[root] = 0
        todo = [root]
        while todo:
            x = todo.pop()
            for y in nbr[x]:
                if color[y] is None:
                    color[y] = 1 - color[x]
                    todo.append(y)
                elif color[y] == color[x]:
                    return components, False
    return components, True

def is_connected(n, edges):
    nbr=[[] for _ in range(n)]
    for u,v in edges:nbr[u].append(v);nbr[v].append(u)
    seen={0}; todo=[0]
    while todo:
        x=todo.pop()
        for y in nbr[x]:
            if y not in seen:seen.add(y);todo.append(y)
    return len(seen)==n

def para_line_adjacency(n, edges):
    # A vertex in the para-line graph corresponds to an incidence (v,e).
    # Distinct incidences are adjacent when their edges of the subdivision
    # meet: equal original vertex or equal subdivided edge.
    incidences=[]
    for i,(u,v) in enumerate(edges):
        incidences.extend(((u,i),(v,i)))
    s=len(incidences)
    return [[int(i!=j and (incidences[i][0]==incidences[j][0] or
                            incidences[i][1]==incidences[j][1]))
              for j in range(s)] for i in range(s)]

def exact_inertia(a):
    """Exact symmetric congruence, including zero-diagonal 2x2 pivots."""
    a=[[Fraction(v) for v in row] for row in a]
    positive=negative=0
    while a:
        n=len(a)
        diag=next((i for i in range(n) if a[i][i]),None)
        if diag is not None:
            if diag:
                a[diag],a[0]=a[0],a[diag]
                for row in a:row[diag],row[0]=row[0],row[diag]
            d=a[0][0]
            if d>0:positive+=1
            else:negative+=1
            a=[[a[i][j]-a[i][0]*a[0][j]/d for j in range(1,n)]
               for i in range(1,n)]
            continue
        off=next(((i,j) for i in range(n) for j in range(i+1,n) if a[i][j]),None)
        if off is None:break
        i,j=off
        perm=[i,j]+[k for k in range(n) if k!=i and k!=j]
        a=[[a[u][v] for v in perm] for u in perm]
        b=a[0][1]
        positive+=1;negative+=1
        a=[[a[i][j]-(a[i][0]*a[1][j]+a[i][1]*a[0][j])/b
             for j in range(2,n)] for i in range(2,n)]
    return positive,len(a),negative

def prediction(n,m,bipartite):
    if not bipartite:return (n,m-n,m)
    if m==n-1:return (n-1,0,n-1)
    if m==n:return (n-1,2,n-1)
    return (n,m-n+1,m-1)

def check(n,edges):
    assert is_connected(n,edges)
    m=len(edges)
    b=components_and_bipartite(n,edges)[1]
    got=exact_inertia(para_line_adjacency(n,edges))
    want=prediction(n,m,b)
    assert got==want, (n,m,edges,b,got,want)
    assert sum(got)==2*m
    return (n,m,b,got)

def run():
    counts={}
    checked=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        connected=0
        for mask in range(1,1<<len(pairs)):
            es=[e for bit,e in enumerate(pairs) if mask>>bit&1]
            if not is_connected(n,es):continue
            check(n,es); checked+=1;connected+=1
        counts[n]=connected
    assert counts=={2:1,3:4,4:38,5:728}, counts
    print('All connected labelled graphs on 2..5 vertices:',counts)
    # Additional cases designed to include high cyclomatic number, sparse
    # bipartite bicyclic, several nonregular families, and long cycles.
    rng=Random(104729)
    extra=0
    for n in range(6,12):
        pairs=list(combinations(range(n),2))
        for j in range(24):
            p=(j+2)/30
            es=[e for e in pairs if rng.random()<p]
            if not is_connected(n,es):continue
            check(n,es);extra+=1
    for n in range(3,15):
        check(n,[(i,i+1) for i in range(n-1)]+[(0,n-1)]);extra+=1
    for n in range(3,13):
        check(n,[(i,i+1) for i in range(n-1)]);extra+=1
    for n in range(3,12):
        # K_{2,n-2}, including the first bipartite bicyclic base K_{2,3}.
        es=[(i,j) for i in (0,1) for j in range(2,n)]
        check(n,es);extra+=1
    print('Additional sparse/dense connected cases:',extra)
    print('Total independently checked graphs:',checked+extra)
    print('All exact-rational adjacency-inertia comparisons: PASS')
if __name__=='__main__':run()
