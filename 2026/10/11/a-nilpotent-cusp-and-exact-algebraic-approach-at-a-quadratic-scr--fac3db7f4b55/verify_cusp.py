"""Reproduce exact linear and weighted-leading coefficients of the cusp proof.

The dynamical existence argument is the stable-manifold theorem in the
blown-up chart; this script checks its algebraic hypotheses, not that theorem.
"""
import sympy as s

a,b,c,d=s.symbols('a b c d',positive=True)
u,v,r,q=s.symbols('u v r q',real=True)
lam=s.symbols('lam')
# Vector field at the coalesced equilibrium (b,0,a), under ad=bc.
J=s.Matrix([[0,0,0],[a,0,0],[c,b,-d]])
assert s.factor(J.charpoly(lam).as_expr()) == lam**2*(lam+d)
alpha=(c*d-a*b)/d**2
beta=b/d
H1=alpha*u+beta*v
# Derivative along the center nilpotent linear flow u'=0, v'=a u.
assert s.simplify(s.diff(H1,v)*a*u - (c*u+b*v-d*H1))==0
# Quadratic terms of the center flow: u'=-v H1, v'=(a+H1)u.
up=-v*H1
vp=(a+H1)*u
assert s.expand(up).coeff(v,2)==-beta
assert s.expand(vp).coeff(u)==a+s.expand(H1).coeff(v)*v
# Weighted blow-up u=r^3 q, v=-r^2 (r>0).
Hblow=H1.subs({u:r**3*q,v:-r**2})
ublow=r**2*Hblow
vblow=(a+Hblow)*r**3*q
rdot=-vblow/(2*r)
qdot=s.cancel((ublow-3*r**2*rdot*q)/r**3)
# Desingularize ds/dt=r; the boundary vector field is hyperbolic.
F=s.simplify(s.limit(rdot/r**2,r,0))
G=s.simplify(s.limit(qdot/r,r,0))
assert s.simplify(F+a*q/2)==0
assert s.simplify(G-(3*a*q**2/2-beta))==0
Q=s.sqrt(2*beta/(3*a))
assert s.simplify(G.subs(q,Q))==0
assert s.simplify(G.subs(q,-Q))==0
assert s.simplify(F.subs(q,Q)+a*Q/2)==0
assert s.simplify(s.diff(G,q).subs(q,Q)-3*a*Q)==0
# t r(t) -> 2/(aQ) on incoming forward-time branch.
Lr=2/(a*Q)
Lv=s.simplify(-Lr**2)
Lu=s.simplify(Q*Lr**3)
Lw=s.simplify(-beta*Lr**2)
assert s.simplify(Lv+6*d/(a*b))==0
assert s.simplify(Lu-12*d/(a*a*b))==0
assert s.simplify(Lw+6/a)==0
print('CHECK_OK')
