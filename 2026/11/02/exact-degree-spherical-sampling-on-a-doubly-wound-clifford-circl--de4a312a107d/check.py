#!/usr/bin/env python3
"""Reproduce exact arithmetic checks of cyclic Clifford-circle harmonic ranks.
Only Python standard library is required. This checker confirms finite cases;
the all-degree assertion uses the separate analytic proof.
"""
from math import comb
from collections import defaultdict


def jacobi_at_zero_numerator(s, a, b):
    # 2**s * P_s^{(a,b)}(0)
    return sum((-1)**(s-j)*comb(s+a,j)*comb(s+b,s-j) for j in range(s+1))


def weight_support(degree):
    ans=set()
    for a in range(-degree,degree+1):
        for b in range(-degree,degree+1):
            t=degree-abs(a)-abs(b)
            if t<0 or t%2:continue
            s=t//2
            if jacobi_at_zero_numerator(s,abs(a),abs(b)):
                ans.add(a+2*b)
    return ans


def predicted_support(degree):
    if degree==0:return {0}
    if degree==1:return {-2,-1,1,2}
    if degree==2:return set(range(-4,5))-{0}
    if degree==4:return set(range(-8,9))-{-3,3}
    return set(range(-2*degree,2*degree+1))


def recurrence_step(P,Q):
    # If P=2^(ell-1) U_(ell-1)((cos t+cos 2t)/2),
    # Q=2^(ell-2) U_(ell-2)(...), produce 2^ell U_ell(...).
    A=defaultdict(int)
    for k,c in P.items():
        for delta in (-2,-1,1,2):A[k+delta]+=c
    for k,c in Q.items():A[k]-=4*c
    return {k:c for k,c in A.items() if c}


def expected_rank(n,ell):
    return len({k%n for k in predicted_support(ell)})


def test():
    p0={0:1};p1={k:1 for k in (-2,-1,1,2)}
    comparisons=0
    for ell in range(0,61):
        if ell==0:p=p0
        elif ell==1:p=p1
        else:
            p=recurrence_step(p1,p0)
            p0,p1=p1,p
        jac=weight_support(ell)
        predicted=predicted_support(ell)
        assert set(p)==jac==predicted,(ell,set(p)^predicted,jac^predicted)
        assert all(c>0 for c in p.values()),ell
        for n in range(2,65):
            # Fourier eigenvalues of the circulant addition kernel are
            # proportional to nonnegative sums of these coefficients.
            actual=sum(1 for r in range(n) if sum(c for k,c in p.items() if k%n==r)>0)
            assert actual==expected_rank(n,ell),(n,ell,actual)
            comparisons+=1
    assert expected_rank(6,3)==6 and expected_rank(6,4)==5 and expected_rank(6,5)==6
    assert expected_rank(12,3)==12 and expected_rank(12,4)==10 and expected_rank(12,5)==12
    print('PASS: 61 exact Laurent-Chebyshev/Jacobi support identities,')
    print(f'      {comparisons} circulant rank comparisons, and 6 nonmonotonic rank spot checks.')

if __name__=='__main__':test()
