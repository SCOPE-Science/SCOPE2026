"""Exact rational spot-checks for the normalized cat–oocyst equilibrium theorem.

The algebraic proof in RESULT.md establishes the parameter-uniform assertions.
These finite tests are independent checks of the specified rational witnesses.
"""
from fractions import Fraction as F


def check(beta):
    mu, gamma, alpha, t1, t2, k, mu0, beta_m = (
        F(1), F(1), F(1, 2), F(1, 4), F(1, 2),
        F(1), F(1), F(1)
    )
    d = alpha - mu*t1
    a = alpha - mu*(t1+t2)
    H = mu+a
    beta_c = d*mu0*(mu+gamma)/(mu*k)
    q = -a
    beta_max = d*mu0*(gamma+q)/(k*q)
    assert (d, a, H, q, beta_c, beta_max) == (
        F(1, 4), F(-1, 4), F(3, 4), F(1, 4), F(1, 2), F(5, 4)
    )
    S = d*mu0/(beta*k)
    I = (mu-(mu+gamma)*S)/H
    O = k*I/mu0
    M = F(0)
    V = 1-S-I
    residual = (
        mu-(mu+gamma)*S-beta*S*O-mu*(1-t2)*I,
        beta*S*O-d*I,
        k*I-mu0*O,
        -beta_m*M*O,
    )
    assert residual == (F(0),)*4
    assert V == (a+(gamma-a)*S)/H
    assert I>0 and O>0 and S>0 and M==0
    return S,I,O,M,V, beta/beta_c

assert check(F(1)) == (F(1,4), F(2,3), F(2,3), F(0), F(1,12), F(2))
assert check(F(5,4)) == (F(1,5), F(4,5), F(4,5), F(0), F(0), F(5,2))
assert check(F(2)) == (F(1,8), F(1), F(1), F(0), F(-1,8), F(4))

# Boundary-face obstruction at a<0: V'=gamma*S+a*I when V=0.
assert F(1)*F(0) + F(-1,4)*F(1) == F(-1,4)
# beta_max > beta_c exactly.
assert F(5,4) > F(1,2)
print('VERIFY_OK')
