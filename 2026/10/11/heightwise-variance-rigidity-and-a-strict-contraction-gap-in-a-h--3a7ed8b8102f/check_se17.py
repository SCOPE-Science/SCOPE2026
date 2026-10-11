"""Exact symbolic and rational checks for the quadratic hidden-attractor flow."""
import sympy as s
x,y,z,k,p,q,c=s.symbols('x y z k p q c',real=True)
F=s.Matrix([z,x-y,c-k*x-p*x*z+q*y*z])
vars=(x,y,z)
D=lambda f:s.expand(sum(s.diff(f,w)*g for w,g in zip(vars,F)))
P=z+s.Rational(1,2)*p*x**2-q*x*y+s.Rational(1,2)*q*y**2
assert s.simplify(D(P)-(c-k*x-q*(x-y)**2))==0
assert s.simplify(D(y**2/2)-(x*y-y*y))==0
assert s.simplify(D(x**2/2)-x*z)==0
assert s.simplify(D(x*y)-(y*z+x*x-x*y))==0
assert s.simplify(s.trace(F.jacobian(vars))-(-1-p*x+q*y))==0
Xeq=s.Matrix([c/k,c/k,0])
assert [s.simplify(t.subs(dict(zip(vars,Xeq)))) for t in F]==[0,0,0]
R={k:s.Rational(31,10),p:s.Rational(3,10),q:s.Rational(1,5),c:s.Rational(57,100)}
assert s.simplify((c/k).subs(R))==s.Rational(57,310)
assert s.simplify((q/k).subs(R))==s.Rational(2,31)
assert s.simplify(((p-q)*q/k).subs(R))==s.Rational(1,155)
assert s.simplify((-1-(p-q)*c/k).subs(R))==-1-s.Rational(57,3100)
print('SE17_SYMBOLIC_CHECKS_PASS')
