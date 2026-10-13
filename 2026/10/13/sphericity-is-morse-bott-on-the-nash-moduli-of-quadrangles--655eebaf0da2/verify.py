#!/usr/bin/env python3
import sympy as sp

a,b,c,u,v,w = sp.symbols("a b c u v w", real=True)

lhs = 2*(a*a + 2*b*b + c*c)
rhs = (a+c)**2 + (a-c)**2 + 4*b*b
assert sp.expand(lhs-rhs) == 0

# Chart w=1 around all points of the aspect -1 line except [0:1:0].
hm = u**2/(u**2 + 1 + 4*v**2)
gm = [sp.simplify(sp.diff(hm,z)) for z in (u,v)]
Hm = sp.hessian(hm,(u,v))
assert all(sp.simplify(g.subs(u,0)) == 0 for g in gm)
Hm0 = sp.simplify(Hm.subs(u,0))
assert sp.simplify(Hm0[0,0] - 2/(1+4*v**2)) == 0
assert sp.simplify(Hm0[0,1]) == 0
assert sp.simplify(Hm0[1,0]) == 0
assert sp.simplify(Hm0[1,1]) == 0

# Remaining point of the line, in the chart v=1.
hr = u**2/(u**2 + w**2 + 4)
gr = [sp.simplify(sp.diff(hr,z)) for z in (u,w)]
Hr = sp.hessian(hr,(u,w))
point = {u:0,w:0}
assert all(sp.simplify(g.subs(point)) == 0 for g in gr)
Hr0 = Hr.subs(point)
assert Hr0 == sp.Matrix([[sp.Rational(1,2),0],[0,0]])

# Aspect +1 point, chart u=1.
hp = 1/(1 + w**2 + 4*v**2)
gp = [sp.simplify(sp.diff(hp,z)) for z in (v,w)]
Hp = sp.hessian(hp,(v,w))
origin = {v:0,w:0}
assert all(sp.simplify(g.subs(origin)) == 0 for g in gp)
Hp0 = Hp.subs(origin)
assert Hp0 == sp.Matrix([[-8,0],[0,-2]])
assert list(Hp0.eigenvals().keys()) == [-8,-2]

print("homogeneous_identity=OK")
print("aspect_minus_one_gradient=0")
print("aspect_minus_one_normal_hessian=positive_rank_1")
print("aspect_plus_one_gradient=0")
print("aspect_plus_one_hessian=eigenvalues(-8,-2)")
print("VERIFY_OK")
