from itertools import combinations, product
from collections import deque

def connected(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    seen={0}; q=[0]
    for u in q:
        for v in adj[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    return len(seen)==n, adj

def bfs_tree(adj):
    n=len(adj); par=[-1]*n; par[0]=0; q=deque([0])
    while q:
        u=q.popleft()
        for v in sorted(adj[u]):
            if par[v]<0:
                par[v]=u; q.append(v)
    T=[set() for _ in range(n)]
    for v in range(1,n):
        u=par[v]; T[u].add(v); T[v].add(u)
    return T

def tree_square_matching(T):
    # Greedy induction: repeatedly use an endpoint x of a diameter and its neighbor v.
    A=[set(s) for s in T]
    alive={i for i in range(len(A))}
    pairs=[]
    while len(alive)>=2:
        start=next(iter(alive))
        def farthest(s):
            dist={s:0}; par={s:None}; q=deque([s])
            while q:
                u=q.popleft()
                for w in A[u]:
                    if w in alive and w not in dist:
                        dist[w]=dist[u]+1; par[w]=u; q.append(w)
            z=max(dist, key=lambda x:(dist[x],x))
            return z,par,dist
        x,_,_=farthest(start)
        y,par,_=farthest(x)
        if len(alive)==2:
            other=next(v for v in alive if v!=x)
            pairs.append((x,other)); alive.clear(); break
        v=par[y]  # neighbor of diameter endpoint y toward x
        leaves=[w for w in A[v] if w in alive and len(A[w]&alive)==1]
        if len(leaves)>=2:
            a,b=leaves[0],leaves[1]
            pairs.append((a,b))
            for z in (a,b):
                alive.remove(z)
        else:
            # Diameter-neighbor v has exactly one leaf child y; pair them.
            a=y; b=v
            pairs.append((a,b))
            alive.remove(a); alive.remove(b)
    unmatched=next(iter(alive)) if alive else None
    return pairs,unmatched

def corona_adj(base):
    n=len(base); adj=[set() for _ in range(2*n)]
    for u in range(n):
        for v in base[u]:
            adj[u].add(v)
        adj[u].add(n+u); adj[n+u].add(u)
    return adj

def is_dominating(adj,S):
    S=set(S)
    return all(v in S or bool(adj[v]&S) for v in range(len(adj)))

def dist_le2(adj,u,v):
    return v in adj[u] or bool(adj[u]&adj[v])

def has_pairing(adj,S):
    S=tuple(sorted(S)); memo={}
    def rec(R):
        if not R: return True
        if R in memo: return memo[R]
        u=R[0]
        for j in range(1,len(R)):
            v=R[j]
            if dist_le2(adj,u,v):
                N=R[1:j]+R[j+1:]
                if rec(N): memo[R]=True; return True
        memo[R]=False; return False
    return rec(S)

def semipaired_min(adj):
    N=len(adj)
    for k in range(2,N+1,2):
        for S in combinations(range(N),k):
            if is_dominating(adj,S) and has_pairing(adj,S):
                return k
    return None

def constructed_set(base):
    n=len(base); T=bfs_tree(base); pairs,u=tree_square_matching(T)
    D=set(range(n)); P=list(pairs)
    if u is not None:
        D.add(n+u); P.append((u,n+u))
    return D,P,T

def check_instance(base):
    n=len(base); C=corona_adj(base); D,P,T=constructed_set(base)
    exp=n if n%2==0 else n+1
    assert len(D)==exp
    assert is_dominating(C,D)
    used=[]
    for u,v in P:
        assert u in D and v in D and dist_le2(C,u,v)
        used += [u,v]
    assert sorted(used)==sorted(D)
    return exp

print('VERIFY_OK')
# Exhaust every labeled connected simple graph through order 5, compare with brute-force optimum.
instances=0
for n in range(2,6):
    E=[(i,j) for i in range(n) for j in range(i+1,n)]
    conn=0
    for mask in range(1,1<<len(E)):
        edges=[E[k] for k in range(len(E)) if (mask>>k)&1]
        ok,base=connected(n,edges)
        if not ok: continue
        conn+=1; instances+=1
        exp=check_instance(base)
        got=semipaired_min(corona_adj(base))
        assert got==exp,(n,edges,got,exp)
    print(f'n={n}: connected_labeled_graphs={conn}, exact_corona_checks={conn}')

# Exhaust all Prüfer-coded labeled trees through order 7; validate constructive pairing/corona set.
def prufer_tree(code,n):
    deg=[1]*n
    for x in code: deg[x]+=1
    edges=[]
    code=list(code)
    for x in code:
        leaf=min(i for i,d in enumerate(deg) if d==1)
        edges.append((leaf,x)); deg[leaf]-=1; deg[x]-=1
    rem=[i for i,d in enumerate(deg) if d==1]
    edges.append(tuple(rem))
    _,adj=connected(n,edges)
    return adj

trees=0
for n in range(2,8):
    if n==2:
        codes=[()]
    else:
        codes=product(range(n), repeat=n-2)
    c=0
    for code in codes:
        base=prufer_tree(code,n); check_instance(base); c+=1; trees+=1
    print(f'n={n}: prufer_trees_checked={c}')

# Deterministic denser connected examples through order 50.
for n in range(2,51):
    base=[set() for _ in range(n)]
    for i in range(n-1):
        base[i].add(i+1); base[i+1].add(i)
    for i in range(n):
        for step in (2,5):
            j=(i+step)%n
            if j!=i:
                base[i].add(j); base[j].add(i)
    check_instance(base)

print('connected_graphs_bruteforce_optimum_checked =',instances)
print('labeled_trees_constructively_checked =',trees)
print('deterministic_construction_range = 2..50')
print('all checks matched least_even_at_least_n')
