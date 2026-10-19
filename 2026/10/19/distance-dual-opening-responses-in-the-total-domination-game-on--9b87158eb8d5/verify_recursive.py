"""Independent recursive checker for game total domination of G(10,2) and G(10,3).
Python 3 standard library only; run: python3 verify_recursive.py
"""
from functools import lru_cache
from collections import Counter, deque

def generalized_petersen(k):
    graph = [set() for _ in range(20)]
    for i in range(10):
        for u,v in [(i,(i+1)%10),(i,i+10),(i+10,10+(i+k)%10)]:
            graph[u].add(v)
            graph[v].add(u)
    return graph

def examine(name,k,expected,table):
    adj=generalized_petersen(k)
    N=[sum(1<<j for j in sorted(neigh)) for neigh in adj]
    whole=(1<<20)-1
    @lru_cache(None)
    def solve(dominated,chooser):
        if dominated==whole: return 0
        outcomes=[]
        for nbrs in N:
            if nbrs&~dominated:
                outcomes.append(1+solve(dominated|nbrs,1-chooser))
        return min(outcomes) if chooser==0 else max(outcomes)
    assert (solve(0,0),solve(0,1))==expected
    assert all(1+solve(N[i],1)==expected[0] and 1+solve(N[i],0)==expected[1] for i in range(20))
    print(f'{name} D={solve(0,0)} S={solve(0,1)}')
    for distance in range(1,6):
        nsets=Counter()
        for first in range(20):
            dist=[-1]*20;dist[first]=0;que=deque([first])
            while que:
                x=que.popleft()
                for y in adj[x]:
                    if dist[y]<0:
                        dist[y]=dist[x]+1;que.append(y)
            eligible=[second for second in range(20) if dist[second]==distance]
            assert len(eligible)==table[distance-1][0]
            for second in eligible:
                assert N[second]&~N[first]
                mask=N[first]|N[second]
                vals=(2+solve(mask,0),2+solve(mask,1))
                nsets[vals]+=1
        assert len(nsets)==1
        (dstart,sstart),freq=nsets.popitem()
        assert freq==20*table[distance-1][0]
        assert (dstart,sstart)==tuple(table[distance-1][1:])
        print(f'distance {distance} count_per_first={freq//20} forced_Dstart={dstart} forced_Sstart={sstart}')
    print(f'{name} ALL_380_ORDERED_PAIRS_CHECKED')

examine('DODECAHEDRON',2,(11,10),[(3,10,11),(6,11,11),(6,10,11),(3,10,11),(1,10,10)])
examine('DESARGUES',3,(10,10),[(3,10,10),(6,10,10),(6,10,10),(3,10,10),(1,10,10)])
print('VERIFY_OK')
