#!/usr/bin/env python3
"""Reproduce matrix identities and sample stability thresholds for a two-group SIS linearization.

Uses only the Python standard library. The analytic proof, rather than sampled tests,
establishes the statements for all admissible real parameters.
"""
import math
import random


def growth(p, q, mu, tau):
    a = math.sqrt(p*q)
    kappa = (p+q)/(2*a)
    return -mu + math.asinh(kappa*math.sinh(a*tau))/tau


def matrix_exp_core(p, q, tau):
    a = math.sqrt(p*q)
    c = math.cosh(a*tau)
    s = math.sinh(a*tau)/a
    return ((c, p*s), (q*s, c))


def mul(U, V):
    return tuple(tuple(U[i][0]*V[0][j] + U[i][1]*V[1][j]
                       for j in range(2)) for i in range(2))


def close(x, y, tol=2e-10):
    return abs(x-y) <= tol*max(1.0, abs(x), abs(y))


def bisect_threshold(p, q, mu):
    a = math.sqrt(p*q)
    mid = (p+q)/2
    assert p != q and a < mu < mid
    def f(t):
        return growth(p,q,mu,t)
    lo, hi = 1e-5, 1.0
    assert f(lo) > 0
    while f(hi)>0:
        hi *= 2
        assert hi<300
    for _ in range(110):
        midt=(lo+hi)/2
        if f(midt)>0:lo=midt
        else: hi=midt
    return (lo+hi)/2


def main():
    rng=random.Random(480016)
    matrix_tests=0
    for _ in range(1300):
        p=math.exp(rng.uniform(-1.5,1.5))
        q=math.exp(rng.uniform(-1.5,1.5))
        mu=rng.uniform(0.1,3)
        tau=rng.uniform(.002,1.0)
        a=math.sqrt(p*q)
        k=(p+q)/(2*a)
        E1=matrix_exp_core(p,q,tau)
        E2=matrix_exp_core(q,p,tau)
        product=mul(E2,E1)
        tr=product[0][0]+product[1][1]
        det=product[0][0]*product[1][1]-product[0][1]*product[1][0]
        assert close(tr,2+4*k*k*math.sinh(a*tau)**2)
        assert close(det,1,1e-8)
        # Largest eigenvalue of the unattenuated 2x2 monodromy product.
        lambda_plus=(tr+math.sqrt(max(0,tr*tr-4*det)))/2
        direct=math.exp(-2*mu*tau)*lambda_plus
        from_formula=math.exp(2*tau*growth(p,q,mu,tau))
        assert close(direct,from_formula,1e-9)
        matrix_tests+=1
    monotone_tests=0
    for _ in range(260):
        p=rng.uniform(2.8,6.3)
        q=rng.uniform(.2,1.0)
        a=math.sqrt(p*q)
        mu=(a+(p+q)/2)/2
        times=[0.01, 0.05, 0.1, 0.2, .4, .8, 1.5, 3]
        values=[growth(p,q,mu,t) for t in times]
        assert all(x>y for x,y in zip(values,values[1:])), (p,q,values)
        root=bisect_threshold(p,q,mu)
        assert growth(p,q,mu,max(.0001, root*.9))>0
        assert growth(p,q,mu,root*1.1)<0
        monotone_tests+=1
    p,q,mu=4.0,1.0,2.25
    root=bisect_threshold(p,q,mu)
    assert abs(root-0.84415264994258796)<3e-12
    assert close(math.exp(2*.2*growth(p,q,mu,.2)),1.0902442189024493,1e-12)
    assert close(math.exp(2*growth(p,q,mu,1)),0.9353925203135692,1e-12)
    k=(p+q)/(2*math.sqrt(p*q))
    a=math.sqrt(p*q)
    for eps in [0.01,0.001,0.0001]:
        # Upper boundary: mu tends to (p+q)/2 from below.
        mup=(p+q)/2-eps
        t=bisect_threshold(p,q,mup)
        approximate=math.sqrt(6*eps/(k*(k*k-1)*a**3))
        assert abs(t/approximate-1) < 2*math.sqrt(eps)
    for eps in [0.03,0.015,0.0075]:
        # Lower boundary: mu approaches sqrt(pq) from above.
        mup=a+eps
        t=bisect_threshold(p,q,mup)
        approximate=math.log(k)/eps
        assert abs(t/approximate-1) < .015
    print('VERIFICATION_OK matrix_tests=%d monotonic_cases=%d' % (matrix_tests,monotone_tests))
    print('example_critical_half_period=%.16f'%root)
    print('example_rho_tau_0.2=%.16f'%math.exp(2*.2*growth(p,q,mu,.2)))
    print('example_rho_tau_1.0=%.16f'%math.exp(2*growth(p,q,mu,1)))


if __name__=='__main__':
    main()
