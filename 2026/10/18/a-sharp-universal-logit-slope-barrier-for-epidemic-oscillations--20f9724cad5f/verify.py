#!/usr/bin/env python3
"""Self-contained finite checks for an SIS–logit oscillation theorem.

This program checks exact identities and samples; the analytical proof establishes
all infinite-parameter and infinite-time conclusions.
"""
from fractions import Fraction as Q
from math import exp, log


def exact_identity_checks():
    tests = 0
    for eta in (Q(1, 100), Q(1, 10), Q(1, 2), Q(9, 10)):
        m = 4 + eta
        beta = eta
        gamma = 3 * eta / 8
        a1, b1, a0, b0 = m/2, 3*m/2, -7*m/2, -5*m/2
        assert a1 > 0 and b1 > 0
        assert max(Q(0), b1-a1, b0-a0) == m
        for x in (Q(0), Q(1, 10), Q(1, 2), Q(4, 5), Q(1)):
            for infection in (Q(0), Q(1, 10), Q(1, 4), Q(1, 2), Q(1)):
                delta = ((1-infection)*(b1+(a1-b1)*x)
                         +infection*(b0+(a0-b0)*x))
                assert delta == m*(Q(3, 2)-x-4*infection)
                tests += 1
        xstar, istar = Q(1, 2), Q(1, 4)
        assert m*(Q(3, 2)-xstar-4*istar) == 0
        assert beta*(1-xstar)*(1-istar) == gamma
        # Independently differentiate the payoffs and SIS vector field at E.
        ddx = ((1-istar)*(a1-b1) + istar*(a0-b0))
        ddi = (b0+(a0-b0)*xstar) - (b1+(a1-b1)*xstar)
        # At E the exact logistic response is 1/2, derivative factor 1/4.
        J11, J12 = -ddx/4 - 1, -ddi/4
        J21 = -beta*istar*(1-istar)
        J22 = beta*(1-xstar)*(1-2*istar) - gamma
        assert (J11,J12,J21,J22) == (eta/4,m,-3*eta/16,-eta/8)
        trace = J11 + J22
        determinant = J11*J22 - J12*J21
        discriminant = trace*trace - 4*determinant
        assert trace == eta/8 > 0
        assert determinant == eta*(24+5*eta)/32 > 0
        assert discriminant == -eta*(192+39*eta)/64 < 0
        assert m/4 > 1
        assert Q(1, 2)*Q(15, 16) - Q(3, 8) == Q(3, 32)
        tests += 9
    return tests


def floating_consistency_checks():
    tests = 0
    for eta in (0.01, 0.1, 0.5, 0.9):
        m = 4+eta
        def logistic(delta):
            return 1/(1+exp(delta))
        def F(x, infected):
            return logistic(m*(1.5-x-4*infected))-x
        def G(x, infected):
            return eta*infected*((1-x)*(1-infected)-3/8)
        assert abs(F(0.5, 0.25)) < 1e-14
        assert abs(G(0.5, 0.25)) < 1e-14
        # Disease-free response is strictly below 1/8; it is a contraction.
        for k in range(101):
            x = k/100
            y = logistic(m*(1.5-x))
            assert 0 < y < 1/8
            assert m*y*(1-y) < 5/8
            tests += 1
        # For I<=1/16, logit response <1/3 and x'<=-1/6 at x>=1/2.
        for k in range(101):
            x = 0.5 + k/200
            for i in (0, 1/32, 1/16):
                delta = m*(1.5-x-4*i)
                assert delta >= m/4 > 1
                assert logistic(delta) < 1/3
                assert F(x, i) < -1/6
                tests += 1
        # Positive epidemic growth in the lower-left thin strip.
        for k in range(101):
            x = k/200
            for i in (1/256, 1/32, 1/16):
                assert G(x,i)/i >= 3*eta/32 - 1e-14
                tests += 1
        # Endemic fixed-point curve: the right-hand derivative stays positive.
        for k in range(1, 624):
            x = k/1000
            assert m*(-1 + 1.5/(1-x)**2) > 0
            tests += 1
    return tests


if __name__ == '__main__':
    a = exact_identity_checks()
    b = floating_consistency_checks()
    print('PASS: {} exact rational checks; {} sampled inequalities'.format(a,b))
    print('The continuous-domain and omega-limit claims require the proof in RESULT.md.')
