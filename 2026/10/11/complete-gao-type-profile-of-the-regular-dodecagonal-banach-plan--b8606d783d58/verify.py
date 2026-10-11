import sympy as s

rt3=s.sqrt(3)
r=2-rt3
q=rt3-1
half=s.Rational(1,2)

def simp(x):
    return s.simplify(s.expand(x))

# Signed facet normals, represented without trigonometric ambiguity.
facets=[
    (s.Integer(1),s.Integer(0)),
    (rt3/2,s.Rational(1,2)),
    (s.Rational(1,2),rt3/2),
    (s.Integer(0),s.Integer(1)),
    (-s.Rational(1,2),rt3/2),
    (-rt3/2,s.Rational(1,2)),
    (-s.Integer(1),s.Integer(0)),
    (-rt3/2,-s.Rational(1,2)),
    (-s.Rational(1,2),-rt3/2),
    (s.Integer(0),-s.Integer(1)),
    (s.Rational(1,2),-rt3/2),
    (rt3/2,-s.Rational(1,2)),
]

def dot(f,v):
    return simp(f[0]*v[0]+f[1]*v[1])

# Vertex v_k is the intersection of facets k and k+1.
verts=[]
for k in range(12):
    f=facets[k]
    g=facets[(k+1)%12]
    M=s.Matrix([[f[0],f[1]],[g[0],g[1]]])
    b=s.Matrix([1,1])
    sol=M.LUsolve(b)
    verts.append((simp(sol[0]),simp(sol[1])))

# Every vertex lies in all halfspaces and exactly on its two incident facets.
for k,v in enumerate(verts):
    vals=[dot(f,v) for f in facets]
    assert all(s.N(z)<=1+1e-12 for z in vals)
    tight=[i for i,z in enumerate(vals) if simp(z-1)==0]
    assert set(tight)=={k,(k+1)%12}

# Edge E_k is facet k, with endpoints v_{k-1},v_k.
edges=[]
for k in range(12):
    edges.append([verts[(k-1)%12],verts[k]])

# Exact support certificates for E_0 versus E_k, k=2,...,6.
# The listed signed facet gives a uniform lower bound on N(x-y).
witness={2:10,3:0,4:0,5:0,6:0}
target={
    2:2*r,
    3:q,
    4:1+r,
    5:rt3,
    6:s.Integer(2),
}
for k in range(2,7):
    f=facets[witness[k]]
    vals=[dot(f,(simp(a[0]-b[0]),simp(a[1]-b[1])))
          for a in edges[0] for b in edges[k]]
    assert min(vals,key=lambda z:float(s.N(z))) == target[k]
    assert all(s.simplify(z-target[k])>=0 for z in vals)
    assert s.simplify(target[k]-2*r)>=0

assert s.simplify(2*r-half)>0

# Critical algebra.
assert simp(r*(2+rt3)-1)==0
assert simp(4*r-(1+r**2))==0
assert simp(rt3/2+(r-half)/r)==0

# Symbolic adjacent-edge extremizer family.
t=s.symbols('t', real=True)
x=(s.Integer(1), simp(r*(1-2*t)))
y=(simp(1-r*t), simp(r+rt3*r*t))
d=(simp(x[0]-y[0]),simp(x[1]-y[1]))
sm=(simp(x[0]+y[0]),simp(x[1]+y[1]))
assert d==(simp(r*t),-t)

# x lies on facet 0; y lies on facet 1.
assert simp(dot(facets[0],x)-1)==0
assert simp(dot(facets[1],y)-1)==0

# For 0<=t<=1/2, the claimed active facets of d and sm evaluate to t and 2-r t.
assert simp(-d[1]-t)==0
assert simp(dot(facets[0],sm)-(2-r*t))==0
assert simp(dot(facets[1],sm)-(2-r*t))==0

# Check all facet inequalities symbolically at t=0 and t=1/2.
# Every facet evaluation is affine in t, so endpoint checks certify the whole interval.
for v in (x,y):
    for f in facets:
        expr=simp(dot(f,v))
        for tv in (s.Integer(0),half):
            assert s.N(expr.subs(t,tv))<=1+1e-12

for f in facets:
    expr=simp(dot(f,d))
    for tv in (s.Integer(0),half):
        val=simp(expr.subs(t,tv))
        assert s.N(val)<=s.N(tv)+1e-12
for f in facets:
    expr=simp(dot(f,sm))
    for tv in (s.Integer(0),half):
        val=simp(expr.subs(t,tv))
        rhs=simp(2-r*tv)
        assert s.N(val)<=s.N(rhs)+1e-12

# Balanced p>=2 pair.
e1=(s.Integer(1),s.Integer(0))
e2=(s.Integer(0),s.Integer(1))
ap=(simp((1+rt3)/2))
for z in ((1,1),(1,-1)):
    vals=[dot(f,z) for f in facets]
    assert max(vals,key=lambda w:float(s.N(w)))==ap

# Junction identity at p=2.
q2=r
left=simp((1+q2**2)/(1+r*q2)**2)
right=simp(2*((1+rt3)/4)**2)
assert simp(left-right)==0
assert simp(left-(2+rt3)/4)==0

print("VERIFY_OK vertices=12 facets=12 nonincident_edge_cases=5 junction=p2")
