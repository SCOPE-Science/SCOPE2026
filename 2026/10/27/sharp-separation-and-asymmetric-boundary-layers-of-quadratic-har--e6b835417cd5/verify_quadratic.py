#!/usr/bin/env python3
"""Reproducibility checks for an exact quadratic harmonic-Bergman spectrum theorem.

Uses Python standard library only. Finite checks complement the proof, and do
not establish the infinite-dimensional absence of other eigenvalues.
"""
from fractions import Fraction as Q
from math import cos, sin, pi, isclose, log, log1p


def coeff(u, n):
    a, b = u
    alpha, beta = -Q(3)*a/7, -Q(4)*a/7
    return beta**(-n) if n>=1 else (1-n)*alpha**(-n)


def toeplitz_monomial_coeff(u, degree, n):
    j = n-degree
    a, b = u
    raw = coeff(u, j)
    if j >= 0:
        weight = Q(1)
    elif n <= 0:
        weight = Q(1-n, 1-j)
    else:
        weight = Q(n+1, degree+1)
    return raw*weight


def projection_polynomial_coeff(k, ell):
    """Coefficient of z^(k-ell) in P(z^k conjugate(z)^ell)."""
    return Q(k-ell+1, k+1) if 0<=ell<=k else Q(0)


def test_projection_identity():
    # For monic quadratic: P[(q(z)-q(w))/(1-w conjugate(z))^2]
    # equals z(z+a+4w/3). Match every coefficient over Q.
    checks=0
    for a in (Q(-5,3),Q(0),Q(2),Q(11,7)):
        for w in (Q(-7,11),Q(0),Q(3,5)):
            # k=1 contributes a*z, k=2 contributes z^2+(4w/3)*z.
            k1 = Q(0)
            for ell in range(1):
                k1 += (ell+1)*w**ell*projection_polynomial_coeff(1,ell)
            k2 = [(ell+1)*w**ell*projection_polynomial_coeff(2,ell)
                  for ell in range(2)]
            assert k1==1 and k2[0]==1 and k2[1]==Q(4,3)*w
            assert a*k1+k2[1] == a+Q(4,3)*w
            checks+=1
    return checks


def test_exact_eigenvector():
    checks=0
    for a in (Q(9,5),Q(2),Q(-2),Q(11,5)):
        for b in (Q(0),Q(3,5),Q(-7,4)):
            uv=(a,b)
            alpha,beta=-Q(3)*a/7,-Q(4)*a/7
            assert abs(alpha)<1<abs(beta)
            eigenvalue=b-Q(12)*a*a/49
            # q(z)-lambda=(z-alpha)(z-beta): both coefficients exact.
            assert alpha+beta == -a
            assert alpha*beta == b-eigenvalue
            assert a+Q(7,3)*alpha == 0
            for n in range(-60,61):
                lhs=toeplitz_monomial_coeff(uv,2,n)+a*toeplitz_monomial_coeff(uv,1,n)+b*coeff(uv,n)
                rhs=eigenvalue*coeff(uv,n)
                assert lhs==rhs, (a,b,n,lhs,rhs)
                checks+=1
    return checks


def test_gap():
    checks=0
    for num in range(176,233):
        t=Q(num,100)
        alpha=-Q(3)*t/7
        beta=-Q(4)*t/7
        d=(1-abs(alpha))*(abs(beta)-1)
        assert d==t-1-Q(12)*t*t/49
        assert d>0
        assert Q(1,48)-d == Q(12,49)*(t-Q(49,24))**2
        checks+=1
    for t in [Q(7,4),Q(7,3)]:
        assert t-1-Q(12)*t*t/49==0
        checks+=1
    return checks


def test_numerical_phase_and_distance():
    checks=0
    from cmath import exp
    for t in (1.76, 1.83, 2.0, 49/24, 2.21, 2.32):
        for phase in (0.0,0.4,1.3):
            a=t*exp(1j*phase)
            alpha=-3*a/7
            beta=-4*a/7
            eig=-12*a*a/49
            assert abs(alpha)<1<abs(beta)
            distance=(1-abs(alpha))*(abs(beta)-1)
            candidate=abs((-a/abs(a))**2+a*(-a/abs(a))-eig)
            assert abs(candidate-distance)<2e-12
            closest=min(abs(z*z+a*z-eig)
                        for z in (exp(2j*pi*k/4096) for k in range(4096)))
            assert closest+1e-12>=distance
            assert closest-distance<0.00002
            checks+=1
    return checks


def test_boundary_layer_norms():
    checks = 0
    lower = 7/4
    upper = 7/3
    constant = 256/49 - 1 - log(8/7)
    for delta in (1e-3, 1e-5, 1e-7, 1e-9):
        t = lower+delta
        av = (3*t/7)**2
        bv = (7/(4*t))**2
        norm2 = (1-av)**(-2)+(-log1p(-bv)-bv)/bv
        assert abs(norm2-log(1/delta)-constant)<0.08
        checks += 1
    for delta in (1e-3, 1e-5, 1e-7):
        t=upper-delta
        av=(3*t/7)**2
        bv=(7/(4*t))**2
        norm2=(1-av)**(-2)+(-log1p(-bv)-bv)/bv
        assert abs(norm2*delta*delta-Q(49,36))<0.002
        checks += 1
    return checks


def main():
    counts={
        'Bergman projection polynomial identity':test_projection_identity(),
        'exact rational eigenvector mode identities':test_exact_eigenvector(),
        'exact sharp spectral-gap quadratic identities':test_gap(),
        'complex phase and boundary-distance checks':test_numerical_phase_and_distance(),
        'distinct logarithmic and quadratic eigenfunction norm blowups':test_boundary_layer_norms(),
    }
    for name,count in counts.items():
        print(f'PASS {name}: {count}')
    print('PASS ALL CHECKS',sum(counts.values()))


if __name__=='__main__':
    main()
