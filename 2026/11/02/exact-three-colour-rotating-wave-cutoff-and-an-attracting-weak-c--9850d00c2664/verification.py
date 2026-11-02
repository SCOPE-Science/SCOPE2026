"""Reproducibility checks for three-site quadratic coupled-map rotating waves.
Requires Python >=3.10 and SymPy. All asserted algebraic signs are exact.
"""
import sympy as sp
x, a, S, u, t, z = sp.symbols('x a S u t z', real=True)
D = 7*a*a-14*a+1
A = 2*(1-a)
s = A*S-3*a/4
c = sp.expand(A*(a*S/2-(1-a))-a/4-a*a/16)
period_sum = sp.factor(s*s+s+c+2)
assert sp.factor(period_sum.subs(S,-sp.Rational(1,4)+sp.sqrt(D)/(4*(1-a)))) == 0
assert sp.factor(period_sum.subs(S,-sp.Rational(1,4)-sp.sqrt(D)/(4*(1-a)))) == 0
rr = u**3-t*u**2-(t*t+2*t+3)*u+t**3+2*t*t+3*t+1
assert sp.factor(sp.discriminant(rr,u)-(4*t*t+6*t+9)**2)==0
assert sp.factor(sp.resultant(rr,u*u-u-t*t-t-2,u)-(4*t*t+6*t+9)) == 0
C=-t*t-t-2
q2=sp.rem((u*u+C)**2+C,rr,u)
assert sp.rem(q2*q2+C-u,rr,u)==0
# Moving-frame derivative: P^-1 times the one-step Jacobian.
xx,yy,zz=sp.symbols('xx yy zz')
J=sp.Matrix([[4*(1-a)*xx,a/2,a/2],[a/2,4*(1-a)*yy,a/2],[a/2,a/2,4*(1-a)*zz]])
P=sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])
ch=sp.Poly((z*sp.eye(3)-P.T*J).det(),z)
assert sp.factor(ch.coeff_monomial(z**2)+3*a/2)==0
assert sp.factor(ch.coeff_monomial(z)-(-2*a*(1-a)*(xx+yy+zz)+3*a*a/4))==0
assert sp.factor(ch.coeff_monomial(1)+J.det())==0
# The stable-wave case a=7/100, larger-S branch.
a0=sp.Rational(7,100)
rt=sp.sqrt(543)
S0=-sp.Rational(1,4)+rt/372
s0=sp.simplify(s.subs({a:a0,S:S0}))
A0=A.subs(a,a0)
poly=sp.Poly(sp.expand(rr.subs(t,s0)),u)
# Exact rational enclosure for the sole square root.
lo=sp.Rational(23302,1000); hi=sp.Rational(23303,1000)
assert lo**2<543<hi**2
rad=sp.sqrt(543)
def sign_interval(expr):
    expr=sp.expand(sp.simplify(expr))
    alpha=sp.simplify(expr.subs(rad,0))
    beta=sp.simplify(sp.diff(expr,rad)) if False else sp.simplify(expr.coeff(rad))
    assert sp.simplify(expr-(alpha+beta*rad))==0,(expr,alpha,beta)
    ends=(alpha+beta*lo,alpha+beta*hi)
    if min(ends)>0:return +1
    if max(ends)<0:return -1
    raise AssertionError('radical enclosure inconclusive '+str((expr,ends)))
intervals=[(-1,sp.Rational(-9,10)),(0,sp.Rational(1,10)),(sp.Rational(7,10),sp.Rational(4,5))]
for (left,right),(want_l,want_r) in zip(intervals,[(-1,+1),(+1,-1),(-1,+1)]):
    left_u=A0*left-a0/4
    right_u=A0*right-a0/4
    assert sign_interval(poly.eval(left_u))==want_l
    assert sign_interval(poly.eval(right_u))==want_r
# Exactly one root in each interval (degree three, disjoint); all in (-1,1).
pu=-s*s-2*s-3; ru=-s*s*s-2*s*s-3*s-1
b=-a/4
prod_x=(ru-b*pu+b*b*s-b**3)/A**3
Det=sp.factor(64*(1-a)**3*prod_x-a*a*(1-a)*S+a**3/4)
c2=-3*a/2; c1=-2*a*(1-a)*S+3*a*a/4; c0=-Det
c2,c1,c0=[sp.simplify(v.subs({a:a0,S:S0})) for v in (c2,c1,c0)]
# Jury/Schur positivity for a real cubic (monic).
for expr in [1-c0,1+c0,1+c2+c1+c0,1-c2+c1-c0,1-c1+c2*c0-c0*c0]:
    assert sign_interval(expr)==1,expr
# This Schur test establishes local exponential attraction for F^3 (equiv. B^3).
print('PASS: exact three-cycle algebra, discriminant, nonfixed roots, exact root enclosures in (-1,1), and five strict cubic Schur inequalities at a=7/100')
print('Branch-sum',S0)
print('Moving-frame characteristic coefficients',c2,c1,c0)
