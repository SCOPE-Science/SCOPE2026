import itertools
import sympy as sp

x,y,z,u,v = sp.symbols("x y z u v")
lam,mu = sp.symbols("lam mu")
vars_ = [x,y,z,u,v]
q = 3*z*u - 2*y*v + z*v
f = 6*x*y + 3*x*z + 3*y*z + 6*x*u + 12*x*v - 4*y*v - z*v - 6*u*v

J = sp.Matrix([[sp.diff(q,t) for t in vars_], [sp.diff(f,t) for t in vars_]])
mins = [sp.expand(J[0,i]*J[1,j]-J[0,j]*J[1,i]) for i,j in itertools.combinations(range(5),2)]
ideal = [q,f] + mins

expected = {
    x: [y,z,u,v],
    y: [x,z,u+1,v],
    z: [sp.Integer(1)],
    u: [x,y+1,z,v],
    v: [sp.Integer(1)],
}
for chart in vars_:
    cvars = [t for t in vars_ if t != chart]
    G = sp.groebner([sp.expand(p.subs(chart,1)) for p in ideal], *cvars, order="lex", domain=sp.QQ)
    got = [sp.expand(g.as_expr()) for g in G.polys]
    want = [sp.expand(g) for g in expected[chart]]
    assert got == want, (chart, got, want)

# Local node at P=[1:0:0:0:0].  On x=1, solve f=0 for u.
f1 = sp.expand(f.subs(x,1))
uexpr = sp.solve(sp.Eq(f1,0),u)[0]
loc1 = sp.factor(q.subs({x:1,u:uexpr}))
num1,den1 = sp.fraction(sp.together(loc1))
assert sp.expand(den1 - 2*(v-1)) == 0
H1 = sp.hessian(num1,(y,z,v)).subs({y:0,z:0,v:0})
assert sp.det(H1) == 384

# Local node at Q=[0:1:0:-1:0].  Put y=1, u=U-1.
X,Z,U,V = sp.symbols("X Z U V")
q2 = sp.expand(q.subs({x:X,y:1,z:Z,u:U-1,v:V}))
f2 = sp.expand(f.subs({x:X,y:1,z:Z,u:U-1,v:V}))
g2 = sp.expand(f2+q2)
Vexpr = sp.solve(sp.Eq(q2,0),V)[0]
loc2 = sp.factor(g2.subs(V,Vexpr))
num2,den2 = sp.fraction(sp.together(loc2))
assert sp.expand(den2 - (Z-2)) == 0
H2 = sp.hessian(num2,(X,U,Z)).subs({X:0,U:0,Z:0})
assert sp.det(H2) == 17280

# Symmetric matrices for q and f.
def quad_matrix(poly, variables):
    M = sp.zeros(len(variables))
    P = sp.Poly(poly,*variables,domain=sp.QQ)
    for mon,coef in P.terms():
        assert sum(mon) == 2
        inds = [i for i,e in enumerate(mon) for _ in range(e)]
        i,j = inds
        if i == j:
            M[i,i] += coef
        else:
            M[i,j] += coef/2
            M[j,i] += coef/2
    return M
A = quad_matrix(q,vars_)
B = quad_matrix(f,vars_)
assert sp.expand((sp.Matrix(vars_).T*A*sp.Matrix(vars_))[0] - q) == 0
assert sp.expand((sp.Matrix(vars_).T*B*sp.Matrix(vars_))[0] - f) == 0
D = sp.factor((lam*A+mu*B).det())
assert sp.expand(D - 54*mu**2*(lam-mu)**2*(lam+4*mu)) == 0
assert A.rank() == 4
assert (A+B).rank() == 4
assert A*sp.Matrix([1,0,0,0,0]) == sp.zeros(5,1)
assert (A+B)*sp.Matrix([0,1,0,-1,0]) == sp.zeros(5,1)

# The line joining the two nodes lies on the surface.
s,t = sp.symbols("s t")
line = {x:s,y:t,z:0,u:-t,v:0}
assert sp.expand(q.subs(line)) == 0
assert sp.expand(f.subs(line)) == 0

print("VERIFY_OK")
