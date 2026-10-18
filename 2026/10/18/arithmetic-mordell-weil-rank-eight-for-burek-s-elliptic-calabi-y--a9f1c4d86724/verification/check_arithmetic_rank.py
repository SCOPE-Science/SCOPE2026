#!/usr/bin/env python3
"""Exact arithmetic descent check for Burek's elliptic curve, arXiv:2610.01276.

Requires Python 3 and SymPy. Execute from any directory; the cross-pairing
certificate is read relative to this script. All matrix arithmetic is exact.
"""
import json
from pathlib import Path
import sympy as s
v,t=s.symbols('v t'); u=s.symbols('u'); I=s.I
A=lambda z:z**8+14*z**4+1
B=lambda z:z*(z**4-1)
C=lambda z:z**12-33*z**8-33*z**4+1
as_=[-18*(1+I)*(u*v+I),18*(1+I)*(u*v+I),18*(1-I)*(u*v-I),18*(1-I)*(u+I*v),-18*(1+I)*(u-I*v),0]
b1=-3*(5*u**4*v**4-u**4-v**4+24*I*u**3*v**3-24*u**2*v**2-24*I*u*v+5)
b3=-3*(5*u**4*v**4-u**4-v**4-24*I*u**3*v**3-24*u**2*v**2+24*I*u*v+5)
b4=3*(u**4*v**4-5*u**4-5*v**4-24*I*u**3*v+24*u**2*v**2+24*I*u*v**3+1)
b5=3*(u**4*v**4-5*u**4-5*v**4+24*I*u**3*v+24*u**2*v**2-24*I*u*v**3+1)
b6=3*(u**4*v**4+u**4+v**4+6*u**4*v**2+6*u**2*v**4-12*u**2*v**2+6*u**2+6*v**2+1)
bs_=[b1,b1,b3,b4,b5,b6]
# polynomials x=t**2*(a*(gamma*t+delta/t)+b), y=t**3*(54*z**2+c*z+d)
sections=[]
for uv in (2,2*I):
 for a0,b0 in zip(as_,bs_):
  a=s.expand(s.sympify(a0).subs(u,uv)); b=s.expand(b0.subs(u,uv)); gamma=s.expand(B(uv)); delta=B(v);m=s.expand(gamma*delta)
  c=s.expand(a**3/108);d=s.expand((3*a*a*b-11664*m-c*c)/108);
  z=gamma*t+delta/t
  x=s.expand(t**2*(a*z+b));y=s.expand(t**3*(54*z*z+c*z+d));
  sections.append((s.simplify(x),s.simplify(y)))

# Symbolic Weierstrass identities for all twelve source sections.
rhs_coeff=lambda xx:xx**3-27*481*A(v)*t**4*xx+2916*(B(2)**4*t**10+B(v)**4*t**2)+54*(-4879)*C(v)*t**6
assert len(sections)==12
for xx,yy in sections:
 assert s.expand(yy*yy-rhs_coeff(xx))==0

def specialize(v0):
 S=[]
 for idx,(x,y) in enumerate(sections):
  S.append((s.Poly(x.subs(v,v0),t,extension=I),s.Poly(y.subs(v,v0),t,extension=I),1 if idx<6 else -1))
 return S
def conjugate_sections(S):
 return [(s.Poly(s.conjugate(x.as_expr()).subs({s.conjugate(t):t}),t,extension=I),
          s.Poly(s.conjugate(y.as_expr()).subs({s.conjugate(t):t}),t,extension=I),grp)
         for x,y,grp in S]
def ord0(p):
 if p.is_zero:return 1000
 return min(k[0] for k,x in p.terms())
def height(P,Q):
 xp,yp,gp=P;xq,yq,gq=Q
 if xp==xq and yp==yq:return s.Rational(8,3)
 xx=xp-xq;yy=yp-yq
 g=s.gcd(xx, yy) if not (xx.is_zero and yy.is_zero) else s.Poly(1,t)
 away=g.degree()-ord0(g)
 at0=max(0,ord0(xx)-1)
 # change x∞ = r4*x(1/r), leading exponent from degree of xdiff: 4-deg(xdiff)
 atinfty=max(0, 4-xx.degree()-1) if gp==gq else 0
 intr=away+at0+atinfty
 return 2-intr-s.Rational(2,3)-(s.Rational(2,3) if gp==gq else s.Rational(1,3))

# Source Appendix A matrix, included as a check on the intersection algorithm.
M=s.Matrix([[8,-4,2,2,2,2],[-4,8,2,2,2,2],[2,2,8,2,2,2],[2,2,2,8,2,2],[2,2,2,2,8,2],[2,2,2,2,2,8]])
N=s.Matrix([[3,-3,-3,0,0,0],[-3,3,3,0,0,0],[3,-3,3,0,0,0],[0,0,0,3,3,0],[0,0,0,-3,3,0],[0,0,0,0,0,0]])
H_ref=M.row_join(N).col_join(N.T.row_join(M))/3
certificate=json.loads((Path(__file__).resolve().parent/'cross_pairing.json').read_text())
G_ref=s.Matrix(certificate['three_times_cross_pairing'])/3
assert G_ref.shape==(12,12) and G_ref==G_ref.T

def run_at(v0):
 S=specialize(v0)
 CS=conjugate_sections(S)
 H=s.Matrix(12,12,lambda i,j:height(S[i],S[j]))
 G=s.Matrix(12,12,lambda i,j:height(S[i],CS[j]))
 assert H==H_ref,('source height mismatch',v0)
 assert G==G_ref,('conjugate cross pairing mismatch',v0)
 plus=2*(H+G)
 minus=2*(H-G)
 ap=[j-1 for j in certificate['plus_minor_indices_one_based']]
 am=[j-1 for j in certificate['minus_minor_indices_one_based']]
 dplus=plus.extract(ap,ap).det()
 dminus=minus.extract(am,am).det()
 assert dplus==s.Rational(16777216,9)
 assert dminus==256
 assert plus.rank()==8 and minus.rank()==4
 assert H.det()==s.Rational(4096,9)
 # This is an additional algebraic check, not needed for the rank deduction.
 T=H.inv()*G
 assert T*T==s.eye(12)
 assert s.factor(T.charpoly().as_expr())==(T.charpoly().gen-1)**8*(T.charpoly().gen+1)**4
 return T
T=run_at(5)
assert run_at(7)==T

# Independent exact group-law comparison at three non-singular point evaluations:
# corroborates that the cross-height matrix encodes the Galois involution.
def field_value(z):return s.expand_complex(z).expand()
def check_group_action(v0,t0):
 acoef=-27*481*A(v0)*t0**4
 def add(P,Q):
  if P is None:return Q
  if Q is None:return P
  x1,y1=P; x2,y2=Q
  if field_value(x1-x2)==0:
   if field_value(y1+y2)==0:return None
   slope=field_value((3*x1*x1+acoef)/(2*y1))
  else:slope=field_value((y2-y1)/(x2-x1))
  x3=field_value(slope*slope-x1-x2)
  y3=field_value(slope*(x1-x3)-y1)
  return x3,y3
 def mul(n,P):
  if n<0:return mul(-n,(P[0],-P[1]))
  acc=None
  while n:
   if n&1:acc=add(acc,P)
   P=add(P,P);n//=2
  return acc
 pts=[(field_value(x.subs({v:v0,t:t0})),field_value(y.subs({v:v0,t:t0}))) for x,y in sections]
 for j in range(12):
  acc=None
  for i in range(12):
   if T[i,j]:acc=add(acc,mul(int(T[i,j]),pts[i]))
  assert acc is not None
  conj=(field_value(s.conjugate(pts[j][0])),field_value(s.conjugate(pts[j][1])))
  assert field_value(acc[0]-conj[0])==0
  assert field_value(acc[1]-conj[1])==0
for v0,t0 in ((5,2),(7,2),(5,3)):
 check_group_action(v0,t0)
print('PASS: twelve symbolic section identities')
print('PASS: specialized height matrix matches originating Appendix A at v=5,7')
print('PASS: 12 x 12 conjugate cross-height certificate independently recomputed at v=5,7')
print('PASS: trace Gram 8x8 determinant 16777216/9; anti-trace 4x4 determinant 256')
print('PASS: trace rank eight and anti-trace rank four; geometric rank bound twelve')
print('PASS: direct point group-law conjugation action at (v,t)=(5,2),(7,2),(5,3)')
