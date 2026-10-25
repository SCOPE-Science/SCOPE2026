#!/usr/bin/env python3
"""Reproducible exact finite tests for balanced rank-two base-polytope inertia.

Uses no third-party packages. Tests do not replace the symbolic proof.
"""
from fractions import Fraction as F
from math import comb, factorial, sqrt
from random import Random


def beta_tail_half(a, b):
    # P(Beta(a,b)>1/2), for positive integers a,b.
    return F(sum(comb(a+b-1,j) for j in range(a)), 2**(a+b-1))


def spectra(r,m):
    assert r>=3 and m>=1
    n=r*m; k=(r-1)*m
    p=beta_tail_half(m,k)
    good=1-r*p
    assert good>0
    u0=F(m*(m+1),n*(n+1))
    u=u0*(1-beta_tail_half(m+2,k)-(r-1)*beta_tail_half(m,k+2))/good
    lam_in=4*u/F(m*(m+1))
    lam_out=F(4*r,(r-1)*m)*(u-F(1,r*r))
    B=F(factorial(m-1)*factorial(k-1),factorial(n-1))
    gap=F(r-2, 2**(n-1)*(r-1)*(m+1)*(k+1)) / (B*good)
    return lam_in,lam_out,gap,u


def integrate_three_parts(m, second=False):
    # Independent polynomial integration on simplex: t_i=1-S_i, sum_i t_i=1.
    # The group totals S_i=2 T_i, conditional density prod(1-t_i)^(m-1).
    total=F(0)
    for a in range(m):
        for b in range(m):
            for c in range(m):
                coef=(-1)**(a+b+c)*comb(m-1,a)*comb(m-1,b)*comb(m-1,c)
                # Integrate t1^a t2^b t3^c over the standard 2-simplex.
                baseline=F(factorial(a)*factorial(b)*factorial(c),factorial(a+b+c+2))
                if second:
                    i0=baseline
                    i1=F(factorial(a+1)*factorial(b)*factorial(c),factorial(a+b+c+3))
                    i2=F(factorial(a+2)*factorial(b)*factorial(c),factorial(a+b+c+4))
                    total+=coef*(i0-2*i1+i2)/4
                else:
                    total+=coef*baseline
    return total


def run():
    exact=0
    for r in range(3,9):
        for m in range(1,10):
            li,lo,gap,u=spectra(r,m)
            assert li>0 and lo>0 and gap==li-lo and gap>0
            if m>=2:
                assert 0<lo/li<1
            exact+=1
    direct=0
    for m in range(1,7):
        u_ind=integrate_three_parts(m,True)/integrate_three_parts(m)
        u_formula=spectra(3,m)[3]
        assert u_ind==u_formula,(m,u_ind,u_formula)
        direct+=1
    # Empirical test: Dirichlet(m,...,m) conditioned all T_i <= 1/2.
    rng=Random(20261019)
    mc=0
    for r,m in ((3,2),(3,4),(4,2),(5,2)):
        sums=0.0; sums2=0.0; count=0
        for i in range(65000):
            gs=[rng.gammavariate(m,1.) for _ in range(r)]
            s=sum(gs)
            if 2*max(gs)>s:continue
            x=gs[0]/s; sums+=x; sums2+=x*x; count+=1
        assert count>=10000, (r,m,count)
        estimate=sums2/count
        u=float(spectra(r,m)[3])
        assert abs(estimate-u)<0.003,(r,m,count,estimate,u)
        mc+=1
    # Check the exact asymptotic scale without rounding off tiny eigen-gaps.
    import math
    asym=0
    for r,m in ((3,50),(3,100),(4,40),(5,35)):
        li,lo,gap,u=spectra(r,m)
        rho=r**r/(2**r*(r-1)**(r-1))
        coeff=(r**1.5)*(r-2)/(2*math.sqrt(2*math.pi)*(r-1)**1.5)
        exactratio=float(gap/li)
        prediction=coeff*math.sqrt(m)*rho**m
        assert 0.80 < exactratio/prediction < 1.16,(r,m,exactratio/prediction)
        asym+=1
    print('VERIFY_OK exact_spectra=%d independent_polytope_integrals=%d seeded_mc=%d asymptotic_ratios=%d'%(exact,direct,mc,asym))

if __name__=='__main__':run()
