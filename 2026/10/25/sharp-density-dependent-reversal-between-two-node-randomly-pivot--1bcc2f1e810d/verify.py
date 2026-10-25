"""Numerical consistency checks for a two-point first-harmonic kernel quadrature theorem.

All universal identities and sign classifications have elementary analytic proofs
in RESULT.md. These finite tests are reproducibility checks, not such proofs.
Run: python verify.py
"""
import math
import random

TAU = 2.0 * math.pi


def rp_difference_density(angle, beta):
    c = math.cos(angle)
    return 2.0 * (1.0-c) * (2.0+beta*(1.0+c))/(beta+4.0)


def conditional_error_average(angle, beta, a, u, v):
    c2 = math.cos(angle/2.0)**2
    return beta*(a*a*c2+(u*u+v*v)/8.0)/(1.0+beta*c2)


def analytic_rates(beta, a, u, v):
    benergy=(u*u+v*v)/2.0
    rp=beta/(beta+4.0)*(a*a+benergy)
    iid=(1.0-1.0/math.sqrt(1.0+beta))*a*a + beta/(4.0*math.sqrt(1.0+beta))*benergy
    return rp,iid


def signed_gap(beta, a, u, v):
    s=math.sqrt(1.0+beta)
    return (s-1.0)*(s-3.0)/(s*(beta+4.0))*(a*a-beta*(u*u+v*v)/8.0)


def integrate_1d(func, nodes=32768):
    return sum(func(TAU*(j+0.5)/nodes) for j in range(nodes))/nodes


def check():
    assertions=0
    for beta in (0.0625,0.25,1.0,3.0,7.9,8.0,8.1,15.0,64.0):
        assert abs(integrate_1d(lambda d: rp_difference_density(d,beta))-1.0)<1e-11
        assertions+=1
        for a,u,v in ((1.0,0.0,0.0),(0.0,1.0,0.0),(0.0,0.0,1.0),(1.0,0.6,0.8),(1.4,0.2,-0.9)):
            rp,iid=analytic_rates(beta,a,u,v)
            numerical_rp=integrate_1d(lambda d: conditional_error_average(d,beta,a,u,v)*rp_difference_density(d,beta))
            numerical_iid=integrate_1d(lambda d: conditional_error_average(d,beta,a,u,v))
            assert abs(numerical_rp-rp)<2e-10*(1+rp)
            assert abs(numerical_iid-iid)<2e-10*(1+iid)
            assert abs(rp-iid-signed_gap(beta,a,u,v))<2e-13*(1+rp+iid)
            assertions+=3
        if beta<8.0:
            for t in (0.0,0.25,0.7,1.0):
                rp,iid=analytic_rates(beta,1.0,t,0.0)
                assert rp<iid
                assertions+=1
        elif beta>8.0:
            rp,iid=analytic_rates(beta,1.0,0.0,0.0)
            assert rp>iid
            rp,iid=analytic_rates(beta,1.0,1.0,0.0)
            assert rp<iid
            assertions+=2
    rng=random.Random(20261018)
    for _ in range(3000):
        beta=10.0**rng.uniform(-3,3)
        a,u,v=(rng.uniform(-2.0,2.0) for _ in range(3))
        rp,iid=analytic_rates(beta,a,u,v)
        assert math.isclose(rp-iid,signed_gap(beta,a,u,v),rel_tol=1e-9,abs_tol=1e-11)
        assertions+=1
    print(f'PASS: {assertions} deterministic assertions; analytic proof is in RESULT.md')


if __name__=='__main__':
    check()
