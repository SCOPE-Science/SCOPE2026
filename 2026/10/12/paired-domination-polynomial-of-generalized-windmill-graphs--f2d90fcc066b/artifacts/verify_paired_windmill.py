from itertools import combinations
from math import comb

def graph(k,m):
    # vertices 0=center; 1+i*m+j blade i, j
    N=1+k*m
    adj=[set() for _ in range(N)]
    for i in range(k):
        vs=[1+i*m+j for j in range(m)]
        for v in vs:
            adj[0].add(v); adj[v].add(0)
        for a,b in combinations(vs,2):
            adj[a].add(b); adj[b].add(a)
    return adj

def dominates(S,adj):
    S=set(S)
    return all(v in S or any(u in S for u in adj[v]) for v in range(len(adj)))

def has_pm(S,adj):
    S=frozenset(S)
    if len(S)%2: return False
    memo={}
    def rec(T):
        if not T: return True
        if T in memo: return memo[T]
        v=min(T)
        R=T-{v}
        for u in adj[v] & R:
            if rec(R-{u}):
                memo[T]=True; return True
        memo[T]=False; return False
    return rec(S)

def actual(k,m):
    adj=graph(k,m); N=len(adj)
    coeff=[0]*(N+1)
    for mask in range(1<<N):
        S=[v for v in range(N) if mask>>v&1]
        if dominates(S,adj) and has_pm(S,adj): coeff[len(S)]+=1
    return coeff

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def powpoly(a,k):
    r=[1]
    for _ in range(k):r=conv(r,a)
    return r

def expected(k,m):
    E=[0]*(m+1); O=[0]*(m+1)
    for r in range(m+1):
        (E if r%2==0 else O)[r]=comb(m,r)
    Em1=E[:]; Em1[0]-=1
    a=powpoly(Em1,k)
    b=conv(O,powpoly(E,k-1))
    b=[0]+[k*x for x in b]
    L=max(len(a),len(b)); out=[0]*L
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return out

def rule(S,k,m):
    S=set(S); c=0 in S
    ss=[]
    for i in range(k):
        ss.append(sum(1 for j in range(m) if 1+i*m+j in S))
    if c:
        return sum(x%2 for x in ss)==1
    return all(x>=1 and x%2==0 for x in ss)

subsets=0; rule_checks=0
pairs=[]
for k,m in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,2)]:
    adj=graph(k,m); N=len(adj)
    act=actual(k,m); exp=expected(k,m)
    exp += [0]*(len(act)-len(exp)); exp=exp[:len(act)]
    assert act==exp,(k,m,act,exp)
    for mask in range(1<<N):
        S=[v for v in range(N) if mask>>v&1]
        truth=dominates(S,adj) and has_pm(S,adj)
        assert truth==rule(S,k,m),(k,m,S,truth,rule(S,k,m))
        subsets+=1; rule_checks+=1
    nonzero=[i for i,x in enumerate(act) if x]
    assert nonzero[0]==2
    assert act[2]==k*m
    assert sum(act)==k*(2**(m-1))**k + (2**(m-1)-1)**k
    pairs.append((k,m,N,sum(act),act[2]))
print('VERIFY_OK parameter_pairs=%d subset_checks=%d minimum_checks=%d max_order=%d' % (len(pairs),subsets,len(pairs),max(x[2] for x in pairs)))
for row in pairs:
    print('k=%d m=%d order=%d paired_sets=%d minima=%d'%row)
