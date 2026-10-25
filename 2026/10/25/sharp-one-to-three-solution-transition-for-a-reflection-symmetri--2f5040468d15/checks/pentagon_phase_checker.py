"""Exact algebra checks and independent numerical substitutions for a five-normal cone-volume fiber."""
import sympy as S
from math import comb
v=S.sqrt(5); q=(v-1)/4; r,B=S.symbols('r B',real=True)
A=S.factor((v-1)*(B**2+(1-v)*B+1)/(B-v+1))
yratio=-1/(B-v+1)
J=B**3-(1+19*v)*B**2/11+(42+6*v)*B/11-(12+8*v)/11
J0=B**3-(1+3*v)*B**2/2+(3+3*v)*B/2+(v-7)/2
Z=S.factor(B*(A-1)+2*q*(B*B-A*A))/(yratio-2*q)
H=S.factor(B+1-2*q+(yratio-(1+2*q)*yratio**2)*Z)
T=2*A*(B-q*A)/H
assert S.simplify(Z-(13-5*v)*J/((1-v)*(B-v+1)))==0
assert S.simplify(H-(4*(3-v)/(v-1))*(B+(3-v)/2)*J0/(B-v+1)**3)==0
assert S.simplify(B*B-Z-(4*(3-v)/(v-1))*(B-(1+v)/2)*(B*B+(1-v)*B+1)/(B-v+1))==0
assert S.simplify(1-yratio**2*Z-(4*(3-v)/(v-1))*J0/(B-v+1)**3)==0
for poly in (J,J0):assert S.discriminant(poly,B)<0
P6=(B**6-(1+3*v)*B**5+(S.Rational(23,2)+S.Rational(11,2)*v)*B**4+(-52+6*v)*B**3+(-64+44*v)*B**2+(-85+31*v)*B+(21*v-41)/2)
assert S.simplify(S.diff(T,B)-((v-1)**2*(1-v)/(4*(v-3)))*P6/J0**2)==0
# Bernstein coefficients on [2,23/10] are strictly negative. Converting from powers on t=(B-2)/(3/10).
t=S.symbols('t');p=S.Poly(S.expand(P6.subs(B,2+S.Rational(3,10)*t)),t)
co=[p.nth(i) for i in range(7)]; bern=[S.simplify(sum(co[i]*S.Rational(comb(k,i),comb(6,i)) for i in range(k+1))) for k in range(7)]
assert all(float(c.evalf()) < -1.3 for c in bern)
assert S.simplify(S.diff(T,B)).subs(B,S.Rational(11,5)).evalf()<0
# Symmetric solution uniqueness: positive derivative of t(r) for allowed r.
g=r+2*q*(1-r*r);tsym=S.factor(2*r*(1-q*r)/(g*(1+(1-2*q)*g)))
snum=S.factor(S.together(S.diff(tsym,r)).as_numer_denom()[0],extension=v)
print('sym_derivative_num=',snum)
print('Bernstein=',bern)
for x in [S.Rational(21,10),S.Rational(11,5),S.Rational(9,4)]:
    av=float(A.subs(B,x));z=float(Z.subs(B,x));h=float(H.subs(B,x));ta=float(T.subs(B,x));qq=float(q);ss=float(S.sin(2*S.pi/5))
    dd=(2*ss/h)**0.5;aa=av*dd;bb=float(x)*dd;xx=dd*z**0.5;yy=float(yratio.subs(B,x))*xx
    vals=[aa,bb+xx,dd+yy,dd-yy,bb-xx]
    assert min(vals)>0
    f=[vals[i]*(vals[(i-1)%5]+vals[(i+1)%5]-2*qq*vals[i])/(2*ss) for i in range(5)]
    assert max(abs(f[i]-[ta,ta,1,1,ta][i]) for i in range(5))<1e-9
    rev=[aa,bb-xx,dd-yy,dd+yy,bb+xx]
    f2=[rev[i]*(rev[(i-1)%5]+rev[(i+1)%5]-2*qq*rev[i])/(2*ss) for i in range(5)]
    assert max(abs(f2[i]-[ta,ta,1,1,ta][i]) for i in range(5))<1e-9
root0=float(S.nroots(J0,maxsteps=200)[0]);rootstar=float(S.nroots(J,maxsteps=200)[0]);tstar=float(T.subs(B,rootstar))
assert 2<root0<2.1<2.25<rootstar<2.3
assert 3.08<tstar<3.09
print('CONE_VOLUME_PENTAGON_OK endpoints',root0,rootstar,'threshold',tstar,'branch_tests',6)
