"""Symbolic and exact-arithmetic checks for a period-two census of a rational map."""
import sympy as S
s,u,m=S.symbols('s u m', real=True, nonzero=True)
k=2+m
p=S.expand((1+(s+u)**2)*(1+(s-u)**2))
a=k*p/(4*s)
g=lambda x:a/(1+x*x)
y1=s-u-g(s+u)
y2=s+u-g(s-u)
F=lambda x,y:(S.factor(g(x)+y),S.factor(y-m*(x-s)))
x2,Y2=F(s+u,y1)
x1,Y1=F(s-u,y2)
assert S.simplify(x2-(s-u))==0
assert S.simplify(Y2-y2)==0
assert S.simplify(x1-(s+u))==0
assert S.simplify(Y1-y1)==0
# All identities use the cycle relation a = (2+m)*P/(4*s).
d=lambda x:-2*a*x/(1+x*x)**2
d1,d2=d(s+u),d(s-u)
assert S.cancel(d1*d2-k*k*(s*s-u*u)/(4*s*s))==0
assert S.cancel(d1+d2 +k*(1-4*u*u*(u*u+1-s*s)/p))==0
T=S.factor(1-2*m+d1*d2)
D=S.factor((d1+m)*(d2+m))
assert S.cancel(1-T+D-4*m*k*u*u*(u*u+1-s*s)/p)==0
# Exact example: sigma=2, alpha=5, mu=1/1000.
sm=S.Integer(2); am=S.Integer(5); mm=S.Rational(1,1000)
R=S.cancel(4*am*sm/(2+mm))
delta=S.factor(R-4*sm**2)
assert delta==S.Rational(7984,2001)
assert S.Rational(1997,1000)**2 < delta < S.Rational(1998,1000)**2
qp=S.Integer(3)+S.sqrt(delta)
qm=S.Integer(3)-S.sqrt(delta)
assert 0<qm and qp>4
# Strict Schur stability criteria, checked as exact algebraic inequalities.
def jury(q):
 p0=S.cancel((1+sm**2)**2+2*(1-sm**2)*q+q*q)
 ds=-(2+mm)*(1-4*q*(q+1-sm**2)/p0)
 dp=(2+mm)**2*(sm**2-q)/(4*sm**2)
 tr=1-2*mm+dp
 det=dp+mm*ds+mm**2
 return [S.simplify(1-tr+det), S.simplify(1+tr+det), S.simplify(1-det)], tr,det
jp,tp,dp=jury(qp)
jm,tm,dm=jury(qm)
assert all(float(z)>0 for z in jp)
assert float(jm[0])<0 and 0<float(dm)<1
# Under exact interval 1997/1000 < sqrt(delta) < 1998/1000,
# the positive branch has q in (4.997,4.998), p=40000/2001,
# -1/4 < d1*d2 < 0 and 0 < d1+d2 < 3.
assert S.simplify(S.cancel((1+4)**2+2*(1-4)*qp+qp**2)-R)==0
jstar=S.Matrix([[-2*am*sm/(1+sm**2)**2,1],[-mm,1]])
tstar=jstar.trace();dstar=jstar.det()
assert all(z>0 for z in [1-tstar+dstar,1+tstar+dstar,1-dstar])
print('PASS exact reconstruction and Jacobian identities')
print('delta',delta,'q lower/upper',qm,qp)
print('Jury upper',jp,'lower first',jm[0]);print('fixed-point Jury', [1-tstar+dstar,1+tstar+dstar,1-dstar])
