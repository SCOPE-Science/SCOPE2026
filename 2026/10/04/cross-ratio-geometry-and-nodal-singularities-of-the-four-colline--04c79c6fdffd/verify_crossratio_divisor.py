import sympy as sp

v1,v2,v3,v4 = sp.symbols('v1 v2 v3 v4')
y1,y2,y3,y4 = sp.symbols('y1 y2 y3 y4')
z1,z2,z3,z4 = sp.symbols('z1 z2 z3 z4')
t1,t2,t3,t4 = sp.symbols('t1 t2 t3 t4')
a,b,c,d = sp.symbols('a b c d')
vs=[v1,v2,v3,v4]
ys=[y1,y2,y3,y4]
zs=[z1,z2,z3,z4]
ts=[t1,t2,t3,t4]

# Published four-collinear correction determinant (Example 5.5 of arXiv:2303.02066).
F = sp.expand(sp.Matrix([
    [v1*z1, v2*z2, v3*z3, v4*z4],
    [v1*y1, v2*y2, v3*y3, v4*y4],
    [z1,    z2,    z3,    z4],
    [y1,    y2,    y3,    y4],
]).det())

br=lambda i,j: sp.expand(zs[i]*ys[j]-zs[j]*ys[i])
F_br = sp.expand(
    (v1-v4)*(v2-v3)*br(0,2)*br(1,3)
    - (v1-v3)*(v2-v4)*br(0,3)*br(1,2)
)
assert sp.expand(F-F_br) == 0

# On y_i != 0, t_i=z_i/y_i and F/(prod y_i) is the cross-ratio numerator.
D = sp.expand(sp.Matrix([
    [v1*t1, v2*t2, v3*t3, v4*t4],
    [v1,    v2,    v3,    v4],
    [t1,    t2,    t3,    t4],
    [1,     1,     1,     1],
]).det())
subs_aff={z1:t1*y1,z2:t2*y2,z3:t3*y3,z4:t4*y4}
assert sp.expand(F.subs(subs_aff) - y1*y2*y3*y4*D) == 0
cross_num = sp.expand(
    (v1-v4)*(v2-v3)*(t1-t3)*(t2-t4)
    - (v1-v3)*(v2-v4)*(t1-t4)*(t2-t3)
)
assert sp.expand(D-cross_num) == 0

# Every projective transform t=(a v+b)/(c v+d) lies on the divisor after clearing denominators.
phi_sub={
    z1:a*v1+b, y1:c*v1+d,
    z2:a*v2+b, y2:c*v2+d,
    z3:a*v3+b, y3:c*v3+d,
    z4:a*v4+b, y4:c*v4+d,
}
assert sp.expand(F.subs(phi_sub)) == 0

# Singular-locus certificate on an affine target chart.
H = sp.Matrix([[sp.diff(D,ti,tj) for tj in ts] for ti in ts])
assert all(sp.expand(sum(H[i,j] for j in range(4))) == 0 for i in range(4))
Delta = sp.prod(vs[j]-vs[i] for i in range(4) for j in range(i+1,4))
# With the chosen ordering, the principal minors have the following sign.
principal=[]
for omit in range(4):
    inds=[i for i in range(4) if i!=omit]
    principal.append(sp.factor(H.extract(inds,inds).det()))
for q in principal:
    assert sp.expand(q - 2*Delta) == 0

# D is exactly the quadratic form 1/2 t^T H t; hence grad(D)=H t.
T=sp.Matrix(ts)
assert sp.expand(D - (T.T*H*T)[0]/2) == 0
for i,ti in enumerate(ts):
    assert sp.expand(sp.diff(D,ti) - (H*T)[i]) == 0

# Concrete specialization checks the rank-3 Hessian and diagonal singular locus.
Hv=H.subs({v1:0,v2:1,v3:2,v4:3})
assert Hv.rank()==3
assert Hv.nullspace()==[sp.Matrix([1,1,1,1])]
Dv=sp.expand(D.subs({v1:0,v2:1,v3:2,v4:3}))
for s in [0,1,sp.Rational(5,7)]:
    sub={t1:s,t2:s,t3:s,t4:s}
    assert Dv.subs(sub)==0
    assert all(sp.diff(Dv,t).subs(sub)==0 for t in ts)
# A non-diagonal point on the divisor is smooth (identity transform t_i=v_i).
sub_id={t1:0,t2:1,t3:2,t4:3}
assert Dv.subs(sub_id)==0
assert any(sp.diff(Dv,t).subs(sub_id)!=0 for t in ts)

print('VERIFY_OK')
print('bracket_identity=PASS')
print('cross_ratio_identity=PASS')
print('PGL2_orbit_vanishing=PASS')
print('hessian_principal_minors=2*Vandermonde')
print('singular_locus_certificate=diagonal')
