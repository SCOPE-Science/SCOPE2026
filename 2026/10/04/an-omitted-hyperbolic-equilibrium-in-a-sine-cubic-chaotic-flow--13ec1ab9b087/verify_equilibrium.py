#!/usr/bin/env python3
from fractions import Fraction as Q
from math import factorial

class I:
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo, Q) else Q(lo)
        self.hi = self.lo if hi is None else (hi if isinstance(hi, Q) else Q(hi))
        assert self.lo <= self.hi
    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, other): return self + -(other if isinstance(other, I) else I(other))
    def __rsub__(self, other): return I(other) - self
    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        vals = (self.lo*other.lo, self.lo*other.hi, self.hi*other.lo, self.hi*other.hi)
        return I(min(vals), max(vals))
    __rmul__ = __mul__
    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        if n == 0: return I(1)
        if n & 1: return I(self.lo**n, self.hi**n)
        vals = (self.lo**n, self.hi**n)
        lo = Q(0) if self.lo <= 0 <= self.hi else min(vals)
        return I(lo, max(vals))

def sin_pos_point(t):
    assert Q(0) <= t <= Q(6,5)
    def s(m):
        out = Q(0)
        for k in range(m+1):
            out += (-1 if k & 1 else 1) * t**(2*k+1) / factorial(2*k+1)
        return out
    return s(11), s(10)  # lower, upper by alternating series

def sin_point(t):
    if t >= 0: return sin_pos_point(t)
    lo, hi = sin_pos_point(-t)
    return -hi, -lo

def cos_point(t):
    t = abs(t)
    assert t <= Q(6,5)
    def s(m):
        out = Q(0)
        for k in range(m+1):
            out += (-1 if k & 1 else 1) * t**(2*k) / factorial(2*k)
        return out
    return s(11), s(10)

def sinI(x):
    assert x.lo >= -Q(6,5) and x.hi <= Q(6,5)
    lo, _ = sin_point(x.lo)
    _, hi = sin_point(x.hi)
    return I(lo, hi)

def cosI(x):
    assert x.lo >= -Q(6,5) and x.hi <= Q(6,5)
    if x.lo >= 0:
        lo, _ = cos_point(x.hi); _, hi = cos_point(x.lo)
        return I(lo, hi)
    if x.hi <= 0:
        lo, _ = cos_point(x.lo); _, hi = cos_point(x.hi)
        return I(lo, hi)
    lo1, _ = cos_point(x.lo); lo2, _ = cos_point(x.hi)
    return I(min(lo1, lo2), Q(1))

p = [Q(991,250), Q(7), Q(7), Q(5), Q(9,2), Q(29,10), Q(1)]
A = [
    [Q(10175,10**6), Q(-90707,10**6), Q(-63282,10**6)],
    [Q(126889,10**6), Q(-119762,10**6), Q(217899,10**6)],
    [Q(68180,10**6), Q(-75210,10**6), Q(586802,10**6)],
]
c = [Q(1003723,10**6), Q(747237,10**6), Q(-393482,10**6)]
r = Q(1,1000)

def F(x,y,z):
    p1,p2,p3,p4,p5,p6,p7 = p
    return [
        -p1*x**3 + p2*y**3 + p3*x*z**2,
        p4*sinI(x*y-z) - p5*x**3,
        p6*sinI(x*y*z) + p7*sinI(x),
    ]

def G(x,y,z):
    f = F(x,y,z)
    return [sum((I(A[i][j])*f[j] for j in range(3)), I(0)) for i in range(3)]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def face_worst(i, sign, N=10):
    other = [j for j in range(3) if j != i]
    worst = None
    for a in range(N):
        for b in range(N):
            v = [None,None,None]
            v[i] = I(c[i] + sign*r)
            for qidx,k in enumerate(other):
                q = a if qidx == 0 else b
                lo = c[k] - r + Q(2*r*q, N)
                hi = c[k] - r + Q(2*r*(q+1), N)
                v[k] = I(lo,hi)
            gi = G(*v)[i]
            candidate = gi.hi if sign < 0 else gi.lo
            if worst is None or (candidate > worst if sign < 0 else candidate < worst):
                worst = candidate
            assert gi.hi < 0 if sign < 0 else gi.lo > 0
    return worst

def J(x,y,z):
    p1,p2,p3,p4,p5,p6,p7 = p
    c1, c2 = cosI(x*y-z), cosI(x*y*z)
    return [
      [-3*p1*x**2+p3*z**2, 3*p2*y**2, 2*p3*x*z],
      [p4*c1*y-3*p5*x**2, p4*c1*x, -p4*c1],
      [p6*c2*y*z+p7*cosI(x), p6*c2*x*z, p6*c2*x*y],
    ]

def coeffs(x,y,z):
    M=J(x,y,z)
    tr=M[0][0]+M[1][1]+M[2][2]
    a1=-tr
    a2=(M[0][0]*M[1][1]-M[0][1]*M[1][0]
       +M[0][0]*M[2][2]-M[0][2]*M[2][0]
       +M[1][1]*M[2][2]-M[1][2]*M[2][1])
    return a1,a2,-det3(M)

def dec(q, digits=15):
    return f"{float(q):.{digits}g}"

detA = det3(A)
assert detA == Q(1236309158097179,250000000000000000)
assert detA != 0
face = {(i,s):face_worst(i,s) for i in range(3) for s in (-1,1)}
B=[I(c[j]-r,c[j]+r) for j in range(3)]
a1,a2,a3=coeffs(*B)
assert a1.lo > 0 and a2.lo > 0 and a3.hi < 0
print("detA", detA)
for i in range(3):
    print("face", i+1, "lower_max", dec(face[(i,-1)]), "upper_min", dec(face[(i,1)]))
print("a1", dec(a1.lo), dec(a1.hi))
print("a2", dec(a2.lo), dec(a2.hi))
print("a3", dec(a3.lo), dec(a3.hi))
print("VERIFY_OK")
