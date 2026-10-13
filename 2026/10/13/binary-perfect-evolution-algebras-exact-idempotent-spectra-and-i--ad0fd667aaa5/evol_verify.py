"""Reproduce binary-field idempotent distributions for regular evolution-algebra structure matrices.
Uses only the Python standard library; no external records or mathematical software required.
"""
from itertools import product
from math import prod

def grank(rows,n):
    rows=list(rows)
    piv=0
    for bit in range(n):
        nxt=next((j for j in range(piv,len(rows)) if rows[j]>>bit&1),None)
        if nxt is None: continue
        rows[piv],rows[nxt]=rows[nxt],rows[piv]
        for j in range(len(rows)):
            if j!=piv and rows[j]>>bit&1: rows[j]^=rows[piv]
        piv+=1
    return piv

def gaussian(n,r):
    if r<0 or r>n: return 0
    num=prod(2**(n-j)-1 for j in range(r))
    den=prod(2**(r-j)-1 for j in range(r))
    return num//den

def gl(n): return prod(2**n-2**j for j in range(n))

def count_formula(n,r):
    return gaussian(n,r)*sum((-1)**j * 2**(j*(j-1)//2) * gaussian(n-r,j) * 2**((r+j)*(n-r-j))*gl(n-r-j) for j in range(n-r+1))

def independent_enumerate(n):
    counts=[0]*(n+1)
    total=0
    for rows in product(range(2**n),repeat=n):
        if grank(rows,n)!=n:continue
        # x^2 = x in F2, hence idempotents are kernel of (M^T - I).
        # row representation of M^T-I from rows of M
        mtrows=[sum(((rows[i]>>j)&1)<<i for i in range(n)) ^ (1<<j) for j in range(n)]
        nullity=n-grank(mtrows,n)
        counts[nullity]+=1
        total+=1
    return counts,total

if __name__=='__main__':
    for n in range(1,5):
        formula=[count_formula(n,r) for r in range(n+1)]
        brute,total=independent_enumerate(n)
        assert formula==brute,(n,formula,brute)
        assert sum(formula)==total==gl(n)
        print('n=',n,'counts_by_nullity=',formula,'GL_size=',total)
    for n in range(5,9):
        formula=[count_formula(n,r) for r in range(n+1)]
        assert sum(formula)==gl(n)
        assert formula[0]>0
        print('n=',n,'idempotent_free=',formula[0], 'total=',gl(n))
    print('VERIFY_OK')
