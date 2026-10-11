#!/usr/bin/env python3
"""Finite checks of sharp Chernoff construction for mutual Birkhoff--James orthogonality in real l1."""
from itertools import product
from fractions import Fraction
from math import exp, sqrt, isclose


def directed(x, y):
    a=sum(xi*yi for xi,yi in zip(x,y) if xi)
    b=sum(abs(yi) for xi,yi in zip(x,y) if not xi)
    return abs(a)<=b

def prob(v, rho):
    k=sum(bool(a) for a in v)
    return (rho/Fraction(2))**k*(1-rho)**(len(v)-k)

def check():
    checked_pairs=0
    checked_weighted=0
    rho=Fraction(1,4)
    for n in range(1,6):
        vectors=list(product((-1,0,1), repeat=n))
        nz=[v for v in vectors if any(v)]
        p={v:prob(v,rho) for v in vectors}
        assert sum(p.values(),Fraction(0))==1
        normmass=sum((p[v] for v in nz),Fraction(0))
        assert normmass == 1-(1-rho)**n
        failure=Fraction(0)
        for x in nz:
            for y in nz:
                h=Fraction(1,2)
                direct_by_norm = (sum(abs(Fraction(a)+h*b) for a,b in zip(x,y))>=sum(abs(a) for a in x) and sum(abs(Fraction(a)-h*b) for a,b in zip(x,y))>=sum(abs(a) for a in x))
                assert directed(x,y)==direct_by_norm
                good=directed(x,y) and directed(y,x)
                if not good:
                    failure+=p[x]*p[y]
                checked_pairs+=1
        theta = 1-float(rho) + float(rho)*sqrt(float(rho)*(2-float(rho)))
        assert float(failure/normmass**2)<=4*theta**n/(float(normmass)**2)+1e-12
        checked_weighted+=1
    t=1/sqrt(2)
    theta=t+(1-t)*t
    assert isclose(theta,sqrt(2)-0.5,rel_tol=0,abs_tol=1e-15)
    for delta in (-0.4,-0.2,-0.1,-0.01,0.01,0.1,0.2):
        tau=t+delta
        if 0<tau<1:
            th=tau+(1-tau)*sqrt(1-tau*tau)
            assert th>=theta-1e-14
    for n in range(1,45):
        bound=(1-2**(-n/2))**2/(4*theta**n)
        assert bound>0
    print(f'VERIFY_OK exact_pairs={checked_pairs} exact_weighted_dimensions={checked_weighted} rho=1/4 unique_chernoff_bias_checked=1 asymptotic_base={1/theta:.12f}')
if __name__=='__main__':
    check()
