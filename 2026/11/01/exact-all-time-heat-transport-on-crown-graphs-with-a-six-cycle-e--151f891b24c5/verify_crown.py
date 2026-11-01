"""Exact-rational checks for crown-graph heat transport formulas.

All computations use fractions. Independent finite-size checks support the
all-size analytic argument; they do not substitute for its quantifiers.
Run: python verify_crown.py
"""
from fractions import Fraction as F
from itertools import product


def matrix(n, z):
    """Heat kernel at e^{-t}=z, directly from the four eigenspaces."""
    q = 2*n
    u, v, w = z**(2*n-2), z**n, z**(n-2)
    H = [[F(0) for _ in range(q)] for _ in range(q)]
    for i in range(n):
        for j in range(n):
            ij = F(int(i == j)) - F(1,n)
            H[i][j] = F(1+u,2*n) + F(v+w,2)*ij
            H[n+i][n+j] = H[i][j]
            H[i][n+j] = F(1-u,2*n) + F(v-w,2)*ij
            H[n+i][j] = H[i][n+j]
    return H


def graph(n):
    q=2*n
    edges=[(i,n+j) for i in range(n) for j in range(n) if i!=j]
    distance=[[0 if i==j else 3 for j in range(q)] for i in range(q)]
    for i,j in edges:distance[i][j]=distance[j][i]=1
    for i in range(n):
        for j in range(n):
            if i!=j:
                distance[i][j]=distance[j][i]=2
                distance[n+i][n+j]=distance[n+j][n+i]=2
    return edges,distance


def expected(n,z):
    u,w=z**(2*n-2),z**(n-2)
    adjacent=((4*w-u)/3 if n==3 else (2*(n-2)*w-(n-4)*u)/n)
    same=2*w
    matched=(4*(n-1)*w-(n-4)*u)/n
    return [adjacent,same,matched]


def witness(n,which):
    f=[F(0)]*(2*n)
    if which==0:
        f[0]=f[1]=F(1,2);f[n]=f[n+1]=-F(1,2)
        for j in range(2,n):
            f[j]=-F(3,2) if n==3 else -F(1,2)
            f[n+j]=-f[j]
    if which==1:
        f[0]=F(1);f[1]=-F(1)
        f[n]=-F(1);f[n+1]=F(1)
    if which==2:
        f[0]=F(3,2);f[n]=-F(3,2)
        for j in range(1,n):f[j]=-F(1,2);f[n+j]=F(1,2)
    return f


def signed_int_potentials(n):
    """Enumerate *all* integer potentials fixing vertex A_0 at 0.

    The anchored graph Lipschitz polytope has integral vertices because its
    constraint matrix is a vertex-edge incidence matrix (totally unimodular).
    The graph-distance pointwise bounds are complete for those potentials.
    """
    edges,d=graph(n)
    q=2*n
    # A_0 is fixed. Place all cross-neighbors first to prune.
    variables=list(range(n+1,2*n))+list(range(1,n))+[n]
    nb=[[] for _ in range(q)]
    for a,b in edges:nb[a].append(b);nb[b].append(a)
    f=[None]*q;f[0]=0
    count=0
    def walk(j):
        nonlocal count
        if j==len(variables):
            count+=1
            yield tuple(f)
            return
        k=variables[j]
        for val in range(-d[0][k],d[0][k]+1):
            if all(f[h] is None or abs(f[h]-val)<=1 for h in nb[k]):
                f[k]=val
                yield from walk(j+1)
        f[k]=None
    return list(walk(0))


def check():
    matrices=0;potchecks=0;int_potentials=0
    for n in range(3,9):
        edges,_=graph(n)
        pairs=((0,n+1),(0,1),(0,n))
        integer=list(signed_int_potentials(n)) if n<=5 else None
        if integer is not None:int_potentials+=len(integer)
        for z in [F(1),F(1,2),F(2,3),F(3,4)]:
            H=matrix(n,z)
            matrices+=1
            assert all(sum(row)==1 for row in H)
            assert all(0<=v<=1 for row in H for v in row)
            assert H==[list(row) for row in zip(*H)]
            exp=expected(n,z)
            for case,(p,q) in enumerate(pairs):
                D=[H[p][k]-H[q][k] for k in range(2*n)]
                f=witness(n,case)
                assert all(abs(f[a]-f[b])<=1 for a,b in edges)
                assert sum(D[k]*f[k] for k in range(2*n))==exp[case]
                potchecks+=1
                if integer is not None:
                    maximum=max(sum(D[k]*g[k] for k in range(2*n)) for g in integer)
                    assert maximum==exp[case],(n,z,case,maximum,exp[case])
    print(f'CERTIFICATE_OK rational_matrices={matrices} transport_witnesses={potchecks} exhaustive_integer_potentials={int_potentials}')


if __name__=='__main__':check()
