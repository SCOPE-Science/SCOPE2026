#!/usr/bin/env python3
"""Reproducible exact finite checks for prism power-propagation latency."""
from itertools import combinations
from collections import Counter

BASE = {
    ('same', 1): (1, -1, 2),
    ('same', 2): (2, -1, 3),
    ('same', 3): (2, -1, 4),
    ('cross', 0): (0, -1, 1),
    ('cross', 1): (1, -1, 2),
    ('cross', 2): (1, -1, 3),
}

def adjacency(n):
    graph = []
    for row in (0, 1):
        for col in range(n):
            graph.append({row*n+(col-1)%n, row*n+(col+1)%n,
                          (1-row)*n+col})
    return graph

def rounds(n, seeds, graph):
    active = set(seeds)
    for v in seeds:
        active |= graph[v]
    states = [frozenset(active)]
    while len(active) < 2*n:
        new = set()
        for v in active:
            white = graph[v]-active
            if len(white) == 1:
                new.update(white)
        if not new:
            return None, states
        active |= new
        states.append(frozenset(active))
    return len(states), states  # conventional time 1: N[S]

def typename(a,b,n):
    r1,c1=divmod(a,n)
    r2,c2=divmod(b,n)
    return ('same' if r1==r2 else 'cross',min((c1-c2)%n,(c2-c1)%n))

def expected_time(n):
    return n//2

def inspect(n):
    graph=adjacency(n)
    hist=Counter()
    pdpairs=0
    for s in combinations(range(2*n),2):
        t,states=rounds(n,s,graph)
        tname=typename(*s,n)
        expect=tname in BASE
        assert (t is not None)==expect,(n,s,tname,t)
        if expect:
            pdpairs+=1
            fast=(tname in ({('cross',0),('cross',2)} if n%2 else
                               {('same',1),('same',3),('cross',0),('cross',1),('cross',2)}))
            want=n//2+(not fast)
            assert t==want,(n,s,tname,t,want)
            hist[t]+=1
    assert pdpairs==11*n,(n,pdpairs)
    expected=({n//2:3*n,n//2+1:8*n} if n%2 else
              {n//2:9*n,n//2+1:2*n})
    assert hist==expected,(n,hist,expected)
    for typ,(base_t,left,right) in BASE.items():
        row,d=typ
        seed=(0,d if row=='same' else n+d)
        t,states=rounds(n,seed,graph)
        interval={r*n+(i%n) for r in (0,1) for i in range(left,right+1)}
        assert states[base_t]==interval,(n,typ,base_t)
        for k in range(base_t,t):
            anticipated={r*n+(i%n) for r in (0,1)
                         for i in range(left-(k-base_t),right+(k-base_t)+1)}
            assert states[k]==anticipated,(n,typ,k)
    return pdpairs

if __name__=='__main__':
    total=sum(inspect(n) for n in range(7,51))
    assert all(rounds(n,(0,),adjacency(n))[0] is None for n in range(7,51))
    print('VERIFY_OK n=7..50 all_unordered_pairs every_latency_and_nonforcing checked_pdpairs=%d base_intervals=264 singleton_nonforcing=44' % total)
