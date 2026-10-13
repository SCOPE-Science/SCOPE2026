from itertools import combinations
from collections import deque
from math import comb

def crown(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def distances(adj):
    N=len(adj); D=[]
    for s in range(N):
        d=[99]*N; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==99:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D

def is_mixed(adj,D,S):
    S=tuple(S); N=len(adj)
    seen=set()
    for v in range(N):
        sig=tuple(D[v][s] for s in S)
        if sig in seen: return False
        seen.add(sig)
    for u in range(N):
        for v in adj[u]:
            if u<v:
                sig=tuple(min(D[u][s],D[v][s]) for s in S)
                if sig in seen: return False
                seen.add(sig)
    return True

def dominates(adj,S):
    S=set(S)
    return all(v in S or any(u in S for u in adj[v]) for v in range(len(adj)))

def structural_minimum(n,S):
    S=set(S)
    if n<7 or len(S)!=n-1: return False
    P={i for i in range(n) if i in S}
    Q={i for i in range(n) if n+i in S}
    if P & Q: return False
    missing=set(range(n))-(P|Q)
    return len(missing)==1 and len(P)>=3 and len(Q)>=3

def predicted_value(n):
    return 3 if n==3 else (n if n<=6 else n-1)

def predicted_count(n):
    if n>=7:
        return n*((1<<(n-1))-n*n+n-2)
    return None

graphs=subsets=minimum_sets=0
for n in range(3,10):
    adj=crown(n); D=distances(adj); N=2*n
    target=predicted_value(n)
    # Exhaustively rule out smaller dominant mixed sets.
    for k in range(target):
        for S in combinations(range(N),k):
            subsets+=1
            assert not (is_mixed(adj,D,S) and dominates(adj,S)), (n,k,S)
    actual=[]
    for S in combinations(range(N),target):
        subsets+=1
        if is_mixed(adj,D,S) and dominates(adj,S):
            actual.append(S)
    assert actual, n
    if n>=7:
        assert all(structural_minimum(n,S) for S in actual)
        # Generate predicted structural sets and compare exactly.
        predicted=set()
        for h in range(n):
            rest=[i for i in range(n) if i!=h]
            for p in range(3,n-3):
                for P in combinations(rest,p):
                    P=set(P); 
                    S=tuple(sorted(list(P)+[n+i for i in rest if i not in P]))
                    predicted.add(S)
        assert set(actual)==predicted, (n,len(actual),len(predicted))
        assert len(actual)==predicted_count(n), (n,len(actual),predicted_count(n))
    else:
        # Full A and full B are witnesses for n=3..6.
        assert is_mixed(adj,D,range(n)) and dominates(adj,range(n))
        assert is_mixed(adj,D,range(n,2*n)) and dominates(adj,range(n,2*n))
    minimum_sets += len(actual); graphs += 1

# Separately verify the mixed-basis obstruction at size n-1 for n=4..6:
# all size-(n-1) mixed bases are one-sided and therefore not dominating.
one_sided_mixed=0
for n in range(4,7):
    adj=crown(n); D=distances(adj); N=2*n
    for S in combinations(range(N),n-1):
        if is_mixed(adj,D,S):
            P=sum(1 for x in S if x<n)
            assert P in (0,n-1), (n,S,P)
            assert not dominates(adj,S)
            one_sided_mixed += 1
    assert one_sided_mixed >= 2*n

print("VERIFY_OK")
print("crown_parameters_checked =", graphs)
print("vertex_subsets_checked_for_dominant_mixed_optima =", subsets)
print("minimum_dominant_mixed_sets_checked =", minimum_sets)
print("parameters n = 3..9")
print("all smaller dominant mixed sets failed directly")
print("n=3..6 values matched 3,n,n,n")
print("n=7..9 values matched n-1")
print("all stable minimum sets matched the one-omitted-pair balanced-transversal classification")
print("all stable counts matched n*(2^(n-1)-n^2+n-2)")
print("size-(n-1) mixed bases checked as one-sided/non-dominating for n=4..6 =", one_sided_mixed)
