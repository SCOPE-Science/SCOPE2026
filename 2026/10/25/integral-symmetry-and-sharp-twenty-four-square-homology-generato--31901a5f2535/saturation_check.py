#!/usr/bin/env python3
"""Supplemental exact Smith-normal-form check of the quadrilateral lattice."""
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def quadrilateral(i,j,k,l):
    return {tuple(sorted(p)):s for p,s in (((i,j),1),((k,l),1),((i,k),-1),((j,l),-1))}

for n in (4,5,6):
    pairs=list(combinations(range(n),2))
    cols=[]
    for i,j,k,l in combinations(range(n),4):
        for q in (quadrilateral(i,j,k,l),quadrilateral(i,j,l,k),quadrilateral(i,k,l,j)):
            cols.append([q.get(p,0) for p in pairs])
    m=Matrix(len(pairs),len(cols),lambda r,c:cols[c][r])
    snf=smith_normal_form(m,domain=ZZ)
    nonzero=[abs(int(snf[i,i])) for i in range(min(snf.rows,snf.cols)) if snf[i,i]]
    expected=n*(n-3)//2
    assert nonzero==[1]*expected, (n,nonzero)
    print('n',n,'quad_columns',len(cols),'rank',len(nonzero),'all_smith_factors_one',True)
print('VERIFY_OK_INTEGRAL_QUADRILATERAL_LATTICE')
