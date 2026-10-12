from itertools import combinations
from collections import deque

def half_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj

def distances(n):
    adj=half_adj(n)
    D=[]
    for s in range(2*n):
        d=[10**9]*(2*n)
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

def signature(D,v,S):
    return tuple(sorted(D[v][w] for w in S))

def is_multiset_resolving(D,S):
    seen=set()
    for v in range(len(D)):
        sig=signature(D,v,S)
        if sig in seen:
            return False
        seen.add(sig)
    return True

def involution(n,S):
    out=set()
    for v in S:
        if v<n:
            i=v+1
            out.add(n+(n-i))
        else:
            j=v-n+1
            out.add(n-j)
    return frozenset(out)

def predicted_bases(n):
    if n%2==0:
        m=n//2
        W1={2*r-1 for r in range(1,m+1)}
        W1 |= {n+(2*r-1) for r in range(1,m)}
        W2={2*r for r in range(1,m)}
        W2 |= {n+(2*r-2) for r in range(1,m+1)}
        return {frozenset(W1),frozenset(W2)}
    m=(n+1)//2
    fam=set()
    for c in range(1,m+1):
        B=set()
        for i in range(1,n+1):
            if (i%2==0 and i<=2*c-2) or (i%2==1 and 2*c-1<=i<=n-1):
                B.add(n+i-1)
        for d in range(c):
            A=set()
            for i in range(1,n+1):
                if (i%2==0 and i<=2*d) or (i%2==1 and i>=2*d+1):
                    A.add(i-1)
            W=frozenset(A|B)
            fam.add(W)
            fam.add(involution(n,W))
    return fam

total_subsets=0
print("VERIFY_OK")
for n in range(2,10):
    D=distances(n)
    target=n-1 if n%2==0 else n
    if n==2:
        target=1
    actual=set()
    for k in range(1,target+1):
        found=[]
        for S in combinations(range(2*n),k):
            total_subsets += 1
            if is_multiset_resolving(D,S):
                found.append(frozenset(S))
        if found:
            assert k==target,(n,k,target)
            actual=set(found)
            break
    expected=predicted_bases(n)
    assert actual==expected,(n,len(actual),len(expected),actual^expected)
    expected_count=2 if n%2==0 else ((n+1)*(n+3))//4
    assert len(actual)==expected_count,(n,len(actual),expected_count)
    print(f"n={n}: md={target}, bases={len(actual)}")
print("subsets_checked =",total_subsets)
print("all minimum bases matched the parity classification")
