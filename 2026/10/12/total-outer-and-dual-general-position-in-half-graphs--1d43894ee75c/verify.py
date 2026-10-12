from itertools import combinations
from collections import deque

def half_graph(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(i,n):
            adj[i].add(n+j)
            adj[n+j].add(i)
    return adj

def distances(adj):
    N=len(adj)
    D=[]
    for s in range(N):
        d=[10**9]*N
        d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1
                    q.append(v)
        D.append(d)
    return D

def positionable(D, X, u, v):
    X=set(X)
    for x in X-{u,v}:
        if D[u][x]+D[x][v]==D[u][v]:
            return False
    return True

def is_general(D,X):
    return all(positionable(D,X,u,v) for u,v in combinations(X,2))

def is_total(D,X):
    N=len(D)
    return all(positionable(D,X,u,v) for u,v in combinations(range(N),2))

def is_outer(D,X):
    X=set(X); N=len(D)
    if not is_general(D,X):
        return False
    for u in X:
        for v in range(N):
            if v not in X and not positionable(D,X,u,v):
                return False
    return True

def is_dual(D,X):
    X=set(X); N=len(D)
    if not is_general(D,X):
        return False
    comp=[v for v in range(N) if v not in X]
    return all(positionable(D,X,u,v) for u,v in combinations(comp,2))

print("VERIFY_OK")
checked=0
for n in range(4,8):
    D=distances(half_graph(n))
    N=2*n
    fams={"total":[], "outer":[], "dual":[]}
    for mask in range(1<<N):
        X=[v for v in range(N) if (mask>>v)&1]
        checked += 1
        if is_total(D,X): fams["total"].append(frozenset(X))
        if is_outer(D,X): fams["outer"].append(frozenset(X))
        if is_dual(D,X): fams["dual"].append(frozenset(X))

    leaves=frozenset({n-1,n})
    expected_outer={
        frozenset({i,n+j})
        for i in range(n)
        for j in range(n)
        if i>j
    }

    for name in fams:
        m=max(map(len,fams[name]), default=0)
        maxs={S for S in fams[name] if len(S)==m}
        if name=="total":
            assert m==2
            assert maxs=={leaves}
        elif name=="outer":
            assert m==2
            assert maxs==expected_outer
        else:
            assert m==2
            assert maxs=={leaves}

    print(f"n={n}: gp_t=2 (1 max set), gp_o=2 ({len(expected_outer)} max sets), gp_d=2 (1 max set)")

print("subsets_checked =",checked)
print("all maximum-set classifications matched the theorem")
