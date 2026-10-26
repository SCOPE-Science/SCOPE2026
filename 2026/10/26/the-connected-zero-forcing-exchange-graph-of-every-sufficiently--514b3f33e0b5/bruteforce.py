#!/usr/bin/env python3
"""Independent exhaustive check of four-vertex connected forcing sets of prism graphs."""
from itertools import combinations
from collections import Counter, deque
import sys

def exhaustive(n):
    vertices=range(2*n)
    nbr=[{(r*n+(i-1)%n),(r*n+(i+1)%n),((1-r)*n+i)} for r in range(2) for i in range(n)]
    all_vertices=frozenset(vertices)
    def connected(s):
        seen={next(iter(s))};queue=list(seen)
        while queue:
            v=queue.pop()
            for u in nbr[v]&s:
                if u not in seen: seen.add(u);queue.append(u)
        return seen==s
    def forcing(s):
        blue=set(s)
        while True:
            new=set()
            for v in blue:
                white=nbr[v]-blue
                if len(white)==1:new.update(white)
            if not new:return blue==all_vertices
            blue.update(new)
    good=[frozenset(combo) for combo in combinations(vertices,4) if connected(set(combo)) and forcing(combo)]
    assert len(good)==9*n,(n,'count',len(good))
    index=set(good);deg=Counter();pairs=[]
    for a in good:
        neighbors=sum(1 for b in good if len(a&b)==3)
        deg[neighbors]+=1
        pairs.extend((a,b) for b in good if len(a&b)==3 and tuple(sorted(a))<tuple(sorted(b)))
    assert deg==Counter({6:8*n,8:n}),(n,'degrees',deg)
    assert len(pairs)==28*n,(n,'edges',len(pairs))
    adj={s:set() for s in good}
    for a,b in pairs:adj[a].add(b);adj[b].add(a)
    visited={good[0]};queue=deque([good[0]])
    while queue:
        for b in adj[queue.popleft()]:
            if b not in visited:visited.add(b);queue.append(b)
    assert len(visited)==len(good),(n,'components',len(visited))
    # The lower bound check is independent of the structural proof.
    if n<=11:
        for k in (1,2,3):
            assert not any(connected(set(c)) and forcing(c) for c in combinations(vertices,k)),(n,k)
    return {'n':n,'vertices':len(good),'edges':len(pairs),'degrees':dict(sorted(deg.items())),'connected':True}

if __name__=='__main__':
    for n in range(6,int(sys.argv[1])+1):print(exhaustive(n))
