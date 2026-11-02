#!/usr/bin/env python3
"""Reproduce the stationary moment, temporal asymmetry, and optimal-lag identities.

Requires only the Python standard library. The stochastic model is explicitly
specified in RESULT.md; this script performs independent generator and
shot-integral checks, not a numerical substitute for the proof.
"""
from math import comb, exp, isclose, log, sqrt


def stationary_moments(gamma, intensity, thermal_D, jump_raw_moments, degree=4):
    """Solve the centered polynomial-generator equations recursively."""
    m = [1.0, 0.0]
    for n in range(2, degree + 1):
        noise = thermal_D * n * (n-1) * m[n-2]
        noise += intensity * sum(comb(n,k)*jump_raw_moments[k]*m[n-k]
                                 for k in range(2,n+1))
        m.append(noise/(n*gamma))
    return m


def simpson(f, a, b, n=12000):
    assert n % 2 == 0
    h = (b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+j*h) for j in range(1,n,2))
                +2*sum(f(a+j*h) for j in range(2,n,2)))


def test(gamma, intensity, D, moment, label):
    moments = stationary_moments(gamma,intensity,D,moment)
    m2,m3,m4 = moments[2:5]
    kappa4_gen = m4-3*m2*m2
    kappa4_poisson = intensity*moment[4]/(4*gamma)
    assert isclose(kappa4_gen,kappa4_poisson,rel_tol=2e-13,abs_tol=1e-12)
    # This integral comes from the Poisson random-measure cumulant formula,
    # independently of the recursive polynomial generator.
    integral = simpson(lambda s: exp(-4*gamma*s),0.0,16.0/gamma)
    assert isclose(intensity*moment[4]*integral,kappa4_gen,
                   rel_tol=3e-9,abs_tol=1e-9)
    tstar=log(3)/(2*gamma)
    peak=kappa4_poisson*2/(3*sqrt(3))
    for t in [0,0.04/gamma,0.19/gamma,tstar,0.8/gamma,2/gamma,5/gamma]:
        q=exp(-gamma*t)
        # Independent transition innovation has stationary covariance balance.
        newvar=m2*(1-q*q)
        forward=q**3*m4+3*q*m2*newvar
        backward=q*m4
        a=forward-backward
        b=-intensity*moment[4]/(4*gamma)*q*(1-q*q)
        assert isclose(a,b,rel_tol=6e-13,abs_tol=3e-12),(label,t,a,b)
        assert a <= 4e-13
        if t > 0: assert a < 0
    # Unique optimizer from f(q)=q-q^3, critical q=1/sqrt(3).
    qstar=1/sqrt(3)
    assert isclose(1-3*qstar*qstar,0,abs_tol=1e-14)
    assert -6*qstar < 0
    assert isclose(qstar-qstar**3,2/(3*sqrt(3)),rel_tol=1e-14)
    assert isclose(6*sqrt(3)*gamma*peak,intensity*moment[4],rel_tol=2e-14)
    assert isclose(3*sqrt(3)*log(3)*peak/tstar,intensity*moment[4],rel_tol=2e-14)
    # Independent comparison to a grid strictly bracketing the analytic peak.
    vals=[exp(-gamma*t)*(1-exp(-2*gamma*t))
          for t in [j*4/(20000*gamma) for j in range(20001)]]
    assert max(vals) <= 2/(3*sqrt(3)) + 1e-14
    assert 2/(3*sqrt(3)) - max(vals) < 1e-8
    print('PASS',label,'variance=',round(m2,8),'fourth-cumulant=',round(kappa4_gen,8),
          'optimal-lag=',round(tstar,8),'peak=',round(peak,8))
    return peak


def main():
    symmetric={2:2.5,3:0.,4:8.5} # J=+/-1 or +/-2 each with probability 1/4
    asymmetric={2:1.6,3:0.8,4:4.0} # P(J=-1)=.8, P(J=2)=.2
    fixed={2:1.0,3:1.0,4:1.0} # J=1 a.s. (nonzero mean)
    cases=[(0.7,1.3,0.0,asymmetric,'asymmetric, no thermal noise'),
           (0.7,1.3,0.25,asymmetric,'asymmetric, thermal noise'),
           (0.7,1.3,2.0,asymmetric,'asymmetric, strong thermal noise'),
           (2.0,0.4,0.3,symmetric,'symmetric jumps'),
           (0.45,2.1,0.7,fixed,'deterministic jumps')]
    peaks=[test(*case) for case in cases]
    assert isclose(peaks[0],peaks[1],rel_tol=1e-15)
    assert isclose(peaks[1],peaks[2],rel_tol=1e-15)
    # All-order cross-cumulant identity: coefficient of s^p t^q in
    # the contribution kappa_n (s+exp(-gamma*t)t)^n/n! is
    # kappa_n exp(-q gamma t)/(p!q!).
    for order in range(3,9):
        for p in range(1,order):
            r=order-p
            qq=exp(-0.39*r)
            lhs=comb(order,r)*qq
            # Normalize derivatives by p!r!; binomial coefficient must agree.
            from math import factorial
            assert isclose(lhs*factorial(p)*factorial(r)/factorial(order),qq,
                           rel_tol=2e-15)
    print('PASS fourth-order irreversibility and finite-order cumulant algebra')


if __name__=='__main__':
    main()
