from fractions import Fraction
import sympy as sp

x,y,z,w=sp.symbols('x y z w')
a,b,c,d=1,2,3,4
Q=(
 b**2*(c**3-d**3)*x**3*y + a**2*(d**3-c**3)*x*y**3
 +c**2*(d**3-b**3)*x**3*z + c**2*(a**3-d**3)*y**3*z
 +a**2*(b**3-d**3)*x*z**3 + b**2*(d**3-a**3)*y*z**3
 +d**2*(b**3-c**3)*x**3*w + d**2*(c**3-a**3)*y**3*w
 +d**2*(a**3-b**3)*z**3*w + a**2*(c**3-b**3)*x*w**3
 +b**2*(a**3-c**3)*y*w**3 + c**2*(b**3-a**3)*z*w**3)
Q=sp.expand(Q)
grad=[sp.diff(Q,t) for t in (x,y,z,w)]

# The five source-prescribed singular sections, specialized at R=(1:2:3:4),
# all written in the affine chart w=1.
pts=[
 (sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4)),
 (sp.Rational(-1,2),sp.Rational(1,2),sp.Rational(3,4)),
 (sp.Rational(1,4),sp.Rational(-1),sp.Rational(3,4)),
 (sp.Rational(1,4),sp.Rational(1,2),sp.Rational(-3,2)),
 (sp.Rational(-1,8),sp.Rational(-1,4),sp.Rational(-3,8)),
]
for p in pts:
    sub={x:p[0],y:p[1],z:p[2],w:1}
    assert Q.subs(sub)==0
    assert all(g.subs(sub)==0 for g in grad)

# Exact singular-support exhaustion in w=1.
aff=[sp.expand(g.subs(w,1)) for g in grad]
G=sp.groebner(aff,x,y,z,order='lex',domain=sp.QQ)
elim=sp.factor(G.polys[-1].as_expr())
assert sp.expand(elim - (2*z+3)*(4*z-3)**4*(8*z+3)/sp.Integer(4096))==0
roots=[sp.Rational(-3,2),sp.Rational(3,4),sp.Rational(-3,8)]
found=[]
for zr in roots:
    sols=sp.solve([f.subs(z,zr) for f in aff],[x,y], dict=True)
    for s0 in sols:
        found.append((sp.simplify(s0[x]),sp.simplify(s0[y]),zr))
assert set(found)==set(pts)

# There are no singular points at infinity w=0. Cover P^2_{x:y:z} by z=1,
# then z=0,y=1, then the remaining point (1:0:0).
Gz=sp.groebner([g.subs({w:0,z:1}) for g in grad],x,y,order='lex',domain=sp.QQ)
assert len(Gz.polys)==1 and Gz.polys[0].as_expr()==1
Gy=sp.groebner([g.subs({w:0,z:0,y:1}) for g in grad],x,order='lex',domain=sp.QQ)
assert len(Gy.polys)==1 and Gy.polys[0].as_expr()==1
assert any(g.subs({w:0,z:0,y:0,x:1})!=0 for g in grad)

# At the moving triple point, the degree-three tangent cone is smooth in P^2.
u,v,s=sp.symbols('u v s')
R=pts[0]
loc=sp.Poly(sp.expand(Q.subs({x:R[0]+u,y:R[1]+v,z:R[2]+s,w:1})),u,v,s)
T=sp.expand(sum(coef*u**mon[0]*v**mon[1]*s**mon[2]
                for mon,coef in loc.terms() if sum(mon)==3))
assert sp.expand(T + sp.Rational(3,2)*(84*s**2*u-378*s**2*v-252*s*u**2+567*s*v**2+74*u**2*v-37*u*v**2))==0
dT=[sp.diff(T,t) for t in (u,v,s)]
for fixed,vars2 in [(s,(u,v)),(v,(u,s)),(u,(v,s))]:
    gg=sp.groebner([f.subs(fixed,1) for f in dT],*vars2,order='lex',domain=sp.QQ)
    assert len(gg.polys)==1 and gg.polys[0].as_expr()==1

# The four additional double points have nondegenerate affine Hessians, hence are A1 nodes.
H=sp.hessian(Q.subs(w,1),(x,y,z))
expected=[sp.Rational(10762227,2),-sp.Integer(530181288),sp.Rational(4921675101,2),-sp.Integer(121002336)]
for p,e in zip(pts[1:],expected):
    det=sp.factor(H.subs({x:p[0],y:p[1],z:p[2]}).det())
    assert det==e and det!=0

print('VERIFY_OK')
