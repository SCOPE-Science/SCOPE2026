from itertools import combinations
from math import comb

def graph(n):
    adj=[set() for _ in range(2*n)]
    def add(a,b): adj[a].add(b); adj[b].add(a)
    for i in range(n):
        add(i,(i+1)%n); add(i,n+i)
    return adj

def connected(adj,S):
    if not S:return False
    S=set(S); seen={next(iter(S))}; stack=list(seen)
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v in S and v not in seen:
                seen.add(v); stack.append(v)
    return seen==S

def forcing(adj,S):
    blue=set(S)
    while True:
        nxt=[]
        for u in tuple(blue):
            w=[v for v in adj[u] if v not in blue]
            if len(w)==1:nxt.append(w[0])
        if not nxt:break
        blue.update(nxt)
    return len(blue)==len(adj)

def criterion(n,S):
    S=set(S); core={i for i in range(n) if i in S}; leaves={i for i in range(n) if n+i in S}
    # Any selected leaf must have its support selected for a nontrivial connected forcing set.
    if not leaves <= core:return False
    missing=set(range(n))-core
    if not missing:return True
    if len(missing)==1:
        i=next(iter(missing))
        return ((i-1)%n in leaves) or ((i+1)%n in leaves)
    if n>=4 and len(missing)==2:
        a,b=tuple(missing)
        if (a-b)%n not in (1,n-1):return False
        # orient b=a+1
        if b==(a+1)%n:i=a
        else:i=b
        return ((i-1)%n in leaves) and ((i+2)%n in leaves)
    return False

def expected_coeffs(n):
    # Build coefficients combinatorially without symbolic packages.
    co=[0]*(2*n+1)
    # all cores + arbitrary leaves
    for j in range(n+1): co[n+j]+=comb(n,j)
    # one core omitted; at least one of 2 boundary leaves; n-3 other leaves arbitrary
    for j in range(n-2):
        q=comb(n-3,j)
        co[n-1+1+j]+=n*2*q
        co[n-1+2+j]+=n*q
    if n>=4:
        for j in range(n-3):
            co[n-2+2+j]+=n*comb(n-4,j)
    return co

subset_checks=criterion_checks=coefficient_checks=0
for n in range(3,10):
    adj=graph(n); actual=[0]*(2*n+1)
    for mask in range(1<<(2*n)):
        S=[v for v in range(2*n) if mask>>v&1]
        cf=connected(adj,S) and forcing(adj,S)
        cr=criterion(n,S)
        subset_checks+=1; criterion_checks+=1
        assert cf==cr,(n,mask,cf,cr)
        if cf: actual[len(S)]+=1
    exp=expected_coeffs(n)
    assert actual==exp,(n,actual,exp)
    coefficient_checks += 2*n+1
    assert min(i for i,a in enumerate(actual) if a)==n
    assert actual[n]==(7 if n==3 else 3*n+1)
    assert sum(actual)==(17 if n==3 else (2**(n-4))*(7*n+16))
print(f'VERIFY_OK n_range=3..9 subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} min_counts=7_then_3n_plus_1 total_counts=17_then_2^(n-4)(7n+16) max_order=18')
