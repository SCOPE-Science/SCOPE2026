"""Reproducible finite checks for the stated Schreier permutation theorem.
Requires Python 3, SciPy, NumPy. The universal proof is analytic, not numerical.
"""
from fractions import Fraction
from math import floor, log2
import numpy as np
from scipy.optimize import linprog

def admissible_masks(n):
    return [mask for mask in range(1, 1 << n)
            if mask.bit_count() <= ((mask & -mask).bit_length())]

def exact_lp(m):
    masks=admissible_masks(m)
    A=np.array([[int(bool(mask & (1 << i))) for i in range(m)]
                for mask in masks],dtype=float)
    primal=linprog(-np.ones(m), A_ub=A, b_ub=np.ones(len(masks)),bounds=(0,None),method='highs')
    dual=linprog(np.ones(len(masks)),A_ub=-A.T,b_ub=-np.ones(m),bounds=(0,None),method='highs')
    assert primal.success and dual.success
    x=[Fraction(float(t)).limit_denominator(100000) for t in primal.x]
    z=[Fraction(float(t)).limit_denominator(100000) for t in dual.x]
    assert all(t>=0 for t in x+z)
    assert all(sum(x[i] for i in range(m) if mask&(1<<i))<=1 for mask in masks)
    assert all(sum(z[j] for j,mask in enumerate(masks) if mask&(1<<i))>=1 for i in range(m))
    assert sum(x)==sum(z), (m,sum(x),sum(z))
    J=m.bit_length()-1
    B=Fraction(J,1)+Fraction(m-(1<<J)+1,1<<J)
    assert B<=sum(x)<=J+1
    return sum(x)

def test_dyadic(n):
    y=[Fraction(1,1 << (i.bit_length()-1)) for i in range(1,n+1)]
    assert all(sum(y[j] for j in range(k-1,2*k-1))==1 for k in range(1,(n+1)//2+1))
    return y

def test_subset_compression():
    cases=0
    for n in range(1,10):
        m=(n+1)//2
        C=exact_lp(m)
        masks=admissible_masks(n)
        A=np.array([[int(bool(mask & (1 << i))) for i in range(n)]
                    for mask in masks],dtype=float)
        for B in range(1, 1<<n):
            if B.bit_count()>m: continue
            c=np.array([int(bool(B & (1 << i))) for i in range(n)],dtype=float)
            res=linprog(-c, A_ub=A, b_ub=np.ones(len(masks)),
                        bounds=(0,None),method='highs')
            assert res.success and -res.fun <= float(C)+1e-8
            cases+=1
        terminal=sum(1<<i for i in range(n-m,n))
        assert terminal in masks
    return cases

if __name__=='__main__':
    values=[exact_lp(m) for m in range(1,14)]
    assert values[:8]==[Fraction(t) for t in [1,2,2,Fraction(5,2),Fraction(8,3),3,3,Fraction(13,4)]]
    test_dyadic(512)
    subset_cases=test_subset_compression()
    print('Exact finite Schreier primal-dual certificates: m=1,...,13')
    print('C_m:',', '.join(f'{m}:{v}' for m,v in enumerate(values,1)))
    print('Dyadic sliding-window identities: k=1,...,256 (exact fractions).')
    print('Subset functional domination cases:', subset_cases, 'for N=1,...,9.')
