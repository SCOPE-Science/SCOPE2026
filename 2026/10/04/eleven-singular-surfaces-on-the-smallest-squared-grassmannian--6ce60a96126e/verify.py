import sympy as s
from itertools import product

a,b,c,d,e,f=s.symbols('a b c d e f')
Q=s.Matrix([[0,a,b,c],[a,0,d,e],[b,d,0,f],[c,e,f,0]])
F=s.expand(Q.det())
F0=s.expand(a*a*f*f+b*b*e*e+c*c*d*d-2*a*b*e*f-2*a*c*d*f-2*b*c*d*e)
assert s.expand(F-F0)==0
X= a*f-b*e-c*d
Y= a*f-b*e+c*d
Z= a*f+b*e-c*d
fac = {
 a:2*f*X, f:2*a*X,
 b:-2*e*Y, e:-2*b*Y,
 c:-2*d*Z, d:-2*c*Z,
}
for v,rhs in fac.items():
    assert s.expand(s.diff(F,v)-rhs)==0

# Eight coordinate planes: select one from each opposite pair (a,f),(b,e),(c,d), set complement to zero.
pairs=[(a,f),(b,e),(c,d)]
planes=[]
for bits in product([0,1],repeat=3):
    keep=[pairs[i][bits[i]] for i in range(3)]
    zero=[pairs[i][1-bits[i]] for i in range(3)]
    sub={z:0 for z in zero}
    assert s.expand(F.subs(sub))==0
    assert all(s.expand(s.diff(F,v).subs(sub))==0 for v in (a,b,c,d,e,f))
    planes.append((tuple(str(x) for x in keep),tuple(str(x) for x in zero)))
assert len(set(planes))==8

# Three smooth quadrics are in singular locus.
quadrics=[
    ({c:0,d:0}, a*f-b*e),
    ({b:0,e:0}, a*f-c*d),
    ({a:0,f:0}, b*e-c*d),
]
for zeros,rel in quadrics:
    # reduce using substitution for relation via Groebner remainder after zeroing
    vars=(a,b,c,d,e,f)
    pols=[s.expand(s.diff(F,v).subs(zeros)) for v in vars]
    remaining=[v for v in vars if v not in zeros]
    G=s.groebner([rel],*remaining,order='lex')
    for p in pols:
        assert G.reduce(p)[1]==0

# Plane generic transverse Hessian determinant in normals f,e,d at c,d? representative keep a,b,c, zeros f,e,d
H=s.hessian(F,(f,e,d))
Hplane=s.simplify(H.subs({f:0,e:0,d:0}))
assert s.factor(Hplane.det()) == -32*a**2*b**2*c**2  # Hessian of F, 2*M -> det 8*det(M)

# Quadric exact local rewrite for c=d=0 component: u=af-be.
u=s.symbols('u')
# Verify F=(af-be-cd)^2 - 4*b*e*c*d
assert s.expand(F - ((a*f-b*e-c*d)**2 - 4*b*e*c*d))==0

# Singularity case logic encoded on products A=af, B=be, C=cd.
A,B,C=s.symbols('A B C')
X0=A-B-C; Y0=A-B+C; Z0=A+B-C
G=s.groebner([X0,Y0,Z0],A,B,C,order='lex')
assert set(G.polys)==set(s.groebner([A,B,C],A,B,C,order='lex').polys)

# Check quadric smoothness: gradients of af-be cannot vanish at any projective point of its P3.
# algebraically, all partials f,a,-e,-b vanish iff all a,b,e,f=0.
assert [s.diff(a*f-b*e,v) for v in (a,b,e,f)] == [f,-e,-b,a]

print('VERIFY_OK')
print('F=',F)
print('planes=',planes)
print('plane_normal_hessian_det=',s.factor(Hplane.det()))
print('quadric_rewrite=',s.expand((a*f-b*e-c*d)**2 - 4*b*e*c*d))
