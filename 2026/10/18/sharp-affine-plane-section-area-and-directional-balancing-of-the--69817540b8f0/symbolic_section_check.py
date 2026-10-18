"""Symbolic, exact checks of the cuboctahedron section identities.
Requires SymPy. This verifies identities, not the geometric completeness proof."""
import sympy as S
A,B,C,H=S.symbols('a b c h', real=True)
u=S.Matrix([A,B,C])
V=[((1,-1,0),(0,-1,-1)),((1,0,-1),(0,-1,-1)),
   ((0,1,-1),(-1,0,-1)),((0,1,-1),(-1,1,0)),
   ((0,1,1),(-1,1,0)),((0,1,1),(-1,0,1)),
   ((1,0,1),(0,-1,1)),((1,-1,0),(0,-1,1))]
def meet(p,q,normal,level=0):
    p,q=S.Matrix(p),S.Matrix(q)
    t=(normal.dot(p)-level)/(normal.dot(p-q))
    return p+t*(q-p)
pts=[meet(p,q,u) for p,q in V]
shoelace=S.factor(sum(u.dot(pts[j].cross(pts[(j+1)%8])) for j in range(8)))
expected=4*(A*A+B*B+C*C)*(2*A*A+2*A*B-B*B-3*C*C)/((A+B)*(A*A-C*C))
assert S.cancel(shoelace-expected)==0
s,r=S.symbols('s r', real=True)
Q=2+2*s-s*s-3*r
W=(1+s*s+r)*Q**2/((1+s)**2*(1-r)**2)
N=3*r*r-(s*s-2*s+7)*r-2*s**4+4*s**3-5*s*s+6*s
assert S.cancel(S.diff(W,r)/W-N/((1+s*s+r)*(1-r)*Q))==0
assert S.expand(N.subs(r,s*s)-6*s*(1-s)**2)==0
g=4*(1+2*s)*S.sqrt(1+2*s*s)/(1+s)**2
assert S.simplify(S.diff(g,s)/g-6*s*s/((1+s)*(1+2*s)*(1+2*s*s)))==0
assert S.factor((1+s*s)*(2+2*s-s*s)**2-4*(1+s)**2)==s**3*(s**3-4*s*s+s+4)
# Diagonal plane: the six polygon vertices come from the positive-to-zero edges.
u=S.Matrix([1,1,1])
W=[((1,0,1),(1,-1,0)),((1,1,0),(1,0,-1)),
   ((1,1,0),(0,1,-1)),((0,1,1),(-1,1,0)),
   ((0,1,1),(-1,0,1)),((1,0,1),(0,-1,1))]
pts=[meet(p,q,u,H) for p,q in W]
shoelace=S.factor(sum(u.dot(pts[j].cross(pts[(j+1)%6])) for j in range(6)))
assert S.factor(shoelace-3*(H*H-12*H+24)/4)==0
print('SYMBOLIC_SECTION_IDENTITIES_OK generic_area derivative_factors diagonal_profile')
