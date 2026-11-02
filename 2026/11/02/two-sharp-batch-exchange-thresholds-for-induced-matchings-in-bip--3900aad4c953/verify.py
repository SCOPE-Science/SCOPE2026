"""Independent finite exhaustive checks of induced-matching exchange thresholds.
Run: python3 verify.py
"""
from itertools import combinations
from collections import defaultdict, deque

def graph(m,n):
    L=[('L',i) for i in range(m)]
    R=[('R',j) for j in range(n)]
    X={(i,j):('X',i,j) for i in range(m) for j in range(n)}
    edges=[]
    for i in range(m):
        for j in range(n):
            edges.append((L[i],X[i,j]))
            edges.append((R[j],X[i,j]))
    adj=defaultdict(set)
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    return edges,adj

def exhaustive(m,n):
    edges,adj=graph(m,n)
    k=m+n-2
    good=[]
    for picks in combinations(range(len(edges)),k):
        pairs=[edges[i] for i in picks]
        endpoints=[v for pair in pairs for v in pair]
        if len(set(endpoints)) != 2*k:continue
        if any((a in adj[b] or a in adj[c] or d in adj[b] or d in adj[c])
               for z,(a,d) in enumerate(pairs) for b,c in pairs[z+1:]):
            continue
        good.append(frozenset(picks))
    expected=[]
    for r in range(m):
        for c in range(n):
            exp=set()
            for idx,(a,b) in enumerate(edges):
                if a[0]=='L' and a[1]!=r and b==('X',a[1],c):exp.add(idx)
                if a[0]=='R' and a[1]!=c and b==('X',r,a[1]):exp.add(idx)
            assert len(exp)==k
            expected.append(frozenset(exp))
    assert set(good)==set(expected) and len(good)==m*n,(m,n,len(good),len(expected))
    diffs={}
    for r in range(m):
        for c in range(n):
            for s in range(m):
                for d in range(n):
                    if (r,c)==(s,d):continue
                    dist=len(expected[r*n+c]-expected[s*n+d])
                    theoretical=n if c==d else (m if r==s else k)
                    assert dist==theoretical,(m,n,r,c,s,d,dist,theoretical)
    # Enumerate threshold graph directly from discovered optima; test components.
    for t in range(1,k+1):
        nbr=[[] for _ in good]
        for i in range(len(expected)):
            for j in range(i+1,len(expected)):
                if len(expected[i]-expected[j])<=t:
                    nbr[i].append(j);nbr[j].append(i)
        unseen=set(range(m*n)); sizes=[]
        while unseen:
            start=unseen.pop();queue=[start]
            for v in queue:
                for w in nbr[v]:
                    if w in unseen:
                        unseen.remove(w);queue.append(w)
            sizes.append(len(queue))
        if t<min(m,n):want=[1]*(m*n)
        elif t<max(m,n):want=sorted([max(m,n)]*min(m,n))
        else:want=[m*n]
        assert sorted(sizes)==want,(m,n,t,sorted(sizes),want)
    print(f'EXHAUSTIVE_OK m={m} n={n} edges={len(edges)} optimum_size={k} optima={len(good)} threshold={max(m,n)}')

if __name__=='__main__':
    for m,n in [(3,3),(3,4),(4,3),(3,5),(4,4)]:exhaustive(m,n)
    print('INDEPENDENT_FINITE_CERTIFICATE_OK')
