#!/usr/bin/env python3
"""Reproduce finite majority and minimal-weight checks for the rank-homogeneous fibre family.

The infinite topological and measurability claims require the symbolic proof.
"""
from itertools import product


def eps(k): return k%2


def weights(K):
    a=[1,3]
    for k in range(1,K):
        a.append(1+sum(a[:k])+eps(k))
    return a[:K+1]


def test(K=14):
    a=weights(K+1)
    assert a[:9]==[1,3,3,5,9,13,23,35,59]
    assert all(a[j]%2==1 and a[j]<=a[j+1] for j in range(len(a)-1))
    for k in range(K):
        child=a[:k]+([1] if eps(k) else [])
        S=sum(child)
        assert S%2==0
        for ell in range(k+1,K+2):
            assert a[ell]>S
        if k>=1:
            assert a[k+1]==S+1
        if k>=1 and k+2<=K+1:
            assert a[k+2]==a[k+1]+a[k]+(-1)**k
        if k<=7:
            for bits in product((0,1),repeat=len(child)):
                same=sum(v for v,b in zip(child,bits) if b==0)
                opp=S-same
                assert a[k+1]+same>opp
                assert a[k+1]+opp>same
        for ell in range(k+1,K+2):
            degree=a[ell]+S
            assert degree%2==1 and degree>=3
        if k%2:
            assert a[k]>=3
    # Relative to the source's odd weights (3^(k+1)-(-1)^k)/2.
    for k,w in enumerate(a):
        old=(3**(k+1)-(-1)**k)//2
        assert old>=w
    print('VERIFY_OK: optimal odd rank weights; parent-majority for every k<ell;',
          'local color checks; min degree three; Fibonacci recurrence, k<=',K)
    print('rank weights k=0..14:', a[:15])

if __name__=='__main__': test()

# Additional finite checks for the normalized invariant counting probability:
# the full convergence/divergence statements are proved symbolically in RESULT.md.
if __name__ == '__main__':
    from fractions import Fraction
    z=Fraction(1,2)
    A=(1+3*z+z*z-2*z**3)/((1+z)*(1-z-z*z))
    assert A == Fraction(20,3)
    eta_mass=Fraction(1,2)*A+Fraction(1,3)
    assert eta_mass==Fraction(11,3)
    print('NORMALIZATION_OK: eta(Y)=11/3; invariant probability eta*(3/11).')
    W=weights(51)
    # Lower bounds on invariant edge-cost from configurations whose first two 1s are consecutive.
    cost_lb=[sum(Fraction(W[k]*W[k+1],2**(k+2)) for k in range(K)) for K in (10,20,30,40,50)]
    assert all(cost_lb[i] < cost_lb[i+1] for i in range(len(cost_lb)-1))
    print('COST_LOWER_BOUNDS:',[float(v) for v in cost_lb])
