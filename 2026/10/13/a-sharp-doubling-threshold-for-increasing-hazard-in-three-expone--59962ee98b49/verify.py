#!/usr/bin/env python3
"""Self-contained exact-arithmetic checks for the three-exponential hazard theorem.

Use: python3 verify.py
Analytic inequalities and asymptotic statements are proved in RESULT.md;
these finite checks do not replace those proofs.
"""
from fractions import Fraction as Q
from math import log, exp, isfinite


def polynomial_curvature(x,y,r):
    """D=(S')**2-S*S'', with y=x**r and derivatives in s (normalized time)."""
    S=2*x-x*x+y*(1-x)**2
    # S = 2 e^-s - e^-2s + e^-rs -2e^-(r+1)s +e^-(r+2)s
    Sp=-2*x+2*x*x-r*y+2*(r+1)*x*y-(r+2)*x*x*y
    Spp=2*x-4*x*x+r*r*y-2*(r+1)**2*x*y+(r+2)**2*x*x*y
    return Sp*Sp-S*Spp,S

def factor_curvature(x,y,r):
    B= -r*r*(2-x)*(1-x)**2 +4*r*(1-x)-2*(2*x*x-2*x+1)
    return x*(2*x*x+y*B+2*y*y*(1-x)**2)


def run():
    n=0
    for ix in range(1,20):
        x=Q(ix,20)
        for iy in range(1,12):
            y=Q(iy,13)
            for ir in range(1,17):
                r=Q(ir,7)
                D,S=polynomial_curvature(x,y,r)
                assert S>0
                assert D==factor_curvature(x,y,r)
                n+=1
    # Verify the same derivative identity on actual exponential-power curves,
    # and the exact signs for each integer r >=2.
    m=0
    for den in (3,5,7,13,23,101):
        for num in range(1,den):
            x=Q(num,den)
            for r in range(2,17):
                D,S=polynomial_curvature(x,x**r,Q(r))
                assert D==factor_curvature(x,x**r,Q(r)) and D>0
                m+=1
            D,_=polynomial_curvature(x,x,Q(1))
            assert D>0
    x=Q(1,10000)
    y=Q(1,1000000) # x^(3/2), exact
    D,_=polynomial_curvature(x,y,Q(3,2))
    assert D<0
    y=Q(1,100) # x^(1/2), exact
    D,_=polynomial_curvature(x,y,Q(1,2))
    assert D<0
    # Exact polynomial coefficients in the sufficiency argument:
    # 2+B(2)=4*x*(4-x)*(1-x)
    # B(2+u)=B(2)+u*(-4*(1-x)*(x*x-3*x+1))
    #                 -u*u*(2-x)*(1-x)**2
    for ix in range(1,40):
        x=Q(ix,40)
        b=lambda r:-r*r*(2-x)*(1-x)**2+4*r*(1-x)-2*(2*x*x-2*x+1)
        assert 2+b(Q(2))==4*x*(4-x)*(1-x)
        b1=-4*(1-x)*(x*x-3*x+1)
        for u in [Q(0),Q(1,100),Q(1,3),Q(1),Q(3),Q(20)]:
            assert b(Q(2)+u)==b(Q(2))+b1*u-u*u*(2-x)*(1-x)**2
    # Numerical stress tests at noninteger ratios; these are diagnostics only.
    numerics=0
    for r in (0.2,0.5,0.95,0.999,1.001,1.01,1.1,1.5,1.95,1.99,1.999,2.,2.0001,2.01,2.2,3.01,7.5,75.):
        for t in (.0001,.01,.1,.4,1.,2.,4.,7.,10.,15.,20.):
            x=exp(-t)
            y=exp(-r*t)
            D,S=polynomial_curvature(x,y,r)
            assert isfinite(D) and S>0
            if r>=2 or r==1:
                assert D> -1e-14*S*S, (r,t,D,S)
            numerics+=1
    print(f'PASS: {n} exact independent-power curvature identities; {m} exact integer-rate IFR signs;')
    print(f'PASS: rational 1/2 and 3/2 tail counterexamples, exact coefficient expansions, {numerics} floating diagnostics.')
    print('LIMIT: numerical grids are not proofs of a universal statement.')

if __name__=='__main__':
    run()
