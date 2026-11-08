"""Complete finite checks of minimum 2-quasiperfect rook configurations.
Uses no third-party modules. Run: python check_exhaustive.py
"""
import itertools
import json
from collections import deque
from math import factorial

def valid(S, m, n):
    for i in range(m):
        for j in range(n):
            if (i, j) not in S:
                c = sum((a == i or b == j) for a, b in S)
                if not 1 <= c <= 2:
                    return False
    return True

def predicted(m, n):
    if m > n:
        return {frozenset((j, i) for i,j in s) for s in predicted(n, m)}
    if m == n:
        perms = {frozenset((i, j) for i,j in enumerate(p)) for p in itertools.permutations(range(n))}
        rows = {frozenset((i, j) for j in range(n)) for i in range(n)}
        cols = {frozenset((i, j) for i in range(m)) for j in range(n)}
        return perms | rows | cols
    if m == 2:
        return {frozenset((i, j) for i,j in enumerate(p)) for p in itertools.product(range(n), repeat=m)}
    perms = {frozenset((i, j) for i,j in enumerate(p)) for p in itertools.permutations(range(n), m)}
    cols = {frozenset((i, j) for i in range(m)) for j in range(n)}
    return perms | cols

def stats(states, slide=False):
    sets = sorted(states, key=lambda s:sorted(s))
    N = len(sets)
    adj = [[] for _ in sets]
    for i in range(N):
        for j in range(i):
            if len(sets[i] & sets[j]) != len(sets[i])-1: continue
            if slide:
                a = next(iter(sets[i]-sets[j])); b = next(iter(sets[j]-sets[i]))
                if a[0] != b[0] and a[1] != b[1]: continue
            adj[i].append(j); adj[j].append(i)
    done=set(); components=[]
    for start in range(N):
        if start in done: continue
        pending=[start]; done.add(start); this=[]
        while pending:
            x=pending.pop(); this.append(x)
            for y in adj[x]:
                if y not in done:done.add(y); pending.append(y)
        components.append(this)
    sizes=sorted((len(c) for c in components),reverse=True)
    large=max(components,key=len)
    ecc=[]
    if len(large) > 1:
        for s in large:
            d={s:0}; queue=deque([s])
            while queue:
                x=queue.popleft()
                for y in adj[x]:
                    if y not in d:d[y]=d[x]+1;queue.append(y)
            assert len(d)==len(large)
            ecc.append(max(d.values()))
    return {'states':N,'edges':sum(map(len,adj))//2,'components':len(components),
            'largest_component':sizes[0], 'isolated':sizes.count(1),
            'radius':min(ecc) if ecc else 0,'diameter':max(ecc) if ecc else 0}

def expected(m, n, slide):
    if m==n==2:return dict(states=6,edges=8 if slide else 12,components=1,largest_component=6,isolated=0,radius=2,diameter=2)
    if m==n:
        z=factorial(n)+2*n
        return dict(states=z,edges=0,components=z,largest_component=1,isolated=z,radius=0,diameter=0)
    if m==2:
        return dict(states=n*n,edges=n*n*(n-1),components=1,largest_component=n*n,isolated=0,radius=2,diameter=2)
    count=factorial(n)//factorial(n-m)
    return dict(states=count+n,edges=count*m*(n-m)//2,components=n+1,
                largest_component=count,isolated=n,radius=m+m//2,diameter=m+m//2)

results=[]
for m,n in [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)]:
    board=list(itertools.product(range(m),range(n)))
    # Exhaustive lower bound (all subsets below m are rejected).
    for size in range(m):
        assert all(not valid(set(s),m,n) for s in itertools.combinations(board,size)),(m,n,size)
    solutions={frozenset(s) for s in itertools.combinations(board,m) if valid(set(s),m,n)}
    assert solutions == predicted(m,n),(m,n,len(solutions),len(predicted(m,n)))
    row={'m':m,'n':n,'exhaustive_optimal_count':len(solutions)}
    for slide in (False,True):
        got=stats(solutions,slide)
        assert got==expected(m,n,slide),(m,n,slide,got,expected(m,n,slide))
        row['slide' if slide else 'jump']=got
    results.append(row)
print(json.dumps({'status':'PASS','check':'exhaustive minimum configurations and two reconfigurations','results':results},sort_keys=True))
