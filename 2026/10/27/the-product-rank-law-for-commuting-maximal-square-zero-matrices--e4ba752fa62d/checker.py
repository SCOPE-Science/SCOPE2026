#!/usr/bin/env python3
"""Direct finite-field enumeration of commuting maximal square-zero matrices.

Enumerate possible F in the centralizer of E=[0 I; 0 0] and test
F^2=0 and rank F=m directly. All operations are over prime fields.
"""
from itertools import product
from fractions import Fraction


def rank(matrix, p):
    a=[list(map(lambda x:x%p,row)) for row in matrix]
    n=len(a); k=len(a[0]) if n else 0; r=0
    for j in range(k):
        pivot=next((i for i in range(r,n) if a[i][j]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        z=pow(a[r][j],-1,p)
        a[r]=[(x*z)%p for x in a[r]]
        for i in range(n):
            if i!=r and a[i][j]:
                z=a[i][j]
                a[i]=[(a[i][h]-z*a[r][h])%p for h in range(k)]
        r+=1
        if r==n: break
    return r


def mm(a,b,p):
    n=len(a); k=len(b); t=len(b[0]) if b else 0
    return tuple(tuple(sum(a[i][u]*b[u][j] for u in range(k))%p
                 for j in range(t)) for i in range(n))


def phi_fraction(k,p):
    v=Fraction(1)
    for j in range(1,k+1): v*=Fraction(p**j-1,p**j)
    return v


def check_case(m,p):
    vals=range(p)
    mats=[tuple(tuple(t[i*m:(i+1)*m]) for i in range(m))
          for t in product(vals,repeat=m*m)]
    z=tuple((0,)*m for i in range(m))
    by_r=[0]*(m//2+1)
    tested=0; nil_A=0; eligible=0
    for A in mats:
        if mm(A,A,p)!=z: continue
        nil_A+=1
        r=rank(A,p)
        for B in mats:
            tested+=1
            AB=mm(A,B,p); BA=mm(B,A,p)
            if any((AB[i][j]+BA[i][j])%p for i in range(m) for j in range(m)):
                continue
            F=tuple(A[i]+B[i] for i in range(m))+tuple(z[i]+A[i] for i in range(m))
            if rank(F,p)==m:
                eligible+=1
                by_r[r]+=1
    phm=phi_fraction(m,p)
    theory=[]
    for r in range(m//2+1):
        val=Fraction(p**(m*m))*phm/phi_fraction(r,p)
        assert val.denominator==1,(m,p,r,val)
        theory.append(val.numerator)
    assert by_r==theory,(m,p,by_r,theory)
    assert sum(by_r)==eligible
    total_squarezero=Fraction(p**(2*m*m))*phi_fraction(2*m,p)/phm
    assert total_squarezero.denominator==1
    prob=Fraction(eligible,total_squarezero.numerator)
    expected=Fraction(1,p**(m*m))*phm*phm/phi_fraction(2*m,p)*sum(
        (Fraction(1,1)/phi_fraction(r,p) for r in range(m//2+1)),Fraction(0))
    assert prob==expected,(m,p,prob,expected)
    print(f'PASS q={p} m={m} nilpotent_A={nil_A} tested_AB_pairs={tested} '
          f'commuting_F={eligible} by_product_rank={by_r} '
          f'all_maximal_squarezero_F={total_squarezero.numerator} '
          f'commutation_probability={prob}')
    return tested

if __name__=='__main__':
    t=0; cases=[(1,2),(1,3),(1,5),(1,7),(2,2),(2,3),(2,5),(2,7),(3,2)]
    for m,p in cases: t+=check_case(m,p)
    print(f'ALL_MAXIMAL_SQUAREZERO_COMMUTATION_TESTS_PASSED cases={len(cases)} pairs={t}')
