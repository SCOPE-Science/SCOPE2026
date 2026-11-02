#!/usr/bin/env python3
"""Standalone numerical cross-checks for the stated Abel-oscillator formulas.

Requires scipy and numpy. Numerical evidence is not a substitute for the proof.
"""
import math
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

PI = math.pi


def constants(kappa):
    q = math.sqrt(kappa)
    a = 0.5*(q + 1.0/q)
    C = 16.0*PI*kappa*kappa/(1.0-kappa)**2
    return q, a, C


def J(theta, q):
    _, a, _ = constants(q*q)
    return 2.0*math.sin(theta) - 4.0*a*math.atan2(q*math.sin(theta), 1.0+q*math.cos(theta))


def defect_coefficient(kappa):
    q, a, _ = constants(kappa)
    return 0.5*quad(lambda t: math.sin(t)*J(t,q)**2/(a+math.cos(t))**2,
                    0.0, PI, epsabs=2e-12, epsrel=2e-12)[0]


def propagate(c_init, eps, kappa):
    def field(theta, state):
        c, log_derivative = state
        den = c-1.0+math.cos(theta)
        if den <= 0:
            raise ValueError('Trajectory left the positive radial sector')
        A = math.cos(2.0*theta)-kappa
        return [-eps*A/den, eps*A/(den*den)]
    sol = solve_ivp(field, (0.0,2.0*PI), (c_init, 0.0), method='DOP853',
                    atol=3e-13, rtol=3e-13, max_step=0.025,
                    dense_output=True)
    if not sol.success:
        raise RuntimeError(sol.message)
    return float(sol.y[0,-1]), float(sol.y[1,-1]), float(sol.sol(PI)[0])


def find_cycle(eps,kappa):
    q,a,C = constants(kappa)
    cstar = a+1.0
    def displacement(c):
        return propagate(c,eps,kappa)[0]-c
    radius=0.01
    for _ in range(6):
        lo=cstar-radius; hi=cstar+radius
        if lo>2.02 and displacement(lo)*displacement(hi)<0:
            break
        radius*=1.3
    else:
        raise RuntimeError('No admissible bracket for cycle')
    c=brentq(displacement,lo,hi,xtol=3e-13,rtol=1e-13)
    end,log_mult,c_pi=propagate(c,eps,kappa)
    assert abs(end-c)<3e-10
    return c,c_pi,log_mult


def main():
    tests=0
    for kappa in (0.04,0.25):
        q,a,C=constants(kappa)
        D=defect_coefficient(kappa)
        assert D>0
        for theta in (0.1,0.7,1.3,2.2,3.6,5.5):
            h=1e-5
            assert abs((J(theta+h,q)-J(theta-h,q))/(2*h) -
                       (math.cos(2*theta)-kappa)/(a+math.cos(theta)))<2e-9
            tests+=1
        for eps in (0.008,0.004):
            c, cp, lm = find_cycle(eps,kappa)
            cm, cpm, lmm = find_cycle(-eps,kappa)
            axial=cp-c
            assert abs(c-cm)<2e-8, ('reversal axis at 0',kappa,eps,c,cm)
            assert abs(cp-cpm)<2e-8, ('reversal axis at pi',kappa,eps,cp,cpm)
            assert abs(lm+lmm)<2e-8, ('inverse Floquet law',kappa,eps,lm,lmm)
            assert abs(c-(a+1))<8.0*eps*eps/(1-kappa)**3
            assert abs(lm/(eps*C)-1.0)<0.05
            assert axial>0
            assert abs(axial/(eps*eps)-D)<max(1.0e-5,0.005*D)
            tests+=7
        c8,cp8,_=find_cycle(0.008,kappa)
        c4,cp4,_=find_cycle(0.004,kappa)
        error8=abs((cp8-c8)/(0.008**2)-D)
        error4=abs((cp4-c4)/(0.004**2)-D)
        if kappa==0.25:
            assert error4 < 0.35*error8, ('quadratic error refinement',error4,error8)
        tests+=1
        print('kappa=',kappa,'D=',format(D,'.12g'),'Floquet linear=',format(C,'.12g'),
              'error at 0.008=',format(error8,'.4g'),'error at 0.004=',format(error4,'.4g'))
    print('PASS:',tests,'numerical identity and convergence checks')


if __name__=='__main__':
    main()
