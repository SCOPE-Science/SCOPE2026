"""Standalone numerical and algebraic checks for the critical dual-channel epidemic ODE.

The full-time asymptotic statement is established analytically in RESULT.md;
finite integrations here are corroborative and not substitutes for its proof.
"""
import math
import sympy as sp
from scipy.integrate import solve_ivp

x, y, d, s, a = sp.symbols('x y d s a', real=True)
F = (x+y)*(1-x)/2-x
T = sp.atan(s*x)/s
G = T*(1-y)-y
V = x+y/2
J = sp.simplify(sp.Matrix([F, G]).jacobian([x,y]).subs({x:0,y:0}))
assert J == sp.Matrix([[-sp.Rational(1,2),sp.Rational(1,2)],[1,-1]])
assert J.eigenvals() == {sp.S.Zero:1,-sp.Rational(3,2):1}
assert sp.simplify(sp.diff(V,x)*F+sp.diff(V,y)*G-((T-x)-x*x-(x+T)*y)/2)==0

xdot = sp.factor(F.subs(y, x+d))
ddot = sp.simplify((G-F).subs(y,x+d))
assert sp.simplify(xdot-(-x*x + (1-x)*d/2))==0
assert sp.simplify(ddot-(-(3+x)*d/2+(T-x)*(1-x-d)))==0
# Parameter-independent quadratic jet, cubic arctan term, unique cubic
# center-manifold coefficient from the polynomial invariance equation.
T3 = x-s*s*x**3/3
lhs = sp.diff(a*x**3,x)*xdot.subs(d,a*x**3)
rhs = (-(3+x)*d/2+(T3-x)*(1-x-d)).subs(d,a*x**3)
res = sp.series(lhs-rhs,x,0,4).removeO().expand()
assert sp.simplify(res.coeff(x,2)) == 0
assert sp.simplify(res.coeff(x,3)-(sp.Rational(3,2)*a+s*s/3))==0
coef = sp.solve(res.coeff(x,3),a)[0]
assert coef==-2*s*s/9
assert sp.expand(xdot.subs(d,coef*x**3)).coeff(x,3)==-s*s/9
print('Exact critical Jacobian, Lyapunov derivative, transformed ODE, cubic jet: PASS')

for size in (3,4,6):
    def f(_, u):
        p,q=u
        return ((p+q)*(1-p)/2-p,math.atan(size*p)*(1-q)/size-q)
    sol=solve_ivp(f,(0,20000),(.25,.12),method='DOP853',rtol=4e-13,
                  atol=5e-15,dense_output=True,max_step=50)
    assert sol.success,sol.message
    values=[]
    for t in (10000,20000):
        p,q=sol.sol(t)
        assert p>0 and q>0 and abs(t*p-1)<0.015
        assert abs(q/p-1)<0.0005
        values.append(1/p-t-size*size/9*math.log(t))
    assert abs(values[1]-values[0])<0.025,(size,values)
    print(f's={size}: reciprocal intercept at t=10000,20000: {values[0]:.9f}, {values[1]:.9f}; PASS')
print('All reproducibility checks PASS; finite tests are not infinity proofs.')
