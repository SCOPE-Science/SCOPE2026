#!/usr/bin/env python3
"""Independent integer and finite-field checks for multiset incidence matrices.

Requires Python 3 and SymPy.  All tested matrices are constructed directly
from deletion of labeled multisets and the interlacing inequalities.
"""
from itertools import combinations_with_replacement
from math import comb
from collections import Counter
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def multisets(m, degree):
    return list(combinations_with_replacement(range(m), degree))

def matrices(n, r):
    m = n-r+1
    rows=multisets(m,r-1); cols=multisets(m,r)
    E=[]; U=[]
    for s in rows:
        E.append([sum(t[:i]+t[i+1:]==s for i in range(r)) for t in cols])
        U.append([int(all(t[i] <= s[i] <= t[i+1] for i in range(r-1))) for t in cols])
    return rows,cols,Matrix(E),Matrix(U)

def target(n,r):
    if r==n: return [r]
    return sorted([j for j in range(1,r+1) for _ in range(comb(n-j-1,r-j))])

def prime_rank(M,p):
    a=[[int(t)%p for t in row] for row in M.tolist()]
    rr=0
    for c in range(M.cols):
        pivot=next((i for i in range(rr,M.rows) if a[i][c]),None)
        if pivot is None: continue
        a[rr],a[pivot]=a[pivot],a[rr]
        v=pow(a[rr][c],-1,p)
        a[rr]=[(v*x)%p for x in a[rr]]
        for i in range(rr+1,M.rows):
            v=a[i][c]
            if v: a[i]=[(x-v*y)%p for x,y in zip(a[i],a[rr])]
        rr+=1
        if rr==M.rows: return rr
    return rr

def expected_invariant_factors(d):
    vals={}
    for x in d:
        for p in [2,3,5,7]:
            exponent=0
            while x%p==0 and x>1:
                x//=p
                exponent+=1
            if exponent: vals.setdefault(p,[]).append(exponent)
        assert x==1
    N=len(d)
    out=[1]*N
    for p,exps in vals.items():
        exps.sort()
        for i,e in enumerate(exps,N-len(exps)):
            out[i]*=p**e
    return out

def verify():
    count=0; snf_count=0; rank_count=0
    for n in range(1,10):
        for r in range(1,n+1):
            s,t,E,U=matrices(n,r)
            assert E.rows == comb(n-1,r-1) and E.cols == comb(n,r)
            assert all(sum(E.row(i))==n for i in range(E.rows))
            assert all(sum(E.col(j))==r for j in range(E.cols))
            # Test all actual supports satisfy the interlacing constraint.
            for i in range(E.rows):
                for j in range(E.cols):
                    if E[i,j]: assert U[i,j]
            # The lex-ordered t_s=(s_1,...,s_{r-1}, m-1) minor.
            rankcols=[t.index(x+(n-r,)) for x in s]
            W=U[:,rankcols]
            for i in range(W.rows):
                assert W[i,i]==1
                for j in range(i+1,W.cols): assert W[i,j]==0
            # For modular rank, determine Smith elementary cyclic factors from domain change.
            fac=target(n,r)
            for p in (2,3,5,7):
                assert prime_rank(E,p)==sum(v%p!=0 for v in fac),(n,r,p)
                assert prime_rank(U,p)==U.rows,(n,r,p)
                rank_count+=1
            if n<=7:
                diag=smith_normal_form(E,domain=ZZ)
                observed=sorted(abs(int(diag[i,i])) for i in range(E.rows))
                # Invariant factors combine primary cyclic factors, not simply sorted j's.
                assert observed==sorted(expected_invariant_factors(fac)),(n,r,observed,fac)
                snf_count+=1
            count+=1
    print(f'VERIFY_OK cases={count} integer_snf={snf_count} prime_rank_comparisons={rank_count}')
if __name__=='__main__': verify()
