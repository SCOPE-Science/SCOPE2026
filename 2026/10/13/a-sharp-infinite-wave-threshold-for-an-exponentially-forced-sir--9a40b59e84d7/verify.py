#!/usr/bin/env python3
"""Standalone exact algebra checks for an exponentially forced SIR theorem.

The geometric existence of periodic orbits is proved analytically in RESULT.md;
finite code is not a proof of recurrence on an unbounded time interval.
"""
from fractions import Fraction as F

DIM = 4  # formal variables: a, gamma, Q, P
ZERO_EXP = (0, 0, 0, 0)

class Poly:
    def __init__(self, terms=None):
        self.c = {k: F(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def const(x):
        return Poly({ZERO_EXP: F(x)})

    @staticmethod
    def var(i):
        key = tuple(1 if j == i else 0 for j in range(DIM))
        return Poly({key: F(1)})

    def __add__(self, other):
        if not isinstance(other, Poly):
            other = Poly.const(other)
        d = self.c.copy()
        for k, v in other.c.items():
            d[k] = d.get(k, F(0)) + v
        return Poly(d)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.c.items()})

    def __sub__(self, other):
        if not isinstance(other, Poly):
            other = Poly.const(other)
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        if not isinstance(other, Poly):
            other = Poly.const(other)
        d = {}
        for k, v in self.c.items():
            for j, w in other.c.items():
                m = tuple(k[z] + j[z] for z in range(DIM))
                d[m] = d.get(m, F(0)) + v * w
        return Poly(d)

    __rmul__ = __mul__

    def __eq__(self, other):
        if not isinstance(other, Poly):
            other = Poly.const(other)
        return self.c == other.c

    def substitute_p_one(self):
        d = {}
        for k, v in self.c.items():
            z = (k[0], k[1], k[2], 0)
            d[z] = d.get(z, F(0)) + v
        return Poly(d)

one = Poly.const(1)
a, g, Q, P = [Poly.var(i) for i in range(DIM)]
Qdot = a * Q * (one - P)
Pdot = P * (g * Q - g + a)

# Transformed SIR equations after clearing only nonzero positive factors.
assert g * (Qdot - a * Q) + a * g * Q * P == 0
assert a * (Pdot - a * P) - a * g * P * (Q - one) == 0

# Energy H=gamma*Q-(gamma-a)*log(Q)+a*P-a*log(P).
# Its derivative is polynomial after cancellation of Q and P.
energy_derivative = a * (g * Q - g + a) * (one - P) + a * (P - one) * (g * Q - g + a)
assert energy_derivative == 0

# log incidence derivative is Qdot/Q+Pdot/P-a.
log_incidence_derivative = a * (one - P) + (g * Q - g + a) - a
assert log_incidence_derivative.substitute_p_one() == g * (Q - one)

# Exact, positive and physically feasible rational input data.
N = F(1)
gamma = F(1)
alpha = F(1, 2)
beta0 = F(5)
S0, I0, R0 = F(2, 5), F(1, 10), F(1, 2)
assert S0 > 0 and I0 > 0 and R0 >= 0
assert S0 + I0 + R0 == N
assert 0 < alpha < gamma
q0 = beta0 * S0 / (gamma * N)
p0 = beta0 * I0 / (alpha * N)
assert (q0, p0) == (F(2), F(1))

# E-H(1,1)=1-(log 2)/2>1/2: log 2 = integral_1^2 (1/t)dt<1.
from decimal import Decimal
assert Decimal(2).ln() < Decimal(1)
assert F(5, 2) - F(3, 2) > F(1, 2)
print('VERIFY_OK')
