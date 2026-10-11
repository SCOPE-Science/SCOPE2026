import sympy as s

rt3=s.sqrt(3)
r=2-rt3

normals=[
    s.Matrix([1,0]),
    s.Matrix([rt3/2,s.Rational(1,2)]),
    s.Matrix([s.Rational(1,2),rt3/2]),
    s.Matrix([0,1]),
    s.Matrix([-s.Rational(1,2),rt3/2]),
    s.Matrix([-rt3/2,s.Rational(1,2)]),
]
normals += [-v for v in normals]

def dot(a,b):
    return s.simplify(a.dot(b))

def norm(v):
    vals=[dot(f,v) for f in normals]
    return s.simplify(max(vals,key=lambda z: float(s.N(z))))

def vertex(j):
    f=normals[j%12]
    g=normals[(j+1)%12]
    A=s.Matrix([[f[0],f[1]],[g[0],g[1]]])
    return s.simplify(A.inv()*s.Matrix([1,1]))

verts=[vertex(j) for j in range(12)]

# Relevant exact points and active-facet geometry.
v11=verts[11]
v0=verts[0]
v3=verts[3]
e3=s.Matrix([0,1])
m4=normals[4]

assert s.simplify(v11-s.Matrix([1,-r]))==s.zeros(2,1)
assert s.simplify(v0-s.Matrix([1,r]))==s.zeros(2,1)
assert s.simplify(v3-s.Matrix([-r,1]))==s.zeros(2,1)

for j,v in enumerate(verts):
    assert norm(v)==1
    active=[i for i,f in enumerate(normals) if dot(f,v)==1]
    assert set(active)=={j,(j+1)%12}

assert norm(e3)==1
assert norm(m4)==1
assert dot(normals[0],e3)==0

# At v0 the normal cone is conv(n0,n1); y is BJ-admissible when endpoint
# evaluations have opposite signs or one is zero. Check endpoints of the reduced arc.
for y in (e3,v3,m4):
    a=dot(normals[0],y)
    b=dot(normals[1],y)
    assert s.simplify(a*b)<=0

d=(7+5*rt3)/26
mu=5*rt3-7
c=(17+rt3)/26
assert 0<float(c)<1
assert s.simplify(d*mu-1)==0

# Certificate on T_E.
hE=s.simplify(c*normals[1]+(1-c)*normals[2])
vals_E=[dot(hE,p) for p in (v11,v0,e3)]
assert vals_E[0]==d and vals_E[2]==d
assert s.simplify(vals_E[1]-d)>0

# Certificate on T_1.
vals_1=[dot(normals[2],p) for p in (v0,e3,v3)]
assert vals_1[0]==rt3-1 and vals_1[2]==rt3-1
assert vals_1[1]==rt3/2
assert all(s.simplify(v-d)>0 for v in vals_1)

# Certificate on T_2.
h2=s.simplify(c*normals[2]+(1-c)*normals[3])
vals_2=[dot(h2,p) for p in (v0,v3,m4)]
assert vals_2[0]==d and vals_2[2]==d
assert s.simplify(vals_2[1]-d)>0

# Equality chord.
a=s.simplify(1/(4-rt3))
z=s.simplify(a*v11+(1-a)*e3)
assert s.simplify(z-a*s.Matrix([1,1]))==s.zeros(2,1)
assert norm(z)==d
lam=s.simplify((1-a)/a)
assert lam==3-rt3
assert s.simplify((1+lam)/norm(v11+lam*e3)-mu)==0

# The explicit x,y are unit and Birkhoff--James orthogonal because n0 norms x and annihilates y.
assert norm(v11)==1 and norm(e3)==1
assert dot(normals[0],v11)==1
assert dot(normals[0],e3)==0

print("VERIFY_OK facets=12 canonical_triangles=3 min=(7+5sqrt3)/26 mu=5sqrt3-7")
