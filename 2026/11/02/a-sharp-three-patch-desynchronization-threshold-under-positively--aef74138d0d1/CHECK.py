#!/usr/bin/env python3
"""Exact polynomial replay of a three-patch stationary covariance claim.

Pure Python 3, standard library only. Run: python3 CHECK.py
"""
from fractions import Fraction as F
from math import sqrt


def poly(*coeffs):
    a = tuple(F(c) for c in coeffs)
    while len(a) > 1 and a[-1] == 0:
        a = a[:-1]
    return a or (F(0),)


def plus(a, b):
    return poly(*( (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                    for i in range(max(len(a), len(b))) ))


def neg(a):
    return poly(*(-x for x in a))


def times(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai * bj
    return poly(*c)


def diff(a):
    return poly(*(i*a[i] for i in range(1, len(a))))


def at(a, x):
    y = F(0)
    for c in reversed(a):
        y = y*x + c
    return y


ONE = poly(1)
ZERO = poly(0)
T = poly(0, 1)


def scalar(c):
    return poly(F(c))


def pp(*factors):
    out = ONE
    for f in factors:
        out = times(out, f)
    return out


class Rat:
    def __init__(self, n, d=ONE):
        self.n = n
        self.d = d
        if d == ZERO:
            raise ZeroDivisionError

    def __add__(self, other):
        other = other if isinstance(other, Rat) else Rat(scalar(other))
        return Rat(plus(times(self.n, other.d),times(other.n, self.d)),times(self.d,other.d))

    def __radd__(self, other):
        return self + other

    def __truediv__(self, other):
        other = other if isinstance(other, Rat) else Rat(scalar(other))
        return Rat(times(self.n,other.d),times(self.d,other.n))

    def __neg__(self):
        return Rat(neg(self.n), self.d)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, Rat) else Rat(scalar(other))
        return Rat(times(self.n,other.n),times(self.d,other.d))

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        other = other if isinstance(other, Rat) else Rat(scalar(other))
        return times(self.n, other.d) == times(other.n, self.d)

    def eval(self, x):
        return at(self.n,x)/at(self.d,x)


m1=poly(1,1)
m2=poly(2,1)
two_m1=poly(1,2)
three_m1=poly(1,3)
three_m2=poly(2,3)
D=pp(m1,m2,two_m1,three_m1,three_m2)
Dmid=pp(m2,two_m1,three_m1,three_m2)
Dend=pp(m1,three_m1,three_m2)
Dcenter=pp(three_m1,three_m2)
P_A=poly(36,268,759,1031,763,278)
P_C=poly(276,1948,4899,5351,2383,278)
P_B=poly(40,188,268,139)
P_12=poly(16,156,464,601,278)
P_22=poly(10,41,139)
P_23=poly(16,276,1004,1141,278)
S=[[None]*3 for _ in range(3)]
for i,j,r in [
    (0,0,Rat(P_A,times(poly(8),D))),
    (0,1,Rat(P_12,times(poly(8),Dmid))),
    (0,2,Rat(P_B,times(poly(8),Dend))),
    (1,1,Rat(P_22,times(poly(8),Dcenter))),
    (1,2,Rat(P_23,times(poly(8),Dmid))),
    (2,2,Rat(P_C,times(poly(8),D)))]:
    S[i][j]=S[j][i]=r

L=((1,-1,0),(-1,2,-1),(0,-1,1))
Q=((F(9,4),F(1),F(5)),
   (F(1),F(5,4),F(1)),
   (F(5),F(1),F(69,4)))
A=[[Rat(plus(poly(int(i==j)),poly(0,L[i][j]))) for j in range(3)] for i in range(3)]

symbolic=0
for i in range(3):
    for j in range(i,3):
        lhs=sum((A[i][k]*S[k][j]+S[i][k]*A[j][k] for k in range(3)), Rat(ZERO))
        assert lhs == Rat(scalar(Q[i][j])), (i,j)
        symbolic+=1

# The Pearson-correlation rational form is K/sqrt(P_A P_C).
K=pp(m2,two_m1,P_B)
assert (S[0][2]*S[0][2]) == Rat(times(K,K),times(P_A,P_C)) * S[0][0]*S[2][2]
symbolic+=1

# Derivative sign polynomial for K/sqrt(P_A P_C).
N=plus(times(poly(2),pp(diff(K),P_A,P_C)),
       neg(plus(pp(K,diff(P_A),P_C),pp(K,P_A,diff(P_C)))))
P_expected=poly(-40704,-212480,3518496,45433888,238288032,722717640,
                1402044574,1824837840,1671621225,1185727765,
                743643377,406303950,152176644,26431128)
assert N == times(poly(2),P_expected)
assert P_expected[0] < 0 and P_expected[1] < 0
assert all(z>0 for z in P_expected[2:])
# Descartes' sign rule, with opposite endpoint signs, gives one positive zero.
assert at(P_expected,F(7967,100000))<0
assert at(P_expected,F(7968,100000))>0
symbolic+=5

# Exact derivative at zero for the full diagonal-noise family.
# Set gamma=1; rescaling m by gamma gives the general formula.
delta=Rat(T)
a=Rat(poly(2,1)); c=Rat(poly(17,1))
s11_prime=-(Rat(poly(1,1)))/2
s33_prime=-(Rat(poly(16,1)))/2
s13_prime=Rat(poly(-2))
raw_slope=2*s13_prime-Rat(poly(5))*(s11_prime/(a*Rat(poly(F(1,2))))+s33_prime/(c*Rat(poly(F(1,2)))))*Rat(poly(F(1,2)))
expected=Rat(poly(-27,28,2),times(poly(2),times(poly(2,1),poly(17,1))))
assert raw_slope == expected
symbolic+=1

# Independent exact finite-rate numerical calculations, for reporting only.
samples=0
for u in [F(0),F(1,100),F(1,10),F(1,4),F(1,2),F(1),F(10),F(100)]:
    s11,s13,s33=(S[i][j].eval(u) for i,j in [(0,0),(0,2),(2,2)])
    r=float(s13)/sqrt(float(s11*s33))
    assert 0<r<1
    assert abs(r-(float(at(K,u))/sqrt(float(at(P_A,u)*at(P_C,u)))))<1e-12
    samples+=2

# The general initial-slope rule for the three-site chain follows from the
# Lyapunov derivative at m=0: S'(0)=-(LQ+QL)/(4 gamma^2).
for delta in [F(0),F(1,4),F(1),F(4)]:
    q11,q33=F(2)+delta,F(17)+delta
    numer=2*delta*delta+28*delta-27
    local=2-F(5)/q11-F(5)/q33
    assert local == numer/(q11*q33)
    assert (local<0)==(numer<0)
    samples+=2

print('VERIFY_OK symbolic_identities=%d exact_sample_checks=%d' % (symbolic,samples))
print('unique_minimum_interval=(0.07967, 0.07968) in m/gamma units')
