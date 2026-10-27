"""Independent checks of ladder geodesic-transversal counting formulas.

Uses graph distances and explicit shortest-path enumeration to construct all
maximal geodesics, then exhaustively tests subsets. No external dependencies.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb


def ladder_paths(n):
    N = 2 * n
    adj = [[] for _ in range(N)]
    for row in range(2):
        for j in range(n - 1):
            u, v = row*n+j, row*n+j+1
            adj[u].append(v)
            adj[v].append(u)
    for j in range(n):
        adj[j].append(n + j)
        adj[n + j].append(j)
    paths = set()
    for src in range(N):
        dist = [-1]*N
        dist[src] = 0
        todo=deque([src])
        while todo:
            u=todo.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v]=dist[u]+1
                    todo.append(v)
        for dst in range(src+1,N):
            def rec(path):
                u=path[-1]
                if u==dst:
                    paths.add(tuple(path))
                    return
                for v in adj[u]:
                    if dist[v]==dist[u]+1:
                        rec(path+[v])
            rec([src])
    def included(p,q):
        return any(tuple(q[i:i+len(p)])==p or
                   tuple(reversed(q[i:i+len(p)]))==p
                   for i in range(len(q)-len(p)+1))
    maxpaths=[p for p in paths if not any(len(q)>len(p) and included(p,q) for q in paths)]
    return maxpaths


def formula(n):
    # polynomial ((1+z)^n-1)^2 + 2z^2(1+z)^(n-2)
    #            - 2z^2 sum_(j=0)^(n-3) (j+1)(1+z)^j.
    A=Counter()
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i+j]+=comb(n,i)*comb(n,j)
    for j in range(n-1):
        A[j+2]+=2*comb(n-2,j)
    for j in range(max(0,n-2)):
        for k in range(j+1):
            A[k+2]-=2*(j+1)*comb(j,k)
    return +A


def check():
    checked=0
    successful=0
    for n in range(2,9):
        paths=ladder_paths(n)
        masks=[sum(1 << v for v in p) for p in paths]
        assert len(masks)==2*n,(n,len(masks))
        # The proposed 2n corner-to-corner geodesics, with switch at each rung.
        expected=set()
        for c in range(n):
            expected.add(sum(1<<v for v in list(range(c+1))+list(range(n+c,2*n))))
            expected.add(sum(1<<v for v in list(range(n,n+c+1))+list(range(c,n))))
        assert set(masks)==expected,(n,len(expected),len(set(masks)))
        actual=Counter()
        minimal=Counter()
        for S in range(1 << (2*n)):
            good=all(S & m for m in masks)
            b=[j+1 for j in range(n) if (S>>j)&1]
            t=[j+1 for j in range(n) if (S>>(n+j))&1]
            predicted=((min(b) if b else n+1) <= (max(t) if t else 0)+1
                       and (min(t) if t else n+1) <= (max(b) if b else 0)+1)
            assert good==predicted,(n,S,good,predicted)
            if good:
                successful+=1
                actual[S.bit_count()]+=1
                if all(not all((S ^ (1<<v)) & m for m in masks)
                       for v in range(2*n) if S & (1<<v)):
                    minimal[S.bit_count()]+=1
        target=Counter({2:3*n})
        if n>=6:
            target[3]=n*(n-4)*(n-5)//3
        assert actual == formula(n), (n,actual,formula(n))
        assert minimal==target,(n,minimal,target)
        checked+=1
    print('ALL_LADDER_CHECKS_PASS', 'orders=2..8', 'graphs=',checked,
          'successful_sets=',successful, 'maximal_geodesics=2n')


if __name__=='__main__':
    check()
