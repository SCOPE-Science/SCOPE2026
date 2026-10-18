#!/usr/bin/env python3
"""Exact algebraic checks for a four-dimensional signed mixed discriminant."""
import itertools
import sympy as s

ell=s.symbols('l1 l2 l3 l4')
w=lambda i,j: sum(ell[k] for k in range(4) if k not in (i,j))
W=s.Matrix(4,4,lambda i,j: 0 if i==j else w(i,j))
e1=sum(ell)
e3=sum(s.prod(ell[k] for k in range(4) if k!=i) for i in range(4))
e4=s.prod(ell)
assert s.expand(W.det()+4*(e1*e3-4*e4))==0

# Polarization via the exact determinant coefficient of t^2 r u:
a11,a22,a33,a44,a12,a13,a14,a23,a24,a34=s.symbols(
    'a11 a22 a33 a44 a12 a13 a14 a23 a24 a34')
A=s.Matrix([[a11,a12,a13,a14],[a12,a22,a23,a24],
            [a13,a23,a33,a34],[a14,a24,a34,a44]])
# Homogeneous 4th-degree determinant: two A, one Z, one I.
# Coefficient of t^2*r*u equals 4!/(2!*1!*1!)=12 times D(A,A,Z,I).
T,R,U=s.symbols('t r u')
poly=(T*A+R*s.diag(*ell)+U*s.eye(4)).det(method='domain-ge')
coefficient=s.Poly(s.expand(poly),T,R,U).coeff_monomial(T**2*R*U)
formula=sum(w(i,j)*(A[i,i]*A[j,j]-A[i,j]**2)
           for i,j in itertools.combinations(range(4),2))
assert s.expand(coefficient-formula)==0
# Since coeff=12 D, the Q formula is formula/12.

examples=[((-1,3,4,100),s.Integer(56528),s.Integer(-226112)),
          ((-1,1,2,3),s.Integer(-1),s.Integer(4))]
for zs,expectedE,expectedDet in examples:
    sub=dict(zip(ell,zs))
    assert (e1*e3-4*e4).subs(sub)==expectedE
    assert W.subs(sub).det()==expectedDet

zs=(-1,1,2,3)
sub=dict(zip(ell,zs))
Q=lambda M: s.expand(sum(w(i,j).subs(sub)*(M[i,i]*M[j,j]-M[i,j]**2)
                         for i,j in itertools.combinations(range(4),2))/12)
B=lambda X,Y:s.expand((Q(X+Y)-Q(X)-Q(Y))/2)
I=s.eye(4);H=s.diag(0,1,3,-4);t=s.Symbol('t')
assert Q(I)==s.Rational(5,4)
assert Q(H)==s.Rational(1,6)
assert B(I,H)==s.Rational(5,12)
assert s.expand(B(I+t*H,I)**2-Q(I+t*H)*Q(I))==-5*t**2/144
print('FOUR_DIMENSIONAL_MIXED_DISCRIMINANT_CERTIFICATE_OK')
