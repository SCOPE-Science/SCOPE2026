#!/usr/bin/env python3
"""Finite exact-arithmetic checks for signed transversals in odd graphs.

Run: python3 verify.py
No external packages or downloaded data are required.
The finite checks are not a substitute for the unrestricted proof.
"""
from itertools import combinations

checks_adjacency=0
checks_moments=0
checks_orthogonality=0
for k in range(1,7):
    n=2*k+1
    vertices=list(combinations(range(n),k))
    vertex_sets=[set(v) for v in vertices]
    a=tuple(range(0,2*k,2))
    b=tuple(range(1,2*k,2))
    c=2*k

    def psi(s):
        v=1
        for t in range(k):
            v*=int(a[t] in s)-int(b[t] in s)
        return v

    values=[psi(s) for s in vertex_sets]
    for i,s in enumerate(vertex_sets):
        adjacency_sum=sum(values[j] for j,t in enumerate(vertex_sets) if s.isdisjoint(t))
        assert adjacency_sum==(-1)**k*values[i],(k,i,adjacency_sum)
        checks_adjacency+=1

    for j in range(k+1):
        def h(s):
            if j==0:
                return 1
            if j==1:
                return int(a[0] in s)-int(c in s)
            m=j if j%2==0 else j-1
            r=1
            for i in range(m):
                r*=int(a[i] in s)-int(b[(i+1)%m] in s)
            if j%2:
                r*=int(a[j-1] in s)-int(c in s)
            return r
        hv=[h(s) for s in vertex_sets]
        overlap=sum(values[i]*values[i]*hv[i] for i in range(len(vertices)))
        expected=2**k if j==0 else 2**(k-1) if j==1 else 2**(k+1-j)
        assert overlap==expected,(k,j,overlap,expected)
        checks_moments+=1
        if k<=4:
            for degree in range(j):
                for subset in combinations(range(n),degree):
                    subset=set(subset)
                    moment=sum(hv[i] for i,s in enumerate(vertex_sets) if subset.issubset(s))
                    assert moment==0,(k,j,degree,tuple(subset),moment)
                    checks_orthogonality+=1

print('VERIFY_OK exact_adjacency_vertices=%d transversal_moments=%d lower_degree_orthogonality=%d range_k=1..6'
      %(checks_adjacency,checks_moments,checks_orthogonality))
