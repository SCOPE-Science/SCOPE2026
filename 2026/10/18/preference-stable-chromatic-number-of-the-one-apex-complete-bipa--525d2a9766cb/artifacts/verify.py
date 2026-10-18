#!/usr/bin/env python3
"""Exhaustive finite checks for a preference-stable coloring theorem.
Only mathematical data and verification; no network access is required.
"""
from itertools import product


def is_acyclic(edges, n):
    indeg = [0]*n
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);indeg[v]+=1
    todo=[u for u in range(n) if indeg[u]==0]; visited=0
    while todo:
        u=todo.pop();visited+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:todo.append(v)
    return visited==n

def preferences(a,b):
    # Palette 0..b. For every i=0..b-1, one vertex in each
    # bipartition class ranks i first and b second.
    q=b+1; pre=[]
    for j in range(a):
        i=j%b;pre.append([i,b]+[x for x in range(q) if x not in (i,b)])
    for j in range(b):
        pre.append([j,b]+[x for x in range(q) if x not in (j,b)])
    pre.append(list(range(q)))
    return pre

def count_stable(a,b,verbose=True):
    q=b+1; n=a+b+1
    prefs=preferences(a,b)
    pos=[{c:i for i,c in enumerate(row)} for row in prefs]
    proper=0; stable=0
    # Color the universal vertex first, then the two parts.
    for col_u in range(q):
        rem=[x for x in range(q) if x!=col_u]
        for left in product(rem, repeat=a):
            seen=set(left)
            if len(seen)==q-1: continue
            rcolors=[x for x in rem if x not in seen]
            if not rcolors:continue
            for right in product(rcolors,repeat=b):
                c=(*left,*right,col_u); proper+=1
                edges=[(u,v) for u in range(n) for v in range(n)
                       if u!=v and pos[u][c[v]]<pos[u][c[u]]]
                if is_acyclic(edges,n):stable+=1
    if verbose:print(f'K_{{{a},{b},1}}, {q} colors: proper={proper}, stable={stable}')
    assert proper>0 and stable==0
    return proper,stable

if __name__=='__main__':
    for b in range(2,4):
        for a in range(b,b+3):
            count_stable(a,b)
    print('ALL_FINITE_CHECKS_PASS')

# Additional independent upper-bound checks for arbitrary random preferences.
def greedy_upper(a,b,profile):
    q=b+2;n=a+b+1
    remaining=set(range(q)); colors=[None]*n
    for v in [n-1]+list(range(a,a+b)):
        choice=min(remaining,key=lambda c:profile[v].index(c))
        colors[v]=choice;remaining.remove(choice)
    assert len(remaining)==1
    last=next(iter(remaining))
    for v in range(a):colors[v]=last
    return colors

def upper_checks():
    import random
    rng=random.Random(27182818)
    checks=0
    for a,b in [(1,1),(2,1),(2,2),(3,2),(3,3),(4,3),(5,4)]:
        k=b+2;n=a+b+1
        for _ in range(100):
            pre=[]
            for v in range(n):
                x=list(range(k));rng.shuffle(x);pre.append(x)
            col=greedy_upper(a,b,pre)
            assert len({col[i] for i in range(a)})==1
            assert len(set(col[:a]).intersection(col[a:a+b]))==0
            assert col[-1] not in col[:-1]
            positions=[{c:j for j,c in enumerate(rank)} for rank in pre]
            arc=[(u,v) for u in range(n) for v in range(n)
                 if u!=v and positions[u][col[v]]<positions[u][col[u]]]
            assert is_acyclic(arc,n)
            checks+=1
    print(f'GREEDY_UPPER_CHECKS_PASS; profiles={checks}')

if __name__=='__main__': upper_checks()
