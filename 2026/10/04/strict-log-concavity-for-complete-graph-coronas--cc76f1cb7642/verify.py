import itertools, math
from collections import deque

def graph(n):
    # vertices 0..n-1 are the K_n core; n..2n-1 are their pendant leaves
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(i+1,n):
            adj[i].add(j); adj[j].add(i)
        adj[i].add(n+i); adj[n+i].add(i)
    return adj

def distances(adj):
    N=len(adj)
    D=[]
    for s in range(N):
        d=[-1]*N; d[s]=0
        q=deque([s])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if d[w]<0:
                    d[w]=d[v]+1
                    q.append(w)
        D.append(d)
    return D

def forbidden_triples(D):
    N=len(D)
    out=[]
    for a,b,c in itertools.combinations(range(N),3):
        bad = (
            D[a][c] == D[a][b] + D[b][c] or
            D[a][b] == D[a][c] + D[c][b] or
            D[b][c] == D[b][a] + D[a][c]
        )
        if bad:
            out.append((1<<a)|(1<<b)|(1<<c))
    return out

def is_gp(mask, forb):
    return all((mask&t)!=t for t in forb)

def predicted(n):
    c=[0]*(max(n,2)+1)
    c[0]=1
    c[1]=2*n
    c[2]=math.comb(2*n,2)
    for k in range(3,n+1):
        c[k]=(2**k)*math.comb(n,k)
    return c

total_subsets=0
for n in range(2,11):
    adj=graph(n)
    D=distances(adj)
    forb=forbidden_triples(D)
    actual=[0]*(n+1)
    for mask in range(1<<(2*n)):
        total_subsets += 1
        if is_gp(mask,forb):
            k=mask.bit_count()
            assert k <= n
            actual[k]+=1
    pred=predicted(n)
    assert actual==pred, (n,actual,pred)
    assert all(actual[k]*actual[k] > actual[k-1]*actual[k+1]
               for k in range(1,len(actual)-1)), (n,actual)

print("VERIFY_OK")
print("n_values_checked = 2..10")
print("subsets_checked =", total_subsets)
print("definition-level geodesic test matched every coefficient")
print("strict log-concavity matched for every tested n")
