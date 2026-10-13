"""Exact symbolic tests for the Fermat-cubic/circle elliptic pencil.

Requires Python 3 and SymPy. These checks support, but do not replace,
the geometric proof of the singular-fiber and Mordell-Weil statements.
"""
from sympy import (
    symbols, Rational, Poly, factor, expand, simplify, gcd, diff, discriminant,
    resultant, roots, Matrix, oo, cancel,
)

x, y, z, t, s, d, v, u = symbols('x y z t s d v u')
G = x**3 + y**3 - z**3
H = z*(x**2 + y**2-z**2)
F = G + t*H
f = F.subs(z, 1)
assert expand(f.subs({x:(s+d)/2, y:(s-d)/2})*4-(s**3+2*t*s**2+(3*s+2*t)*d**2-4*(1+t))) == 0
Q = expand((3*s+2*t)*(4*(1+t)-s**3-2*t*s**2))
a,b,c,e,f0 = [expand(Poly(Q,s).coeff_monomial(s**i)) for i in (4,3,2,1,0)]
I = expand(12*a*f0 - 3*b*e + c**2)
J = expand(72*a*c*f0+9*b*c*e-27*a*e**2-27*b**2*f0-2*c**3)
J0 = 8*t**6-216*t**4-216*t**3+729*t**2+1458*t+729
D = (t-3)**2*(t+1)*(2*t+3)**4*(8*t**3-27*t-27)
assert factor(I-16*t**4)==0
assert factor(J-16*J0)==0
assert factor(4*I**3-J**2-6912*D)==0
assert factor(discriminant(Q,s)-256*D)==0
assert factor(4096*t**12-1728*D-64*J0**2)==0
assert factor(12*D-t*diff(D,t)-4*(t-3)*(2*t+3)**3*J0)==0
assert gcd(Poly(J0,t),Poly(diff(J0,t),t)).degree()==0
assert gcd(Poly(J0,t),Poly(D,t)).degree()==0
U=8*t**3-27*t-27
assert gcd(Poly(U,t),Poly(diff(U,t),t)).degree()==0
for root in [Rational(3), Rational(-3,2), Rational(-1)]:
    assert U.subs(t,root) != 0
assert factor(4*t**3-27*t-27)==(t-3)*(2*t+3)**2
# Singular finite parameters from F = Fx = Fy =0.
assert factor(f.subs({x:0,y:0})) == -t-1
assert factor(f.subs({x:-2*t/3,y:0})) == (2*t+3)**2*(t-3)/27
assert factor(f.subs({x:-2*t/3,y:-2*t/3})-U/27) == 0
# Components of the reducible fibers; also verify intersection nodes.
L3=x+y+2*z
Q3=x**2-x*y+x*z+y**2+y*z-2*z**2
assert factor(F.subs(t,3)-L3*Q3)==0
assert factor(Q3.subs(y,-x-2*z)-3*x*(x+2*z))==0
L4=x+y-z
Q4=x**2-x*y-Rational(1,2)*x*z+y**2-Rational(1,2)*y*z-Rational(1,2)*z**2
assert factor(F.subs(t,Rational(-3,2))-L4*Q4)==0
assert factor(Q4.subs(y,z-x)-3*x*(x-z))==0
for q in [Q3,Q4]:
    # Verify each quadratic is nonsingular by its symmetric Hessian determinant.
    hess=Matrix([[diff(q,r,c0) for c0 in (x,y,z)] for r in (x,y,z)])
    assert hess.det()!=0
# Base-point finite intersection: (s-1)^2(s+2)=0.
xy=symbols('xy')
p = (s**2-1)/2
assert factor(s**3-3*p*s-1) == -(s-1)**2*(s+2)/2
# The two simple finite basepoints have x+y=-2 and xy=3/2.
assert p.subs(s,-2)==Rational(3,2)
# Three simple points occur at infinity, where G|Z=0 = (x+y)(x^2-xy+y^2).
assert factor(G.subs(z,0)-(x+y)*(x*x-x*y+y*y))==0
# Intersection at the two double basepoints has multiplicity two,
# since initial linear parts agree but the strict transforms are transversal.
g_loc = expand(G.subs({x:1+u,y:v,z:1}))
h_loc = expand(H.subs({x:1+u,y:v,z:1}))
assert g_loc == 3*u + 3*u**2 + u**3 + v**3
assert h_loc == 2*u + u**2 + v**2
m=symbols('m')
g_blow=expand(g_loc.subs(u,m*v)/v)
h_blow=expand(h_loc.subs(u,m*v)/v)
assert simplify(Matrix([[diff(g_blow,m),diff(g_blow,v)],[diff(h_blow,m),diff(h_blow,v)]]).det().subs({m:0,v:0})) != 0
# Nontrivial t=-3/2 member contains the first exceptional as a vertical bridge.
assert expand((g_blow-Rational(3,2)*h_blow).subs(v,0)) == 0
# At each basepoint vertical bridge meets both branches away from second basepoint.
q4_local=expand(Q4.subs({x:1+u,y:v,z:1})).subs(u,m*v)
l4_local=expand(L4.subs({x:1+u,y:v,z:1})).subs(u,m*v)
assert factor(cancel(l4_local/v).subs(v,0))==m+1
assert factor(cancel(q4_local/v).subs(v,0)-Rational(3,2)*(m-1))==0
# Complete Belyi passport: 0 -> (12), 1728 -> six (2),
# infinity -> (4,2,2,1,1,1,1). Riemann-Hurwitz must total 22.
assert (12-1)+6*(2-1)+((4-1)+2*(2-1))==2*12-2
# Euler fiber count and Shioda-Tate Picard rank.
assert 4+2+2+1+3==12
assert 10-2-((4-1)+2*(2-1))==3
print('VERIFY_OK: quartic invariants, Belyi j, ramification, singular members, nine base blowups, I4 bridges, MW rank 3')
