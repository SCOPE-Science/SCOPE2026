"""Exact symbolic checks for a matched-weight predator-prey reaction-diffusion identity.
Run: python CHECK.py (requires sympy). Analytical global parabolic estimates are in RESULT.md.
"""
import sympy as sp
x = sp.symbols('x', real=True)
a, b, c, e, U, V, A, B, P, S, d, D = sp.symbols('a b c e U V A B P S d D', positive=True)
# Reaction part of derivative of weighted relative entropy.
reaction = (A*U**2*(P-1)*(-a*U*(P-1)-b*V*(S-1))
            + B*V**2*(S-1)*(c*U*(P-1)-e*V*(S-1)))
diagonal = -A*a*U**3*(P-1)**2-B*e*V**3*(S-1)**2
cross = (B*c*V**2*U-A*b*U**2*V)*(P-1)*(S-1)
assert sp.expand(reaction-diagonal-cross)==0
assert sp.simplify(cross.subs(b, B*c*V/(A*U)))==0
# Ground-state transformed divergence operator identity in one dimension.
u = sp.Function('u')(x)
p = sp.Function('p')(x)
assert sp.simplify((sp.diff(u*u*sp.diff(p,x),x)/(u*u))
                   - sp.diff(p,x,2)-2*sp.diff(u,x)*sp.diff(p,x)/u)==0
# Explicit nonproportional, nonconstant equilibrium with negative predator intrinsic growth.
Ue=1+sp.cos(sp.pi*x)/10
Ve=1+sp.cos(2*sp.pi*x)/20
ce=sp.Integer(2)
be=sp.simplify(ce*Ve/Ue)
ae=sp.Integer(1); ee=sp.Rational(1,5)
de=De=sp.Rational(1,10)
re=sp.simplify((ae*Ue+be*Ve)-de*sp.diff(Ue,x,2)/Ue)
me=sp.simplify((ee*Ve-ce*Ue)-De*sp.diff(Ve,x,2)/Ve)
assert sp.simplify(be*Ue-ce*Ve)==0
assert sp.simplify(de*sp.diff(Ue,x,2)+Ue*(re-ae*Ue-be*Ve))==0
assert sp.simplify(De*sp.diff(Ve,x,2)+Ve*(me+ce*Ue-ee*Ve))==0
assert sp.diff(Ue,x).subs(x,0)==sp.diff(Ue,x).subs(x,1)==0
assert sp.diff(Ve,x).subs(x,0)==sp.diff(Ve,x).subs(x,1)==0
# Global algebraic bounds use 9/10 <= Ue <= 11/10,
# 19/20 <= Ve <= 21/20, and pi^2 < 10.
assert sp.Rational(1,5)*sp.Rational(21,20) -2*sp.Rational(9,10) + sp.Rational(1,5)/sp.Rational(19,20) <0
assert sp.Rational(9,10)+2*sp.Rational(19,20)**2/sp.Rational(11,10)-sp.Rational(1,10)/sp.Rational(9,10)>0
print('PASS: exact reaction cancellation, weighted diffusion identity, equilibrium substitution, Neumann endpoints, and strict sign bounds.')
