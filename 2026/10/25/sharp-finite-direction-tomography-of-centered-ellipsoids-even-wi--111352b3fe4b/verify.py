#!/usr/bin/env python3
"""Exact illustrations of central-section inversion and ambiguity.
Run: python verify.py  (requires sympy).
These finite checks do not replace the all-dimensional proof.
"""
import sympy as s

# Rational 3D centered ellipsoid and six canonical projective directions.
Q=s.Matrix([[7,1,2],[1,9,-1],[2,-1,5]])
assert Q.is_positive_definite
d=s.factor(Q.det())
n=3
normals=[s.eye(3).col(i) for i in range(n)]
normals += [(s.eye(3).col(i)+s.eye(3).col(j))/s.sqrt(2)
            for i in range(n) for j in range(i+1,n)]
# Central section data, divided by known unit-ball factor, have squares d/q.
q=[s.factor((u.T*Q*u)[0]) for u in normals]
normalized_section_squares=[d/x for x in q]
hvals=[1/x for x in normalized_section_squares]
H=s.zeros(3)
for i in range(3): H[i,i]=hvals[i]
k=3
for i in range(3):
 for j in range(i+1,3):
  H[i,j]=H[j,i]=s.factor(hvals[k]-(H[i,i]+H[j,j])/2)
  k+=1
D_rec=s.det(H)**s.Rational(-1,2)
assert s.simplify(D_rec-d)==0
assert Q==s.simplify(D_rec)*H
print('3D central inversion: exact PASS')

# Two directions in 2D are insufficient despite equal determinant and full profiles.
T=s.Matrix([[0,1],[1,-2]])
z_minus=-1-s.sqrt(6)/2
z_plus=-1+s.sqrt(6)/2
Qminus=s.eye(2)+z_minus*T
Qplus=s.eye(2)+z_plus*T
assert Qminus.is_positive_definite and Qplus.is_positive_definite
assert Qminus!=Qplus
assert s.simplify(Qminus.det()-s.Rational(1,2))==0
assert s.simplify(Qplus.det()-s.Rational(1,2))==0
v=s.Matrix([1/s.sqrt(2),1/s.sqrt(2)])
for u in [s.Matrix([1,0]),v]:
 assert s.simplify((u.T*Qminus*u)[0]-1)==0
 assert s.simplify((u.T*Qplus*u)[0]-1)==0
print('2D equal-volume all-offset ambiguity: exact PASS')

q,t,n=s.symbols('q t n',positive=True)
F=(q-t**2)**((n-1)/2)/q**(n/2)
assert s.simplify((n-1)/(2*(q-t**2))-n/(2*q)-(n*t**2-q)/(2*q*(q-t**2)))==0
print('Single-height derivative identity: symbolic PASS')
