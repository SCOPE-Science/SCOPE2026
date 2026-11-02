#!/usr/bin/env python3
"""Exact rational-polynomial checks for a three-site Beta-split exchange process.

Pure standard library; no external computer algebra or numerical integration.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product

CHECKS = 0

def assert_equal(a, b, description):
    global CHECKS
    assert a == b, f"{description}: {a!r} != {b!r}"
    CHECKS += 1

def trim(p):
    p = tuple(F(v) for v in p)
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return p

def plus(a, b):
    return trim(tuple((a[i] if i < len(a) else F(0)) +
                      (b[i] if i < len(b) else F(0))
                      for i in range(max(len(a), len(b)))))

def times(a, b):
    ret = [F(0)] * (len(a) + len(b) - 1)
    for i, j in product(range(len(a)), range(len(b))):
        ret[i+j] += a[i]*b[j]
    return trim(ret)

def minus(a, b):
    return plus(a, tuple(-v for v in b))

class Rat:
    """Unreduced rational function of the indeterminate t over Q."""
    def __init__(self, numerator, denominator=(1,)):
        self.n = trim(numerator)
        self.d = trim(denominator)
        assert any(self.d)
    @staticmethod
    def cast(v):
        return v if isinstance(v, Rat) else Rat((F(v),))
    def __add__(self, other):
        other = Rat.cast(other)
        return Rat(plus(times(self.n, other.d),times(other.n,self.d)),times(self.d,other.d))
    __radd__ = __add__
    def __neg__(self):
        return Rat(tuple(-x for x in self.n),self.d)
    def __sub__(self, other):
        return self + (-Rat.cast(other))
    def __rsub__(self, other):
        return Rat.cast(other) - self
    def __mul__(self, other):
        other = Rat.cast(other)
        return Rat(times(self.n,other.n),times(self.d,other.d))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = Rat.cast(other)
        return Rat(times(self.n,other.d),times(self.d,other.n))
    def __eq__(self, other):
        other = Rat.cast(other)
        return times(self.n,other.d) == times(other.n,self.d)
    def at(self, v):
        v = F(v)
        def evaluate(p):
            s = F(0)
            for x in reversed(p): s = s*v+x
            return s
        return evaluate(self.n)/evaluate(self.d)

T = Rat((0,1))
ONE = Rat((1,))
den = 221*T*T + 114*T + 13
m0, m1, m2 = Rat.cast(F(1,13)), Rat.cast(F(4,13)), Rat.cast(F(8,13))
U = (T+1)*(17*T+13)/(13*den)
W = 8*(2*T+1)*(68*T+13)/(13*den)
V = 4*T*(34*T+11)/(13*den)
left_second = (T+1)/(5*(5*T+1))
right_second = 2*(2*T+1)/(3*(3*T+1))

# Generator conditions for constants, first moments and three basis second moments.
assert_equal(m0, (ONE-m2)/5, 'first moment, site 0')
assert_equal(m2, 2*(ONE-m0)/3, 'first moment, site 2')
assert_equal(m0+m1+m2, ONE, 'total mass')
assert_equal(U, left_second*(ONE-2*m2+W), 'second moment U')
assert_equal(W, right_second*(ONE-2*m0+U), 'second moment W')
assert_equal(2*V, (m2-W)/5+F(2,3)*(m0-U), 'cross moment V')
assert_equal(F(1,5)*F(1,4)+F(2,3)*F(1,4)+F(1,2),F(43,60),'two-step coupling contraction')

C00=U-m0*m0
C22=W-m2*m2
C02=V-m0*m2
C01=-C00-C02
C12=-C22-C02
C11=C00+C22+2*C02
C=((C00,C01,C02),(C01,C11,C12),(C02,C12,C22))
A=((12*(23*T+13), 4*(16*T-13), -4*(85*T+26)),
   (4*(16*T-13),12*(173*T+39),-4*(535*T+104)),
   (-4*(85*T+26),-4*(535*T+104),40*(62*T+13)))
for i,j in product(range(3),repeat=2):
    assert_equal(C[i][j], A[i][j]/(169*den),f'exact polynomial covariance identity {i},{j}')
for i in range(3):
    assert_equal(sum(C[i], Rat.cast(0)),Rat.cast(0),f'conservation row {i}')
for i,j in product(range(3), repeat=2):
    assert_equal(C[i][j], C[j][i],f'symmetry {i},{j}')

# Algebraic sign boundary, rational test values, and low-noise/high-noise limits.
assert_equal(C01,4*(16*T-13)/(169*den),'sharp sign law')
assert_equal(C01.at(F(13,16)), F(0),'transition at t=13/16')
assert_equal(C01.at(F(1,2)), F(-80,84669),'negative rational example')
assert_equal(C01.at(F(1)), F(1,4901),'positive rational example')
assert_equal(C01.at(F(2)), F(76,190125),'second positive rational example')
for t in (F(1,100),F(1,7),F(1,2),F(13,16),F(1),F(2),F(100)):
    for i,j in product(range(3),repeat=2):
        assert_equal(C[i][j].at(t),A[i][j].at(t)/(169*den.at(t)),f'parameter t={t}, element {i}{j}')
    assert C00.at(t)>0 and C22.at(t)>0 and C02.at(t)<0 and C12.at(t)<0
    CHECKS+=1
print(f'PASS: {CHECKS} exact tests (including rational-polynomial identities for all t).')
