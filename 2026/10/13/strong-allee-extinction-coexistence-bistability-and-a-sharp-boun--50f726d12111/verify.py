#!/usr/bin/env python3
"""Exact algebraic replay for an exponential predator–prey fixed-point classification."""
import math
import sympy as sp

x, y, alpha = sp.symbols('x y alpha', real=True)
a=sp.Integer(4); b=beta=c=d=e=sp.Integer(1); f=sp.Rational(3,2)
prey_exp = a-b*x-alpha/(beta+x)-c*y/(e+x)
pred_exp = f*x/(e+x)-d
# The map is (x*exp(prey_exp), y*exp(pred_exp)).
F = sp.Matrix([x*sp.exp(prey_exp),y*sp.exp(pred_exp)])
J = F.jacobian([x,y])

q=sp.expand((x+1)*(4-x)-alpha)
assert sp.expand(q-(-x*x+3*x+4-alpha))==0
assert sp.simplify(prey_exp.subs({x:2,y:6-alpha}))==0
assert sp.simplify(pred_exp.subs(x,2))==0
assert sp.simplify(sp.Matrix(F).subs({x:2,y:6-alpha})-sp.Matrix([2,6-alpha]))==sp.zeros(2,1)
Jstar=sp.simplify(J.subs({x:2,y:6-alpha}))
Jexpected=sp.Matrix([[sp.Rational(1,3),-sp.Rational(2,3)],[(6-alpha)/6,1]])
assert sp.simplify(Jstar-Jexpected)==sp.zeros(2)
T=sp.simplify(sp.trace(Jstar)); D=sp.simplify(Jstar.det())
assert T==sp.Rational(4,3)
assert sp.simplify(D-(1-alpha/9))==0
assert sp.simplify((1-D)-alpha/9)==0
assert sp.simplify((1-T+D)-(6-alpha)/9)==0
assert sp.simplify((1+T+D)-(30-alpha)/9)==0

J0=sp.simplify(J.subs({x:0,y:0}))
assert J0==sp.diag(sp.exp(4-alpha),sp.exp(-1))

# At a prey-only root alpha=(4-H)(1+H), the two triangular multipliers.
alpha_boundary=(4-x)*(1+x)
Jboundary=sp.simplify(J.subs(y,0).subs(alpha,alpha_boundary))
assert sp.simplify(Jboundary[1,0])==0
prey_lambda=sp.simplify(Jboundary[0,0])
pred_lambda=sp.simplify(Jboundary[1,1])
assert sp.simplify(prey_lambda-(1+x*(3-2*x)/(1+x)))==0
assert sp.simplify(pred_lambda-sp.exp((x-2)/(2*(1+x))))==0

Hflip=(5+sp.sqrt(41))/4
alpha_flip=(29+sp.sqrt(41))/8
assert sp.simplify(prey_lambda.subs(x,Hflip)+1)==0
assert sp.simplify(alpha_boundary.subs(x,Hflip)-alpha_flip)==0
assert 4<float(alpha_flip)<6

for av in (sp.Rational(41,10),sp.Rational(9,2),sp.Rational(5),sp.Rational(11,2),sp.Rational(59,10)):
    hminus=(3-sp.sqrt(25-4*av))/2
    hplus=(3+sp.sqrt(25-4*av))/2
    assert 0<float(hminus)<1<2<float(hplus)<3
    for h in (hminus,hplus):
        assert abs(float(prey_exp.subs({x:h,y:0,alpha:av})))<1e-13
        assert abs(float(F[0].subs({x:h,y:0,alpha:av})-h))<1e-13
        assert abs(float(F[1].subs({x:h,y:0,alpha:av})))<1e-13
    assert float(prey_lambda.subs(x,hminus))>1
    assert 0<float(pred_lambda.subs(x,hminus))<1
    assert float(pred_lambda.subs(x,hplus))>1
    ptop=float(prey_lambda.subs(x,hplus))
    if float(av)<float(alpha_flip):assert ptop < -1
    if float(av)>float(alpha_flip):assert -1<ptop<1
    Tnum=float(T.subs(alpha,av)); Dnum=float(D.subs(alpha,av))
    eig=sp.nroots(sp.Symbol('z')**2-Tnum*sp.Symbol('z')+Dnum, maxsteps=300)
    assert all(abs(complex(z))<1-1e-5 for z in eig)
    assert 0<float(sp.exp(4-av))<1
    assert 0<float(sp.exp(-1))<1
print('VERIFY_OK')
print('alpha_flip',float(alpha_flip))
print('Jstar_at_alpha5',Jstar.subs(alpha,sp.Integer(5)))
