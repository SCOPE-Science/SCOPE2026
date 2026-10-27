#!/usr/bin/env python3
"""Independent finite checks for the ideal-lattice/expander construction."""
from itertools import combinations, product
from fractions import Fraction
from math import prod

def rank(rows, modulus=None):
    a = [list(x) for x in rows]
    if not a: return 0
    m,n=len(a),len(a[0]); piv=0
    for c in range(n):
        k=next((k for k in range(piv,m) if a[k][c] % modulus != 0),None) if modulus else next((k for k in range(piv,m) if a[k][c]!=0),None)
        if k is None: continue
        a[k],a[piv]=a[piv],a[k]
        scale=pow(int(a[piv][c]),-1,modulus) if modulus else Fraction(1,a[piv][c])
        a[piv]=[v*scale % modulus if modulus else v*scale for v in a[piv]]
        for z in range(m):
            if z!=piv and a[z][c]:
                b=a[z][c]
                a[z]=[(v-b*w)%modulus if modulus else v-b*w for v,w in zip(a[z],a[piv])]
        piv+=1
        if piv==m: break
    return piv

def rref_subspaces(n,q):
    for r in range(n+1):
        for pivots in combinations(range(n),r):
            free=[j for j in range(n) if j not in pivots]
            cells=[(i,j) for i,p in enumerate(pivots) for j in free if j>p]
            for choices in product(range(q), repeat=len(cells)):
                basis=[[0]*n for _ in pivots]
                for i,p in enumerate(pivots):basis[i][p]=1
                for (i,j),v in zip(cells,choices):basis[i][j]=v
                yield basis

def graph(n,edges):
    A=[[0]*n for _ in range(n)]
    for i,j in edges:A[i][j]=A[j][i]=1
    return A

def check_graph(A):
    n=len(A); d=sum(A[0]); assert all(sum(row)==d for row in A)
    lam=d+1
    B=[[A[i][j]+(lam if i==j else 0) for j in range(n)] for i in range(n)]
    assert rank(B)==n
    S=[[B[i][j] for j in range(n) for b in range(2)] for i in range(n) for a in range(2)]
    assert rank(S)==n
    C=[[int(i!=j and S[i][j]!=0) for j in range(2*n)] for i in range(2*n)]
    assert all(sum(row)==2*d+1 for row in C)
    L=[[ (2*d+1 if i==j else 0)-C[i][j] for j in range(2*n)] for i in range(2*n)]
    L0=[[ (d if i==j else 0)-A[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        plus=[int(i//2==k) for i in range(2*n)]
        minus=[(1 if i==2*k else -1 if i==2*k+1 else 0) for i in range(2*n)]
        assert [sum(L[i][j]*plus[j] for j in range(2*n)) for i in range(2*n)]==[2*L0[i//2][k] for i in range(2*n)]
        assert [sum(L[i][j]*minus[j] for j in range(2*n)) for i in range(2*n)]==[2*(d+1)*v for v in minus]
    return n,d

def check_ideals_n2_q5():
    q=5;n=2;D=4;B=[[2,1],[1,2]]
    # x_{i,a}^2 = sum_j B_{ij} (x_{j,0}+x_{j,1}), cross products zero.
    squares=[[B[i//2][j//2] for j in range(D)] for i in range(D)]
    I=[[1,1,0,0],[0,0,1,1]]
    I_rank=rank(I,q)
    assert I_rank==2
    total=0; ideals=[]
    for basis in rref_subspaces(D,q):
        total+=1
        r=len(basis)
        good=True
        for u in basis:
            for j in range(D):
                # x_j u = u_j x_j^2
                v=[u[j]*z%q for z in squares[j]]
                if rank(basis+[v],q)>r:
                    good=False;break
            if not good:break
        if good:ideals.append(basis)
    assert total==1120,(total,len(ideals))
    assert len(ideals)==9,(total,len(ideals))
    assert sum(1 for basis in ideals if not basis)==1
    assert all(not basis or rank(basis+I,q)==len(basis) for basis in ideals)
    assert sum(1 for basis in ideals if len(basis) in (0,2,3,4))==9
    return total,len(ideals)

if __name__=='__main__':
    graphs=[graph(2,[(0,1)]), graph(3,[(0,1),(1,2),(2,0)]), graph(4,list(combinations(range(4),2))),graph(4,[(0,1),(1,2),(2,3),(3,0)]),graph(8,[(i,i^(1<<j)) for i in range(8) for j in range(3) if i<(i^(1<<j))])]
    print('GRAPHS', [check_graph(A) for A in graphs]); print('FINITE_IDEALS', check_ideals_n2_q5());print('VERIFY_OK')
