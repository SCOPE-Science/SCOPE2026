#!/usr/bin/env python3
"""Exact finite-dimensional checks for hyperplane syzygy bundles on projective five-space."""
from itertools import combinations, product
from math import comb
import sympy as sp

n=6
pairs=list(combinations(range(n),2))

def skew_matrix(terms):
    A=sp.zeros(n)
    for (i,j),z in terms.items():
        A[i,j]=z
        A[j,i]=-z
    return A

def w_basis(terms):
    # Hyperplane of two-forms annihilating a bivector with given coordinates.
    omega=sp.Matrix([terms.get(p,0) for p in pairs])
    W=sp.Matrix.hstack(*sp.Matrix([list(omega)]).nullspace())
    assert W.shape==(15,14)
    return W

def contraction(x):
    # Columns are contraction by x of basis two-forms.
    M=sp.zeros(6,15)
    for j,(a,b) in enumerate(pairs):
        M[b,j]+=x[a]
        M[a,j]-=x[b]
    return M

def line_kernel(terms,a,b):
    W=w_basis(terms)
    K=contraction(a).col_join(contraction(b))*W
    return 14-K.rank()

omega6={(0,1):1,(2,3):1,(4,5):1}
omega4={(0,1):1,(2,3):1}
assert skew_matrix(omega6).rank()==6
assert skew_matrix(omega4).rank()==4
E=sp.eye(6)
def e(i):return E[:,i]
assert line_kernel(omega6,e(0),e(2))==5
assert line_kernel(omega6,e(0),e(1))==5
assert line_kernel(omega4,e(0),e(2))==6
assert line_kernel(omega4,e(0),e(1))==5
assert line_kernel(omega4,e(4),e(5))==5
# Reconstruct the fourteen 2-form columns displayed in the October 2026 paper.
source_cols=list(range(15))
removed=[pairs.index(p) for p in [(0,1),(2,3),(4,5)]]
Ncols=[sp.eye(15)[:,j] for j in range(15) if j not in removed]
Ncols.append(sp.eye(15)[:,removed[0]]+sp.eye(15)[:,removed[1]])
Ncols.append(sp.eye(15)[:,removed[1]]+sp.eye(15)[:,removed[2]])
N=sp.Matrix.hstack(*Ncols)
assert N.shape==(15,14) and N.rank()==14
src_annihilator=sp.Matrix.hstack(*N.T.nullspace())
assert src_annihilator.shape==(15,1)
terms={ij:src_annihilator[j] for j,ij in enumerate(pairs) if src_annihilator[j]}
assert skew_matrix(terms).rank()==6
assert line_kernel(terms,e(2),e(4))==5
assert line_kernel(terms,e(2),e(3))==5
assert line_kernel(omega4,e(0),e(2))==6

# Full finite-geometry census of two-subspaces in the rank-four support over F_3.
def rank_modp(A,p=3):
    a=[[int(x)%p for x in row] for row in A]
    m=len(a); nn=len(a[0]) if m else 0
    r=0
    for c in range(nn):
        q=next((q for q in range(r,m) if a[q][c]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r]
        inv=pow(a[r][c],-1,p)
        a[r]=[(x*inv)%p for x in a[r]]
        for k in range(m):
            if k!=r and a[k][c]:
                f=a[k][c]
                a[k]=[(a[k][j]-f*a[r][j])%p for j in range(nn)]
        r+=1
        if r==m:break
    return r

def rref_lines_4(p=3):
    # Unique rank-two row-reduced echelon representatives in F_p^4.
    for piv in combinations(range(4),2):
        free=[(i,j) for i in range(2) for j in range(piv[i]+1,4) if j not in piv]
        for vals in product(range(p),repeat=len(free)):
            B=[[0]*4 for _ in range(2)]
            for i,j in enumerate(piv):B[i][j]=1
            for (i,j),v in zip(free,vals):B[i][j]=v
            yield B

def projection_zero(B,terms):
    # Rank of the linear map: omega restricted to Lambda^2 Ann(U).
    u,v=map(lambda z:sp.Matrix(list(z)+[0,0]),B)
    W=w_basis(terms)
    mat=contraction(u).col_join(contraction(v))*W
    return rank_modp(mat.tolist())==8

all_lines=list(rref_lines_4())
jumping=sum(projection_zero(B,omega4) for B in all_lines)
assert len(all_lines)==130 and jumping==40
assert jumping==(3+1)*(3*3+1)  # |LG(2,4)(F_3)|.
print('VERIFY_OK rank6_no_jumping_by_rank_bound=true rank6_source_matrix=true rank4_limit=true generic_h0=5 jumping_h0=6 LG_2_4_F3=40_of_130')
