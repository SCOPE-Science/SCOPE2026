from itertools import combinations
from collections import Counter, deque


def graph(m,n):
    # centers 0..m-1, rims m..m+n-1
    N=m+n
    adj=[set() for _ in range(N)]
    for i in range(n):
        a=m+i; b=m+((i+1)%n)
        adj[a].add(b); adj[b].add(a)
    for c in range(m):
        for i in range(n):
            r=m+i
            adj[c].add(r); adj[r].add(c)
    return adj

def dists(adj):
    N=len(adj); D=[]
    for s in range(N):
        d=[99]*N; d[s]=0; q=deque([s])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if d[w]==99:
                    d[w]=d[v]+1; q.append(w)
        D.append(d)
    return D

def strongly_resolves(D,w,u,v):
    return D[w][u] == D[w][v]+D[v][u] or D[w][v] == D[w][u]+D[u][v]

def is_strong(adj,D,S):
    N=len(adj); S=set(S)
    for u in range(N):
        for v in range(u+1,N):
            if not any(strongly_resolves(D,w,u,v) for w in S):
                return False
    return True

def predicted(m,n,S):
    S=set(S); centers=set(range(m)); rims=set(range(m,m+n))
    oc=centers-S; rr=sorted(rims-S)
    if n==3 and m==1:
        return len(oc)+len(rr) <= 1
    if n==3:
        return len(oc)<=1 and len(rr)<=1
    if len(oc)>1 or len(rr)>2: return False
    if len(rr)==2:
        i=(rr[0]-m)%n; j=(rr[1]-m)%n
        return (i-j)%n in (1,n-1)
    return True

def expected_poly(m,n):
    # dict degree -> coeff
    A={m:1,m-1:m}
    if n==3 and m==1:
        return {4:1,3:4}
    if n==3:
        B={3:1,2:3}
    else:
        B={n:1,n-1:n,n-2:n}
    out=Counter()
    for a,ca in A.items():
        for b,cb in B.items(): out[a+b]+=ca*cb
    return dict(out)

subset_checks=classification_checks=coefficient_checks=minimum_checks=0
pairs=0
for m in range(1,5):
    for n in range(3,8):
        pairs+=1; adj=graph(m,n); D=dists(adj); N=m+n; hist=Counter()
        for mask in range(1<<N):
            S=[i for i in range(N) if mask>>i&1]
            got=is_strong(adj,D,S); want=predicted(m,n,S)
            subset_checks+=1; classification_checks+=1
            assert got==want,(m,n,S,got,want)
            if got: hist[len(S)]+=1
        exp=expected_poly(m,n)
        for k in range(N+1):
            coefficient_checks+=1
            assert hist[k]==exp.get(k,0),(m,n,k,hist[k],exp.get(k,0))
        minimum_checks+=1
        min_k=min(hist)
        if n==3 and m==1:
            assert min_k==3 and hist[min_k]==4
        elif n==3:
            assert min_k==m+1 and hist[min_k]==3*m
        else:
            assert min_k==m+n-3 and hist[min_k]==m*n
print(f'VERIFY_OK pairs={pairs} subset_checks={subset_checks} classification_checks={classification_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order={4+7}')
