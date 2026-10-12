from sympy import Matrix, symbols, simplify, solve

# Basis vectors are columns in the ordered basis (t,x).
a,b,c,d,r,s,lam,beta = symbols('a b c d r s lam beta', nonzero=False)
t = Matrix([1,0])
x = Matrix([0,1])
P = Matrix([[a,b],[c,d]])

def bracket(u,v):
    # [u0 t+u1 x, v0 t+v1 x] = (u0*v1-u1*v0) x
    return Matrix([0, u[0]*v[1]-u[1]*v[0]])

def phi(u,v,M=P):
    return (u.T*M*v)[0]

# Kato identity residual: phi([u,v],w)+phi(v,[u,w])-phi(u,[v,w]).
basis=[t,x]
res=[]
for u in basis:
    for v in basis:
        for w in basis:
            res.append(simplify(phi(bracket(u,v),w)+phi(v,bracket(u,w))-phi(u,bracket(v,w))))
nonzero = sorted({str(e) for e in res if e != 0})
assert set(nonzero) == {'-b - c', '-2*d', '2*d', 'b + c'}

# Under char != 2 the solution is c=-b,d=0; determinant is b^2.
Pab=Matrix([[a,b],[-b,0]])
assert simplify(Pab.det()-b**2)==0

# Solve the induced product from Pab*w pairing equations.
def induced(u,v):
    q0,q1=symbols('q0 q1')
    q=Matrix([q0,q1])
    eqs=[]
    for z in basis:
        eqs.append(simplify(phi(q,z,Pab)+phi(v,bracket(u,z),Pab)))
    sol=solve(eqs,[q0,q1],dict=True)[0]
    return Matrix([simplify(sol[q0]),simplify(sol[q1])])

products = {
    'tt': induced(t,t),
    'tx': induced(t,x),
    'xt': induced(x,t),
    'xx': induced(x,x),
}
assert products['tt'] == Matrix([-1,-a/b])
assert products['tx'] == Matrix([0,0])
assert products['xt'] == Matrix([0,-1])
assert products['xx'] == Matrix([0,0])

# Work with r=a/b.  Left multiplications verify the pre-Lie identity.
Lt=Matrix([[-1,0],[-r,0]])
Lx=Matrix([[0,0],[-1,0]])
assert simplify(Lt*Lx-Lx*Lt-Lx) == Matrix.zeros(2)

# Every Lie automorphism has t -> t+beta*x, x -> lam*x (lam != 0).
T=Matrix([[1,0],[beta,lam]])
pull=simplify(T.T*Pab*T)
assert pull == Matrix([[a,b*lam],[-b*lam,0]])

# LSA isomorphism P_r -> P_s through such an automorphism forces s=r*lam.
# Check t*t; all other products are then automatically respected.
left_image = Matrix([-1, -(beta+r*lam)])
right_product = Matrix([-1, -(s+beta)])
assert simplify(left_image-right_product) == Matrix([0, s-r*lam])

# Idempotents v=alpha*t+gamma*x solve the displayed equations.
alpha,gamma=symbols('alpha gamma')
# v*v - v for P_r:
def prod_r(u,v):
    # bilinear from t*t=-t-rx, t*x=0, x*t=-x, x*x=0
    return Matrix([-u[0]*v[0], -r*u[0]*v[0]-u[1]*v[0]])
v=Matrix([alpha,gamma])
id_res=simplify(prod_r(v,v)-v)
assert all(simplify(e)==0 for e in (id_res-Matrix([-alpha**2-alpha, -alpha**2*r-alpha*gamma-gamma])))
# For alpha=-1 the second residual equals -r; alpha=0 forces gamma=0.
assert simplify(id_res.subs(alpha,-1)) == Matrix([0,-r])
assert simplify(id_res.subs(alpha,0)) == Matrix([0,-gamma])

print('NDB_RESIDUALS', nonzero)
print('FORM_MATRIX', Pab)
print('PRODUCTS', products)
print('AUT_PULLBACK', pull)
print('ISO_DEFECT', simplify(left_image-right_product))
print('IDEMPOTENT_DEFECT_ALPHA_MINUS_ONE', simplify(id_res.subs(alpha,-1)))
print('CHECK_OK')
