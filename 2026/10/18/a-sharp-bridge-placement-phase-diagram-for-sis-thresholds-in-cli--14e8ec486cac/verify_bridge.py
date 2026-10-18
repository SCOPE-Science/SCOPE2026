#!/usr/bin/env python3
"""Reproducible symbolic checks for a weighted community-bridge SIS threshold.

Requirements: Python 3 and SymPy. Run: python verify_bridge.py
All finite values are computed with exact integer/rational arithmetic.
"""
import sympy as s
z,k=s.symbols('z k')
P=z**4-3*z**3-(k+5)*z**2+(3*k+3)*z+4*k
ra=(z-3)*(z*z-k)/P
rh=z*(z-4)*(z+1)/P
rl=1/z+rh/z**2
# Four-class elimination gives the same quotient determinant and Green entries.
Q=s.Matrix([[z,-4,-1,0],[-1,z-3,0,0],[-1,0,z,-k],[0,0,-1,z]])
assert s.factor(Q.det()-P)==0
assert s.factor(ra-rh-((4-k)*z+3*k)/P)==0
assert s.factor(ra-rl-4*(z*z-k+1)/(z*P))==0
assert s.factor(rh-rl-(k*(z-4)*(z+1)+4)/(z*P))==0
# The other-clique diagonal derives from the K5 rank-one update.
q=(z-4)*(z+1);d=(z-3)/q;o=1/q;t=z/(z*z-k)
rb=d+t*o**2/(1-t*d)
assert s.factor(ra-rb-z*(z-2)/((z+1)*P))==0
assert s.factor(P.subs(z,4)+4)==0
assert s.factor(s.diff(P,z).subs(z,4)-5*(15-k))==0
assert s.factor(s.diff(P,z,2).subs(z,4)-2*(55-k))==0
xc=3*k/(k-4)
Pxc=s.factor(4*k*(k*k-20*k+28)*(k*k-14*k+4)/(k-4)**4)
assert s.factor(P.subs(z,xc)-Pxc)==0
w2=s.factor((P*(z*z-1)/(z*(z-3)*(z*z-k))).subs(z,xc))
for j in range(5,14):
 assert s.factor(Pxc.subs(k,j))>0
 assert s.factor(w2.subs(k,j))>0
for j in (14,15): assert s.factor(Pxc.subs(k,j))<0
assert s.factor(w2.subs(k,7)-40)==0
# Independently instantiate the actual 13-by-13 graph, solve rational
# systems, and compare matrix Green diagonals for four inequivalent vertices.
N=13
A=s.zeros(N)
for i in range(5):
 for j in range(i+1,5): A[i,j]=A[j,i]=1
A[0,5]=A[5,0]=1
for i in range(6,13): A[5,i]=A[i,5]=1
assert A.rows==13 and sum(int(A[5,i]) for i in range(13))==8
assert s.factor(A.charpoly(z).as_expr()-z**6*(z+1)**3*P.subs(k,7))==0
for zz in (s.Rational(9,2),s.Rational(5),s.Rational(7),s.Rational(8)):
 M=zz*s.eye(N)-A
 for v,expr in ((0,ra),(1,rb),(5,rh),(6,rl)):
  col=s.zeros(N,1);col[v]=1
  got=M.inv().row(v)[v] if False else M.LUsolve(col)[v]
  expect=s.factor(expr.subs({k:7,z:zz}))
  assert s.factor(got-expect)==0,(zz,v,got,expect)
# Exact rational sign certificates and direct full-matrix checks at each example.
gstar=z/(z*z-1)
expect={
 (6,0,s.Rational(1000,149)):s.Rational(161921311387069,30945671139799931),
 (6,5,s.Rational(1000,149)):-s.Rational(75260970757,80798096970757),
 (7,0,s.Rational(2000,263)):-s.Rational(10771563216311279,2415836082953935779),
 (7,5,s.Rational(2000,263)):s.Rational(3475861420267,1067536934579733),
}
for (ww,v,zz),right in expect.items():
 gg={0:ra,5:rh}[v]
 val=s.cancel(ww*ww*gg.subs({k:7,z:zz})*gstar.subs(z,zz)-1)
 assert val==right
 B=s.zeros(15);B[:13,:13]=A;B[13,14]=B[14,13]=1;B[v,13]=B[13,v]=ww
 assert B==B.T
 # Block determinant identity: exact full graph spectral certificate.
 detfull=(zz*s.eye(15)-B).det(method='domain-ge')
 detfree=(zz*s.eye(13)-A).det(method='domain-ge')*(zz*zz-1)
 assert s.factor(detfull/detfree+val)==0
 assert s.sign(detfull)==-s.sign(val)
print('VERIFY_OK: quotient, 13x13 exact Green entries, family threshold, and four 15x15 determinant signs')
