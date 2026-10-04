#!/usr/bin/env python3
from itertools import combinations


def vertices(n):
    return tuple(range(1, (1<<n)-1))

def adj(a,b,n):
    full=(1<<n)-1
    return a!=b and (a|b)==full

def is_total_dom(D,n):
    V=vertices(n); D=set(D)
    return all(any(adj(v,d,n) for d in D) for v in V)

def has_perfect_matching(D,n):
    D=tuple(D)
    if len(D)%2: return False
    def rec(rem):
        if not rem: return True
        a=rem[0]
        for j in range(1,len(rem)):
            b=rem[j]
            if adj(a,b,n):
                nxt=rem[1:j]+rem[j+1:]
                if rec(nxt): return True
        return False
    return rec(D)

def min_total_bruteforce(n):
    V=vertices(n)
    for k in range(1,n+1):
        for D in combinations(V,k):
            if is_total_dom(D,n): return k
    return None

def min_paired_bruteforce(n):
    V=vertices(n)
    for k in range(2, n+3):
        if k%2: continue
        for D in combinations(V,k):
            if is_total_dom(D,n) and has_perfect_matching(D,n): return k
    return None

def required_cosingletons(n):
    full=(1<<n)-1
    return [full ^ (1<<i) for i in range(n)]

# Exhaustive minima for the support graph through n=5.
for n in range(2,6):
    gt=min_total_bruteforce(n)
    gp=min_paired_bruteforce(n)
    assert gt==n,(n,gt)
    assert gp==2*((n+1)//2),(n,gp)

# Structural necessity/sufficiency through n=9.
for n in range(2,10):
    V=vertices(n); req=required_cosingletons(n)
    full=(1<<n)-1
    # A singleton-support vertex has neighbors only in the opposite co-singleton fiber.
    for i in range(n):
        s=1<<i
        neigh=[t for t in V if adj(s,t,n)]
        assert neigh==[full^(1<<i)]
    assert is_total_dom(req,n)
    assert all(adj(req[i],req[j],n) for i in range(n) for j in range(i+1,n))
    if n%2==0:
        assert has_perfect_matching(req,n)
    else:
        extra=full ^ (1<<0) ^ (1<<1)
        D=req+[extra]
        assert is_total_dom(D,n)
        assert has_perfect_matching(D,n)

# Direct ring check for Z/30Z. Vertex set is nonunits outside J=(0), so nonzero nonunits.
def gcd(a,b):
    while b: a,b=b,a%b
    return a
m=30
R=range(m)
units={a for a in R if gcd(a,m)==1}
V=[a for a in R if a not in units and a!=0]
primes=[2,3,5]
T=[]
for p in primes:
    T.append({a for a in V if a%p==0 and all(a%q!=0 for q in primes if q!=p)})
assert all(T)
def radj(a,b): return gcd(gcd(a,b),m)==1
# Comaximal in Z/mZ iff gcd(a,b,m)=1.
D={next(iter(t)) for t in T}
assert all(any(radj(v,d) for d in D if d!=v) for v in V)
# Exact classification of all total dominating sets by T_i intersection.
for mask in range(1<<len(V)):
    S={V[i] for i in range(len(V)) if mask>>i & 1}
    td=all(any(radj(v,d) for d in S if d!=v) for v in V)
    cell=all(S & t for t in T)
    assert td==cell

print('VERIFY_OK')
print('support_graph_exact_n=2..5')
print('structural_checks_n=2..9')
print('Z30_total_domination_classification=exact')
