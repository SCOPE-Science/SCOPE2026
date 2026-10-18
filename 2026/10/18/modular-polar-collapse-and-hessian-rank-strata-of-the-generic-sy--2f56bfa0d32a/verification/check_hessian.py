#!/usr/bin/env python3
"""Reproducible finite diagnostics for the symmetric determinant Hessian theorem.
The infinite formulas are proved in RESULT.md; these checks alone are not proofs.
"""
import itertools
import sympy as s

def setup(n):
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    var=s.symbols('x0:'+str(len(pairs)))
    A=s.zeros(n)
    for (i,j),v in zip(pairs,var): A[i,j]=A[j,i]=v
    f=s.expand(A.det(method='berkowitz'))
    H=s.hessian(f,var)
    grad=[s.diff(f,x) for x in var]
    return pairs,var,A,f,H,grad

def det_rank_mod(A,p):
    rows=[[int(v)%p for v in A.row(i)] for i in range(A.rows)]
    rank=0
    for c in range(A.cols):
        q=next((k for k in range(rank,A.rows) if rows[k][c]%p),None)
        if q is None:continue
        rows[rank],rows[q]=rows[q],rows[rank]
        inv=pow(rows[rank][c],-1,p)
        rows[rank]=[(v*inv)%p for v in rows[rank]]
        for i in range(A.rows):
            if i!=rank and rows[i][c]:
                w=rows[i][c]; rows[i]=[(a-w*b)%p for a,b in zip(rows[i],rows[rank])]
        rank+=1
        if rank==A.rows:break
    return rank

def check(n):
    pairs,x,A,f,H,g=setup(n)
    N=len(x); m=n*(n-1)//2; E=(n+1)*(n-2)//2
    c=(-1)**(n-1+m)*(n-1)*2**m
    # Identity Hessian block determinant and exact predicted ranks.
    identity={v: int(i==j) for (i,j),v in zip(pairs,x)}
    Hi=H.subs(identity)
    assert Hi.det(method='berkowitz')==c
    for p in (2,3,5,7):
        r=det_rank_mod(Hi,p)
        expect= (n if n%2==0 else n-1) if p==2 else N-int((n-1)%p==0)
        assert r==expect,(n,p,r,expect)
    for corank in (1,2,3):
        if corank>n: continue
        diagonal={v: int(i==j and i<n-corank) for (i,j),v in zip(pairs,x)}
        M=H.subs(diagonal)
        for p in (2,3,5):
            r=det_rank_mod(M,p)
            expect=(0 if corank>=3 else (2 if p==2 else (3 if corank==2 else n+1)))
            assert r==expect,(n,corank,p,r,expect)
    if n==3:
        assert s.expand(H.det(method='berkowitz')-c*f**E)==0
    if n==4:
        # Check at one nonsingular symmetric integer matrix, not as polynomial proof.
        val={v: int(i==j)*(i+2)+(0 if i==j else ((i+j)%3-1)) for (i,j),v in zip(pairs,x)}
        detA=int(A.subs(val).det())
        assert int(H.subs(val).det(method='berkowitz'))==c*detA**E
    # Characteristic two: all offdiagonal polar coordinates vanish identically.
    for (i,j),gij in zip(pairs,g):
        if i!=j:
            assert all(int(z)%2==0 for z in s.Poly(gij,*x).coeffs())
    # Characteristic two alternating full-rank is an exceptional polar base point.
    if n==4:
        alt={v:int((i,j) in ((0,1),(2,3))) for (i,j),v in zip(pairs,x)}
        assert int(A.subs(alt).det())%2==1
        assert all(int(z.subs(alt))%2==0 for z in g)
        assert det_rank_mod(H.subs(alt),2)==n
    if n==3:
        alt_corank={v:int((i,j)==(0,1)) for (i,j),v in zip(pairs,x)}
        assert det_rank_mod(A.subs(alt_corank),2)==2
        assert det_rank_mod(H.subs(alt_corank),2)==0
    return f'n={n} N={N} E={E} c={c} identity_ranks=OK singular_ranks=OK polar_mod2=OK'

if __name__=='__main__':
    for n in (3,4):print(check(n))
    print('VERIFY_OK')
