"""Symbolic consistency checks for the 3-delay torus observation theorem.

These finite symbolic checks supplement the written topology and algebra proof.
"""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

m,p,q,r=sp.symbols('m p q r', integer=True)
A=sp.Matrix([[0,-2,0],[1,4,0],[0,0,m]])
k=sp.Matrix([[p,q,r]])
O=sp.Matrix.vstack(k,k*A,k*(A**2))
f=m*m-4*m+2
Q=-2*p*p+4*p*q-q*q
assert sp.factor(O.det()-r*f*Q)==0
assert sp.expand((A**3-(m+4)*A**2+(4*m+2)*A-2*m*sp.eye(3)))==sp.zeros(3,3)
assert sp.factor(A.charpoly().as_expr()-(sp.Symbol('lambda')**2-4*sp.Symbol('lambda')+2)*(sp.Symbol('lambda')-m))==0

for mm in range(2,20):
  Am=A.subs(m,mm)
  km=sp.Matrix([[0,1,1]])
  M=sp.Matrix.vstack(km,km*Am,km*Am**2)
  assert M.det()==-(mm*mm-4*mm+2)
  sm=smith_normal_form(M,domain=ZZ)
  assert sorted([abs(int(sm[i,i])) for i in range(3)])==sorted([1,1,abs(mm*mm-4*mm+2)])
  assert (abs(M.det())==1)==(mm==3)
  for pp in range(-3,4):
    for qq in range(-3,4):
      for rr in range(-2,3):
        kk=sp.Matrix([[pp,qq,rr]])
        Om=sp.Matrix.vstack(kk,kk*Am,kk*Am**2)
        assert Om.det()==rr*(mm*mm-4*mm+2)*(-2*pp*pp+4*pp*qq-qq*qq)
        assert Om.det()%(mm*mm-4*mm+2)==0
print('PASS: symbolic recurrence/determinant, Smith forms m=2..19, finite lattice range.')
