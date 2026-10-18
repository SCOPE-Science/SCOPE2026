#!/usr/bin/env python3
"""Exact arithmetic checks for Apéry and affine-generator descriptions of a numerical semigroup."""
from math import gcd

def verify(q, n):
    assert q > 2 and n >= 4 and n % 2 == 0
    Q=q**n; N=Q+1; b=q*(q-1)
    r=(q**(n-1)-1)//(q-1)
    K=q*(q**(n-2)-1)//(q*q-1)
    m=q*q*(q**(n-1)+1)//(q+1)
    j0=1+b*K
    assert (q**(n-2)-1) % (q*q-1) == 0
    assert (q**(n-1)+1) % (q+1) == 0
    assert N == b*r+q+1
    assert r == 1+(q+1)*K
    assert r*j0==1+K*N
    assert j0 == N-m
    assert m+b*K==Q
    assert q*j0+b==m
    assert gcd(N,r)==1 and 2*m>N
    w=[q*j+b*((j*r)%N) for j in range(N)]
    assert len({v%N for v in w}) == N
    genus=(q*q-1)*Q//2
    assert sum(w)//N-(N-1)//2 == genus
    gens=[N]+[m+b*k for k in range(K+1)]
    assert all((m+b*k) in w for k in range(K+1))
    assert max(w)==q*m+b*Q
    assert w[m] == max(w)
    conductor=q*m+(b-1)*Q
    assert max(w)-N+1 ==conductor
    assert 2*genus-conductor ==q*q*(q-1)*K
    assert len(gens)==len(set(gens)) and all(m<=a<=N for a in gens)
    # Dijkstra residue shortest paths, independent from the explicit Apery formula
    import heapq
    dist=[float('inf')]*N; dist[0]=0; heap=[(0,0)]
    while heap:
        v,k=heapq.heappop(heap)
        if v!=dist[k]:continue
        for a in gens:
            r1=(k+a)%N; cand=v+a
            if cand<dist[r1]:dist[r1]=cand;heapq.heappush(heap,(cand,r1))
    assert dist[0]==0
    assert all(dist[(-j)%N]==w[j] for j in range(N))
    assert gens[0]==N and gens[1]==m and all(gens[i]<gens[i+1] for i in range(1,len(gens)-1))
    # all element generators under N cannot decompose because 2m>N
    for k in range(K+1):
        j=j0-b*k; a=1+(q+1)*k
        assert 1<=j<N and 1<=a<N
        assert (r*j-a)%N==0
        assert q*j+b*a==m+b*k
        if k<K:
            j2=j-b;a2=a+q+1
            assert j*a2-j2*a==N
    assert q*m+b*Q == max(w)
    print(f'q={q},n={n},N={N},K={K},m={m},g={genus},conductor={conductor},embedding_dim={K+2}: PASS')

if __name__=='__main__':
    for q,n in [(3,4),(4,4),(5,4),(3,6),(4,6),(3,8)]:
        verify(q,n)
    print('VERIFY_OK')
