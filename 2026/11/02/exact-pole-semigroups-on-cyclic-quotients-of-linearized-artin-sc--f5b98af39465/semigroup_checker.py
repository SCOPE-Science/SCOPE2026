#!/usr/bin/env python3
"""Finite arithmetic checks for a pole semigroup theorem; no infinite proof is inferred."""
import heapq
from math import gcd

def test(p, N):
    assert p >= 5 and p % 2 == 1 and N >= 2
    L = (p - 1) // 2
    e = (p**N - 1) // (p - 1)
    d = e - 2
    g = (p**N - 1) // 2
    gens = [p] + [p + k*d for k in range(1, L+1)]
    assert gcd(p, d) == 1
    assert e*(p-1) == p**N-1
    A = [0] + [p * ((k+L-1)//L) + k*d for k in range(1,p)]
    assert len({a % p for a in A}) == p
    # Dijkstra independently computes the shortest nonnegative semigroup value
    # in every congruence class modulo p from just the minimal generators.
    INF=10**100
    dist=[INF]*p; dist[0]=0
    pq=[(0,0)]
    while pq:
        v,r=heapq.heappop(pq)
        if v!=dist[r]: continue
        for t in gens:
            s=(r+t)%p
            if v+t<dist[s]:
                dist[s]=v+t; heapq.heappush(pq,(dist[s],s))
    for a in A:
        assert dist[a%p]==a, (p,N,a,dist[a%p])
    assert sum(A)//p-(p-1)//2 == g, (p,N,A)
    assert (sum(A) % p) == 0
    c=max(A)-p+1
    assert c==p**N-p+2
    # Numerical semigroup gap count directly from Apéry distances.
    gaps=[m for m in range(c) if m<dist[m%p]]
    assert len(gaps)==g, (p,N,len(gaps),g)
    assert gaps[-1]==c-1
    # The expected pseudo-Frobenius values are all and only those gaps
    # which become nongaps upon adding every positive generator.
    PF=[m for m in gaps if all(m+t>=dist[(m+t)%p] for t in gens)]
    expected=sorted(A[k]-p for k in range(L+1,p))
    assert PF==expected, (p,N,PF,expected)
    # Formula for dimensions of Riemann-Roch spaces at small degrees.
    for M in range(0,min(c+2*p,1000)):
        q1=sum(max(0,(M-a)//p+1) for a in A)
        q2=sum(h>=dist[h%p] for h in range(M+1))
        assert q1==q2,(p,N,M,q1,q2)
    return f'p={p} N={N} genus={g} conductor={c} type={L} generators={gens} CHECK_OK'

def main():
    cases=[(p,N) for p in (5,7,11,13,17) for N in (2,3)] + [(5,4),(7,4)]
    for p,N in cases:
        print(test(p,N))
    print('VERIFY_OK: finite semigroup, Apery, gap and type arithmetic checks')

if __name__=='__main__':main()
