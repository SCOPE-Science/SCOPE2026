#!/usr/bin/env python3
"""Independent finite checks for the rook-graph zero-forcing classification.

Runs with Python 3 standard library; no external data or packages.
"""
from collections import deque
from math import comb


def stirling(n, k):
    table = [[0]*(k+1) for _ in range(n+1)]
    table[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i,k)+1):
            table[i][j] = j*table[i-1][j] + table[i-1][j-1]
    return table[n][k]


def factorial(n):
    p=1
    for x in range(2,n+1): p*=x
    return p


def minimum_set_formula(m,n):
    return (m*(m-1)**(n-1)*(n**(m-2)-factorial(n)*stirling(m-2,n))
          + n*(n-1)**(m-1)*(m**(n-2)-factorial(m)*stirling(n-2,m)))


def rook_masks(m,n):
    rows=[sum(1<<(r*n+c) for c in range(n)) for r in range(m)]
    cols=[sum(1<<(r*n+c) for r in range(m)) for c in range(n)]
    neighbors=[]
    for r in range(m):
        for c in range(n):
            neighbors.append((rows[r]|cols[c]) ^ (1<<(r*n+c)))
    return rows,cols,neighbors


def force_serial(white,neighbors):
    """An explicit chronological force: scan blue cells and remove one white neighbor."""
    mask=(1<<len(neighbors))-1
    while white:
        advanced=False
        for v in range(len(neighbors)):
            if white&(1<<v): continue
            touches=white&neighbors[v]
            if touches and not(touches & (touches-1)):
                white ^= touches
                advanced=True
                break
        if not advanced: return False
    return True


def force_simultaneous(white,m,n):
    """Independent implementation from row/column occupancy counts (parallel rounds)."""
    a=[[bool(white & (1<<(r*n+c))) for c in range(n)] for r in range(m)]
    while True:
        if not any(any(row) for row in a): return True
        rowdegrees=[sum(row) for row in a]
        coldegrees=[sum(a[r][c] for r in range(m)) for c in range(n)]
        to_remove=set()
        for r in range(m):
            for c in range(n):
                if a[r][c]: continue
                if rowdegrees[r]+coldegrees[c] != 1: continue
                for x in range(n):
                    if a[r][x]: to_remove.add((r,x))
                for x in range(m):
                    if a[x][c]: to_remove.add((x,c))
        if not to_remove: return False
        for r,c in to_remove: a[r][c]=False


def forest_leaf_criterion(white,m,n,rows,cols):
    if not white: return True
    rd=[(white&mask).bit_count() for mask in rows]
    cd=[(white&mask).bit_count() for mask in cols]
    if not ((0 in rd and 1 in cd) or (0 in cd and 1 in rd)):
        return False
    # Independent cycle detection by disjoint-set union on a bipartite root graph.
    parent=list(range(m+n))
    def root(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    for r in range(m):
        for c in range(n):
            if not(white & (1<<(r*n+c))): continue
            x,y=root(r),root(m+c)
            if x==y:return False
            parent[x]=y
    return True


def exchange_stats(minimum_sets,ncells):
    index={v:i for i,v in enumerate(minimum_sets)}
    neighbors=[set() for _ in minimum_sets]
    for i,mask in enumerate(minimum_sets):
        a=[j for j in range(ncells) if mask & (1<<j)]
        b=[j for j in range(ncells) if not (mask & (1<<j))]
        for u in a:
            for v in b:
                t=mask ^ (1<<u) ^ (1<<v)
                if t in index:neighbors[i].add(index[t])
    for i,near in enumerate(neighbors):
        assert all(i in neighbors[j] for j in near)
    seen=set();sizes=[]
    for i in range(len(neighbors)):
        if i in seen:continue
        todo=[i];seen.add(i)
        for j in todo:
            for k in neighbors[j]:
                if k not in seen:seen.add(k);todo.append(k)
        sizes.append(len(todo))
    return sorted(sizes,reverse=True),sum(map(len,neighbors))//2


def complete_test(m,n):
    rows,cols,neighbors=rook_masks(m,n)
    best=m*n+1;minima=[];count=0
    for white in range(1<<(m*n)):
        a=force_serial(white,neighbors)
        b=force_simultaneous(white,m,n)
        c=forest_leaf_criterion(white,m,n,rows,cols)
        assert a==b==c, (m,n,white,a,b,c)
        if not a:continue
        count+=1
        size=m*n-white.bit_count()
        if size<best:best=size;minima=[white]
        elif size==best:minima.append(white)
    assert best==m*n-m-n+2,(m,n,best)
    assert len(minima)==minimum_set_formula(m,n),(m,n,len(minima))
    sizes,edges=exchange_stats(minima,m*n)
    if min(m,n)>=3 or (m,n) in ((2,2),(2,3),(3,2)):
        assert sizes==[len(minima)],(m,n,sizes)
    else:
        t=max(m,n)
        assert sizes==[1+t*(t-1)]*2,(m,n,sizes)
        assert edges==2*t*(t-1)**2,(m,n,edges)
    print('FULL',m,n,'all_white_masks',1<<(m*n),'zero_forcing_sets',count,
          'minimum',best,'minimum_count',len(minima),'components',sizes,
          'exchange_edges',edges,flush=True)


def thin_isomorphism(t):
    # White complements of min sets of K_t square K_2, t>=4.
    patterns=[];labels=[]
    for c in range(2):
        hub=sum(1<<(2*r+c) for r in range(t))
        patterns.append(hub);labels.append((c,'apex'))
        for a in range(t):
            for b in range(t):
                if a==b:continue
                mask=(hub ^ (1<<(2*a+c))) | (1<<(2*b+1-c))
                patterns.append(mask);labels.append((c,(a,b)))
    assert len(set(patterns))==len(patterns)
    for i in range(len(patterns)):
        ci,li=labels[i]
        for j in range(i+1,len(patterns)):
            cj,lj=labels[j]
            actual=(patterns[i]^patterns[j]).bit_count()==2
            expected=(ci==cj and (li=='apex' or lj=='apex'
                        or (li[0]==lj[0] or li[1]==lj[1])))
            assert actual==expected,(t,labels[i],labels[j])
    rows,cols,neighbors=rook_masks(t,2)
    assert all(force_serial(w,neighbors) and w.bit_count()==t for w in patterns)
    assert len(patterns)==minimum_set_formula(t,2)
    print('THIN_ISOMORPHISM',t,'each_component_is_K1_join_line_graph_of_crown',
          'component_vertices',1+t*(t-1),flush=True)

if __name__=='__main__':
    for dimensions in ((2,2),(2,3),(2,4),(2,5),(2,6),(2,7),
                       (3,3),(3,4),(3,5),(4,4)):
        complete_test(*dimensions)
    for t in range(4,13): thin_isomorphism(t)
    print('VERIFY_OK')
