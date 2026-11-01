#!/usr/bin/env python3
"""Exact finite combinatorial checks for reversal quotients of real moment-angle path surfaces."""
from itertools import product
from collections import deque

def check(n):
    assert n>=3
    corners=list(product((-1,1),repeat=n))
    corner_set=set(corners)
    rev=lambda s:tuple(reversed(s))
    fixed={s for s in corners if s==rev(s)}
    free=corner_set-fixed
    remaining=set(free)
    comps=[]
    while remaining:
        start=min(remaining); remaining.remove(start)
        todo=deque([start]); z=0
        while todo:
            p=todo.popleft(); z+=1
            for i in range(n):
                q=p[:i]+(-p[i],)+p[i+1:]
                if q in remaining:
                    remaining.remove(q); todo.append(q)
        comps.append(z)
    f0=2**n; f1=n*2**(n-1); f2=(n-1)*2**(n-2)
    chi=f0-f1+f2
    # Boundary circles of R are the 2^(n-2) sign choices at coordinates 1..n-2 (0-based).
    boundary=list(product((-1,1),repeat=n-2))
    pal={s for s in boundary if s==tuple(reversed(s))}
    k=2**((n-1)//2)
    assert len(pal)==k
    # Each fixed arc has two endpoints on distinct fixed boundary circles.
    index=set(pal)
    pair_graph={x:set() for x in pal}
    arcs={}
    for halves in product((-1,1),repeat=(n-1)//2):
        if n%2:
            first=halves # n=2m+1, m pairs
            endpoints=[]
            for v in (-1,1):
                s=first+(v,)+tuple(reversed(first))
                endpoints.append(s[1:-1])
        else:
            first=halves # n=2m, m-1 pairs
            endpoints=[]
            for v in (-1,1):
                s=first+(v,v)+tuple(reversed(first))
                endpoints.append(s[1:-1])
        a,b=endpoints
        assert a!=b and a in index and b in index
        pair_graph[a].add(b); pair_graph[b].add(a)
        arcs.setdefault(tuple(sorted((a,b))),0)
        arcs[tuple(sorted((a,b)))]+=1
    assert len(arcs)==k//2 and set(arcs.values())=={2}
    # Each palindromic boundary-circle orbit folds to an interval and pairs up through arcs;
    # each graph two-edge cycle gives one component of the quotient boundary.
    visited=set();fixed_bdry_components=0
    for p in sorted(pal):
        if p not in visited:
            fixed_bdry_components+=1
            queue=[p];visited.add(p)
            while queue:
                x=queue.pop()
                for y in pair_graph[x]:
                    if y not in visited:
                        visited.add(y);queue.append(y)
    assert fixed_bdry_components==k//2
    bR=len(boundary)
    bQ=(bR-k)//2+fixed_bdry_components
    assert bQ==2**(n-3)
    # Lefschetz/Burnside fixed-cell trace independently yields Euler of the fixed arcs.
    traced_vertices=len(fixed)
    traced_edges=2**((n-1)//2) if n%2 else 0
    traced_squares=-(2**(n//2-1)) if n%2==0 else 0
    lefschetz=traced_vertices-traced_edges+traced_squares
    assert lefschetz==k
    chiQ=(chi+lefschetz)//2
    assert (chi+lefschetz)%2==0
    h=2-chiQ-bQ
    predicted_h=2+(n-4)*2**(n-3)-2**(((n-1)//2)-1)
    assert h==predicted_h
    if n==3:
        assert len(comps)==2 and (h,bQ)==(0,1)
    else:
        assert len(comps)==1 and h>0
    print(f'n={n:2d} cells=({f0},{f1},{f2}) chi_R={chi:6d} '
          f'boundary_R={bR:5d} fixed_arcs={k:3d} nonfixed_corner_components={len(comps)} '
          f'chi_Q={chiQ:6d} boundary_Q={bQ:5d} nonorientable_genus={h:6d}')

for n in range(3,12): check(n)
print('VERIFY_OK')
