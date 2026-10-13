#!/usr/bin/env python3
from fractions import Fraction

def matvec(M, v):
    return (
        M[0][0]*v[0] + M[0][1]*v[1],
        M[1][0]*v[0] + M[1][1]*v[1],
    )

for R in (Fraction(3,2), Fraction(2), Fraction(3), Fraction(7,2)):
    for gamma in (Fraction(1,3), Fraction(2), Fraction(5,2)):
        beta = gamma*R
        q = 1 - 1/R
        M0 = (
            (-beta*q*q, gamma*q),
            ( beta*q*q,-gamma*q),
        )
        det = M0[0][0]*M0[1][1] - M0[0][1]*M0[1][0]
        tr = M0[0][0] + M0[1][1]
        stable = -gamma*(R-1)
        assert det == 0
        assert tr == stable

        v0 = (Fraction(1), R-1)
        vs = (Fraction(1), Fraction(-1))
        assert matvec(M0, v0) == (0,0)
        assert matvec(M0, vs) == (stable, -stable)

        for f in (Fraction(1,2), Fraction(4,3)):
            for g in (Fraction(2,3), Fraction(5,4)):
                l = Fraction(0)
                B0 = f*g*l**4 + (f*gamma*q + g*beta*q*q)*l*l
                assert B0 == 0
                for l in (Fraction(1,2), Fraction(1), Fraction(3)):
                    A = (f+g)*l*l + beta*q*q + gamma*q
                    B = f*g*l**4 + (f*gamma*q + g*beta*q*q)*l*l
                    assert A > 0
                    assert B > 0

print("VERIFY_OK")
