#!/usr/bin/env python3
"""Reproduce finite algebraic and numerical checks for stochastic Bass campaign ordering.
Requires Python 3, sympy, numpy, scipy. The proof for all populations and durations
is analytic and does not rely on these finite checks.
"""
from fractions import Fraction
from math import exp, log
import random
import numpy as np
import sympy as sp
from scipy.linalg import expm


def generator(n, p, q, exact=False):
    if exact:
        Q = sp.zeros(n + 1)
        for k in range(n):
            lam = (n-k)*(p + q*sp.Rational(k,n-1))
            Q[k,k] = -lam
            Q[k,k+1] = lam
        return Q
    Q = np.zeros((n+1,n+1))
    for k in range(n):
        lam = (n-k)*(p+q*k/(n-1))
        Q[k,k] = -lam
        Q[k,k+1] = lam
    return Q


def exact_commutator_checks():
    assertions=0
    tests = [(sp.Rational(2,3),sp.Rational(4,5),sp.Rational(7,3),sp.Rational(2,7)),
             (sp.Rational(1,2),sp.Rational(0),sp.Rational(3,2),sp.Rational(2)),
             (sp.Rational(2),sp.Rational(1),sp.Rational(1),sp.Rational(2))]
    for n in range(2,11):
        for p,q,r,s in tests:
            A,B=generator(n,p,q,True),generator(n,r,s,True)
            C=A*B-B*A
            d=(p*s-r*q)/sp.Rational(n-1)
            for i in range(n+1):
                for j in range(n+1):
                    expected = (n-i)*(n-i-1)*d if j==i+2 else (-(n-i)*(n-i-1)*d if j==i+1 else 0)
                    assert C[i,j] == expected,(n,i,j,C[i,j],expected)
                    assertions+=1
    return assertions


def exact_two_person_example():
    # n=2, A=(2,1), B=(1,2), both durations log(2)
    P_A = sp.exp(generator(2,sp.Integer(2),sp.Integer(1),True)*sp.log(2))
    P_B = sp.exp(generator(2,sp.Integer(1),sp.Integer(2),True)*sp.log(2))
    row_AB = list((P_A*P_B)[0,:]); row_BA=list((P_B*P_A)[0,:])
    assert row_AB == [sp.Rational(1,64), sp.Rational(3,64), sp.Rational(60,64)],row_AB
    assert row_BA == [sp.Rational(1,64), sp.Rational(6,64), sp.Rational(57,64)],row_BA
    assert row_AB[2]-row_BA[2]==sp.Rational(3,64)
    return 7


def numerical_checks():
    rng = random.Random(459123)
    assertions=0
    for trial in range(700):
        n=rng.randint(2,9)
        m=rng.randint(2,7)
        phases=[]
        for j in range(m):
            p=rng.uniform(0.07,1.7)
            q=rng.uniform(0.07,1.8)
            d=rng.uniform(0.025,0.7)
            phases.append((p,q,d))
        mats=[expm(d*generator(n,p,q)) for p,q,d in phases]
        for M in mats:
            assert np.all(M>=-1.e-12)
            assert np.max(np.abs(M.sum(axis=1)-1)) < 1.e-11
            assertions+=2
        order=sorted(range(m), key=lambda j: phases[j][0]/phases[j][1],reverse=True)
        def terminal(ids):
            v=np.eye(n+1)[0]
            for j in ids: v=v@mats[j]
            return v
        sorted_out=terminal(order)
        random_order=list(range(m))
        rng.shuffle(random_order)
        other=terminal(random_order)
        for k in range(n+1):
            assert sum(sorted_out[k:])+3.e-11 >= sum(other[k:]), (n,trial,k,sorted_out,other)
            assertions+=1
        # Adjacent exchange for all initial counts and all monotone terminal rewards.
        a,b=rng.sample(range(m),2)
        pa,qa,da=phases[a]; pb,qb,db=phases[b]
        early,late=(a,b) if pa*qb>=pb*qa else (b,a)
        delta = mats[early]@mats[late] - mats[late]@mats[early]
        for initial in range(n+1):
            for threshold in range(n+1):
                assert sum(delta[initial,threshold:]) >= -3.e-11,(n,trial,initial,threshold)
                assertions+=1
        # Probability that there is no adoption is order-independent.
        assert abs(sorted_out[0]-exp(-n*sum(p*d for p,q,d in phases))) < 2.e-12
        assertions+=1
    return assertions


if __name__=='__main__':
    a=exact_commutator_checks()
    b=exact_two_person_example()
    c=numerical_checks()
    print('Exact commutator identities:',a)
    print('Exact n=2 example assertions:',b)
    print('Finite numerical comparisons:',c)
    print('TOTAL:',a+b+c,'PASS')
