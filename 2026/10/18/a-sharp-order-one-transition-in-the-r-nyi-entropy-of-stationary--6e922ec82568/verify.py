#!/usr/bin/env python3
"""Independent finite calculations for a lazy-refresh Markov/Renyi theorem.

Requires only Python's standard library; contains finite numerical checks, not
an exhaustive or infinite proof.  The analytic proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import log, exp, sqrt, isclose
import random


def mm(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def power(A, t):
    n = len(A)
    B = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    for _ in range(t):
        B = mm(B, A)
    return B


def joint(pi, v):
    return [[pi[i] * pi[j] * (1-v) + (pi[i] * v if i == j else 0)
             for j in range(len(pi))] for i in range(len(pi))]


def renyi(a, masses):
    if a == 1:
        return -sum(float(q)*log(float(q)) for q in masses if q > 0)
    return log(sum(float(q)**a for q in masses if q > 0)) / (1-a)


def flat(M):
    return [q for row in M for q in row]


def B(a, pi):
    return sum(float(q)**(2*a-1) for q in pi) - sum(float(q)**a for q in pi)**2


def stationary_variance_log(pi):
    mu = sum(float(q)*log(float(q)) for q in pi)
    return sum(float(q)*(log(float(q))-mu)**2 for q in pi)


def derivative_sum(a, pi, v):
    pi = [float(q) for q in pi]
    n = len(pi)
    return a * sum((pi[i]*(int(i == j)-pi[j])) *
                (pi[i]*pi[j]*(1-v) + (pi[i]*v if i == j else 0))**(a-1)
                for i in range(n) for j in range(n))


def maximum_v(a, pi):
    assert 0 < a < 1
    assert B(a, pi) > 0
    lo, hi = 0.0, 1.0 - 1e-13
    for _ in range(100):
        mid = (lo+hi)/2
        if derivative_sum(a, pi, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def check():
    tests = 0
    rng = random.Random(20261013)
    for n in range(2,6):
        for _ in range(10):
            ints = [rng.randint(1,12) for _ in range(n)]
            pi = [F(x,sum(ints)) for x in ints]
            r = F(rng.randint(1,9),10)
            P = [[r*(i==j) + (1-r)*pi[j] for j in range(n)] for i in range(n)]
            for t in range(7):
                P_t = power(P,t)
                Q = [[pi[i]*P_t[i][j] for j in range(n)] for i in range(n)]
                expect = joint(pi, r**t)
                assert Q == expect
                tests += 1
            for a in (0.5,0.75,1.0,1.3,2.0,3.0):
                R = [renyi(a,flat(joint(pi,r**t))) for t in range(19)]
                if a >= 1 or len(set(pi))==1:
                    assert all(R[t+1] > R[t]-1e-12 for t in range(18))
                elif a < 1:
                    # The eventual overshoot need not occur by a prescribed lag.
                    assert B(a,pi) >= -1e-11
                tests += 1
            if len(set(pi)) > 1:
                for a in (0.3,0.5,0.8):
                    vstar = maximum_v(a, pi)
                    e = 2*renyi(a, pi)
                    fstar = renyi(a,flat(joint(pi,vstar)))
                    assert 0<vstar<1 and fstar>e
                    assert derivative_sum(a,pi,vstar-1e-6)>0
                    assert derivative_sum(a,pi,vstar+1e-6)<0
                    tests += 1
    pi=[F(9,10),F(1,10)]
    r=0.7
    vstar=maximum_v(.5,pi)
    jinf=exp(2*renyi(.5,pi))
    def J(t): return exp(renyi(.5,flat(joint(pi,r**t))))
    scores = [J(t) for t in range(1,21)]
    tstar = 1+max(range(20),key=lambda j:scores[j])
    print('two-state pi=(0.9,0.1), r=0.7:')
    print('continuous peak v*',vstar,'peak real t',log(vstar)/log(r))
    print('integer peak t',tstar,'J(t)',scores[tstar-1], 'J(independent)',jinf)
    assert tstar in (4,5,6)
    assert scores[tstar-1]>jinf
    # Check first-order lag asymptotic coefficients for several orders.
    for a in (.3,.5,.8,1.2,2.0):
        pi0=[.9,.1]
        A=sum(q**a for q in pi0)
        coef=a*B(a,pi0)/((1-a)*A*A)
        v=1e-5
        delta=renyi(a,flat(joint(pi0,v)))-2*renyi(a,pi0)
        assert isclose(delta/v,coef,rel_tol=0.003, abs_tol=1e-5), (a,delta/v,coef)
        tests += 1
    # Shannon & uniform expansions, require small enough perturbation.
    v=1e-4
    pi0=[.9,.1]
    dd=renyi(1,flat(joint(pi0,v)))-2*renyi(1,pi0)
    assert isclose(dd/(v*v),-.5,rel_tol=0.01)
    for n in (2,3,5):
        pi0=[1/n]*n
        for a in (.5,1.,2.):
            dd=renyi(a,flat(joint(pi0,v)))-2*renyi(a,pi0)
            assert isclose(dd/v**2,-a*(n-1)/2,rel_tol=0.02,abs_tol=.01), (n,a,dd)
            tests+=1
    # Near-Shannon location and height: avoid cancellation via small finite eps.
    pi0=[.9,.1]
    var=stationary_variance_log(pi0)
    for eta in (.05,.02,.01):
        a=1-eta
        vstar=maximum_v(a,pi0)
        asymv=eta*var
        height=renyi(a,flat(joint(pi0,vstar)))-2*renyi(a,pi0)
        asyh=eta*eta*var*var/2
        print('eta',eta,'vstar',vstar,'pred',asymv,
              'height',height,'pred',asyh)
        assert isclose(vstar/asymv,1,rel_tol=.3)
        assert isclose(height/asyh,1,rel_tol=.4)
        tests += 1
    print('PASS',tests,'finite tests; analytic hypotheses and infinite statements require proof')

if __name__=='__main__':check()
