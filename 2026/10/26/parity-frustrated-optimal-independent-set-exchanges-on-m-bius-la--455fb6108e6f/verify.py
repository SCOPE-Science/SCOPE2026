#!/usr/bin/env python3
"""Independent direct checks for maximum-independent-set exchange on Möbius ladders.

Uses only Python standard library. All graphs and configurations are labeled.
No assertion from the paper is used to generate the independent-set census.
"""
from collections import Counter, deque
from itertools import combinations


def graph(n):
    N=2*n
    return tuple(frozenset({(i-1)%N,(i+1)%N,(i+n)%N}) for i in range(N))


def independent(mask,neighbors):
    return all(not(mask & (1<<v) and any(mask & (1<<u) for u in neighbors[v]))
               for v in range(len(neighbors)))


def enumerate_cycle_independent(n):
    # Enumerate independent subsets of the outer cycle first, then test chords
    N=2*n
    acc=[]
    def visit(i,mask):
        if i==N:
            if not ((mask&1) and (mask & (1<<(N-1)))):
                if all(not ((mask&(1<<j)) and (mask&(1<<(j+n)))) for j in range(n)):
                    acc.append(mask)
            return
        visit(i+1,mask)
        if i==0 or not (mask & (1<<(i-1))):
            visit(i+1,mask|(1<<i))
    visit(0,0)
    max_size=max(x.bit_count() for x in acc)
    return sorted(x for x in acc if x.bit_count()==max_size)


def enumerate_matching_choices(n):
    # Distinct algorithm enumerating at most one endpoint of each antipodal chord
    nbr=graph(n)
    best=-1;seen=[]
    def rec(i,mask):
        nonlocal best,seen
        if i==n:
            k=mask.bit_count()
            if k>=best and independent(mask,nbr):
                if k>best: best=k;seen=[]
                seen.append(mask)
            return
        rec(i+1,mask)
        for v in (i,i+n):
            if all(not(mask & (1<<u)) for u in nbr[v]):
                rec(i+1,mask|(1<<v))
    rec(0,0)
    return sorted(seen)


def rotate(mask,shift,n):
    N=2*n; full=(1<<N)-1;shift%=N
    if shift==0:return mask
    return ((mask<<shift)|(mask>>(N-shift)))&full


def expected(n):
    if n%2:
        return sorted(sum(1<<j for j in range(p,2*n,2)) for p in (0,1))
    seed=sum(1<<j for j in range(1,n,2)) + sum(1<<j for j in range(n+2,2*n,2))
    return sorted({rotate(seed,i,n) for i in range(2*n)})


def exchange_edges(states,n,neighbors):
    # Counting by all unordered pairs; no graph theorem assumptions
    edges=set()
    for a,b in combinations(range(len(states)),2):
        x,y=states[a],states[b]
        if (x^y).bit_count()==2:
            edges.add((a,b))
            outgoing=(x&~y).bit_length()-1
            incoming=(y&~x).bit_length()-1
            assert incoming in neighbors[outgoing], 'TJ/TS differ at maximum cardinality'
    return edges


def slide_edges(states,n,neighbors):
    # Independent second construction: direct single-token graph-edge slides
    idx={s:i for i,s in enumerate(states)};edges=set()
    for a,x in enumerate(states):
        for u in range(2*n):
            if not(x&(1<<u)):continue
            for v in neighbors[u]:
                if x&(1<<v):continue
                y=x^(1<<u)^(1<<v)
                if y in idx:
                    b=idx[y]
                    edges.add((min(a,b),max(a,b)))
    return edges


def components(k,edges):
    adj=[set() for _ in range(k)]
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    seen=set();sizes=[]
    for i in range(k):
        if i in seen:continue
        seen.add(i);todo=[i]
        for a in todo:
            for b in adj[a]:
                if b not in seen:seen.add(b);todo.append(b)
        sizes.append(len(todo))
    return sorted(sizes,reverse=True),Counter(map(len,adj))


def check(n):
    nbr=graph(n)
    a=enumerate_cycle_independent(n)
    b=enumerate_matching_choices(n)
    assert a==b,('nonmatching enumerators',n)
    e=expected(n)
    assert a==e,('maximizer classification',n)
    edge1=exchange_edges(a,n,nbr)
    edge2=slide_edges(a,n,nbr)
    assert edge1==edge2,('exchange vs slide',n)
    cs,ds=components(len(a),edge1)
    if n%2:
        assert len(a)==2 and a[0].bit_count()==n
        assert not edge1 and cs==[1,1] and ds==Counter({0:2})
    else:
        assert len(a)==2*n and a[0].bit_count()==n-1
        assert len(edge1)==2*n and cs==[2*n] and ds==Counter({2:2*n})
        seed=e[0]
        for r in range(2*n):
            x=rotate(seed,r,n)
            i=a.index(x)
            targets={rotate(x,n-1,n),rotate(x,n+1,n)}
            actual={a[v if u==i else u] for u,v in edge1 if i in (u,v)}
            assert actual==targets, ('explicit rotation move',n,r)
    print(f'M{2*n}: alpha={a[0].bit_count()} minima={len(a)} exchange_edges={len(edge1)} components={cs} CHECK_OK')

if __name__=='__main__':
    for n in range(3,16):check(n)
    print('VERIFY_OK')
