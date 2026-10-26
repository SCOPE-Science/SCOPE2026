#!/usr/bin/env python3
"""Finite independent checks for maximum induced-matching exchanges of prisms.

Run with Python 3.9+ using: python verify.py
The mathematical infinite-family classification is proved separately.
"""
from collections import Counter, deque
from functools import lru_cache


def prism(n):
    """Return the labeled graph and its edges (upper, lower, rungs)."""
    vertices = set(range(2*n))
    upper = [(i, (i+1)%n) for i in range(n)]
    lower = [(n+i, n+(i+1)%n) for i in range(n)]
    rungs = [(i, n+i) for i in range(n)]
    edges = upper + lower + rungs
    adjacency = [set() for _ in vertices]
    for a,b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    return edges, adjacency


def conflict(n):
    """Construct conflict masks from induced 2-edge subgraphs, independently."""
    edges, adj = prism(n)
    masks = []
    for j,(a,b) in enumerate(edges):
        cl = 0
        for h,(c,d) in enumerate(edges):
            if j == h or c in (a,b) or d in (a,b) or c in adj[a] or d in adj[a] or c in adj[b] or d in adj[b]:
                cl |= 1<<h
        masks.append(cl)
    return edges, masks


def enumerate_optima(n):
    """Exact branch-and-bound maximum independent-set search in L(P_n)^2."""
    edges, cm = conflict(n)
    m = len(edges)
    full = (1<<m)-1
    @lru_cache(maxsize=None)
    def opt(available):
        if not available:
            return 0
        b = max((1<<i for i in range(m) if available & (1<<i)),
                key=lambda x: (cm[x.bit_length()-1] & available).bit_count())
        return max(opt(available^b), 1+opt(available & ~cm[b.bit_length()-1]))
    maximum = opt(full)
    solutions = set()
    def collect(available, chosen, needed):
        if needed == 0:
            solutions.add(chosen)
            return
        if not available or opt(available)<needed:
            return
        b = max((1<<i for i in range(m) if available & (1<<i)),
                key=lambda x: (cm[x.bit_length()-1] & available).bit_count())
        without = available^b
        if opt(without)>=needed:
            collect(without,chosen,needed)
        with_b = available & ~cm[b.bit_length()-1]
        if opt(with_b)>=needed-1:
            collect(with_b,chosen|b,needed-1)
    collect(full,0,maximum)
    return maximum,solutions


def proposed_labels(n):
    """Generate symbolic families using different construction than search."""
    es, _ = prism(n)
    index = {frozenset(e):i for i,e in enumerate(es)}
    def edge_mask(choices):
        ans=0
        for a,b in choices:
            ans |= 1<<index[frozenset((a,b))]
        return ans
    families={}
    def add(label, choices):
        mask=edge_mask(choices)
        assert mask not in families, (n,label,families.get(mask))
        families[mask]=label
    def rung(i):return (i%n,n+i%n)
    def rail(row,i):
        return ((i%n)+row*n,((i+1)%n)+row*n)
    if n%2==0:
        for parity in (0,1):
            add(('R',parity),[rung(i) for i in range(parity,n,2)])
        if n%4==0:
            for offset in (0,1):
                for row in (0,1):
                    add(('A',offset,row),
                        [rail(row^(t%2),offset+2*t) for t in range(n//2)])
    else:
        k=(n-1)//2
        for i in range(n):
            add(('R',i),[rung(i+2+2*t) for t in range(k)])
            for ell in range(1,k+1):
                for s in (0,1):
                    edges=[rail(s^(t%2),i+2*t) for t in range(ell)]
                    edges += [rung(i+2*ell+1+2*t) for t in range(k-ell)]
                    add(('F',i,ell,s),edges)
    return families


def predicted_odd_neighbors(n,label):
    k=(n-1)//2
    if label[0]=='R':
        i=label[1]
        return {('R',(i+2)%n),('R',(i-2)%n)} | {
            ('F',(i+d)%n,1,s) for d in (-1,1) for s in (0,1)}
    _,i,ell,s=label
    if ell==1:
        return {('R',(i-1)%n),('R',(i+1)%n),
                ('F',i,1,1-s),('F',i,2,s),
                ('F',(i-2)%n,2,1-s)}
    if ell==k:
        return {('F',i,k-1,s),('F',(i+2)%n,k-1,1-s),
                ('F',(i+2)%n,k,1-s),('F',(i-2)%n,k,1-s)}
    return {('F',i,ell-1,s),('F',i,ell+1,s),
            ('F',(i+2)%n,ell-1,1-s),('F',(i-2)%n,ell+1,1-s)}


def check(n):
    maximum,solution=enumerate_optima(n)
    labels=proposed_labels(n)
    assert maximum==n//2,(n,'maximum',maximum)
    assert solution==set(labels),(n,'classification',len(solution),len(labels))
    neighbors={mask:set() for mask in solution}
    for mask in solution:
        for j in range(3*n):
            if mask>>j&1:
                continue
            for i in range(3*n):
                if (mask>>i)&1:
                    m=(mask^(1<<i))|(1<<j)
                    if m in solution:
                        neighbors[mask].add(m)
    spectra=Counter(len(x) for x in neighbors.values())
    seen=set();components=[]
    for a in solution:
        if a in seen:continue
        seen.add(a);stack=[a];cnt=0
        while stack:
            v=stack.pop();cnt+=1
            for w in neighbors[v]:
                if w not in seen:seen.add(w);stack.append(w)
        components.append(cnt)
    components.sort(reverse=True)
    e=sum(map(len,neighbors.values()))//2
    if n%2==0:
        expected=6 if n%4==0 else 2
        assert len(solution)==expected
        assert spectra=={0:expected}
        assert e==0 and components==[1]*expected
    else:
        expected=n*n
        assert len(solution)==expected
        assert e==2*n*(n+1)
        assert spectra=={4:n*(n-3),5:2*n,6:n}
        assert components==[n*n]
        for a,lab in labels.items():
            calculated={labels[b] for b in neighbors[a]}
            assert calculated==predicted_odd_neighbors(n,lab),(n,lab,calculated)
    print('CHECK_OK',n,'alpha',maximum,'states',len(solution),
          'exchange_edges',e,'degree_spectrum',dict(sorted(spectra.items())),
          'components',components,flush=True)


if __name__=='__main__':
    for order in range(4,20):
        check(order)
    print('ALL_VERIFY_OK')
