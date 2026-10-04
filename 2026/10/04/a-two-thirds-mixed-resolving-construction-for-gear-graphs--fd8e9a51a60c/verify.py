from itertools import combinations
from collections import deque

def gear(n):
    N=2*n+1
    z=0
    X=list(range(1,n+1))
    Y=list(range(n+1,2*n+1))
    adj=[set() for _ in range(N)]
    for i,x in enumerate(X):
        y=Y[i]
        xnext=X[(i+1)%n]
        for u,v in [(z,x),(x,y),(xnext,y)]:
            adj[u].add(v); adj[v].add(u)
    return adj,X,Y

def distances(adj):
    N=len(adj)
    D=[[10**9]*N for _ in range(N)]
    for s in range(N):
        D[s][s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if D[s][v]==10**9:
                    D[s][v]=D[s][u]+1
                    q.append(v)
    return D

def mixed_signatures(adj,S):
    D=distances(adj)
    N=len(adj)
    edges=[(u,v) for u in range(N) for v in adj[u] if u<v]
    out={}
    for v in range(N):
        out=("v",v) if False else None
    sig={}
    for v in range(N):
        sig[("v",v)]=tuple(D[s][v] for s in S)
    for e in edges:
        u,v=e
        sig[("e",e)]=tuple(min(D[s][u],D[s][v]) for s in S)
    return sig

def is_mixed(adj,S):
    sig=mixed_signatures(adj,S)
    return len(set(sig.values()))==len(sig)

# The infinite-family construction: all inserted rim vertices y_i except i divisible by 3.
construction_checks=0
for n in range(4,61):
    adj,X,Y=gear(n)
    S=[Y[i-1] for i in range(1,n+1) if i%3!=0]
    assert len(S)==n-n//3
    assert is_mixed(adj,S),(n,S)
    construction_checks+=1

# Verify the closed distance table for every gear G_n in a broad range.
table_checks=0
for n in range(5,41):
    adj,X,Y=gear(n); D=distances(adj)
    for i in range(n):
        xi=X[i]; yi=Y[i]; xnext=X[(i+1)%n]
        for j in range(n):
            yj=Y[j]
            # vertex distances
            assert D[yj][0]==2
            dx=1 if j in ((i-1)%n,i) else 3
            assert D[yj][xi]==dx,(n,i,j,"x",D[yj][xi],dx)
            dy=0 if j==i else 2 if j in ((i-1)%n,(i+1)%n) else 4
            assert D[yj][yi]==dy,(n,i,j,"y",D[yj][yi],dy)
            # edge distances
            ds=min(D[yj][0],D[yj][xi])
            ex=1 if j in ((i-1)%n,i) else 2
            assert ds==ex,(n,i,j,"spoke",ds,ex)
            de1=min(D[yj][xi],D[yj][yi])
            ee1=0 if j==i else 1 if j==(i-1)%n else 2 if j==(i+1)%n else 3
            assert de1==ee1,(n,i,j,"rim1",de1,ee1)
            de2=min(D[yj][xnext],D[yj][yi])
            ee2=0 if j==i else 1 if j==(i+1)%n else 2 if j==(i-1)%n else 3
            assert de2==ee2,(n,i,j,"rim2",de2,ee2)
            table_checks+=5

# Exhaustive exact small cases: all vertex subsets until first mixed layer.
exact=[]
subset_checks=0
for n in range(4,9):
    adj,X,Y=gear(n)
    N=len(adj)
    bases=[]
    found=None
    for k in range(N+1):
        for S in combinations(range(N),k):
            subset_checks+=1
            if is_mixed(adj,S):
                bases.append(S)
        if bases:
            found=k
            break
    exact.append((n,found,len(bases)))
assert exact==[(4,3,8),(5,4,25),(6,4,3),(7,5,14),(8,6,56)],exact

# Smallest published case: explicit certificate and exhaustive lower bound.
adj,X,Y=gear(4)
S=tuple(Y[:3])
assert is_mixed(adj,S)
sigs=mixed_signatures(adj,S)
assert len(sigs)==21 and len(set(sigs.values()))==21
assert all(not is_mixed(adj,T) for T in combinations(range(9),2))

print("VERIFY_OK")
print("construction_gears_checked =",construction_checks)
print("distance_table_entries_checked =",table_checks)
print("exhaustive_candidate_subsets_checked =",subset_checks)
print("exact_small_mixed_dimensions =",exact)
print("G4_explicit_landmarks =",S)
print("G4_objects_resolved =",len(sigs))
print("all constructions matched mdim upper bound ceil(2n/3)")
print("published formula mdim(G_n)=n is contradicted for every tested n=4..60")
