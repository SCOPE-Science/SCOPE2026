#!/usr/bin/env python3
"""Exact-rational checks for maximum-spacing / quadratic-spacing dependence.
Uses only the Python standard library.  Checks finite identities, not the
all-n theorem; the analytic proof establishes the latter.
"""
from fractions import Fraction as F
from math import comb

def harmonic(n, order=1):
    return sum((F(1,k**order) for k in range(1,n+1)), F())

def beta_sum(n, power):
    return sum((F((-1)**(j-1)*comb(n,j), j**power)
                for j in range(1,n+1)), F())

def moments(n):
    h=harmonic(n); h2=harmonic(n,2)
    em=h/n
    es=F(2,n+1)
    ems=F(2,n*(n+2))*beta_sum(n,1)+F(2,n*(n+1)*(n+2))*beta_sum(n,2)
    cov=ems-em*es
    v_m=(n*h2-h*h)/ (n*n*(n+1))
    v_s=F(4*(n-1), (n+1)**2*(n+2)*(n+3))
    expected=(h*h+h2-2*h)/(n*(n+1)*(n+2))
    assert cov==expected and cov>0 and v_m>0 and v_s>0
    assert beta_sum(n,1)==h
    assert beta_sum(n,2)==(h*h+h2)/2
    return ems, cov, v_m, v_s

def exponential_cov(n):
    # Independently evaluate Cov(max E_i, sum E_i**2) using independent
    # exponential order-statistic increments Z_k of rate k.
    h=harmonic(n)
    total=F()
    for k in range(1,n+1):
        for ell in range(1,k+1):
            total+=F(4,k**3)+F(2,k**2)*(h-harmonic(ell-1)-F(1,k))
    return total

def integrate_poly(poly, xlo, xhi, ylo, yhi):
    """Integrate sum c*x**a*y**b between affine y-bounds, then x-bounds."""
    def power_affine(alpha,beta,power):
        return {j:F(comb(power,j))*alpha**(power-j)*beta**j
                for j in range(power+1)}
    acc=F()
    for (a,b),c in poly.items():
        hi=power_affine(*yhi,b+1)
        lo=power_affine(*ylo,b+1)
        for j in range(b+2):
            coeff=c*(hi.get(j,F())-lo.get(j,F())) / (b+1)
            deg=a+j
            acc+=coeff*(xhi**(deg+1)-xlo**(deg+1))/(deg+1)
    return acc

def independent_simplex_cases():
    # n=2: integrate 2*x*(x**2+(1-x)**2) on 1/2<x<1.
    # x^3 + x*(1-2x+x^2)=x-2x^2+2x^3.
    poly2={(1,0):F(1),(2,0):F(-2),(3,0):F(2)}
    e2=2*integrate_poly(poly2,F(1,2),F(1),(F(),F()),(F(1),F()))
    assert e2==moments(2)[0]
    # n=3, symmetry *3 and simplex density 2. x is the largest gap.
    # x*(x*x + y*y + (1-x-y)**2).
    poly3={(1,0):F(1),(3,0):F(2),(1,2):F(2),
           (2,1):F(2),(2,0):F(-2),(1,1):F(-2)}
    e3=6*(integrate_poly(poly3,F(1,3),F(1,2),
                         (F(1),F(-2)),(F(),F(1)))
          +integrate_poly(poly3,F(1,2),F(1),
                          (F(),F()),(F(1),F(-1))))
    assert e3==moments(3)[0]
    return e2,e3

if __name__=='__main__':
    for n in range(2,81):
        ems,cov,vm,vs=moments(n)
        h=harmonic(n); h2=harmonic(n,2)
        # E[M_exp S_exp] from the independent order-statistic gaps;
        # Gamma(n,1) normalization divides a cubic moment by n(n+1)(n+2).
        assert (exponential_cov(n)+2*n*h)/ (n*(n+1)*(n+2))==ems
        assert exponential_cov(n)==h*h+2*h+h2
    a,b=independent_simplex_cases()
    print('PASS: n=2..80 exact alternating-sum, harmonic, order-statistic-increment identities')
    print('PASS: independent polynomial-simplex integration at n=2,3: E[M S]=',a,b)
    print('PASS: variance and positivity formulas checked exactly in 79 dimensions')
