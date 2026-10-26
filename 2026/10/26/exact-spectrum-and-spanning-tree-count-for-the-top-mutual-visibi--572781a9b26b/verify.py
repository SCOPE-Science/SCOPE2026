"""Independent finite checks for the balanced-tripartite mutual-visibility layer.

Only Python 3 standard library is required. These tests complement the
all-parameter eigenspace proof; finite checks are not an infinite proof.
"""
from itertools import combinations
from collections import Counter, deque


def construct(m):
    n = 3*m
    part = lambda x: x // m
    vertices = range(n)
    admissible = []
    for u,v in combinations(vertices,2):
        missing = {u,v}
        selected = [x for x in vertices if x not in missing]
        valid = all(part(x) != part(y) or any(part(z)!=part(x) for z in missing)
                    for x,y in combinations(selected,2))
        if valid:
            admissible.append(frozenset(missing))
    neighbors = [set() for _ in admissible]
    for i,j in combinations(range(len(admissible)),2):
        x,y = admissible[i],admissible[j]
        if len(x ^ y) == 2:
            a,b = tuple(x ^ y)
            if part(a) != part(b):
                neighbors[i].add(j)
                neighbors[j].add(i)
    return admissible, neighbors


def matvec(neigh, vector):
    return [sum(vector[j] for j in nbrs) for nbrs in neigh]


def matrix_polynomial_zero(neigh, m):
    # P(A)=A(A^2-m^2 I)(A-2m I).
    n = len(neigh)
    for j in range(n):
        a0 = [int(i==j) for i in range(n)]
        a1 = matvec(neigh,a0)
        a2 = matvec(neigh,a1)
        a3 = matvec(neigh,a2)
        a4 = matvec(neigh,a3)
        assert all(x4-2*m*x3-m*m*x2+2*m**3*x1==0
                   for x1,x2,x3,x4 in zip(a1,a2,a3,a4))


def det_mod(matrix, p):
    a=[row[:] for row in matrix]
    n=len(a)
    det=1
    for j in range(n):
        pivot=next((r for r in range(j,n) if a[r][j]%p),None)
        assert pivot is not None
        if pivot!=j:
            a[pivot],a[j]=a[j],a[pivot]
            det=-det
        v=a[j][j]%p
        det=det*v%p
        inv=pow(v,-1,p)
        for i in range(j+1,n):
            f=a[i][j]*inv%p
            if f:
                for k in range(j+1,n):
                    a[i][k]=(a[i][k]-f*a[j][k])%p
            a[i][j]=0
    return det%p


def verify(m):
    hole_sets, nbr=construct(m)
    n=len(hole_sets)
    assert n==3*m*m
    assert all(len(N)==2*m for N in nbr)
    assert sum(map(len,nbr))//2==3*m**3
    vis={0};queue=deque([0])
    while queue:
        for x in nbr[queue.popleft()]:
            if x not in vis:
                vis.add(x);queue.append(x)
    assert len(vis)==n
    triangles=sum(len(nbr[i]&nbr[j]) for i in range(n) for j in nbr[i] if i<j)//3
    assert triangles==m**3
    matrix_polynomial_zero(nbr,m)
    # Symmetric A, connected degree-2m regular, square-free annihilator,
    # trace(A)=0 and trace(A^2)=2|E| force the four multiplicities.
    expect={-m:3*m-1,0:3*(m-1)**2,m:3*(m-1),2*m:1}
    assert sum(expect.values())==n
    assert sum(e*c for e,c in expect.items())==0
    assert sum(e*e*c for e,c in expect.items())==n*2*m
    if m<=5:
        # Independent exact matrix-tree check modulo two large primes.
        L=[[(-int(j in nbr[i]) if i!=j else 2*m) for j in range(n)]
           for i in range(n)]
        principal=[row[:-1] for row in L[:-1]]
        numerator=m**(3*(m-1))*(3*m)**(3*m-1)*(2*m)**(3*(m-1)**2)
        assert numerator%(3*m*m)==0
        tau=numerator//(3*m*m)
        for p in (1_000_000_007,1_000_000_009):
            assert det_mod(principal,p)==tau%p
    print('m=',m,'vertices=',n,'edges=',sum(map(len,nbr))//2,
          'triangles=',triangles,'eigen_multiplicities=',expect,'OK')


if __name__=='__main__':
    for m in (4,5,6):
        verify(m)
    print('VERIFY_OK')
