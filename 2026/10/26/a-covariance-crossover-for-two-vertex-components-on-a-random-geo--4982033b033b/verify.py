#!/usr/bin/env python3
"""Reproduce finite Dirichlet-spacing covariance checks and sparse-limit diagnostics."""
from fractions import Fraction
from itertools import product
from math import comb, exp, log


def p(n, r, k):
    return max(Fraction(0), Fraction(1)-k*r)**(n-1)


def formula(n, r):
    v = [p(n, r, k) for k in range(n+1)]
    q = sum((-1)**k * comb(n, k) * v[k] for k in range(n+1))
    exact = n*(2*(v[2]-v[3])+(n-3)*(v[3]-v[4])
               -n*v[1]*(v[2]-v[3])-q*(v[2]-v[3]))
    return exact


def enumerate_gap_masks(n, r):
    # Inclusion-exclusion inversion: P(X_i=1 exactly for i in mask), X_i=1{gap_i>r}.
    ps = [p(n, r, k) for k in range(n+1)]
    ex = eb = ej = ebj = e_cj = Fraction(0)
    count = 0
    for bits in product((0, 1), repeat=n):
        b = sum(bits)
        # Uniform law: every designated set of b long gaps has the same probability.
        mass = sum((-1)**j*comb(n-b,j)*ps[b+j] for j in range(n-b+1))
        assert mass>=0, (n,r,b,mass)
        j = sum(bits[(i-1)%n]*(1-bits[i])*bits[(i+1)%n] for i in range(n))
        comp = max(1,b)
        ex += mass
        eb += b*mass
        ej += j*mass
        ebj += b*j*mass
        e_cj += comp*j*mass
        count += 1
    assert ex == 1
    cov = e_cj-(eb+ps[0]*0+sum((-1)**k*comb(n,k)*ps[k] for k in range(n+1)))*ej
    assert cov==formula(n,r), (n,r,cov,formula(n,r))
    return count


def limit(c):
    t = exp(-c)
    return t*t*(3*t-2)*((1+c*c)*t-1)


def fast_float(n,c):
    r = c/n
    pk = lambda k:max(0.,1-k*r)**(n-1)
    return 2*(pk(2)-pk(3))+(n-3)*(pk(3)-pk(4))-n*pk(1)*(pk(2)-pk(3))


def main():
    strata=0;mask_total=0
    for n in range(4,9):
        for r in (Fraction(1,12),Fraction(1,5),Fraction(1,3),Fraction(2,5)):
            mask_total += enumerate_gap_masks(n,r)
            strata+=1
    print('EXACT_MASK_INCLUSION_EXCLUSION_PASS',strata,'strata;',mask_total,'mask states')
    critical = log(Fraction(3,2))
    assert limit(0.2)<0 and limit(1)>0
    assert abs(limit(critical))<1e-15
    for c in (0.2,0.6,1.5,3.0):
        target=limit(c)
        errors = [abs(fast_float(n,c)-target) for n in (500,1000,2000)]
        assert errors[-1]<errors[0] and errors[-1]<0.015,(c,errors)
    print('ASYMPTOTIC_NUMERICAL_DIAGNOSTIC_PASS',4,'densities')
    print('VERIFY_OK')

if __name__=='__main__':main()
