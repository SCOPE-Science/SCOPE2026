"""Exact symbolic consistency checks for two-community opinion equilibria.

Requires Python 3 and SymPy. These checks supplement, but do not replace,
the analytic classification proved in RESULT.md.
"""
import sympy as sp

s, d, k, a, b, x, y = sp.symbols('s d k a b x y', real=True)
A = lambda z: sp.expand(z*(1-z)*(2*z-1))
left = b*(y-x)/2+a*A(x)
right = b*(x-y)/2+a*A(y)
xy = {x: (1+s-d)/2, y: (1+s+d)/2}
S = sp.factor((left+right).subs(xy)/a)
D = sp.factor((right-left).subs(xy)/a)
# s=(2x-1+2y-1)/2 = x+y-1; d=y-x; tau=alpha*t/2.
assert sp.simplify(S-s*(1-s*s-3*d*d)/2) == 0
assert sp.simplify(D-d*(1-2*b/a-3*s*s-d*d)/2) == 0
f=s*(1-s*s-3*d*d)
g=d*(1-2*k-3*s*s-d*d)
J=sp.Matrix([f,g]).jacobian([s,d]); assert sp.simplify(J[0,1]-J[1,0])==0
# Symmetric polar branch: separate center and gap eigenvalues in original time.
d2=1-2*k
assert sp.simplify(J[0,0].subs({s:0,d*d:d2}) - (6*k-2))==0
assert sp.simplify(J[1,1].subs({s:0,d*d:d2}) - (4*k-2))==0
# Asymmetric equilibria, k in (0, 1/3): exact squared coordinates.
s2=(1-3*k)/4
h2=(1+k)/4
assert sp.simplify(1-s2-3*h2)==0
assert sp.simplify(1-2*k-3*s2-h2)==0
assert sp.simplify((-2*s2-2*h2) - (k-1))==0
assert sp.simplify((-32*s2*h2) - 2*(1+k)*(3*k-1))==0
# Critical k=1/3: h(s)=d0+c*s^2, invariance to leading order.
d0=1/sp.sqrt(3)
c=-3*sp.sqrt(3)/2
h=d0+c*s**2
critical_g=sp.series(g.subs({k:sp.Rational(1,3), d:h}),s,0,4).removeO()
assert critical_g.coeff(s,2)==0
critical_f=sp.series(f.subs({d:h}),s,0,5).removeO()
assert sp.simplify(critical_f.coeff(s,3)-8)==0
# Rational counterexample in source's 'Phase II': alpha/beta=21/10, epsilon=3/10.
assert sp.Rational(2)<sp.Rational(21,10)<2/(1-sp.Rational(3,10)**2)
assert (1-2/sp.Rational(21,10)) < sp.Rational(3,10)**2
assert 3-sp.Rational(21,10)>0 and 2-sp.Rational(21,10)<0
# Stable interacting example: alpha/beta=4, confidence 4/5.
assert (1-2/sp.Integer(4))<sp.Rational(4,5)**2
assert 3-sp.Integer(4)<0 and 2-sp.Integer(4)<0
# Asymmetric saddle example alpha/beta=4.
assert sp.factor((2*(1+sp.Rational(1,4))*(3*sp.Rational(1,4)-1)))==-sp.Rational(5,8)
print('VERIFY_OK: exact reductions, eigenvalues, asymmetric branches, critical cubic and examples')
