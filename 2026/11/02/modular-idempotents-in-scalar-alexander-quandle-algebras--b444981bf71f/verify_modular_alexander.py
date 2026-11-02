"""Reproducibility checks for modular scalar-Alexander quandle idempotents.

Requires Python 3 and NumPy. Direct coefficient multiplication and modular
linear algebra are independent checks of the proved unit-group decomposition.
"""
from itertools import product
import numpy as np


def residues(p, lam):
    mu = (1 - lam) % p
    return [j for j in range(1, p - 1)
            if (pow(lam, j, p) + pow(mu, j, p)) % p == 1]


def count_1d(p, lam, batch=25000, collect=False):
    """Exhaust all p^p elements of F_p[Alex(F_p, lam)] directly."""
    mu = (1 - lam) % p
    result, witnesses = 0, []
    for lo in range(0, p ** p, batch):
        idx = np.arange(lo, min(lo + batch, p ** p), dtype=np.int64)
        A = np.column_stack([(idx // (p ** i)) % p for i in range(p)])
        B = np.zeros_like(A)
        for i in range(p):
            for j in range(p):
                k = (lam * i + mu * j) % p
                B[:, k] = (B[:, k] + A[:, i] * A[:, j]) % p
        rows = A[np.all(A == B, axis=1)]
        result += len(rows)
        if collect:
            witnesses.extend(tuple(int(x) for x in a) for a in rows)
    return result, witnesses


def mul_1d(a, b, p, lam):
    mu=(1-lam)%p
    c=[0]*p
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b):
                c[(lam*i+mu*j)%p]=(c[(lam*i+mu*j)%p]+ai*bj)%p
    return tuple(c)


def nullity_mod_p(A, p):
    """Independent modular row reduction, without external algebra packages."""
    A=[row.copy() for row in A]
    m=len(A); n=len(A[0]); pivot=0
    for col in range(n):
        pos=next((r for r in range(pivot,m) if A[r][col]%p),None)
        if pos is None: continue
        A[pivot], A[pos] = A[pos], A[pivot]
        inv=pow(A[pivot][col],-1,p)
        A[pivot]=[(inv*x)%p for x in A[pivot]]
        for r in range(pivot+1,m):
            z=A[r][col]%p
            if z:
                A[r]=[(a-z*b)%p for a,b in zip(A[r],A[pivot])]
        pivot+=1
        if pivot==m: break
    return n-pivot


def additive_operator_nullity(p,dim,lam):
    """D=T_lam+T_(1-lam)-I on additive group-algebra augmentation J.

    In the basis e_g-e_0 indexed by nonzero g, each T_a permutes columns.
    No quandle-product idempotent equations or eigenspace formulas are used.
    """
    vals=[v for v in product(range(p),repeat=dim) if any(v)]
    loc={v:i for i,v in enumerate(vals)}
    n=len(vals)
    mat=[[0]*n for _ in range(n)]
    for k,v in enumerate(vals):
        for a,sign in ((lam,1),((1-lam)%p,1),(1,-1)):
            w=tuple((a*x)%p for x in v)
            i=loc[w]
            mat[i][k]=(mat[i][k]+sign)%p
    return nullity_mod_p(mat,p)


def main():
    for p in (5,7):
        for lam in range(2,p):
            good=residues(p,lam)
            predicted=1+p**len(good)
            actual,_=count_1d(p,lam)
            assert actual==predicted,(p,lam,predicted,actual)
            print('EXHAUSTIVE',p,lam,'good=',good,'idempotents=',actual)
    for p,dim,lam in [(5,2,2),(5,2,3),(7,2,2),(7,2,4),
                      (7,2,3),(11,2,3),(11,2,5)]:
        good=residues(p,lam)
        predicted=len(good)*((p**dim-1)//(p-1))
        actual=additive_operator_nullity(p,dim,lam)
        assert actual==predicted,(p,dim,lam,predicted,actual)
        print('LINEAR_RANK',p,dim,lam,'kernel_dimension=',actual)
    for lam in (2,4):
        count,ww=count_1d(7,lam,collect=True)
        W=[a for a in ww if any(a)]
        assert len(W)==count-1
        S=set(W)
        for a in W:
            for b in W:
                assert mul_1d(a,b,7,lam) in S
        print('INDUCED_QUANDLE_CLOSURE',7,lam,'nonzero_idempotents=',len(W))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
