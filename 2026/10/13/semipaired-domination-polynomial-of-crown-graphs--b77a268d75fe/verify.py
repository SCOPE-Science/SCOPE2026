from itertools import combinations
from collections import Counter, deque
from math import comb

def crown_adj(n):
    adj=[set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def distances(adj):
    N=len(adj); D=[]
    for s in range(N):
        d=[10**9]*N; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D

def dominates(adj,S):
    S=set(S)
    return all(v in S or bool(adj[v]&S) for v in range(len(adj)))

def pairable(D,S):
    S=tuple(S)
    if len(S)%2: return False
    memo={}
    def rec(T):
        if not T: return True
        if T in memo: return memo[T]
        a=T[0]
        for i in range(1,len(T)):
            b=T[i]
            if D[a][b]<=2 and rec(T[1:i]+T[i+1:]):
                memo[T]=True; return True
        memo[T]=False; return False
    return rec(S)

def semipaired(adj,D,S):
    return dominates(adj,S) and pairable(D,S)

def predicted(adj,D,S,n):
    k=len(S)
    if k<4 or k%2: return False
    return dominates(adj,S)

def predicted_min_count(n):
    base=n*(n-1)*(n*n+3*n-8)//4
    return base + (2 if n==4 else 0)

subsets=0
feasible=0
print('VERIFY_OK')
for n in range(3,9):
    adj=crown_adj(n); D=distances(adj)
    hist=Counter()
    for k in range(2*n+1):
        for S in combinations(range(2*n),k):
            subsets += 1
            a=semipaired(adj,D,S)
            b=predicted(adj,D,S,n)
            assert a==b,(n,S,a,b)
            if a:
                hist[k]+=1; feasible+=1
    assert min(hist)==4
    assert hist[4]==predicted_min_count(n),(n,hist[4],predicted_min_count(n))
    # Closed domination polynomial coefficients and even-part relation.
    dom=Counter()
    for k in range(2*n+1):
        for S in combinations(range(2*n),k):
            if dominates(adj,S): dom[k]+=1
    pred_dom=Counter()
    # two whole sides
    pred_dom[n]+=2
    # both sides at least two
    for a in range(2,n+1):
        for b in range(2,n+1):
            pred_dom[a+b]+=comb(n,a)*comb(n,b)
    # one A and >=1 B, and symmetric, subtract overlap matched pairs once
    for b in range(1,n+1): pred_dom[b+1]+=2*n*comb(n-1,b-1)
    pred_dom[2]-=n
    assert dom==pred_dom,(n,dom,pred_dom)
    for k,c in hist.items():
        assert k%2==0 and k>=4 and c==dom[k]
    print(f'n={n}: gamma_pr2=4, minimum_sets={hist[4]}, total_semipaired_sets={sum(hist.values())}, histogram={dict(sorted(hist.items()))}')
print('vertex_subsets_checked =',subsets)
print('semipaired_sets_checked =',feasible)
print('all semipaired dominating sets were exactly even dominating sets of size at least four')
