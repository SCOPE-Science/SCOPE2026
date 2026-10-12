#!/usr/bin/env python3
from fractions import Fraction as F

class Q2:
    """Exact a + b*sqrt(2), with rational a,b."""
    __slots__ = ("a","b")
    def __init__(self,a=0,b=0):
        self.a = a if isinstance(a,F) else F(a)
        self.b = b if isinstance(b,F) else F(b)
    def __add__(self,o):
        o = o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a+o.a,self.b+o.b)
    __radd__ = __add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self + (-o)
    def __rsub__(self,o): return Q2(o)-self
    def __mul__(self,o):
        o = o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a*o.a + 2*self.b*o.b,
                  self.a*o.b + self.b*o.a)
    __rmul__ = __mul__
    def __eq__(self,o):
        o = o if isinstance(o,Q2) else Q2(o)
        return self.a==o.a and self.b==o.b

zero = Q2()
inv_sqrt2 = Q2(0,F(1,2))

def coeff_array():
    return [[[zero for _ in range(2)] for _ in range(2)] for _ in range(2)]

def w3_raw(state):
    s = Q2()
    for k in range(2):
        d = state[0][0][k]*state[1][1][k] - state[0][1][k]*state[1][0][k]
        s += d*d
    for j in range(2):
        d = state[0][j][0]*state[1][j][1] - state[0][j][1]*state[1][j][0]
        s += d*d
    for i in range(2):
        d = state[i][0][0]*state[i][1][1] - state[i][0][1]*state[i][1][0]
        s += d*d
    return s

psi0 = coeff_array()
psi0[0][0][0] = inv_sqrt2
psi0[1][1][0] = inv_sqrt2

psip = coeff_array()
for i in range(2):
    for j in range(2):
        a0,a1 = psi0[i][j][0], psi0[i][j][1]
        psip[i][j][0] = inv_sqrt2*(a0+a1)
        psip[i][j][1] = inv_sqrt2*(a0-a1)

expected = coeff_array()
for i,j,k in [(0,0,0),(0,0,1),(1,1,0),(1,1,1)]:
    expected[i][j][k] = Q2(F(1,2))
assert psip == expected

raw0 = w3_raw(psi0)
rawp = w3_raw(psip)
assert raw0 == Q2(F(1,4))
assert rawp == Q2(F(1,8))
assert 4*raw0 == Q2(1)
assert 4*rawp == Q2(F(1,2))

det_H = -1
det_iH = (-1)*det_H
assert det_iH == 1

print("VERIFY_OK C2_over_N_before=1 C2_over_N_after=1/2 det_iH=1")
