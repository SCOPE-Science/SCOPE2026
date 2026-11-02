"""Exact algebraic checks for a symmetric nonlinear competition system.
Run with Python 3.10+ and sympy 1.12+ using: python verify.py
Analytic convergence and critical asymptotics are proved separately.
"""
import sympy as S
x,y,s,d,a=S.symbols('x y s d a',real=True)
fx=x*(1-x-a*y**2)
fy=y*(1-y-a*x**2)
new={x:s+d,y:s-d}
fs=S.expand(((fx+fy)/2).subs(new))
fd=S.expand(((fx-fy)/2).subs(new))
assert S.simplify(fs-(s-s*s-a*s**3+(a*s-1)*d**2))==0
assert S.simplify(fd-d*(1-2*s+a*s*s-a*d*d))==0
# algebraic equilibrium: difference of per-capita conditions factors
per_difference=S.factor((1-x-a*y*y)-(1-y-a*x*x))
assert S.simplify(per_difference-(y-x)*(1-a*(x+y)))==0
# asymmetrical branches require x+y=1/a, xy=(1-a)/a**2
pp=(1-a)/a**2
pm=S.sqrt(a-S.Rational(3,4))
X=(S.Rational(1,2)+pm)/a
Y=(S.Rational(1,2)-pm)/a
assert S.simplify(X+Y-1/a)==0
assert S.simplify(X*Y-pp)==0
assert S.simplify(fx.subs({x:X,y:Y}))==0
assert S.simplify(fy.subs({x:X,y:Y}))==0
J=S.Matrix([fx,fy]).jacobian([x,y]); Jpos=J.subs({x:X,y:Y})
assert S.simplify(S.trace(Jpos)+1/a)==0
assert S.simplify(Jpos.det()-(1-a)*(4*a-3)/a**2)==0
# rational interior saddle/sinks and mutual invasion
ar=S.Rational(13,16)
assert (S.simplify(X.subs(a,ar)),S.simplify(Y.subs(a,ar)))==(S.Rational(12,13),S.Rational(4,13))
assert S.simplify(Jpos.det().subs(a,ar))==S.Rational(12,169)
assert S.simplify(S.trace(Jpos).subs(a,ar))==-S.Rational(16,13)
assert 1-ar==S.Rational(3,16)
# critical center-manifold calculation; s=2/3+c d^2 + ...
c=S.symbols('c',real=True)
crit=S.Rational(3,4)
h=S.Rational(2,3)+c*d*d
# residual 2 c d d' - s' must vanish to order d^2
res=S.expand(2*c*d*fd.subs({a:crit,s:h})-fs.subs({a:crit,s:h}))
coef2=S.expand(res).coeff(d,2)
assert S.solve(coef2,c)==[-S.Rational(3,8)]
hcrit=h.subs(c,-S.Rational(3,8))
fd_center=S.series(fd.subs({a:crit,s:hcrit}),d,0,6).removeO().expand()
assert fd_center.coeff(d,3)==-S.Rational(3,8)
assert S.simplify(1/(2*S.Rational(3,8)))==S.Rational(4,3)
assert S.simplify(4*S.Rational(4,3))==S.Rational(16,3)
assert S.simplify(-S.Rational(3,8)*S.Rational(4,3))==-S.Rational(1,2)
print('PASS: exact s,d flow, equilibrium identities, Jacobian trace/determinant,')
print('      rational witness, mutual invasion, critical center manifold and amplitudes.')
