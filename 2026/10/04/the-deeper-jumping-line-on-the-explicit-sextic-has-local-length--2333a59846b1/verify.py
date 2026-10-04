import sympy as sp
import itertools

X,Y,Z,u,v,x,y=sp.symbols("X Y Z u v x y")
F0=sp.prod(X-i*Y for i in range(6)) + Z**2*(X**4+Y**4+Z**4+X*Y*Z*(X+Y+Z))

ders=[sp.diff(F0,t) for t in (X,Y,Z)]
sub={X:x,Y:y,Z:u*x+v*y}
cols=[]
for d in ders:
    e=sp.expand(d.subs(sub))
    cols.extend([sp.expand(x*e),sp.expand(y*e)])

mons=[x**(6-k)*y**k for k in range(7)]
M=sp.Matrix([[sp.Poly(c,x,y).coeff_monomial(m) for c in cols] for m in mons])
M0=M.subs({u:0,v:0})

assert M.shape==(7,6)
assert M0.rank()==4
minor4=M0.extract([0,1,2,3],[0,1,2,3]).det()
assert minor4==-23520

K=sp.Matrix.hstack(*M0.nullspace())
C=sp.Matrix.hstack(*M0.T.nullspace())
assert K.shape==(6,2)
assert C.shape==(7,3)

Mu=M.diff(u).subs({u:0,v:0})
Mv=M.diff(v).subs({u:0,v:0})
A=sp.expand(C.T*Mu*K)*u + sp.expand(C.T*Mv*K)*v

qs=[]
for rr in itertools.combinations(range(3),2):
    qs.append(sp.expand(A.extract(rr,[0,1]).det()))

basis=[u**2,u*v,v**2]
Q=sp.Matrix([[sp.Poly(q,u,v).coeff_monomial(b) for b in basis] for q in qs])
detQ=sp.factor(Q.det())
assert detQ==sp.Rational(2655279064360000,2401)
assert detQ!=0

print("matrix_shape=7x6")
print("rank_at_l0=4")
print("invertible_4x4_minor=-23520")
print("normal_quadratic_coefficient_determinant="+str(detQ))
print("quadratic_initial_minors_span=m^2/m^3")
print("local_length=3")
print("VERIFY_OK")
