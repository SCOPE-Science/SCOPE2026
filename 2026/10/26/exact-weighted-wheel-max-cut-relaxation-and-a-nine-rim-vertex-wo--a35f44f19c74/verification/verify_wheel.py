#!/usr/bin/env python3
"""Independent finite checks of analytic SDP/max-cut formulas for weighted wheels.
Requires Python 3.9+, numpy and sympy (sympy used only in exact tests).
Numerical checks are not a proof of the universal statement.
"""
import itertools
import math
import random
from fractions import Fraction

import numpy as np
import sympy as sp


def exact_formula(n,t):
    c=1.0 if n%2==0 else math.cos(math.pi/n)
    threshold=2*(1+c)
    sdp=n*t if t>=threshold else n/2*(1+t+c+t*t/(4*(1+c)))
    maxcut=n*t if t>=2 else (n if n%2==0 else n-1)+(n//2 if n%2==0 else (n+1)//2)*t
    a=-min(t/threshold,1.0)
    return sdp,maxcut,a,c,threshold


def wheel_cut_bruteforce(n,t):
    best=-1.0
    # hub sign set to +1 without loss of generality
    for spins in itertools.product([-1,1],repeat=n):
        rim=sum(spins[i]!=spins[(i+1)%n] for i in range(n))
        spokes=t*sum(x==-1 for x in spins)
        best=max(best,rim+spokes)
    return best


def construct_gram(n,t):
    sdp,mc,a,c,th=exact_formula(n,t)
    theta=math.pi if n%2==0 else math.pi-math.pi/n
    vectors=np.zeros((n+1,3))
    vectors[0,0]=1
    for i in range(n):
        vectors[i+1]=[a,math.sqrt(max(0,1-a*a))*math.cos(i*theta),math.sqrt(max(0,1-a*a))*math.sin(i*theta)]
    return vectors@vectors.T


def sdp_objective(x,t):
    n=x.shape[0]-1
    return sum((1-x[i+1,1+(i+1)%n])/2 for i in range(n))+t*sum((1-x[0,i+1])/2 for i in range(n))


def verify_exact_fractions():
    cases=[(3,Fraction(1,1),Fraction(1,2)),(3,Fraction(2,1),Fraction(1,2)),
           (4,Fraction(1,1),Fraction(1,1)),(4,Fraction(3,1),Fraction(1,1)),
           (6,Fraction(2,1),Fraction(1,1))]
    for n,t,c in cases:
        th=2*(1+c)
        a=-min(t/th,1)
        gram=sp.zeros(n+1)
        gram[0,0]=1
        for i in range(n):
            gram[0,i+1]=gram[i+1,0]=sp.Rational(a.numerator,a.denominator) if isinstance(a,Fraction) else sp.Rational(a)
            for j in range(n):
                if n==3:
                    f=sp.Integer(1) if i==j else sp.Rational(-1,2)
                else:
                    f=sp.Integer(-1 if (i-j)%2 else 1)
                gram[i+1,j+1]=a*a+(1-a*a)*f
        X=sp.Matrix(gram)
        # Exact Gram matrix positivity from exact eigenvalues
        ev=X.eigenvals()
        assert all(v>=0 for v in ev), (n,t,ev)
        objective=sum((1-X[i+1,1+(i+1)%n])/2 for i in range(n))+t*sum((1-X[0,i+1])/2 for i in range(n))
        expected=sp.Rational(n)*t if t>=th else sp.Rational(n,2)*(1+t+c+t*t/(4*(1+c)))
        assert sp.simplify(objective-expected)==0, (n,t,objective,expected)
    return len(cases)


def run():
    random.seed(417203)
    cuts=0; spec=0; random_gram_checks=0
    tvalues=[0,0.01,0.2,0.5,1,1.2,1.7,2,2.3,2.9,3.0,3.3,3.95,4.0,4.3,8]
    for n in range(3,12):
        for t in tvalues:
            sdp,mc,a,c,threshold=exact_formula(n,t)
            actual=wheel_cut_bruteforce(n,t)
            assert abs(mc-actual)<1e-9,(n,t,mc,actual)
            cuts+=1
            X=construct_gram(n,t)
            assert np.max(abs(np.diag(X)-1))<3e-13
            assert np.linalg.eigvalsh(X)[0]>-2e-12
            assert abs(sdp_objective(X,t)-sdp)<2e-11,(n,t,sdp,sdp_objective(X,t))
            spec+=1
            for j in range(45):
                d=3+(j%6)
                V=np.array([[random.gauss(0,1) for _ in range(d)] for _ in range(n+1)])
                V/=np.linalg.norm(V,axis=1)[:,None]
                obj=sdp_objective(V@V.T,t)
                assert obj < sdp+2e-9,(n,t,obj,sdp)
                random_gram_checks+=1
    # Exactness patterns and sharp max-ratio location; sample n up to 80.
    for n in range(3,81):
        sdp0,mc0,*_=exact_formula(n,0)
        sdp2,mc2,*_=exact_formula(n,2)
        r0=sdp0/mc0; r2=sdp2/mc2
        expect=(n%2==1 and n<=7)
        assert (r0>r2)==expect,(n,r0,r2)
        for t in (0,0.17,0.75,1,1.25,1.85,2,2.1,2.5,3,3.5,3.75,4,4.5,7):
            sdp,mc,*_=exact_formula(n,t)
            assert sdp/mc <= max(r0,r2)+2e-12,(n,t,sdp/mc,r0,r2)
    rational=verify_exact_fractions()
    print('PASS',cuts,'exact brute-force Max-Cut values',spec,'PSD Gram eigenvalue/SDP equalities',
          random_gram_checks,'independent random feasible Gram upper comparisons',rational,
          'exact-rational PSD/objective checks; ratio phase checked n=3..80.')
    for n in (3,4,5,6,7,8,9,10,11):
        v0=exact_formula(n,0);v2=exact_formula(n,2)
        print('n=',n,'SDP/CUT at t=0',round(v0[0]/v0[1],10),
              'at t=2',round(v2[0]/v2[1],10), 'exactness_t=',round(v2[4],10))

if __name__=='__main__':
    run()
