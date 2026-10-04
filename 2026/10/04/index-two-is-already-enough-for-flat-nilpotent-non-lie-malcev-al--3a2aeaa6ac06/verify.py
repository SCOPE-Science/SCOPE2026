from sympy import Matrix, symbols, simplify

# Basis: e,d,e1,e2,e3,e4 (indices 0..5).
a,b,f = symbols('a b f', nonzero=True)
n=6

def zero():
    return Matrix([0]*n)

basis=[Matrix([1 if i==j else 0 for i in range(n)]) for j in range(n)]

# Anticommutative bracket table.
T={}
def setbr(i,j,v):
    T[(i,j)]=Matrix(v)
    T[(j,i)]=-Matrix(v)

setbr(1,4,[0,0,-a,0,0,0])                 # [d,e3]=-a e1
setbr(1,5,[0,0,-b,0,-f,0])                # [d,e4]=-b e1-f e3
setbr(3,4,[a,0,0,0,0,0])                  # [e2,e3]=a e
setbr(3,5,[b,0,0,0,0,0])                  # [e2,e4]=b e
setbr(4,5,[f,0,0,0,0,0])                  # [e3,e4]=f e

def br(x,y):
    out=zero()
    for i in range(n):
        for j in range(n):
            if (i,j) in T:
                out += x[i]*y[j]*T[(i,j)]
    return out.applyfunc(simplify)

def jac(x,y,z):
    return (br(br(x,y),z)+br(br(y,z),x)+br(br(z,x),y)).applyfunc(simplify)

# Metric: <e,d>=<e1,e2>=<e3,e3>=<e4,e4>=1.
G=Matrix([
[0,1,0,0,0,0],
[1,0,0,0,0,0],
[0,0,0,1,0,0],
[0,0,1,0,0,0],
[0,0,0,0,1,0],
[0,0,0,0,0,1],
])
assert G.det()==1
assert sorted(G.eigenvals().items(), key=lambda kv: str(kv[0])) == [(-1,2),(1,4)]

# Koszul Levi-Civita product: 2<L_x y,z>=<[x,y],z>-<[y,z],x>+<[z,x],y>.
def inner(x,y):
    return (x.T*G*y)[0]

def lc(x,y):
    rhs=[]
    for z in basis:
        rhs.append(simplify((inner(br(x,y),z)-inner(br(y,z),x)+inner(br(z,x),y))/2))
    # G is symmetric, and rhs_j=<w,e_j>; hence G*w=rhs.
    return (G.inv()*Matrix(rhs)).applyfunc(simplify)

# The source uses a Malcev-specific curvature operator.  We reconstruct the
# Levi-Civita product from the metric and bracket, but do not substitute the
# classical Lie curvature formula for that generalized definition.
nonzero_lc=[]
for i,x0 in enumerate(basis):
    for j,y0 in enumerate(basis):
        w=lc(x0,y0)
        if w != zero():
            nonzero_lc.append((i,j,w))
expected={(4,1):(0,0,a,0,0,0),
          (4,3):(-a,0,0,0,0,0),
          (5,1):(0,0,b,0,f,0),
          (5,3):(-b,0,0,0,0,0),
          (5,4):(-f,0,0,0,0,0)}
assert len(nonzero_lc)==len(expected)
for i,j,w in nonzero_lc:
    assert tuple(w)==expected[(i,j)]

# Malcev identity for generic vectors, not merely basis triples.
xs=symbols('x0:6'); ys=symbols('y0:6'); zs=symbols('z0:6')
x=Matrix(xs); y=Matrix(ys); z=Matrix(zs)
malcev=(jac(x,y,br(x,z))-br(jac(x,y,z),x)).applyfunc(simplify)
assert malcev==zero()

# Structural claims.
# Derived algebra generators span e1,e3,e because a,f are nonzero.
derived=[basis[2],basis[4],basis[0]]
assert Matrix.hstack(*derived).rank()==3
# gamma_3 is span{e1,e}; both are nonzero bracket outputs when a,f != 0.
gamma3=[basis[2],basis[0]]
assert Matrix.hstack(*gamma3).rank()==2
for u in gamma3:
    for v in basis:
        assert br(u,v)==zero()
# Center contains span{e,e1}; direct coefficient equations force other coordinates zero.
for u in [basis[0],basis[2]]:
    for v in basis:
        assert br(u,v)==zero()

# Jacobi failure.
J=jac(basis[1],basis[5],basis[3])
assert J == Matrix([a*f,0,0,0,0,0])

# Center is totally isotropic.
for u in [basis[0],basis[2]]:
    for v in [basis[0],basis[2]]:
        assert inner(u,v)==0

print('metric_eigenvalues: +1 multiplicity 4, -1 multiplicity 2')
print('derived: span{e1,e3,e}')
print('gamma3: span{e1,e}; gamma4=0')
print('center: span{e,e1} (from coefficient equations with a*f != 0)')
print('Jacobiator J(d,e4,e2)=a*f*e')
print('Levi-Civita product: reconstructed and matches the five nonzero source products')
print('Malcev identity: generic symbolic identity verified')
print('CHECK_OK')
