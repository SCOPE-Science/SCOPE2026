#!/usr/bin/env python3
"""Independent arithmetic checks for the single-incumbent cultural-copying model.

Python standard library only. Executed with: python verify.py
Finite-horizon tests corroborate, but do not prove, the analytic infinite-horizon theorem.
"""
from fractions import Fraction
from math import exp, log, isclose


def thresholds(a):
    kappa = a / (a - 1)
    return ((a*a - 1)/(2*a*a),
            1/(kappa + exp(-log(a)/(a - 1))),
            1 - 1/a)


def limiting(a, e):
    critical = 1 - 1/a
    incumbent = max(0., 1 - a*e/(a - 1))
    ratio = 1/a if e < critical else 1 - e
    return incumbent, ratio


def moments(a, e):
    incumbent, ratio = limiting(a, e)
    shannon = 0. if incumbent == 0 else -incumbent * log(incumbent)
    shannon += -e * log(e)/(1-ratio) - e*ratio*log(ratio)/(1-ratio)**2
    concentration = incumbent*incumbent + e*e/(1-ratio*ratio)
    return shannon, concentration


def finite(a, e, rounds):
    state = [1.]
    for _ in range(rounds):
        total = 1 + (a-1)*state[0]
        state = [(1-e)*a*state[0]/total] + [(1-e)*z/total for z in state[1:]] + [e]
        assert abs(sum(state) - 1) < 2e-12
    return state


def finite_moments(state):
    return -sum(z*log(z) for z in state if z > 0), sum(z*z for z in state)


def run():
    tests = 0
    for a in [1.01, 1.1, 1.5, 2., 3., 10., 100.]:
        e2,e1,ec = thresholds(a)
        assert 0 < e2 < e1 < ec < 1
        tests += 1
        for q in [0.4,0.8,1.,1.2,1.8]:
            e = min(.999, q * ec)
            h,c = moments(a,e)
            assert h >= 0 and 0<c<=1
            tests += 1
            if a <= 10:
                st = finite(a,e,2500 if a < 1.1 else (1200 if a < 2 else 600))
                hf,cf=finite_moments(st)
                # At e=ec the convergence is algebraic rather than geometric.
                tol=.2 if abs(e-ec)<1e-12 else (.04 if a<1.1 else .002)
                assert abs(hf-h)<tol, (a,e,hf,h)
                assert abs(cf-c)<tol, (a,e,cf,c)
                tests+=2
        h1,c1=moments(a,e1)
        h2,c2=moments(a,e2)
        k=a/(a-1)
        assert isclose(exp(h1), 1 + k*exp(log(a)/(a-1)),rel_tol=1e-10)
        assert isclose(1/c2,2*a/(a-1),rel_tol=1e-10)
        assert exp(h1)>exp(h2) and c2 < c1
        tests+=3
    a=Fraction(2,1)
    e2=Fraction(3,8);e1=Fraction(2,5);ec=Fraction(1,2)
    assert Fraction(a*a-1,2*a*a)==e2
    assert Fraction(1,1)-a*e2/(a-1)==Fraction(1,4)
    assert Fraction(1,1)-a*e1/(a-1)==Fraction(1,5)
    assert Fraction(1,4)**2 + e2*e2/(1-Fraction(1,4)) == Fraction(1,4)
    assert e1<ec
    tests+=5
    print(f'PASS: {tests} formula, finite-dynamic and exact-rational assertions.')
    print('For fitness 2: Simpson optimum 3/8, Shannon optimum 2/5, invasion threshold 1/2.')


if __name__=='__main__':
    run()
