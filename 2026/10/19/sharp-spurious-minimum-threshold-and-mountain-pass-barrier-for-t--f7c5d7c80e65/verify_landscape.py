"""Symbolic identities and finite cross-checks for rank-one matrix-energy barriers.

This script verifies algebraic identities; the accompanying proof establishes
universal parameter and path statements independently.
"""
import sympy as s
from fractions import Fraction

a,b,k,x,y,z=s.symbols('a b k x y z',positive=True)
xs=(k*b-a)/(k*k-1)
ys=(k*a-b)/(k*k-1)
fs=-s.Rational(1,2)*(a*xs+b*ys)
fb=-b*b/2
assert s.factor(fs-fb-(k*b-a)**2/(2*(k*k-1)))==0
assert s.simplify(xs*ys-(s.sqrt(xs*ys))**2)==0
assert s.simplify(ys-(b-k*xs))==0
assert s.simplify(xs-(a-k*ys))==0
fxy=(x*x+y*y)/2+k*x*y-a*x-b*y
assert s.simplify(fxy.subs({x:xs,y:ys})-fs)==0
assert s.factor(fxy.subs(y,b-k*x)- (fb+(k*b-a)*x-(k*k-1)*x*x/2))==0
assert s.factor(s.det(s.Matrix([[1,k],[k,1]]))-(1-k*k))==0
# Verify the equality-case quartic leading coefficient with b=1 and a=k.
t=s.symbols('t',real=True)
Y=1-k*t*t
f_bd = ((t**4/Y**2)+Y**2+2*k*t*t)/2 - k*t*t/Y-Y
assert s.simplify(s.limit((f_bd+s.Rational(1,2))/t**4,t,0)-(1-k*k)/2)==0
# Lagrange multiplier stationarity (rank-one determinant constraint).
u,v=s.symbols('u v',real=True)
F=(x*x+y*y+k*(u*u+v*v))/2-a*x-b*y
for sg in [-1,1]:
    pp={x:xs,y:ys,u:sg*s.sqrt(xs*ys),v:sg*s.sqrt(xs*ys)}
    sol=[s.diff(F,w)-(-k)*s.diff(x*y-u*v,w) for w in [x,y,u,v]]
    assert all(s.simplify(item.subs(pp))==0 for item in sol)
# Direct exact rank-one representations for rational t>1.
for n in [2,3,5]:
    d=[s.Rational(2),s.Rational(1,2)]+[s.Integer(1)]*(n-2)
    W=s.Matrix(n,n,lambda i,j:(d[i]/d[j]+d[j]/d[i])/2)
    assert W[0,1]==s.Rational(17,8)
    assert min(W)==1 and max(W)==s.Rational(17,8)
    for aa,bb in [(s.Rational(3,2),s.Integer(1)),(s.Rational(2),s.Integer(1))]:
        X=s.zeros(n)
        X[0,0]=aa
        G=s.Matrix(n,n,lambda i,j:W[i,j]*X[i,j])
        F0=s.diag(aa,bb,*([0]*(n-2)))
        energy=lambda Z: s.expand(sum(W[i,j]*Z[i,j]**2/2-F0[i,j]*Z[i,j] for i in range(n) for j in range(n)))
        assert energy(X)==-aa**2/2
        assert energy(s.diag(0,bb,*([0]*(n-2))))==-bb**2/2
        for rr in [s.Rational(0),s.Rational(1,5),s.Rational(2,5),s.Rational(1),s.Rational(3)]:
            vv=s.zeros(n,1); ww=s.zeros(n,1)
            vv[0]=rr; vv[1]=1; ww[0]=s.Rational(1,3);ww[1]=s.Rational(2,3)
            Y=vv*ww.T
            assert Y.rank()==1
            e=sum(W[i,j]*Y[i,j]**2/2-F0[i,j]*Y[i,j] for i in range(n) for j in range(n))
            assert s.simplify(e-energy(Y))==0
print('PASS: symbolic stationary points, degenerate quartic, barrier, operator spectrum, and rational rank-one checks')
