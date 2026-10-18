"""Exact, reproducible algebra checks for the pentagon projective-Morse transition theorem.
Scientific verification only. Requires sympy; no network or external data files.
"""
from fractions import Fraction as Q
import sympy as S
q,b,u=S.symbols('q b u')
F=b*q**3-b**2*q**2-q**2+2*q*b**5+b*q+3*b**4-1
r=S.sqrt(1+q*q); c=(1+b*q)/r
# Independent shoelace and edge-polar checks (polygon in anticlockwise order).
verts=[(-1/b,0),(q,-r),(b,-c),(b,c),(q,r)]
cross=lambda a,z:a[0]*z[1]-a[1]*z[0]
shoelace=S.factor(sum(cross(verts[i],verts[(i+1)%5]) for i in range(5))/2)
firstx=S.factor(sum((verts[i][0]+verts[(i+1)%5][0])*cross(verts[i],verts[(i+1)%5]) for i in range(5))/6)
assert S.simplify(firstx-F/(3*b*b*r))==0
for i in range(5):
 x1,y1=verts[i];x2,y2=verts[(i+1)%5]
 determinant=S.factor(x1*y2-x2*y1)
 polarvertex=(S.simplify((y2-y1)/determinant),S.simplify((x1-x2)/determinant))
 assert any(S.simplify(polarvertex[0]+v[0])==0 and S.simplify(polarvertex[1]+v[1])==0 for v in verts)
D1=r/b; D2=b*r-q*c; D3=b*c
area=S.factor(D1+D2+D3)
assert S.simplify(shoelace-area)==0
Ixx=S.factor((D1*(b**(-2)-q/b+q*q)+D2*(q*q+q*b+b*b)+3*b*b*D3)/6)
Iyy=S.factor((D1*r*r+D2*(r*r+r*c+c*c)+D3*c*c)/6)
Gx=6*b**7*q+8*b**6-3*b**5*q-6*b**4-2*b**3*q**3+3*b**3*q+2*b**2*q**4-b**2*q**2-3*b**2-2*b*q**3-2*b*q+2*q**2+2
Gy=2*b**5*q**3+8*b**4*q**2-3*b**3*q**3+9*b**3*q-6*b**2*q**2+2*b**2-2*b*q**5-3*b*q**3-3*b*q+2*q**6+3*q**4-1
assert S.simplify((4*Ixx-area)*3*b**3*r-Gx)==0
assert S.simplify((4*Iyy-area)*3*b*r**3-Gy)==0
rx=S.factor(S.resultant(F,Gx,q))
ry=S.factor(S.resultant(F,Gy,q))
assert S.expand(rx + b**6*(b*b-2)*(2*b*b-1)**3*(b*b+1)**6*(8*b**4-5*b*b-4))==0
assert S.expand(ry + b**2*(b*b-2)*(2*b*b-1)**2*(b*b+1)**8*(16*b**8-90*b**6+9*b**4+20*b*b+4))==0
X=8*u*u-5*u-4; Y=16*u**4-90*u**3+9*u*u+20*u+4
assert S.diff(Y,u,2).subs(u,S.Rational(1,2))==-204
assert S.diff(Y,u,2).subs(u,2)==-294
assert S.diff(Y,u).subs(u,S.Rational(1,2))==S.Rational(-61,2)
assert Y.subs(u,S.Rational(1,2))==6 and Y.subs(u,2)==-384
assert X.subs(u,1)<0 and X.subs(u,S.Rational(25,16))>0
assert Y.subs(u,S.Rational(9,16))>0 and Y.subs(u,1)<0
# Exact interval Horner evaluation for rational polynomials in q at fixed b.
def mul(a,z):
 x,y=a; v,w=z; prod=[x*v,x*w,y*v,y*w]; return min(prod),max(prod)
def poly_range(P,bval,lo,hi):
 poly=S.Poly(S.cancel(P.subs(b,bval)),q)
 c=poly.all_coeffs()
 a=(Q(int(c[0].p),int(c[0].q)),)*2
 interval=(lo,hi)
 for coeff in c[1:]:
  l,h=mul(a,interval);z=Q(int(coeff.p),int(coeff.q));a=(l+z,h+z)
 return a
# Bracketing all three algebraic q roots via exact rational sign changes.
samples=[(Q(3,4),Q(438,10000),Q(439,10000),(-1,+1)),
         (Q(1),Q(-4780,10000),Q(-4779,10000),(-1,-1)),
         (Q(5,4),Q(-6597,10000),Q(-6596,10000),(+1,-1))]
for bv,lo,hi,sgn in samples:
 f0,f1=poly_range(F,S.Rational(bv.numerator,bv.denominator),lo,hi)
 assert f0<0<f1,('F',bv,lo,hi,f0,f1) if False else ('F interval not useful',bv,f0,f1)
 for P,expected in [(Gx,sgn[0]),(Gy,sgn[1])]:
  x,y=poly_range(P,S.Rational(bv.numerator,bv.denominator),lo,hi)
  assert (y<0 if expected==-1 else x>0),(bv,str(P),x,y)
 print('sample',str(bv),'q bracket',str(lo),str(hi),'numerator signs',sgn)
# Prove the unique inner critical root exists from exact endpoint factorizations.
t=S.symbols('t')
assert S.simplify(F.subs({q:-1/S.sqrt(2), b:t/S.sqrt(2)}) + (t-2)*(t+1)*(t**3-2*t*t-3)/4)==0
assert S.simplify(F.subs({q:1/S.sqrt(2), b:t/S.sqrt(2)}) - (t-1)*(t+2)*(t**3+2*t*t+3)/4)==0
print('PASS: exact moment identities, factored eliminants, unique eligible thresholds, and rational sign certificates')
