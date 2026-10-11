import sympy as sp

a = sp.symbols("a", real=True)
rt3 = sp.sqrt(3)
pi = sp.pi

q = (5 - 2*rt3) / 13
A = 4 - rt3 + (4*rt3 - 7)*a
B0 = 4 - rt3 + (2*rt3 - 4)*a
B1 = 3*rt3 - 3 + (7 - 4*rt3)*a
C = 2*rt3 - 2 + (5 - 3*rt3)*a

F0 = sp.cancel((A*A + B0*B0)/(5*C*C))
F1 = sp.cancel((A*A + B1*B1)/(5*C*C))

d0 = 3*a*(7+4*rt3)/(5*(4+2*rt3-a)**3)
d1 = (2+rt3)*(a+69+40*rt3)/(5*(4+2*rt3-a)**3)

assert sp.simplify(sp.diff(F0,a)-d0) == 0
assert sp.simplify(sp.diff(F1,a)-d1) == 0
assert sp.simplify(B0.subs(a,q)-B1.subs(a,q)) == 0
assert 0 < float(sp.N(q,50)) < 0.5

v0 = sp.Matrix([1,0])
v1 = sp.Matrix([rt3/2,sp.Rational(1,2)])
x = (1-a)*v0 + a*v1
R = lambda z: sp.Matrix([-z[1],z[0]])
y = R(x)

den = sp.cos(pi/12)
normals = [
    sp.Matrix([sp.cos((2*j+1)*pi/12), sp.sin((2*j+1)*pi/12)])
    for j in range(6)
]

def signed_facet_values(z):
    return [sp.trigsimp(n.dot(z)/den) for n in normals]

def affine_nonnegative_on(expr, lo, hi):
    vlo = sp.simplify(expr.subs(a,lo))
    vhi = sp.simplify(expr.subs(a,hi))
    return float(sp.N(vlo,60)) >= -1e-45 and float(sp.N(vhi,60)) >= -1e-45

def prove_norm_formula(z, candidate, lo, hi):
    vals = signed_facet_values(z)
    for e in vals:
        # candidate >= |e| is equivalent to two affine inequalities.
        assert affine_nonnegative_on(candidate-e,lo,hi)
        assert affine_nonnegative_on(candidate+e,lo,hi)
    # At least one signed facet equals the candidate identically on this interval.
    assert any(sp.simplify(candidate-e)==0 or sp.simplify(candidate+e)==0 for e in vals)

# The reference edge consists of unit vectors.
prove_norm_formula(x, sp.Integer(1), sp.Integer(0), sp.Integer(1))

# Exact active facets on the half-edge.
prove_norm_formula(x+2*y, A, sp.Integer(0), sp.Rational(1,2))
prove_norm_formula(2*x+y, B0, sp.Integer(0), q)
prove_norm_formula(2*x+y, B1, q, sp.Rational(1,2))
prove_norm_formula(x+y, C, sp.Integer(0), sp.Rational(1,2))

# Quarter-turn isometry: it permutes the vertex set.
verts = [
    sp.Matrix([sp.cos(k*pi/6),sp.sin(k*pi/6)])
    for k in range(12)
]
for k,v in enumerate(verts):
    assert sp.simplify(R(v)-verts[(k+3)%12]) == sp.zeros(2,1)

# Equality pair and exact value.
half = sp.Rational(1,2)
xh = sp.simplify(x.subs(a,half))
yh = sp.simplify(y.subs(a,half))
assert xh == sp.Matrix([(2+rt3)/4,sp.Rational(1,4)])
assert yh == sp.Matrix([-sp.Rational(1,4),(2+rt3)/4])

Ah = sp.simplify(A.subs(a,half))
Bh = sp.simplify(B1.subs(a,half))
Ch = sp.simplify(C.subs(a,half))
assert sp.simplify(Ah-(rt3+sp.Rational(1,2))) == 0
assert sp.simplify(Bh-(rt3+sp.Rational(1,2))) == 0
assert sp.simplify(Ch-(1+rt3)/2) == 0

target = sp.Rational(14,5)-rt3
assert sp.simplify(F1.subs(a,half)-target) == 0

print(
    "VERIFY_OK "
    f"facets={len(normals)} transition={float(sp.N(q,16)):.15f} "
    f"omega={float(sp.N(target,16)):.15f} "
    "profile_branches=2 maximizer=edge_midpoint"
)
