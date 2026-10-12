from itertools import combinations
from collections import deque

def half_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def distance_matrix(n):
    adj=half_adj(n)
    N=2*n
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

def sig(D,v,W):
    return tuple(sorted(D[v][w] for w in W))

def is_outer_multiset_resolving(D,W):
    W=set(W)
    seen=set()
    for v in range(len(D)):
        if v in W: continue
        s=sig(D,v,W)
        if s in seen: return False
        seen.add(s)
    return True

def predicted_bases(n):
    ans=set()
    for mask in range(1<<(n-1)):
        T={k for k in range(1,n) if mask>>(k-1)&1}
        if n%2==1 and len(T)==(n-1)//2:
            continue
        W=set()
        for k in range(1,n):
            if k in T:
                W.add(k)
            else:
                W.add(n+k-1)
        ans.add(frozenset(W))
    return ans

checked=0
print("VERIFY_OK")
for n in range(2,11):
    D=distance_matrix(n)
    # No set of size n-2 resolves.
    if n>=3:
        for W in combinations(range(2*n),n-2):
            checked += 1
            assert not is_outer_multiset_resolving(D,W)
    actual=set()
    for W in combinations(range(2*n),n-1):
        checked += 1
        if is_outer_multiset_resolving(D,W):
            actual.add(frozenset(W))
    expected=predicted_bases(n)
    assert actual==expected,(n,len(actual),len(expected))
    expected_count=(2**(n-1) if n%2==0 else
                    2**(n-1)-__import__("math").comb(n-1,(n-1)//2))
    assert len(actual)==expected_count
    print(f"n={n}: outer_multiset_dimension={n-1}, bases={len(actual)}")
print("candidate_subsets_checked =",checked)
print("all bases matched the shifted-complement classification")
