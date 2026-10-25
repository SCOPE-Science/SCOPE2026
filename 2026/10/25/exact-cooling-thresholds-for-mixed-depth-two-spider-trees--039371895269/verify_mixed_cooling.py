#!/usr/bin/env python3
"""Independent finite checks of the cooling number on two-depth mixed spiders.

Usage: python verify_mixed_cooling.py
No external packages or data are needed.
"""
from functools import lru_cache
from collections import deque


def mixed_spider(short_arms, long_arms):
    assert short_arms >= 1 and long_arms >= 1 and short_arms + long_arms >= 3
    neighbours=[set()]
    def new(parent):
        v=len(neighbours)
        neighbours.append({parent})
        neighbours[parent].add(v)
        return v
    for _ in range(short_arms):new(0)
    for _ in range(long_arms):new(new(0))
    return neighbours


def exact_process(neighbours):
    """Exhaustively explore original propagation-then-manual process via DP."""
    n=len(neighbours); all_mask=(1<<n)-1
    N=[sum(1<<u for u in nb) for nb in neighbours]
    @lru_cache(None)
    def finish(cooled):
        if cooled==all_mask:return 0
        next_cooled=cooled
        for v in range(n):
            if (cooled>>v)&1: next_cooled |= N[v]
        if next_cooled==all_mask:return 1
        return 1+max(finish(next_cooled|(1<<u)) for u in range(n)
                     if not(next_cooled>>u)&1)
    return max(1+finish(1<<u) for u in range(n))


def independent_distance_certificate(neighbours, target_rounds):
    """Search source sequences via distances, not cooled-set propagation.

    Length target_rounds-1 source tuple with an uncooled survivor at the end
    of that round implies at least target_rounds total rounds.
    """
    n=len(neighbours); distances=[]
    for v in range(n):
        ds=[99]*n;ds[v]=0;todo=deque([v])
        while todo:
            u=todo.popleft()
            for w in neighbours[u]:
                if ds[w]==99:ds[w]=ds[u]+1;todo.append(w)
        distances.append(ds)
    k=target_rounds-1
    def search(prefix):
        t=len(prefix)+1
        if t==k+1:
            return any(all(distances[v][u]>=k-i+1 for i,u in enumerate(prefix,1))
                       for v in range(n) if v not in prefix)
        for v in range(n):
            if v in prefix:continue
            if all(distances[v][u]>=t-i+1 for i,u in enumerate(prefix,1)):
                ans=search(prefix+[v])
                if ans:return True
        return False
    return search([])


def predicted(a,b):
    if b==1:return 3 if a==2 else 4
    if b>=4 or (b==3 and a>=2):return 5
    return 4


def main():
    checks=0;distchecks=0
    for b in range(1,7):
        for a in range(1,7):
            if a+b<3:continue
            g=mixed_spider(a,b); got=exact_process(g); want=predicted(a,b)
            assert got==want,(a,b,got,want)
            checks+=1
            if a<=4 and b<=4:
                for t in (4,5):
                    test=independent_distance_certificate(g,t)
                    assert test==(got>=t),(a,b,t,test,got)
                    distchecks+=1
    print('PROPAGATION_EXACT_CASES',checks)
    print('INDEPENDENT_DISTANCE_THRESHOLD_CHECKS',distchecks)
    for a,b in [(2,1),(3,1),(1,2),(1,3),(2,3),(1,4),(2,4),(1,5)]:
        print('PROFILE',a,b,predicted(a,b))
    print('VERIFY_OK')

if __name__=='__main__':main()
