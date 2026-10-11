#!/usr/bin/env python3
"""Independent finite moment-determinant checks for a half-interval polynomial projector."""
from fractions import Fraction as Q
from math import comb, factorial, gamma, lgamma, log, exp, pi


def det(a):
    a = [list(row) for row in a]
    n = len(a)
    if not n:
        return Q(1)
    sign = 1
    result = Q(1)
    for i in range(n):
        k = next((k for k in range(i, n) if a[k][i]), None)
        if k is None:
            return Q(0)
        if k != i:
            a[i], a[k] = a[k], a[i]
            sign = -sign
        p = a[i][i]
        result *= p
        for k in range(i+1, n):
            ratio = a[k][i]/p
            for j in range(i+1, n):
                a[k][j] -= ratio*a[i][j]
            a[k][i] = Q(0)
    return sign*result


def moment(alpha, beta, power):
    # Independent binomial integration of t^(power+alpha)*(1-t)^beta.
    assert isinstance(beta, int) and beta >= 0
    return sum((Q((-1)**k * comb(beta,k), 1) /
                (Q(power + k + 1) + alpha) for k in range(beta+1)), Q(0))


def hankel_direct(m, alpha, beta):
    return det([[moment(alpha,beta,i+j) for j in range(m)] for i in range(m)])


def pochhammer(x,n):
    result=Q(1)
    for k in range(n):
        result*=x+k
    return result


def hankel_gamma_exact_integer_beta(m, alpha, beta):
    # Jacobi monic-norm/Selberg product; all factors rational for integer beta.
    result=Q(1,factorial(m))
    for j in range(m):
        result*=Q(factorial(j+beta)*factorial(j+1))/pochhammer(alpha+j+1,beta+m)
    return result


def exact_q(m,beta,method):
    H=method
    return H(m,Q(0),beta)**2/(H(m,Q(-1,2),beta)*H(m,Q(1,2),beta))


def gamma_q(m,beta):
    # The proposed closed form, not a matrix calculation.
    s=0.0
    for j in range(m):
        s += 2*lgamma(j+1)-lgamma(j+0.5)-lgamma(j+1.5)
        s += lgamma(m+j+beta+0.5)+lgamma(m+j+beta+1.5)-2*lgamma(m+j+beta+1)
    return exp(s)


def run():
    checks=0
    for beta in range(4):
        for m in range(1,7):
            for alpha in (Q(-1,2),Q(0),Q(1,2)):
                direct=hankel_direct(m,alpha,beta)
                formula=hankel_gamma_exact_integer_beta(m,alpha,beta)
                assert direct == formula,(m,beta,alpha,direct,formula)
                checks+=1
            exact=exact_q(m,beta,hankel_direct)
            from_product=exact_q(m,beta,hankel_gamma_exact_integer_beta)
            assert exact==from_product and 0<exact<=1,(m,beta,exact,from_product)
            assert abs(float(exact)-gamma_q(m,beta))<2e-8,(m,beta,exact,gamma_q(m,beta))
            checks+=2
    # Supplementary independent numerical comparisons for nonintegral exponents.
    for beta in (-0.75,-0.5,0.25,0.5,1.75):
        for m in range(1,5):
            def general_h(m, alpha, beta):
                logh=-lgamma(m+1)
                for j in range(m):
                    logh+=(lgamma(alpha+j+1)+lgamma(beta+j+1)
                           +lgamma(j+2)-lgamma(alpha+beta+m+j+1))
                return logh
            logq=2*general_h(m,0.0,beta)-general_h(m,-0.5,beta)-general_h(m,0.5,beta)
            assert abs(exp(logq)-gamma_q(m,beta))<1e-9,(m,beta)
            checks+=1
    monotonic_checks=0
    for m in range(1,9):
        parameters=(-0.9,-0.25,0,0.5,1.0,3.0,20.0,100.0)
        vals=[gamma_q(m,beta) for beta in parameters]
        assert all(a>b for a,b in zip(vals,vals[1:])),(m,vals)
        monotonic_checks+=len(vals)-1
    # Deterministic high-order partial-product check against independent Barnes value.
    try:
        import mpmath as mp
        mp.mp.dps=38
        b=mp.mpf('0.5')
        c=2**mp.mpf('.25')*mp.sqrt(mp.pi)*mp.barnesg(b)**2
        for m in (200,1000):
            # Scaled version based on the exact finite Gamma product.
            f=mp.barnesg(m+1)**2 * mp.barnesg(b)*mp.barnesg(b+1) / (mp.barnesg(m+b)*mp.barnesg(m+b+1))
            tail=mp.nprod(lambda j: mp.gamma(m+j+mp.mpf('0.5'))*mp.gamma(m+j+mp.mpf('1.5'))/mp.gamma(m+j+1)**2,[0,m-1])
            estimate=f*tail*m**mp.mpf('.25')
            assert abs(estimate/c-1) < mp.mpf('0.003')
            checks+=1
        uniform_checks=0
        for m in (40,250):
            f=mp.barnesg(m+1)**2 * mp.barnesg(b)*mp.barnesg(b+1) / (mp.barnesg(m+b)*mp.barnesg(m+b+1))
            for beta in (mp.mpf('-.9'),mp.mpf('0'),mp.mpf('.7')*m,mp.mpf('1')*m,mp.mpf('20')*m):
                log_r=mp.fsum(mp.loggamma(m+j+beta+b)+mp.loggamma(m+j+beta+b+1)-2*mp.loggamma(m+j+beta+1) for j in range(m))
                actual=f*mp.exp(log_r)
                predicted=(c/(2**mp.mpf('.25')))*m**(-mp.mpf('.25'))*((2*m+beta+1)/(m+beta+1))**mp.mpf('.25')
                assert abs(actual/predicted-1)<mp.mpf('.006'),(m,beta)
                uniform_checks+=1
        quadrature_checks=0
        for beta in (mp.mpf('0.5'),mp.mpf('1.25')):
            m=2
            def moments_quadrature(alpha):
                matrix=mp.matrix(m,m)
                for i in range(m):
                    for j in range(m):
                        matrix[i,j]=mp.quad(lambda t: t**(i+j+alpha)*(1-t)**beta,[0,mp.mpf('0.5'),1])
                return mp.det(matrix)
            actual=moments_quadrature(0)**2/(moments_quadrature(-b)*moments_quadrature(b))
            target=mp.nprod(lambda j:mp.gamma(j+1)**2/(mp.gamma(j+b)*mp.gamma(j+b+1)) * mp.gamma(m+j+beta+b)*mp.gamma(m+j+beta+b+1)/mp.gamma(m+j+beta+1)**2,[0,m-1])
            assert abs(actual-target)<mp.mpf('1e-16')
            quadrature_checks+=1
        print(f'VERIFY_OK exact_moment_and_selberg_checks=120 nonintegral_checks=20 monotonic_checks={monotonic_checks} asymptotic_checks=2 crossover_checks={uniform_checks} quadrature_checks={quadrature_checks}')
    except ImportError:
        print(f'VERIFY_OK exact_moment_and_selberg_checks=120 nonintegral_checks=20 monotonic_checks={monotonic_checks}; mpmath_asymptotic_checks=not_run')

if __name__=='__main__':
    run()
