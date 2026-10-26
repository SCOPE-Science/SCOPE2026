#!/usr/bin/env python3
"""Exact rational checks of the binary step-reinforced mixing profile.

This is finite arithmetic verification of the stated coefficients, not a
replacement for the increasing-tree species proof of the infinite formula.
"""
from collections import defaultdict
from fractions import Fraction as Q
from math import comb

def poly_mul(a, b, degree):
    out = [Q(0)]*(degree+1)
    for i, x in enumerate(a[:degree+1]):
        for j, y in enumerate(b[:degree+1-i]):
            out[i+j] += x*y
    return out

def binom_general(s, k):
    ans = Q(1)
    for j in range(k):
        ans *= (s-j)/Q(j+1)
    return ans

def lagrange_bias(alpha, m):
    """[v^(m-1)] alpha^-1 (1-v)^-1 Phi(v)^(-2m)."""
    degree = m-1
    exponent = (Q(1)/alpha-Q(1))/2
    phi = [binom_general(exponent,j)*(-1)**j/(alpha*(2*j+1)) for j in range(degree+1)]
    f0 = phi[0]
    h = [Q(0)] + [phi[i]/f0 for i in range(1,degree+1)]
    powers = [Q(1)] + [Q(0)]*degree
    phipower = [Q(0)]*(degree+1)
    for k in range(degree+1):
        coeff=binom_general(Q(-2*m),k)
        for j in range(degree+1):
            phipower[j]+=coeff*powers[j]
        powers=poly_mul(powers,h,degree)
    return sum(phipower)*f0**(-2*m)/alpha

def binary_forest_bias(n, alpha):
    # Independent exact recursion for the component size process.
    states = {(1,): Q(1)}
    for k in range(1,n):
        nxt=defaultdict(Q)
        for sizes, prob in states.items():
            nxt[sizes+(1,)]+=prob*(1-alpha)
            for i, size in enumerate(sizes):
                enlarged=list(sizes)
                enlarged[i]+=1
                nxt[tuple(enlarged)]+=prob*alpha*Q(size,k)
        states=nxt
        assert sum(states.values(),Q(0))==1
    return sum((prob for sizes,prob in states.items() if all(x%2==0 for x in sizes)), Q(0))

def direct_history_bias(n,alpha):
    histories={(0,):Q(1,2),(1,):Q(1,2)}
    for k in range(1,n):
        new=defaultdict(Q)
        for history, weight in histories.items():
            ones=sum(history)
            for bit, count in ((0,k-ones),(1,ones)):
                new[history+(bit,)]+=weight*((1-alpha)/2+alpha*Q(count,k))
        histories=new
    assert sum(histories.values(),Q(0))==1
    return sum((weight*(-1)**sum(history) for history,weight in histories.items()),Q(0))

def one_third_closed(m):
    return Q(3,3**(2*m))*sum((Q(comb(2*m+j-1,j),3**j) for j in range(m)), Q(0))

def main():
    checks=0
    for alpha in (Q(1,4), Q(1,3), Q(1,2), Q(2,3), Q(3,4)):
        for n in range(1,13):
            forest=binary_forest_bias(n,alpha)
            lagrange=Q(0) if n%2 else lagrange_bias(alpha,n//2)
            assert forest==lagrange,(alpha,n,forest,lagrange)
            if n%2==0:
                assert lagrange>0
            else:
                assert lagrange==0
            if alpha==Q(1,3) and n%2==0:
                assert forest==one_third_closed(n//2)
            checks+=1
    direct_checks=0
    for alpha in (Q(1,3),Q(1,2),Q(2,3)):
        for n in range(1,11):
            assert direct_history_bias(n,alpha)==binary_forest_bias(n,alpha)
            direct_checks+=1
    assert binary_forest_bias(2,Q(1,3))==Q(1,3)
    assert binary_forest_bias(4,Q(1,3))==Q(7,81)
    assert binary_forest_bias(6,Q(1,3))==Q(16,729)
    print('VERIFY_OK coefficient_cases=%d direct_history_cases=%d closed_one_third_cases=6 odd_uniform=PASS even_nonuniform=PASS'%(checks,direct_checks))

if __name__=='__main__':
    main()
