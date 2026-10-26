#!/usr/bin/env python3
"""Independent finite-field projection-pair rank check (binary field)."""
import itertools
from collections import Counter
from fractions import Fraction


def rank_rows(rows,n):
    rows=list(rows); rank=0
    for bit in reversed(range(n)):
        piv=next((i for i in range(rank,len(rows)) if (rows[i]>>bit)&1),None)
        if piv is None: continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        for i in range(len(rows)):
            if i!=rank and (rows[i]>>bit)&1: rows[i]^=rows[rank]
        rank+=1
    return rank


def matrix_from_UB(cols_U,rows_B,n,s):
    F=[]
    for i in range(n):
        row=0
        for j in range(n):
            entry=0
            for k in range(s): entry^=((cols_U[k]>>i)&1) & ((rows_B[k]>>j)&1)
            row |=entry<<j
        F.append(row)
    return tuple(F)


def is_idempotent(F,n):
    for i in range(n):
        for j in range(n):
            dot=0
            for k in range(n): dot^=((F[i]>>k)&1)&((F[k]>>j)&1)
            if dot!=((F[i]>>j)&1): return False
    return True


def enumer(n,s):
    forms={}
    for B in itertools.product(range(1<<n),repeat=s):
        if rank_rows(B,n)!=s:continue
        right=[ [x for x in range(1<<n) if tuple((x&row).bit_count()%2 for row in B)==tuple(int(j==i) for j in range(s))] for i in range(s)]
        for U in itertools.product(*right):
            F=matrix_from_UB(U,B,n,s)
            assert is_idempotent(F,n)
            forms[F]=True
    return list(forms)


def diag_counts(n,s,r):
    freqs=Counter()
    fs=enumer(n,s)
    for F in fs:
        # Rank EF is rank of top r ROWS; rank FE rank of first r COLUMNS.
        a=rank_rows(F[:r],n)
        c=rank_rows([row&((1<<r)-1) for row in F],r)
        freqs[a,c]+=1
    return fs,freqs


def pr(m,s,q=2):
    num=1
    for i in range(s):num*=q**m-q**i
    den=q**(m*s)
    return Fraction(num,den)


def ranklaw(r,s):
    out=Counter()
    for A in itertools.product(range(1<<s),repeat=r):
        out[rank_rows(A,s)]+=1
    return {k:Fraction(v,2**(r*s)) for k,v in out.items()}

if __name__=='__main__':
    total=0
    for n,r,s in [(2,1,1),(3,1,1),(4,1,1),(4,2,2),(5,1,1),(5,2,2),(5,3,2)]:
        fs,c=diag_counts(n,s,r)
        total+=len(fs)
        product=ranklaw(r,s)
        tv=sum(abs(Fraction(c.get((i,j),0),len(fs))-product.get(i,0)*product.get(j,0)) for i in range(min(r,s)+1) for j in range(min(r,s)+1))/2
        bound=1-pr(n-r,s)/pr(n,s) if n-r>=s else Fraction(1)
        assert tv<=bound
        if s==1:
            asym=Fraction(2,2)*(1-Fraction(1,2)) if r==1 else None
        print(f'q=2 n={n} r={r} s={s} idempotents={len(fs)} joint={dict(sorted(c.items()))} tv={tv} bound={bound}')
    print('ALL_OPPOSITE_PRODUCT_RANK_CHECKS_PASSED',total)
