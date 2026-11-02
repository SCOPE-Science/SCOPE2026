#!/usr/bin/env python3
"""Exact rational tests of the preimage identity for the stationary cusp model.
No simulated densities or infinite-limit claims are certified by these finite checks.
"""
from fractions import Fraction as Q
from itertools import product

def primitive(k, x):
    if k == 0:  # uniform
        return x
    if k == 1:  # 2x
        return x*x
    if k == 2:  # 6x(1-x)
        return 3*x*x-2*x*x*x
    raise ValueError

def mass(k, lo, hi):
    return primitive(k, hi)-primitive(k,lo)

def preimage_mass(k, ell, q, t):
    # Target (1/2 - 2^(-t-1),1/2); t is an integer divisible by ell.
    eps=Q(1,2**(t+1)); half=Q(1,2)
    left_good=mass(k,Q(1,4)-eps/2,Q(1,4))
    right_both=mass(k,Q(3,4)-eps/2,Q(3,4))
    left_bad=mass(k,half-Q(1,2**(t//ell+1)),half)
    return (1-q)*left_good+q*left_bad+right_both

def rhs_mass(k,ell,q,t):
    return q*mass(k,Q(1,2)-Q(1,2**(t//ell+1)),Q(1,2))+(1-q)*mass(k,Q(1,4)-Q(1,2**(t+2)),Q(1,4))+mass(k,Q(3,4)-Q(1,2**(t+2)),Q(3,4))

def main():
    count=0
    for ell,q,k,j in product((2,3,4),(Q(1,12),Q(1,16),Q(1,20)),(0,1,2),range(1,9)):
        t=ell*j
        a=preimage_mass(k,ell,q,t)
        b=rhs_mass(k,ell,q,t)
        assert a==b,(ell,q,k,t,a,b)
        count+=1
    # Abstract telescope of the discrete renormalization. Choose artificial
    # base m(t)=2^(-t-1) and force j(t)=m(t)-q*m(t/ell).
    count2=0
    for ell,q,t0,N in product((2,3),(Q(1,5),Q(1,7)),(1,2),(1,2,3)):
        def m(t):return Q(1,2**(t+1))
        def j(t):return m(t)-q*m(t//ell)
        t=ell*t0
        # F_N(t)=m(t)+sum_{k=1}^N q^(-k) j(ell^k*t).
        # Check its exact scaling defect is q^(-N) j(ell^(N+1)t).
        def F(T):return m(T)+sum(q**(-k)*j((ell**k)*T) for k in range(1,N+1))
        assert F(ell*t)-q*F(t)==q**(-N)*j((ell**(N+1))*t)
        count2+=1
    print(f'PASS: {count} exact-rational branch-preimage equalities; {count2} telescoping equalities.')
    print('Analytic renewal and asymptotic arguments require the separately stated proof.')

if __name__=='__main__':main()
