#!/usr/bin/env python3
from math import gcd
from itertools import combinations

# Exact polynomial arithmetic in Z[u,v] represented by dict[(a,b)] = coefficient.
def add(p, q, scale=1):
    r = dict(p)
    for k, c in q.items():
        r[k] = r.get(k, 0) + scale*c
        if r[k] == 0:
            del r[k]
    return r

def mul(p, q):
    r = {}
    for (a,b), c in p.items():
        for (d,e), f in q.items():
            k = (a+d,b+e)
            r[k] = r.get(k,0) + c*f
            if r[k] == 0:
                del r[k]
    return r

def mon(a,b,c=1):
    return {(a,b): c}

ONE=mon(0,0); U=mon(1,0); V=mon(0,1)

def geom_u(m):
    return {(k,0):1 for k in range(m)}

def geom_v(m):
    return {(0,k):1 for k in range(m)}

def det_norm(m):
    # det [[1,1,1],[1,u,v],[1,u^m,v^m]]
    p={}
    for term,sgn in [
        (mon(1,m),1), (mon(m,1),-1), (mon(0,m),-1),
        (mon(0,1),1), (mon(m,0),1), (mon(1,0),-1)]:
        p=add(p,term,sgn)
    return p

# Check D = -(u-1)(v-1)(S_m(u)-S_m(v)) for a broad exact range.
Uminus1=add(U,ONE,-1); Vminus1=add(V,ONE,-1)
for m in range(2,61):
    diff=add(geom_u(m), geom_v(m), -1)
    rhs=mul(mul(Uminus1,Vminus1),diff)
    rhs={k:-c for k,c in rhs.items()}
    assert det_norm(m)==rhs, m

# Uniform-distribution equivalence is purely arithmetic; exhaust a useful range exactly.
def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def uniformly_distributed(N,m):
    rows=(0,1,m)
    for d in divisors(N):
        counts=[0]*d
        for r in rows:
            counts[r%d]+=1
        if max(counts)-min(counts)>1:
            return False
    return True

def criterion(N,m):
    return gcd(N,m)<=2 and gcd(N,m-1)<=2

pairs=0
for N in range(3,301):
    for m in range(2,N):
        assert uniformly_distributed(N,m)==criterion(N,m), (N,m)
        pairs += 1

# Exact singular witnesses whenever the gcd criterion fails.
witnesses=0
for N in range(3,151):
    for m in range(2,N):
        g0=gcd(N,m); g1=gcd(N,m-1)
        if g0>=3:
            js=(0,N//g0,2*N//g0)
            assert len(set(j%N for j in js))==3
            assert all((m*j)%N==0 for j in js)
            witnesses += 1
        elif g1>=3:
            js=(0,N//g1,2*N//g1)
            assert len(set(j%N for j in js))==3
            assert all((m*j-j)%N==0 for j in js)
            witnesses += 1

print(f"IDENTITY_OK m=2..60")
print(f"UNIFORMITY_OK pairs={pairs}")
print(f"WITNESS_OK cases={witnesses}")
print("VERIFY_OK")
