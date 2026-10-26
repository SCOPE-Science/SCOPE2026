#!/usr/bin/env python3
"""Finite diagnostics for quadratic Hardy composition Berezin circle geometry."""
import cmath, math
from fractions import Fraction as Q

def run():
    checks = 0
    # Rational exact arithmetic for the identities underpinning the proof.
    for m in range(1, 12):
        u = Q(m, 13)
        a = Q(1, 1) / (2 + u)
        for j in range(1, 40):
            r = Q(j, 41)
            A = 1 - (1 - u) * r * r
            B = u * r**3
            D = A*A - B*B
            assert D > 0 and A > B
            c = (1-r*r)*A/D
            rho = (1-r*r)*B/D
            assert (2+u)*(1-r*r)*A-D == (1-r*r)**2*(1+u+u*u*r*r)
            assert 1-c == u*r*r*(1-r*r)*(1+u*r*r)/D
            assert rho/(1-c) == r/(1+u*r*r)
            assert a < c < 1 and rho < a*(1-c)/(1-a)
            checks += 6
    for u in (.05, .25, .5, .75, .95):
        a=1/(2+u)
        T=1/(1+u)+1j*math.sqrt(u*(2+u))/((1+u)*(2+u))
        assert abs(abs(T-a)-a) < 1e-12
        assert abs(((T-a).conjugate()*(1-T)).real) < 1e-12
        for r in (.01,.2,.6,.9,.99):
            A=1-(1-u)*r*r; B=u*r**3; den=A*A-B*B
            c=(1-r*r)*A/den; rho=(1-r*r)*B/den
            for j in range(20):
                theta=2*math.pi*j/20
                z=(1-r*r)/(A-B*cmath.exp(1j*theta))
                assert abs(abs(z-c)-rho) < 5e-12
                checks += 1
        area=(math.pi+math.sqrt(u*(u+2))-math.acos(1/(1+u)))/(2+u)**2
        assert 0.42 < area < math.pi/4
        checks += 3
    print('PASS',checks,'finite exact and numerical consistency tests')
if __name__=='__main__': run()
