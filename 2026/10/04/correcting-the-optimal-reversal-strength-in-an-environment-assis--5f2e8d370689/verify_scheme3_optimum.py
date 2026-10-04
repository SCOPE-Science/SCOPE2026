#!/usr/bin/env python3
import math

def C(d,q):
    r=1.0-d
    y=1.0-q
    if y==0.0:
        return 0.0
    return 2.0*r*math.sqrt(y)/(r+y)

def P(d,q):
    return ((1.0-q)+(1.0-d))/2.0

def C_from_x_state(d,q):
    # Unnormalized postselected X state for the source's representative Bell branch.
    r=1.0-d
    y=1.0-q
    rho00=y/2.0
    rho01=d*r/2.0
    rho10=0.0
    rho11=r*r/2.0
    coh=r*math.sqrt(y)/2.0
    prob=rho00+rho01+rho10+rho11
    # Normalized X-state concurrence: 2 max(|rho14|-sqrt(rho22*rho33),0).
    return 2.0*max(coh-math.sqrt(rho01*rho10),0.0)/prob, prob

def main():
    cases=0
    derivative_sign_checks=0
    pareto_checks=0

    for k in range(1,100):
        d=k/100.0
        r=1.0-d
        qstar=d
        qpub=2*d-d*d

        cstar=C(d,qstar)
        pstar=P(d,qstar)
        cpub=C(d,qpub)
        ppub=P(d,qpub)

        assert abs(cstar-math.sqrt(r))<2e-14
        assert abs(pstar-r)<2e-14
        assert cstar>cpub
        assert pstar>ppub

        cx,px=C_from_x_state(d,qstar)
        assert abs(cx-cstar)<2e-14
        assert abs(px-pstar)<2e-14
        cases += 1

        # Derivative sign away from the unique critical point y=r.
        for j in range(1,100):
            y=j/100.0
            deriv=r*(r-y)/(math.sqrt(y)*(r+y)**2)
            if y<r-1e-12:
                assert deriv>0
            elif y>r+1e-12:
                assert deriv<0
            derivative_sign_checks += 1

        # Closed Pareto curve on y in [r,1].
        for j in range(51):
            y=r+(1-r)*j/50.0
            p=(r+y)/2.0
            c_front=r*math.sqrt(2*p-r)/p
            q=1-y
            assert -1e-14 <= q <= d+1e-14
            assert abs(c_front-C(d,q))<2e-13
            pareto_checks += 1

    print("VERIFY_OK")
    print("damping_cases =", cases)
    print("derivative_sign_checks =", derivative_sign_checks)
    print("pareto_formula_checks =", pareto_checks)
    print("corrected_optimum = q=d")
    print("published_point_is_strictly_dominated = yes")

if __name__=="__main__":
    main()
