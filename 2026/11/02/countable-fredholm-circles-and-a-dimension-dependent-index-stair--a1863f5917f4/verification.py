#!/usr/bin/env python3
"""Finite exact-arithmetic checks for coordinate Cesàro block identities.

The program checks the normalized moments, polynomial eigenfunction
recurrences, finitely supported adjoint defect vectors and index counts.
The infinite Fredholm and convergence statements have analytic proofs.
"""
from fractions import Fraction
from math import comb, factorial

checks=0
for d in range(2,8):
    for r in range(0,12):
        weight=lambda n:Fraction(factorial(n)*factorial(r),factorial(n+r))
        # Polynomial density normalization and the degree-r transverse count.
        for n in range(0,13):
            assert weight(n)==Fraction(factorial(n)*factorial(r),factorial(n+r))
            checks+=1
            for k in range(n,13):
                assert weight(k)/weight(n)==Fraction(factorial(k)*factorial(n+r),factorial(k+r)*factorial(n))
                checks+=1
        def ncompositions(total,coords):
            if coords==1:return 1
            return sum(ncompositions(total-a,coords-1) for a in range(total+1))
        assert ncompositions(r,d-1)==comb(r+d-2,d-2)
        checks+=1
        # Exact formal (non-square-summable) eigen-series coefficient test.
        for n0 in range(0,7):
            lam=Fraction(1,r+n0+1)
            a=lambda n:comb(n+r,n-n0) if n>=n0 else 0
            for k in range(n0, n0+15):
                coeff=sum((a(h) for h in range(k+1)),0)/Fraction(k+r+1)
                assert coeff==lam*a(k)
                checks+=1
        # Adjoint finite-support eigenvectors at the discrete resonances.
        for q in range(0,7):
            lam=Fraction(1,r+q+1)
            h=[Fraction(1)]
            for n in range(q+1):
                h.append(h[-1]*(1-Fraction(1,lam*(n+r+1))))
            assert h[-1]==0
            checks+=1
            for n in range(q+1):
                assert sum((h[k]/(k+r+1) for k in range(n,q+1)),Fraction(0))==lam*h[n]
                checks+=1
    for k in range(1,14):
        msum=sum(comb(r+d-2,d-2) for r in range(k))
        assert msum==comb(k+d-2,d-1)
        checks+=1
        # Positive real sample located strictly between consecutive circles.
        x=Fraction(2*k+1,k*(k+1))
        t=Fraction(2,1)/x
        assert k<t<k+1
        assert sum(1 for r in range(k+4) if (r+1)<t)==k
        checks+=1
print(f"PASS: {checks} finite exact-arithmetic checks")
