#!/usr/bin/env python3
from fractions import Fraction
import random

def tau(a,b):
    return a*b/(a+b-a*b)

def rho(a,b):
    return 3*a*b/(2*a+2*b-a*b)

def xi(a,b):
    return 2*a*a*b/(3*a+b-2*a*b)

def beta_on_fiber(t,a):
    return t*a/(a*(1+t)-t)

def xmin(t):
    return 16*t*t/(t+3)**2

def xsup(t):
    return 2*t/(3-t)

def optimizer(t):
    return 4*t/(t+3), 4*t/(1+3*t)

def other_from_tail(t,l):
    return t*l/(l*(1+t)-t)

def run():
    rng=random.Random(20261002)
    formula_checks=0
    fiber_checks=0
    optimizer_checks=0
    direction_checks=0
    tail_checks=0

    vals=[Fraction(i,37) for i in range(1,37)]
    for _ in range(20000):
        a=rng.choice(vals); b=rng.choice(vals)
        t=tau(a,b)
        assert rho(a,b)==3*t/(2+t)
        d=xi(a,b)-xi(b,a)
        if a>b:
            assert d>0
        elif a<b:
            assert d<0
        else:
            assert d==0
        # exact factorization
        rhs=2*a*b*(a-b)*(a+b-2*a*b)/((3*a+b-2*a*b)*(a+3*b-2*a*b))
        assert d==rhs
        formula_checks+=1
        direction_checks+=2

    tvals=[Fraction(i,41) for i in range(1,41)]
    for t in tvals:
        ao,bo=optimizer(t)
        assert tau(ao,bo)==t
        assert xi(ao,bo)==xmin(t)
        optimizer_checks+=2

        # exact grid inside t<a<1
        for j in range(1,300):
            a=t+(1-t)*Fraction(j,300)
            b=beta_on_fiber(t,a)
            assert 0<a<1 and 0<b<1
            assert tau(a,b)==t
            x=xi(a,b)
            assert x>=xmin(t)
            assert x<xsup(t)
            fiber_checks+=4

        # tail coefficient and unordered reconstruction
        sym=2*t/(1+t)
        for j in range(1,100):
            l=t+(sym-t)*Fraction(j,100)
            q=other_from_tail(t,l)
            assert l<q<1
            assert tau(l,q)==t
            assert min(l,q)==l
            assert other_from_tail(t,l)==q
            tail_checks+=4
        assert other_from_tail(t,sym)==sym
        tail_checks+=1

    print(
        'VERIFY_OK '
        f'formula_checks={formula_checks} '
        f'fiber_checks={fiber_checks} '
        f'optimizer_checks={optimizer_checks} '
        f'direction_checks={direction_checks} '
        f'tail_checks={tail_checks}'
    )

if __name__=='__main__':
    run()
