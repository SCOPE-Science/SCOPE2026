import sympy as sp

a,b,p,q,t=sp.symbols('a b p q t')
F=(a*a+b*b+p*q)**2-4*(a*a*b*b+p*q)
Fa,Fb,Fp,Fq=[sp.factor(sp.diff(F,z)) for z in (a,b,p,q)]
assert Fa == 4*a*(a*a + p*q - b*b)
assert Fb == 4*b*(-a*a + p*q + b*b)
assert Fp == 2*q*(a*a+b*b+p*q-2)
assert Fq == 2*p*(a*a+b*b+p*q-2)

# Every listed line is contained in the hypersurface and its Jacobian zero set.
polys=[F,Fa,Fb,Fp,Fq]
for sb in (1,-1):
    for g in polys:
        assert sp.expand(g.subs({b:sb*a,p:0,q:0})) == 0
for ea in (1,-1):
    for eb in (1,-1):
        for zero,free in ((p,q),(q,p)):
            for g in polys:
                assert sp.expand(g.subs({a:ea,b:eb,zero:0})) == 0

# Hessian rank-three certificates on generic points of the singular lines.
H=sp.hessian(F,(a,b,p,q))
Hmain=H.subs({a:t,b:t,p:0,q:0})
main_minor=sp.factor(Hmain.extract([0,2,3],[0,2,3]).det())
assert main_minor == -128*t**2*(t-1)**2*(t+1)**2
Hiso=H.subs({a:1,b:1,p:0,q:t})
iso_minor=sp.factor(Hiso.extract([0,1,2],[0,1,2]).det())
assert iso_minor == -512*t**2

# Origin normal form and its nonreduced Jacobian singular scheme.
u,v,P,Q=sp.symbols('u v P Q')
origin_identity=sp.expand((a*a-b*b)**2-p*q*(4-2*(a*a+b*b)-p*q)-F)
assert origin_identity == 0
unit0=4-2*(a*a+b*b)-p*q
assert unit0.subs({a:0,b:0,p:0,q:0}) == 4
G0=P*Q-u**2*v**2
grad0=[sp.diff(G0,z) for z in (P,Q,u,v)]
assert grad0 == [Q,P,-2*u*v**2,-2*u**2*v]
# Modulo (u^2 v, u v^2), uv survives, but u(uv), v(uv), and (uv)^2 vanish.
Gb=sp.groebner([u**2*v,u*v**2],u,v,order='lex')
assert Gb.reduce(u*v)[1] == u*v
assert Gb.reduce(u*(u*v))[1] == 0
assert Gb.reduce(v*(u*v))[1] == 0
assert Gb.reduce((u*v)**2)[1] == 0
# The radical support is the two coordinate axes: radical (uv).
assert sp.factor(u*v) == u*v

# Triple-branch vertex normal form.
U,V=sp.symbols('U V')
vv,uu=sp.symbols('vv uu')
a_sub=1+(vv+uu)/2
b_sub=1+(vv-uu)/2
F_vertex=sp.expand(F.subs({a:a_sub,b:b_sub}))
vertex_rhs=sp.expand(uu**2*((vv+2)**2+p*q)+p*q*(vv*(vv+4)+p*q))
assert sp.expand(F_vertex-vertex_rhs) == 0
A=(vv+2)**2+p*q
B=vv*(vv+4)+p*q
assert A.subs({vv:0,p:0,q:0}) == 4
assert sp.diff(B,vv).subs({vv:0,p:0,q:0}) == 4
Gv=U**2+V*p*q
gradv=[sp.diff(Gv,z) for z in (U,V,p,q)]
assert gradv == [2*U,p*q,V*q,V*p]

print('main_hessian_minor=', main_minor)
print('isotropic_hessian_minor=', iso_minor)
print('origin_unit_at_zero=', unit0.subs({a:0,b:0,p:0,q:0}))
print('origin_singular_ideal=(P,Q,u*v^2,u^2*v)')
print('origin_reduced_radical=(P,Q,u*v)')
print('origin_nilradical_generator=u*v; length=1; square_zero=True')
print('vertex_A_at_zero=', A.subs({vv:0,p:0,q:0}), 'dBdv_at_zero=', sp.diff(B,vv).subs({vv:0,p:0,q:0}))
print('VERIFY_OK')
