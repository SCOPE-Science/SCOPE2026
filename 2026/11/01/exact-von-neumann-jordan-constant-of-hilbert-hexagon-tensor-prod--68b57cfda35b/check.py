"""Reproducible exact algebra and finite-dimensional sanity checks.

Analytic arguments, including the infinite-dimensional bound and duality,
are in RESULT.md. This script is supplementary verification, not a proof.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


class Q3:
    """A rational pair representing a + b * square_root(3)."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    def __add__(self, other):
        if not isinstance(other, Q3): other = Q3(other)
        return Q3(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __neg__(self): return Q3(-self.a, -self.b)
    def __sub__(self, other): return self + (-other if isinstance(other, Q3) else Q3(-other))
    def __rsub__(self, other): return -self + other
    def __mul__(self, other):
        if not isinstance(other, Q3): other = Q3(other)
        return Q3(self.a*other.a + 3*self.b*other.b, self.a*other.b + self.b*other.a)
    __rmul__ = __mul__
    def __eq__(self, other):
        if not isinstance(other, Q3): other = Q3(other)
        return self.a == other.a and self.b == other.b
    def real(self): return float(self.a) + float(self.b)*sqrt(3)
    def __repr__(self): return f'Q3({self.a}, {self.b})'


def dot(u,v): return sum((a*b for a,b in zip(u,v)), Q3())
def add(u,v): return tuple(a+b for a,b in zip(u,v))
def sub(u,v): return tuple(a-b for a,b in zip(u,v))
def scale(t,u): return tuple(t*a for a in u)
def triple_sq(z):
    u,v=z
    return (dot(u,u), dot(v,v), dot(add(u,v),add(u,v)))


ONE, R3 = Q3(1), Q3(0,1)
A = ONE - R3*F(1,3)                   # 1 - 1/sqrt(3)
C = R3*F(2,3) - ONE                 # 2/sqrt(3) - 1
B = ONE + R3*F(1,2)
D = Q3(2) + R3
assert 2*A+C == ONE
assert A.real() > 0 and C.real() > 0
P11, P12 = A+C, C
# P^-1=[[B,-1/2],[-1/2,B]], checked without floating point.
assert P11*B - P12*F(1,2) == ONE
assert -P11*F(1,2) + P12*B == Q3()
assert 2*B == D
# For L(x,y)=(u_x+u_y,v_x-v_y), L P4^-1 L^* = D I2.
assert B+B == D
assert Q3(-F(1,2)) + Q3(F(1,2)) == Q3()

h=(ONE,Q3());k=(Q3(),ONE)
x=(sub(scale(B,h),scale(Q3(F(1,2)),k)),
   add(scale(Q3(-F(1,2)),h),scale(B,k)))
y=(add(scale(B,h),scale(Q3(F(1,2)),k)),
   sub(scale(Q3(-F(1,2)),h),scale(B,k)))
for value in triple_sq(x) + triple_sq(y):
    assert value == D, (value,D)
for pair, expected in ((tuple(add(u,v) for u,v in zip(x,y)),(D*D,ONE,(Q3(1)+R3)*(Q3(1)+R3))),
                       (tuple(sub(u,v) for u,v in zip(x,y)),(ONE,D*D,(Q3(1)+R3)*(Q3(1)+R3)))):
    assert triple_sq(pair) == expected
assert D.real()**2 > (1+sqrt(3))**2
assert D.real()/2 == B.real()

# Deterministic random tests in real Hilbert dimension 2, 3, and 7.
rng=Random(20260927)
tested=0
for dim in (2,3,7):
    for _ in range(3000):
        z=[tuple(rng.uniform(-2,2) for _ in range(dim)) for __ in range(4)]
        def real_norm_pair(u,v):
            return max(sum(t*t for t in u),sum(t*t for t in v),sum((t+s)**2 for t,s in zip(u,v)))
        u,v,s,t=z
        nx=real_norm_pair(u,v);ny=real_norm_pair(s,t)
        up=tuple(a+b for a,b in zip(u,s));vp=tuple(a+b for a,b in zip(v,t))
        um=tuple(a-b for a,b in zip(u,s));vm=tuple(a-b for a,b in zip(v,t))
        quotient=(real_norm_pair(up,vp)+real_norm_pair(um,vm))/(2*(nx+ny))
        assert quotient <= B.real()+1e-12, quotient
        tested += 1
print(f'PASS: exact Q(sqrt(3)) identities and {tested} finite-dimensional norm inequalities')
