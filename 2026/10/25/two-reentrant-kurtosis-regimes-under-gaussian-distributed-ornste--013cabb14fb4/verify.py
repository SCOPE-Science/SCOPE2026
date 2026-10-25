#!/usr/bin/env python3
"""Verify the fourth-cumulant identities for Gaussian OU resetting."""
from fractions import Fraction as F
from math import isclose


def coeff(q):
    mu = lambda j: q / (q + j)
    A = mu(4) - 4 * mu(1) * mu(3) + 12 * mu(1)**2 * mu(2) - 6 * mu(1)**4 - 3 * mu(2)**2
    B = mu(4) - 2 * mu(1) * mu(3) + 2 * mu(1)**2 * mu(2) - mu(2)**2
    C = mu(4) - mu(2)**2
    return A, B, C


def rational_formula(q):
    A = 6*q*(q**3-q*q-6*q+2)/((q+1)**4*(q+2)**2*(q+3)*(q+4))
    B = -4*q*(q*q+q-3)/((q+1)**2*(q+2)**2*(q+3)*(q+4))
    C = 4*q/((q+2)**2*(q+4))
    return A, B, C


def raw_fourth(q, m, v, d):
    mu = lambda j: q / (q + j)
    M1 = m*mu(1)
    M2 = m*m*mu(2) + v + d*mu(2)
    M3 = m**3*mu(3) + 3*m*(v*mu(1)+d*mu(3))
    M4 = m**4*mu(4) + 6*m*m*(v*mu(2)+d*mu(4)) + 3*(v*v+2*v*d*mu(2)+d*d*mu(4))
    return M4-4*M1*M3-3*M2*M2+12*M1*M1*M2-6*M1**4


def run():
    for q in (F(1,10), F(1,3), F(1), F(4), F(20)):
        A,B,C = coeff(q)
        assert (A,B,C) == rational_formula(q), (q,A,B,C)
        discr = 36*B*B-12*A*C
        expected = 288*q*q*(q*q-2*q+3)/((q+1)**4*(q+2)**2*(q+3)**2*(q+4)**2)
        assert discr == expected and discr>0
        for v,d,m in ((F(2),F(1),F(0)), (F(2),F(1),F(3)), (F(2),F(1),F(8)), (F(2),F(-1),F(1))):
            expected = A*m**4+6*B*m*m*d+3*C*d*d
            assert raw_fourth(q,m,v,d) == expected, (q,d,m)
    q=F(4); t=F(9)
    assert raw_fourth(q,3,2,1)<0
    assert raw_fourth(q,0,2,1)>0
    assert raw_fourth(q,8,2,1)>0
    print('PASS: exact rational cumulant, discriminant, and sign witnesses.')

if __name__ == '__main__':
    run()
