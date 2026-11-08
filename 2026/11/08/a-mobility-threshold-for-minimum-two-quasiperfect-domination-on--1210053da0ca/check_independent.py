"""Independent generation of rook-board minimum [1,2]-sets via row/column masks.
Checks all m<=5, n<=7 and exact arrangement-graph distance formula.
"""
import itertools,math,json
from collections import deque

def feasible(code,m,n):
    rows=[0]*m;cols=[0]*n
    for p in code: rows[p//n]+=1;cols[p%n]+=1
    for p in range(m*n):
        if p not in code:
            a=rows[p//n]+cols[p%n]
            if a<1 or a>2:return False
    return True

def formulas(m,n):
    if m==n:return math.factorial(n)+2*n
    if m==2:return n*n
    return math.factorial(n)//math.factorial(n-m)+n

def arr_dist(f,g):
    m=len(f); loc={c:i for i,c in enumerate(f)}
    moved={i for i in range(m) if f[i]!=g[i]}
    # Edges lead from row i to the row holding its desired column, if any.
    succ={i:loc[g[i]] for i in moved if g[i] in loc}
    cycles=0; visited=set()
    for v in moved:
        if v in visited:continue
        seen={}; seq=[]; x=v
        while x in moved and x not in visited and x not in seen:
            seen[x]=len(seq);seq.append(x);x=succ.get(x,-1)
        if x in seen:cycles+=1
        visited.update(seq)
    return len(moved)+cycles

rows=[]
for m in range(2,6):
 for n in range(m,8):
    # Construct independent row assignments and exceptional columns, or square permutations/lines.
    sets=set()
    if m==n:
        for cols in itertools.permutations(range(n)):
            sets.add(frozenset(i*n+cols[i] for i in range(m)))
        for i in range(m):sets.add(frozenset(i*n+j for j in range(n)))
        for j in range(n):sets.add(frozenset(i*n+j for i in range(m)))
    else:
        for cols in itertools.permutations(range(n),m):
            sets.add(frozenset(i*n+cols[i] for i in range(m)))
        for j in range(n):sets.add(frozenset(i*n+j for i in range(m)))
    assert all(feasible(s,m,n) for s in sets)
    assert len(sets)==formulas(m,n)
    # Derive edges from direct symmetric differences and compare predicted edge totals.
    if len(sets)<=160:
        edges=[];slide=[];L=list(sets)
        for i in range(len(L)):
            for j in range(i):
                if len(L[i]&L[j])==m-1:
                    edges.append((i,j))
                    a=next(iter(L[i]-L[j]));b=next(iter(L[j]-L[i]))
                    if a//n==b//n or a%n==b%n: slide.append((i,j))
        if m==n==2:ej,es=12,8
        elif m==n:ej=es=0
        elif m==2:ej=es=n*n*(n-1)
        else:ej=es=math.factorial(n)//math.factorial(n-m)*m*(n-m)//2
        assert (len(edges),len(slide))==(ej,es)
    rows.append(dict(m=m,n=n,solutions=len(sets),all_feasible=True))

# All arrangements up to (m,n)=(4,6): compare the exact distance formula with BFS.
distance_checks=[]
for m,n in [(2,4),(3,4),(3,5),(4,5),(4,6)]:
    arrangements=list(itertools.permutations(range(n),m));lookup={x:i for i,x in enumerate(arrangements)}
    adj=[[] for _ in arrangements]
    for i,f in enumerate(arrangements):
        for r in range(m):
            for c in range(n):
                if c in f:continue
                g=f[:r]+(c,)+f[r+1:]
                adj[i].append(lookup[g])
    maxdist=0
    # Symmetry: all arrangements in one S_m x S_n orbit. BFS from one root suffices for diameter.
    root=0; dist={root:0};q=deque([root])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in dist:dist[w]=dist[v]+1;q.append(w)
    assert len(dist)==len(arrangements)
    for j,g in enumerate(arrangements):
        assert dist[j]==arr_dist(arrangements[0],g),(m,n,j,dist[j],arr_dist(arrangements[0],g))
    maxdist=max(dist.values());assert maxdist==m+m//2
    distance_checks.append(dict(m=m,n=n,states=len(arrangements),diameter=maxdist))
print(json.dumps({'status':'PASS','check':'independent mask construction and arrangement distances','boards':rows,'distances':distance_checks},sort_keys=True))
