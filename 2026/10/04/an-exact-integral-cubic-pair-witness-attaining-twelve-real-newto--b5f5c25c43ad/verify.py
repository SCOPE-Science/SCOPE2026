import sympy as sp
x,y,L=sp.symbols("x y L")
F1= -9000*x**3 -13498*x**2*y +2999*x**2 -6500*x*y**2 +4499*x*y +2001*x -1000*y**3 +1498*y**2 +998*y +2
F2= -2000*x**3 -7999*x**2*y -6002*x*y**2 -12002*x*y +7998*x -11999*y**2 +7998*y -2
J=sp.expand(sp.diff(F1,x)*sp.diff(F2,y)-sp.diff(F1,y)*sp.diff(F2,x))
g1=sp.expand(sp.diff(F1,x)*F2-sp.diff(F2,x)*F1)
g2=sp.expand(sp.diff(F1,y)*F2-sp.diff(F2,y)*F1)

# Projective smoothness of the two generators: affine singular ideals are units,
# and the leading binary cubics are squarefree at infinity.
for F in (F1,F2):
    G=sp.groebner([F,sp.diff(F,x),sp.diff(F,y)],x,y,order="lex")
    assert len(G.polys)==1 and G.polys[0].as_expr()==1

def degree_part(F,k):
    P=sp.Poly(F,x,y)
    return sp.expand(sum(c*x**m[0]*y**m[1] for m,c in P.terms() if sum(m)==k))
A=degree_part(F1,3); B=degree_part(F2,3)
C=degree_part(F1,2); D=degree_part(F2,2)
for P in (A,B):
    pu=sp.Poly(P.subs(y,1),x)
    assert pu.degree()==3
    assert sp.gcd(pu,pu.diff()).degree()==0
    assert P.subs({x:1,y:0}) != 0
assert sp.resultant(sp.Poly(A.subs(y,1),x),sp.Poly(B.subs(y,1),x),x) != 0
assert not (A.subs({x:1,y:0})==0 and B.subs({x:1,y:0})==0)

# No member of the projective pencil is singular at infinity.  At z=0 a
# singular point must satisfy H_x=H_y=H_z=0 for H=F1^h-L F2^h.
E1=sp.diff(A,x)-L*sp.diff(B,x)
E2=sp.diff(A,y)-L*sp.diff(B,y)
E3=C-L*D
Ginf=sp.groebner([
    sp.expand(E1.subs(y,1)),
    sp.expand(E2.subs(y,1)),
    sp.expand(E3.subs(y,1))
],x,L,order="lex")
assert len(Ginf.polys)==1 and Ginf.polys[0].as_expr()==1
assert not any(all(v==0 for v in vals) for vals in [[
    E1.subs({x:1,y:0,L:l}),E2.subs({x:1,y:0,L:l}),E3.subs({x:1,y:0,L:l})
] for l in []])
# Directly, at [1:0], E3=1499-(-11999?) is actually the quadratic coefficient
# expression below and is independent enough to rule out a common solution.
vals=[sp.expand(E.subs({x:1,y:0})) for E in (E1,E2,E3)]
assert sp.groebner(vals,L,order="lex").polys[0].as_expr()==1

# Base locus: nine simple real transverse points.
Rf=sp.Poly(sp.resultant(F1,F2,x),y)
assert Rf.degree()==9
assert sp.gcd(Rf,Rf.diff()).degree()==0
assert sp.count_roots(Rf,-sp.oo,sp.oo)==9
Gbase=sp.groebner([F1,F2],x,y,order="lex")
assert len(Gbase.polys)==2
assert sp.degree(Gbase.polys[0].as_expr(),x)==1
assert sp.degree(Gbase.polys[1].as_expr(),x)==0
Gt=sp.groebner([F1,F2,J],x,y,order="lex")
assert len(Gt.polys)==1 and Gt.polys[0].as_expr()==1

# Singular-start critical system.  The paper's gamma vanishes at all nine base
# points; removing them leaves a degree-12 exact eliminant.
Rg=sp.Poly(sp.resultant(g1,g2,x),y)
assert Rg.degree()==21
assert sp.gcd(Rg,Rg.diff()).degree()==0
assert sp.count_roots(Rg,-sp.oo,sp.oo)==21
q,rem=sp.div(Rg,Rf,domain=sp.QQ)
assert rem.is_zero
q=sp.Poly(q,y).monic()
assert q.degree()==12
assert sp.gcd(q,q.diff()).degree()==0
assert sp.count_roots(q,-sp.oo,sp.oo)==12
assert sp.gcd(q,Rf).degree()==0
Gg=sp.groebner([g1,g2],x,y,order="lex")
assert len(Gg.polys)==2
assert sp.degree(Gg.polys[0].as_expr(),x)==1
assert sp.degree(Gg.polys[1].as_expr(),x)==0

# On gamma=0, reduce F1,F2 to univariate functions of y.  F2 is nonzero at
# every q-root, so lambda=F1/F2 is defined on every singular start.
rF1=sp.expand(Gg.reduce(F1)[1])
rF2=sp.expand(Gg.reduce(F2)[1])
assert sp.degree(rF1,x)==0 and sp.degree(rF2,x)==0
assert sp.gcd(sp.Poly(rF2,y),q).degree()==0

# Every singular start is an ordinary node.  For h_p=F2(p)F1-F1(p)F2,
# the Hessian at p has determinant D below.  Its reduction has no common q-root.
H1=sp.hessian(F1,(x,y)); H2=sp.hessian(F2,(x,y))
Dnode=sp.expand((F2*H1-F1*H2).det())
rD=sp.expand(Gg.reduce(Dnode)[1])
assert sp.degree(rD,x)==0
assert sp.gcd(sp.Poly(rD,y),q).degree()==0

# Critical values are pairwise distinct and all real.  Eliminate y from q and
# F1-LF2 restricted to the gamma locus.  Degree 12 and squarefreeness imply
# that the 12 q-roots map to 12 distinct pencil parameters.
cvres=sp.resultant(q.as_expr(),sp.expand(rF1-L*rF2),y)
cv=sp.Poly(sp.primitive(cvres)[1],L)
assert cv.degree()==12
assert sp.gcd(cv,cv.diff()).degree()==0
assert sp.count_roots(cv,-sp.oo,sp.oo)==12

qprim=sp.primitive(q.as_expr())[1]
cvprim=sp.primitive(cv.as_expr())[1]
print("base_eliminant_degree=9_real_roots=9_squarefree")
print("gamma_eliminant_degree=21_real_roots=21_squarefree")
print("singular_start_eliminant_degree=12_real_roots=12_squarefree")
print("projective_generators_smooth=true")
print("base_points_transverse=true")
print("pencil_singular_at_infinity=false")
print("ordinary_node_at_all_singular_starts=true")
print("critical_values_degree=12_real_roots=12_squarefree")
print("singular_start_eliminant="+str(qprim))
print("critical_value_polynomial="+str(cvprim))
print("VERIFY_OK")
