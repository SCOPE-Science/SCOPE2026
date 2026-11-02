import sympy as s,itertools
L=s.symbols('L',real=True); W=s.symbols('W',positive=True)
a=s.Rational(3,16); H=s.Rational(3,4)*L-s.Rational(23,32); tau=H/a
T=s.Matrix([[1,0],[1,-W/a]]); Ti=T.inv(); z1=[-s.Rational(3,8), L+s.Rational(3,8)]
z2=[[0,s.Rational(3,4)],[s.Rational(3,4),-s.Rational(9,4)]]
z3=lambda i,j,k: s.Rational(9,2) if i==j==k==1 else 0
B={}; C={}
for i in range(2):
 for j,k in itertools.product(range(2),repeat=2):
  B[i,j,k]= (s.Rational(-3,4) if i==0 and j==k==0 else 0) if i==0 else (s.Rational(3,4)*(z1[j]*z1[k]+z2[j][k]))/tau
 for j,k,l in itertools.product(range(2),repeat=3):
  if i==0:
   C[i,j,k,l]=s.Rational(-3,2) if sorted((j,k,l))==[0,0,1] else 0
  else:
   C[i,j,k,l]=(-s.Rational(3,8)*z1[j]*z1[k]*z1[l]+s.Rational(3,4)*(z2[j][k]*z1[l]+z2[j][l]*z1[k]+z2[k][l]*z1[j])+s.Rational(3,4)*z3(j,k,l))/tau

def trans(D,order,i,*inds):
 out=0
 for k in range(2):
  for idx in itertools.product(range(2),repeat=order):
   val=D[(k,*idx)]; fac=Ti[i,k]
   for j,ii in enumerate(idx):fac*=T[ii,inds[j]]
   out+=val*fac
 return s.factor(out)
fx=trans(B,2,0,0,0); fxy=trans(B,2,0,0,1); fyy=trans(B,2,0,1,1)
gxx=trans(B,2,1,0,0); gxy=trans(B,2,1,0,1); gyy=trans(B,2,1,1,1)
fxxx=trans(C,3,0,0,0,0); fxyy=trans(C,3,0,0,1,1)
gxxy=trans(C,3,1,0,0,1); gyyy=trans(C,3,1,1,1,1)
ly=s.cancel(((fxxx+fxyy+gxxy+gyyy)+(fxy*(fx+fyy)-gxy*(gxx+gyy)-fx*gxx+fyy*gyy)/W)/16)
D=a*a*(s.Rational(9,32)-H)/H
num,den=map(s.expand,s.fraction(ly))
poly=s.Poly(num,W); r=s.together(sum(cf*D**(exp[0]//2) for exp,cf in poly.terms()))
# den can also depend W even powers
polyd=s.Poly(den,W); rd=s.together(sum(cf*D**(exp[0]//2) for exp,cf in polyd.terms()))
ls=s.factor(r/rd)
print('L coefficient=',ls)
print('numeric',s.N(ls.subs(L,s.log(3)),24))
print('L enclosed between 10986/10000 & 10987/10000?',1.0986<float(s.log(3))<1.0987)
print('poly numerator',s.factor(s.fraction(ls)[0]))
# Exact symbolic certificate for the Hopf coefficient and its sign.
expected=27*(1728*L**4-4080*L**3+17171*L**2-34432*L+21696)/(4096*(3*L-4)*(24*L-23)**2)
assert s.simplify(ls-expected)==0
from fractions import Fraction
low=Fraction(10986,10000); high=Fraction(10987,10000)
# Alternating no: positive-term logarithm series, with a rigorous geometric tail.
partial=sum(Fraction(2,2**(2*k+1)*(2*k+1)) for k in range(11))
tail=Fraction(2,1)/(2**23*23)*Fraction(4,3)
assert low < partial and partial+tail < high
# Set z=L-11/10, then -14/10000<z<-13/10000.
Z=s.symbols('Z',real=True)
P=1728*L**4-4080*L**3+17171*L**2-34432*L+21696
assert s.expand(P.subs(L,s.Rational(11,10)+Z))==s.expand(1728*Z**4+s.Rational(17616,5)*Z**3+s.Rational(406307,25)*Z**2-s.Rational(283291,125)*Z+s.Rational(4242987,2500))
P_lower=s.Rational(4242987,2500)+s.Rational(283291,125)*s.Rational(13,10000)-s.Rational(17616,5)*s.Rational(14,10000)**3
assert P_lower>1700
assert 3*high-4<0 and 24*low-23>0
# Verify characteristic determinant, trace-crossing derivative and biological bounds.
J=s.Matrix([[-a,a],[-s.Rational(9,32)/tau,H/tau]])
assert s.simplify(s.trace(J))==0
assert s.simplify(s.det(J)-D)==0
assert s.simplify(s.diff(-a+H/s.Symbol('t'),s.Symbol('t')).subs(s.Symbol('t'),tau)+H/tau**2)==0
assert 0<float(H.subs(L,s.log(3)))<float(s.Rational(9,32))
assert 0<float((s.log(3)-s.Rational(9,16)))<1
assert -1.405<float(ls.subs(L,s.log(3)))<-1.403
print('PASS: exact nondegenerate supercritical Hopf, rational logarithm enclosure, polynomial sign, trace crossing.')
