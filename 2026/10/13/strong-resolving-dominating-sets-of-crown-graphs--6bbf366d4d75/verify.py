from itertools import combinations
from collections import deque, Counter

def crown_graph(n):
    # A = 0..n-1, B = n..2n-1, deleted pairs (i,n+i)
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i==j: 
                continue
            u=i; v=n+j
            adj[u].add(v); adj[v].add(u)
    return adj

def all_distances(adj):
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

def strong_resolves(D,w,u,v):
    return D[w][v] == D[w][u] + D[u][v] or D[w][u] == D[w][v] + D[u][v]

def is_strong_resolving(D,S):
    N=len(D)
    S=set(S)
    for u,v in combinations(range(N),2):
        if not any(strong_resolves(D,w,u,v) for w in S):
            return False
    return True

def is_dominating(adj,S):
    S=set(S)
    for v in range(len(adj)):
        if v in S:
            continue
        if not (adj[v] & S):
            return False
    return True

def predicted(n,S):
    S=set(S)
    # At least one endpoint of every deleted matched pair.
    if any(i not in S and n+i not in S for i in range(n)):
        return False
    # The only non-dominating strong resolving sets are the 2n transversals
    # having exactly one selected vertex in one bipartition class.
    A=sum(i in S for i in range(n))
    B=sum(n+i in S for i in range(n))
    if len(S)==n and (A==1 or B==1):
        return False
    return True

subset_trials=0
accepted=0
basis_count=0
poly_checks=0

for n in range(3,9):
    adj=crown_graph(n)
    D=all_distances(adj)
    N=2*n
    counts=Counter()

    for mask in range(1<<N):
        subset_trials += 1
        S=[v for v in range(N) if (mask>>v)&1]
        actual=is_strong_resolving(D,S) and is_dominating(adj,S)
        pred=predicted(n,S)
        assert actual==pred,(n,S,actual,pred)
        if actual:
            accepted += 1
            counts[len(S)] += 1

    # Polynomial x^n((x+2)^n-2n)
    expected=Counter()
    for j in range(n+1):
        k=n+j
        coeff=(2**(n-j))
        # choose j matched pairs to contribute both endpoints
        # and one endpoint from each remaining pair
        from math import comb
        coeff*=comb(n,j)
        if j==0:
            coeff-=2*n
        expected[k]=coeff
    assert counts==expected,(n,counts,expected)
    assert min(counts)==n
    assert counts[n]==2**n-2*n
    basis_count += counts[n]
    poly_checks += len(counts)

print("VERIFY_OK")
print("crown_parameters_checked =", 6)
print("parameters n = 3..8")
print("subset_trials =", subset_trials)
print("accepted_strong_resolving_dominating_sets =", accepted)
print("minimum_bases_checked =", basis_count)
print("polynomial_coefficients_checked =", poly_checks)
print("all strong resolving dominating sets matched the exact classification")
print("all generating polynomials matched x^n((x+2)^n-2n)")
print("all strong resolving domination numbers matched n")
print("all minimum-basis counts matched 2^n-2n")
