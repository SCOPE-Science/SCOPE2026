#!/usr/bin/env python3
"""Exact checks for uniform acyclic orientations of a two-by-n bipartite graph."""
from fractions import Fraction as F
from itertools import product


def is_dag(bits, n):
    # Vertices 0,1 are the two hubs; vertices 2,...,n+1 are leaves.
    m = n + 2
    adj = [[] for _ in range(m)]
    indeg = [0] * m
    for j in range(n):
        for r in range(2):
            u, v = (r, j + 2) if bits[2*j+r] else (j + 2, r)
            adj[u].append(v)
            indeg[v] += 1
    ready = [u for u in range(m) if indeg[u] == 0]
    seen = 0
    while ready:
        u = ready.pop()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                ready.append(v)
    return seen == m


def covariance(n, z, c, d):
    return [[F(1,4) if i == j else
             c if i//2 == j//2 else
             d if i%2 == j%2 else -d
             for j in range(2*n)] for i in range(2*n)]


def formula(n):
    z = 2*3**n-2**n
    c = F(3**(n-1)-2**(n-1),2*z)
    d = F(3**(n-2),2*z)
    s = F(1,4)+c
    a = F(1,2*s)
    b = F(n+1,8*d*(n+2))
    f = F(1,8*d*(n+2))
    q = [[a+b if i == j else
          a-b if i//2 == j//2 else
          -f if i%2 == j%2 else f
          for j in range(2*n)] for i in range(2*n)]
    return z,c,d,covariance(n,z,c,d),q


def matrix_product(A,B):
    N=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(N)),F(0))
             for j in range(N)] for i in range(N)]


def main():
    checks=0
    for n in range(2,9):
        z,c,d,C,Q=formula(n)
        vectors=[]
        for bits in product((0,1),repeat=2*n):
            permitted=not ((0,1) in tuple(tuple(bits[2*j:2*j+2]) for j in range(n))
                         and (1,0) in tuple(tuple(bits[2*j:2*j+2]) for j in range(n)))
            actual=is_dag(bits,n)
            assert permitted == actual, (n,bits)
            checks+=1
            if actual:
                vectors.append(bits)
        assert len(vectors)==z
        checks+=1
        m=2*n
        means=[F(sum(x[i] for x in vectors),z) for i in range(m)]
        for a in means:
            assert a==F(1,2)
            checks+=1
        for i in range(m):
            for j in range(m):
                empir=F(sum(x[i]*x[j] for x in vectors),z)-means[i]*means[j]
                assert empir==C[i][j],(n,i,j,empir,C[i][j])
                checks+=1
        prod=matrix_product(C,Q)
        for i in range(m):
            for j in range(m):
                assert prod[i][j]==(1 if i==j else 0)
                checks+=1
                if i == j:
                    assert Q[i][j]>0
                elif i//2==j//2 or i%2==j%2:
                    assert C[i][j]>0 and Q[i][j]<0
                else:
                    assert C[i][j]<0 and Q[i][j]>0
                checks+=1
        assert c+6*d==F(1,4) and c>0 and d>0
        checks+=1
        print(f'n={n}: acyclic orientations={z}, verified covariance and precision ({m} indicators)')
    # Finite all-parameter algebraic identity for 2 <= n <= 100, not an infinite proof.
    for n in range(2,101):
        z,c,d,C,Q=formula(n)
        assert c+6*d==F(1,4)
        assert 4*d>0 and 2*(n+2)*d>0 and (F(1,4)+c)>0
        checks+=2
    print(f'PASS: {checks} exact assertions')

if __name__=='__main__':
    main()
