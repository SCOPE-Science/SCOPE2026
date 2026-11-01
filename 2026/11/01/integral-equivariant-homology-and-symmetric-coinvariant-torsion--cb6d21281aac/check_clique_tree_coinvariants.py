#!/usr/bin/env python3
"""Exact integer Smith-normal-form checks of symmetric-group coinvariants.
Requires sympy. Computations are supporting finite checks, not an infinite proof.
"""
from itertools import permutations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def test(m, sign_twist):
    rel=[[1]*m]
    for p in permutations(range(m)):
        parity=(-1)**sum(p[i]>p[j] for i in range(m) for j in range(i+1,m)) if sign_twist else 1
        for i in range(m):
            r=[0]*m
            r[i]+=1
            r[p[i]]-=parity
            if any(r):rel.append(r)
    d=smith_normal_form(Matrix(rel),domain=ZZ)
    diag=[abs(int(d[i,i])) for i in range(min(d.rows,d.cols))]
    tor=tuple(x for x in diag if x>1)
    free=m-sum(x!=0 for x in diag)
    if not sign_twist:
        want=((m,),0)
    elif m==2:
        want=((),1)
    elif m%2==0:
        want=((2,),0)
    else:
        want=((),0)
    assert (tor,free)==want,(m,sign_twist,tor,free,want)
    return tor,free

if __name__=='__main__':
    for m in range(2,9):
        print(f'm={m}: untwisted={test(m,False)}, sign-twisted={test(m,True)}')
    print('PASS 14 Smith-normal-form presentations')
