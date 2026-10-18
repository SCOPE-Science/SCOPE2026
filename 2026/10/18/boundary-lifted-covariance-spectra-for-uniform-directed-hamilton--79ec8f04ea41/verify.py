"""Exact verification for the adjacency-covariance spectrum of random directed Hamiltonian paths.

Python 3 standard library only.  Enumerates all permutations through seven vertices,
checks every matrix entry against the asserted universal covariance, and tests
the four orthogonal spectral projections on a spanning set of edge weights.
"""
from fractions import Fraction as F
from itertools import permutations


def dot(v, w):
    return sum((x*y for x,y in zip(v,w)), F(0))


def matrix_formula(n, edges, cyclic=False):
    # Two compatible distinct directed arcs can be jointly prescribed with
    # probability 1/(n(n-1)); arcs with duplicate sources/targets or a directed
    # two-cycle cannot coexist in a Hamiltonian path.
    M = len(edges)
    C = [[F(0) for _ in range(M)] for _ in range(M)]
    for i, (a,b) in enumerate(edges):
        for j, (c,d) in enumerate(edges):
            if i == j:
                C[i][j] = F(n-2,(n-1)*(n-1)) if cyclic else F(n-1,n*n)
            elif a == c or b == d or (a == d and b == c):
                C[i][j] = -F(1,(n-1)*(n-1)) if cyclic else -F(1,n*n)
            else:
                C[i][j] = F(1,(n-1)*(n-1)*(n-2)) if cyclic else F(1,n*n*(n-1))
    return C


def matvec(C, v):
    return [dot(row,v) for row in C]


def row_sums(H,n):
    return [sum((H[a][b] for b in range(n) if b != a),F(0)) for a in range(n)]


def components(v, n, edges):
    # Center the edge weights; split into symmetric/antisymmetric parts;
    # remove the corresponding vertex-potential (row-sum) components.
    size=n*(n-1)
    mu=sum(v,F(0))/size
    H=[[F(0) for _ in range(n)] for _ in range(n)]
    for (a,b),z in zip(edges,v): H[a][b]=z-mu
    S=[[F(0) if a==b else (H[a][b]+H[b][a])/2 for b in range(n)] for a in range(n)]
    A=[[F(0) if a==b else (H[a][b]-H[b][a])/2 for b in range(n)] for a in range(n)]
    sr=row_sums(S,n)
    ar=row_sums(A,n)
    us=[z/F(n-2) for z in sr]
    ua=[z/F(n) for z in ar]
    add_sym=[us[a]+us[b] for a,b in edges]
    add_anti=[ua[a]-ua[b] for a,b in edges]
    res_sym=[S[a][b]-us[a]-us[b] for a,b in edges]
    res_anti=[A[a][b]-ua[a]+ua[b] for a,b in edges]
    return ([mu]*size, add_sym, add_anti, res_sym, res_anti)


def exhaustive_covariance(n, edges, cyclic=False):
    m=len(edges); idx={e:i for i,e in enumerate(edges)}
    joint=[[0]*m for _ in range(m)]
    marginal=[0]*m
    count=0
    candidates=((0,)+tail for tail in permutations(range(1,n))) if cyclic else permutations(range(n))
    for p in candidates:
        ind=[idx[p[k],p[(k+1)%n]] for k in range(n if cyclic else n-1)]
        count+=1
        for i in ind:
            marginal[i]+=1
            for j in ind:
                joint[i][j]+=1
    C=[[F(joint[i][j],count)-F(marginal[i]*marginal[j],count*count)
        for j in range(m)] for i in range(m)]
    assert marginal == [count//(n-1) if cyclic else count//n]*m
    return C


def run():
    tests=0
    for n in range(3,8):
        edges=[(a,b) for a in range(n) for b in range(n) if a!=b]
        for cyclic in (False,True):
            C=matrix_formula(n,edges,cyclic)
            CE=exhaustive_covariance(n,edges,cyclic)
            for rowa,rowb in zip(C,CE):
                for a,b in zip(rowa,rowb):
                    assert a==b, (n,cyclic,a,b)
                    tests+=1
            eigen=([F(0), F(0), F(0),F(1,n-1),F(n,(n-1)*(n-2))]
                   if cyclic else
                   [F(0),F(1,n*(n-1)),F(1,n*(n-1)),F(1,n),F(n+1,n*(n-1))])
            for j in range(len(edges)):
                basis=[F(int(k==j)) for k in range(len(edges))]
                parts=components(basis,n,edges)
                assert all(sum((v[k] for v in parts),F(0)) == basis[k]
                           for k in range(len(edges)))
                tests+=len(edges)
                for v,lam in zip(parts,eigen):
                    assert matvec(C,v)==[lam*x for x in v],(n,cyclic,j,lam)
                    tests+=len(edges)
                assert all(dot(parts[u],parts[v])==0 for u in range(5) for v in range(u+1,5))
                tests+=10
            dims=(1,2*(n-1),n*(n-3)//2,(n-1)*(n-2)//2)
            assert sum(dims)==n*(n-1)
            assert dims[2]>=0 and dims[3]>0
            tests+=3
            weighted=[F((3*a+5*b+a*b)%7-3) for a,b in edges]
            parts=components(weighted,n,edges)
            z=dot(weighted,matvec(C,weighted))
            spectral=sum((lam*dot(v,v) for lam,v in zip(eigen,parts)),F(0))
            assert z==spectral
            tests+=1
    print(f'PASS {tests} exact covariance and spectral assertions (all paths and oriented cycles for n=3..7)')


if __name__=='__main__':run()
