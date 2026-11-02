#!/usr/bin/env python3
"""Independent RREF census for linear Hamming diameter-three anticodes.
Pure Python; q=4 uses GF(4) with x^2+x+1, all other q are prime.
"""
from itertools import combinations, product
from math import comb
from collections import Counter

def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def mult(a,b,q):
    if q!=4:
        return a*b%q
    x=0
    while b:
        if b&1: x^=a
        a<<=1
        if a&4: a^=7
        b>>=1
    return x

def rref_bases(n,k,q):
    for piv in combinations(range(n),k):
        free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
        for choices in product(range(q),repeat=len(free)):
            rows=[[0]*n for _ in range(k)]
            for i,p in enumerate(piv): rows[i][p]=1
            for (i,j),v in zip(free, choices): rows[i][j]=v
            yield rows

def maxweight_and_support(rows,q,n):
    k=len(rows)
    sup=sum(1 for j in range(n) if any(row[j] for row in rows))
    maxw=0
    for coeff in product(range(q),repeat=k):
        w=0
        for j in range(n):
            v=0
            for i,a in enumerate(coeff):v=add(v,mult(a,rows[i][j],q),q)
            w+=v!=0
        maxw=max(maxw,w)
        if maxw>3:break
    return maxw,sup

def expected(q,n):
    x=1+n+q*comb(n,2)+(2*q*q-q)*comb(n,3)
    if q==3: x+=8*comb(n,4)
    return x

def run_case(q,n):
    tally=Counter(); total=0
    for k in range(min(n,3)+1):
        for rows in rref_bases(n,k,q):
            total+=1
            mx,s=maxweight_and_support(rows,q,n)
            if mx<=3:tally[(s,k)]+=1
    assert sum(tally.values())==expected(q,n), (q,n,tally,expected(q,n))
    if n>=4:
        assert tally.get((4,2),0)==(8*comb(n,4) if q==3 else 0)
    return total,dict(sorted(tally.items()))

if __name__=='__main__':
    tests={3:range(0,6),4:range(0,5),5:range(0,5),7:range(0,5)}
    for q,ns in tests.items():
        for n in ns:
            total,tally=run_case(q,n)
            print('MATCH',q,n,expected(q,n),'all_subspaces_dim_le_3',total,'support_rank',tally)
    print('VERIFY_OK')
