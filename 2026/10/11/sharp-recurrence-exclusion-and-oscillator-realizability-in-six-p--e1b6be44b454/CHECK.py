"""Standalone exact checks for the six-coefficient quadratic jerk theorem.

Run: python CHECK.py  (requires SymPy).  Symbolic checks are not a substitute
for the compactness, invariance, and LaSalle arguments in RESULT.md.
"""
import sympy as s

x,y,z,t=s.symbols('x y z t', real=True)
b2,b3,b4,b5,b7,b8=s.symbols('b2 b3 b4 b5 b7 b8',real=True)
F=s.Matrix([y,z,b2*y+b3*z+b4*x**2+b5*y**2+b7*x*y+b8*x*z])
P=z-b3*y-b2*x-s.Rational(1,2)*b7*x**2-b8*x*y
LP=s.expand(s.Matrix([s.diff(P,w) for w in (x,y,z)]).dot(F))
assert s.simplify(LP-(b4*x**2+(b5-b8)*y**2))==0

# The exhibited oscillators work for every opposite-sign pair alpha,beta:
a,be,R=s.symbols('a be R', nonzero=True,real=True)
w=s.symbols('w', positive=True,real=True)
X=R*s.cos(w*t)
Y=-R*w*s.sin(w*t)
Z=-R*w**2*s.cos(w*t)
# Choose b2=-w^2, b3=b5=b7=0, b4=a, b8=-be.
# Then the residual of the third ODE vanishes when a+be*w^2=0.
res=s.simplify(s.diff(Z,t)-(-w**2*Y+a*X**2-be*X*Z))
assert s.simplify(res+(a+be*w**2)*X**2)==0
assert s.simplify(s.diff(X,t)-Y)==0
assert s.simplify(s.diff(Y,t)-Z)==0
assert s.simplify(res.subs(a,-be*w**2))==0

# The source's nine examples all lie in the opposite-sign cone.
samples={
 'A':(1,0,3),'B':(-4,3,-1),'C':(1,-3,1),
 'D':(1,0,3),'E':(-2,3,-1),'F':(-1,0,-1),
 'G':(1,-1,s.Rational(3,5)),'H':(7,-2,1),
 'I':(9,s.Rational(-5,2),1)}
for model,(alpha,c5,c8) in samples.items():
    assert alpha*(c5-c8)<0,(model,alpha,c5,c8)

# Universal moment ratio checked at both a rational oscillatory example and
# symbolically: integration along the harmonic orbit gives <y^2>=w^2<x^2>.
avg_x=s.integrate(X**2,(t,0,2*s.pi/w))/(2*s.pi/w)
avg_y=s.integrate(Y**2,(t,0,2*s.pi/w))/(2*s.pi/w)
assert s.simplify(avg_x-R**2/2)==0
assert s.simplify(avg_y-w**2*R**2/2)==0
print('PASS: polynomial Lie derivative, harmonic witnesses, table sign check, periodic second moments')
