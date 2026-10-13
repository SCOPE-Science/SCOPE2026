#!/usr/bin/env python3
import math

def Q(p,a,s=1.0):
    return s*(2*p-1)*(p*(1-p))**(1/(2*a)-1)

def H(p,a,s=1.0):
    return -2*a*s*(p*(1-p))**(1/(2*a))

def qprime_z(z,a,s=1.0):
    g=1/(2*a)-1
    return s*(1-z*z)**(g-1)*(1-((1-a)/a)*z*z)

def run():
    identity_checks=0
    regression_checks=0
    monotonicity_checks=0

    slopes=[0.5, 2/3, 0.75, 1.0, 1.5, 2.0, 5.0]
    ps=[0.03,0.1,0.25,0.4,0.6,0.75,0.9,0.97]
    for a in slopes:
        for p in ps:
            q=Q(p,a)
            h=H(p,a)
            lhs=(1-2*p)*h
            rhs=2*a*p*(1-p)*q
            assert abs(lhs-rhs) <= 2e-12*(1+abs(lhs)+abs(rhs))
            identity_checks+=1
            lower=h/p
            upper=-h/(1-p)
            mid=(lower+upper)/2
            assert abs(mid-a*q) <= 2e-12*(1+abs(mid)+abs(a*q))
            regression_checks+=1
        for z in (-0.999,-0.8,-0.2,0.2,0.8,0.999):
            assert qprime_z(z,a)>0
            monotonicity_checks+=1

    # The derivative changes sign near an endpoint below the admissible boundary.
    for bad in (0.1,0.25,0.49):
        assert qprime_z(0.999999,bad)<0
        monotonicity_checks+=1

    # Direct algebraic ODE residual at generic numerical points.
    ode_checks=0
    for a in slopes:
        g=1/(2*a)-1
        for z in (-0.9,-0.4,0.3,0.85):
            q=z*(1-z*z)**g
            qp=(1-z*z)**(g-1)*(1-((1-a)/a)*z*z)
            res=a*z*(1-z*z)*qp-(a+(a-1)*z*z)*q
            assert abs(res)<2e-12
            ode_checks+=1

    print(
        "VERIFY_OK "
        f"ode_checks={ode_checks} "
        f"identity_checks={identity_checks} "
        f"conditional_regression_checks={regression_checks} "
        f"monotonicity_checks={monotonicity_checks}"
    )

if __name__=="__main__":
    run()
