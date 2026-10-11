#!/usr/bin/env python3
from itertools import permutations, product
import sympy as sp

def signed_permutation_vectors(n):
    out=[]
    for p in permutations(range(n)):
        for signs in product((-1,1), repeat=n):
            v=[0]*(n*n)
            for i,j in enumerate(p):
                v[i*n+j]=signs[i]
            out.append(tuple(v))
    return out

def facet_normals(n):
    out=set()
    for i in range(n):
        for eps in product((-1,1), repeat=n):
            # eps \otimes e_i: nonzero column i
            a=[0]*(n*n)
            for r in range(n):
                a[r*n+i]=eps[r]
            out.add(tuple(a))
            # e_i \otimes eps: nonzero row i
            b=[0]*(n*n)
            for c in range(n):
                b[i*n+c]=eps[c]
            out.add(tuple(b))
    return sorted(out)

for n in range(1,6):
    V=signed_permutation_vectors(n)
    A=facet_normals(n)
    assert len(V)==2**n*sp.factorial(n)

    for v in V:
        assert sum(x*x for x in v)==n
        assert tuple(-x for x in v) in set(V)

    for a in A:
        assert sum(x*x for x in a)==n
        assert tuple(-x for x in a) in set(A)

    # Every source facet inequality is valid on every source vertex.
    for a in A:
        vals=[sum(x*y for x,y in zip(a,v)) for v in V]
        assert max(vals)==1
        assert min(vals)==-1

    # Both normal families span the full ambient matrix space.
    rankA=sp.Matrix(A).rank()
    rankV=sp.Matrix(V).rank()
    assert rankA==n*n
    assert rankV==n*n

    # Polar contacts: each polar vertex a has norm sqrt(n), and each
    # signed permutation v defines support 1 on the polar.
    for v in V:
        vals=[sum(x*y for x,y in zip(v,a)) for a in A]
        assert max(vals)==1
        assert min(vals)==-1

    print(f"n={n} signed_vertices={len(V)} polar_vertices={len(A)} rank={n*n}")

print("VERIFY_OK signed-Birkhoff-polar-radii n=1..5 exact=yes")
