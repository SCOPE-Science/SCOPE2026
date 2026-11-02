"""Standalone verification of binary cyclic trigram-profile enumerator.

Requires Python 3 standard library only.
"""
from collections import defaultdict
from math import comb


def triple_profile(word, n):
    ans = [0]*8
    for i in range(n):
        a=(word>>i)&1
        b=(word>>((i+1)%n))&1
        c=(word>>((i+2)%n))&1
        ans[(a<<2)|(b<<1)|c]+=1
    return tuple(ans)


def observed(n):
    return len({triple_profile(w,n) for w in range(1<<n)})


def case_counts(n):
    # Two nonzero transitions, exactly one, or neither in the graph.
    main=0
    left=right=0
    for b in range(1,n+1):
        for d in range(1,n+1):
            for c in range(max(0,b-d),n+1):
                excess=n-(b+2*c+3*d)
                if excess>=0: main+=excess+1
    for b in range(1,n+1):
        for c in range(b,n+1):
            if b+2*c<=n: left+=1
    for d in range(1,n+1):
        for c in range(n+1):
            if 2*c+3*d<=n: right+=1
    return 2+main+left+right+(n%2==0)


def connected(counts):
    # Check weak connectivity among all vertices incident to a positive edge.
    edges=[(0,0),(0,1),(1,2),(1,3),(2,0),(2,1),(3,2),(3,3)]
    vertices=set()
    undirected=[set() for _ in range(4)]
    for (u,v),m in zip(edges,counts):
        if m:
            vertices.update([u,v]); undirected[u].add(v); undirected[v].add(u)
    if not vertices:return False
    reach={min(vertices)}
    while True:
        more=reach|set.union(*(undirected[v] for v in reach))
        if more==reach:break
        reach=more
    return reach==vertices


def flow_count(n):
    # Independent graph-connectivity test, not using the four case restrictions.
    found=set()
    for b in range(n+1):
        for c in range(n+1):
            for d in range(n+1):
                f=c+d-b
                if f<0:continue
                remainder=n-(b+2*c+3*d)
                if remainder<0:continue
                for a in range(remainder+1):
                    h=remainder-a
                    counts=(a,b,c,d,b,f,d,h)
                    if connected(counts):found.add(counts)
    return len(found)


def series_coefficients(N):
    # Polynomial-convolution interpretation of four rational summands.
    acc=[0]*(N+1)
    def add_term(sh, coeff, factors):
        a=[0]*(N+1)
        if sh<=N:a[sh]=coeff
        for degree,multiplicity in factors:
            for _ in range(multiplicity):
                for j in range(degree,N+1):a[j]+=a[j-degree]
        for k,v in enumerate(a):acc[k]+=v
    add_term(1,2,[(1,1)])
    add_term(2,1,[(2,1)])
    add_term(3,2,[(1,1),(2,1),(3,1)])
    add_term(4,1,[(1,2),(2,1),(3,1),(4,1)])
    add_term(7,1,[(1,2),(2,1),(3,1),(4,1)])
    return acc


def verify():
    A=series_coefficients(80)
    assert A[1:16]==[2,3,4,6,8,13,18,27,38,53,72,98,128,167,214]
    for n in range(3,81):
        assert case_counts(n)==A[n],(n,case_counts(n),A[n])
    for n in range(3,23):
        assert flow_count(n)==A[n],(n,flow_count(n),A[n])
    for n in range(3,17):
        assert observed(n)==A[n],(n,observed(n),A[n])
    assert A[20]==622 and A[30]==2959 and A[50]==22103
    print('VERIFY_OK: 78 rational/case coefficients, 20 graph-connectivity counts, 14 direct word censuses')

if __name__=='__main__':verify()
