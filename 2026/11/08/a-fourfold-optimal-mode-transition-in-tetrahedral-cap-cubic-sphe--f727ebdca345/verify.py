"""Exact symbolic and independent quadrature checks for the tetrahedral cubic Slepian spectrum."""
import sympy as s
import numpy as np
from math import sqrt, pi, cos, sin
u,c,R,T,H=s.symbols('u c R T H',real=True)
x=u/s.sqrt(3)+R*(T/s.sqrt(2)+H/s.sqrt(6))
y=u/s.sqrt(3)+R*(-T/s.sqrt(2)+H/s.sqrt(6))
z=u/s.sqrt(3)-R*2*H/s.sqrt(6)
poly={'A':x*y*z,'B':x*(5*x*x-3*(x*x+y*y+z*z)),'C':x*(y*y-z*z)}
norm={'A':s.Rational(1,105),'B':s.Rational(4,7),'C':s.Rational(4,105)}
def cm(a,b):
 if a%2 or b%2:return s.S.Zero
 i,j=a//2,b//2
 return s.Rational(s.factorial(2*i)*s.factorial(2*j),2**(2*i+2*j)*s.factorial(i)*s.factorial(j)*s.factorial(i+j))
vals={}
for k,p in poly.items():
 v=s.S.Zero
 for (a,b,r,t),co in s.Poly(s.expand(p*p),T,H,R,u).terms():
  if a%2 or b%2:continue
  assert r%2==0
  v+=co*cm(a,b)*u**t*(1-u*u)**(r//2)
 vals[k]=s.factor(s.Rational(2)*s.integrate(v,(u,c,1))/norm[k])
La=2-s.Rational(35,18)*c-s.Rational(35,9)*c**3+s.Rational(21,2)*c**5-s.Rational(20,3)*c**7
Lb=2-s.Rational(119,108)*c-s.Rational(245,54)*c**3+s.Rational(77,12)*c**5-s.Rational(25,9)*c**7
Lc=2-s.Rational(35,12)*c+s.Rational(35,6)*c**3-s.Rational(119,12)*c**5+5*c**7
for k,v in zip(['A','B','C'],[La,Lb,Lc]):assert s.simplify(vals[k]-v)==0
assert s.factor(La-Lc)==-s.Rational(35,36)*c*(c-1)*(c+1)*(12*c**4-9*c**2+1)
assert s.factor(La-Lb)==-s.Rational(7,108)*c*(c-1)*(c+1)*(60*c**4-3*c**2-13)
assert s.factor(Lb-Lc)==-s.Rational(7,27)*c*(c-1)*(c+1)*(30*c**4-33*c**2+7)
assert s.simplify(La+3*Lb+3*Lc-14*(1-c))==0
critical=s.sqrt((s.Integer(9)+s.sqrt(33))/24)
assert s.simplify((La-Lc).subs(c,critical))==0
assert s.N(Lc.subs(c,s.Rational(3,5)))>s.N(La.subs(c,s.Rational(3,5)))
assert s.N(La.subs(c,s.Rational(9,10)))>s.N(Lc.subs(c,s.Rational(9,10)))
vertices=np.array([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)],float)/sqrt(3)
def basis(x):
 X,Y,Z=x
 return np.array([sqrt(105)*X*Y*Z]+[sqrt(7/4)*q*(5*q*q-3) for q in (X,Y,Z)]+[sqrt(105/4)*X*(Y*Y-Z*Z),sqrt(105/4)*Y*(Z*Z-X*X),sqrt(105/4)*Z*(X*X-Y*Y)])
def matrix(C):
 nodes,weights=np.polynomial.legendre.leggauss(8)
 nodes=C+(nodes+1)*(1-C)/2;weights=weights*(1-C)/2
 G=np.zeros((7,7))
 for v in vertices:
  q=np.array([1.,0.,0.]);e=q-v*np.dot(q,v);e/=np.linalg.norm(e)
  f=np.cross(v,e)
  for U,W in zip(nodes,weights):
   for j in range(32):
    ph=2*pi*j/32
    xx=U*v+sqrt(1-U*U)*(cos(ph)*e+sin(ph)*f)
    h=basis(xx)
    G+=(W/64.)*np.outer(h,h)
 return G
for C in (.60,.72,float(critical),.85,.95):
 G=matrix(C)
 ref=np.diag([float(La.subs(c,C))]+[float(Lb.subs(c,C))]*3+[float(Lc.subs(c,C))]*3)
 assert np.max(np.abs(G-ref))<6e-13,(C,np.max(np.abs(G-ref)))
 assert abs(np.trace(G)-14*(1-C))<6e-13
print('TETRA_CUBIC_SLEPIAN_PASS symbolic_eigenbranches=3 symbolic_differences=3 quadrature_radii=5 dimensions=1+3+3 transition='+str(float(critical)))
