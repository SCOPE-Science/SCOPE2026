"""Exact symbolic verification of the one-step-lag RMSProp cycle theorem.
Run with python verify.py; requires SymPy. The proof is in RESULT.md.
"""
import sympy as sp

x,v,a,eps,b,h,q=sp.symbols('x v a eps b h q',positive=True)
vp=b*v+(1-b)*a**2*x**2
xp=x-h*a*x/(eps+sp.sqrt(v))
F=sp.Matrix([xp,vp])
Jac=F.jacobian([x,v])
S=sp.diag(-1,1)
cycle_subs={x:q,v:a**2*q**2,eps:a*(h/2-q)}
Fp=sp.simplify(F.subs(cycle_subs))
Fm=sp.simplify(F.subs({x:-q,v:a**2*q**2,eps:a*(h/2-q)}))
assert sp.simplify(Fp-sp.Matrix([-q,a**2*q**2]))==sp.zeros(2,1)
assert sp.simplify(Fm-sp.Matrix([q,a**2*q**2]))==sp.zeros(2,1)
Jp=sp.simplify(Jac.subs(cycle_subs))
Jm=sp.simplify(Jac.subs({x:-q,v:a**2*q**2,eps:a*(h/2-q)}))
assert sp.simplify(Jm-S*Jp*S)==sp.zeros(2)
assert sp.simplify(Jp-sp.Matrix([[-1,2/(a**2*h)],[2*(1-b)*a**2*q,b]]))==sp.zeros(2)
K=S*Jp
assert sp.simplify(sp.trace(K)-(1+b))==0
D=sp.simplify(K.det())
assert sp.simplify(D-(b+4*(1-b)*q/h))==0
assert sp.simplify(Jm*Jp-K**2)==sp.zeros(2)
assert sp.simplify(K**2-(1+b)*K+D*sp.eye(2))==sp.zeros(2)
# Change variables from cycle amplitude q to the physical learning rate h.
D_h=sp.factor(D.subs(q,h/2-eps/a))
assert sp.simplify(D_h-(2-b-4*(1-b)*eps/(a*h)))==0
assert sp.simplify(D_h.subs(h,2*eps/a)-b)==0
assert sp.simplify(D_h.subs(h,4*eps/a)-1)==0
h_node=16*eps/(a*(7+b))
discriminant=sp.factor((1+b)**2-4*D_h)
assert sp.simplify(discriminant.subs(h,h_node))==0
assert sp.simplify(sp.diff(D_h,h)-4*(1-b)*eps/(a*h**2))==0
# Rational snapshots check the expected strict cases and degeneracy.
for beta in (sp.Rational(1,25),sp.Rational(1,2),sp.Rational(9,10)):
    node=sp.Rational(16,1)/(7+beta)
    assert 2<node<4
    for gain in (sp.Rational(21,10),node,sp.Rational(3,1),sp.Rational(4,1),sp.Rational(5,1),sp.Rational(100,1)):
        delta=sp.simplify(D_h.subs({a:1,eps:1,b:beta,h:gain}))
        disc=sp.simplify(discriminant.subs({a:1,eps:1,b:beta,h:gain}))
        if gain<4:assert beta<delta<1
        if gain==4:assert delta==1
        if gain>4:assert delta>1 and disc<0
        if gain>node:assert disc<0
        if gain==node:assert disc==0
        if gain<node:assert disc>0
print('PASS: exact cycle, Jacobians, monodromy, characteristic polynomial, thresholds, 18 rational snapshots')
