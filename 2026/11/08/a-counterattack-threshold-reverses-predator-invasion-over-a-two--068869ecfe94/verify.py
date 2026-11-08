#!/usr/bin/env python3
"""Exact rational certificate for invasion of a two-cycle in a juvenile/adult predator map.
Run: python3 verify.py. Requires Python standard library only.
"""
from fractions import Fraction as Q

class K:
    """Element a+b*sqrt(21) over Q; all arithmetic is exact."""
    def __init__(self,a=0,b=0): self.a,self.b=Q(a),Q(b)
    def __add__(self,o):
        o=asK(o); return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,o): return self+(-asK(o))
    def __rsub__(self,o): return asK(o)+(-self)
    def __mul__(self,o):
        o=asK(o); return K(self.a*o.a+21*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o):
        o=asK(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return f'({self.a})+({self.b})*sqrt(21)'

def asK(v): return v if isinstance(v,K) else K(v)
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def eye_minus(A): return [[K(int(i==j))-A[i][j] for j in range(2)] for i in range(2)]

xm=K(Q(21,22),-Q(1,22)); xp=K(Q(21,22),Q(1,22))
prey=lambda x: x+Q(11,5)*x*(1-x)
dprey=lambda x: 1+Q(11,5)*(1-2*x)
assert prey(xm)==xp and prey(xp)==xm
assert xm+xp==Q(21,11) and xm*xp==Q(105,121)
assert dprey(xm)*dprey(xp)==Q(4,25)
assert Q(7,10)<xm.a+4*xm.b and xm.a+5*xm.b<Q(6,5) # sqrt21 in (4,5)

B=Q(4,5); m=Q(4,5); gamma=Q(1,4)
def M(x,A,C): return [[1-B-A*x,C*x],[K(gamma),K(1-m)]]
def cycle(A,C): return mm(M(xp,A,C),M(xm,A,C))
def static_R(A,C): return Q(5,16)*C/(A+B)
def closed_det(A,C):
    return (-Q(504,605)*A*A+Q(504,1375)*A+Q(105,1936)*C*C
            +(Q(21,242)*A-Q(273,550))*C+Q(576,625))

# The determinant is a polynomial of total degree at most two in A,C:
# det(I-P) = 1-tr(P)+det(M(x+))det(M(x-)).
# Six unisolvent exact tests (0,0),(1,0),(2,0),(0,1),(0,2),(1,1)
# therefore prove that the displayed quadratic polynomial is identically correct.
for aa,cc in [(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]:
    assert det(eye_minus(cycle(Q(aa),Q(cc))))==closed_det(Q(aa),Q(cc))
for A in [Q(1,100),Q(2,35),Q(1,10)]:
    C0=Q(16,5)*(A+B)
    P=cycle(A,C0)
    assert det(eye_minus(P))==closed_det(A,C0)
    assert det(eye_minus(P))==(-Q(48,15125))*(35*A-2)
    assert static_R(A,C0)==1
    # All entries in M(x-) and M(x+) are positive for these values.
    for z in [xm,xp]:
        assert Q(1,5)-A*(z.a+5*abs(z.b))>0
    # P22<1 follows from x-<1 and C0*gamma=m*(A+B)<m.
    assert P[1][1]==K(Q(1,25))+K(gamma*C0)*xm

# Exact rational witnesses on OPPOSITE sides of the static threshold.
witnesses=[
 (Q(1,100),Q(13,5),Q(325,324),Q(21327,6050000),True),
 (Q(1,10),Q(287,100),Q(287,288),-Q(58119,19360000),False),
]
for A,C,R,D,suppressed in witnesses:
    P=cycle(A,C)
    assert static_R(A,C)==R
    assert det(eye_minus(P))==K(D)
    assert closed_det(A,C)==D
    # x-<1, C<3 imply 0<P22<1; positivity of product follows M>0.
    assert C<3 and A<Q(1,10)+Q(1,100)
    assert P[1][1]==K(Q(1,25))+K(gamma*C)*xm
    if suppressed: assert D>0 and R>1
    else: assert D<0 and R<1

# Sharp counterattack crossover at fixed static index 1.
assert -Q(48,15125)*(35*Q(2,35)-2)==0
assert Q(1,100)<Q(2,35)<Q(1,10)
print('VERIFY_OK: exact two-cycle, multiplier, Floquet determinants, counterattack crossover, two opposite invasion witnesses')
