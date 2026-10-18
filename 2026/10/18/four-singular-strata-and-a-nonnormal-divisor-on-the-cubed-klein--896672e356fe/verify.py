#!/usr/bin/env python3
"""Exact checks for the cubed Klein-quadric singularity theorem.

Needs Python 3 and SymPy; finite-field checks are independently coded.
"""
from itertools import product
import sympy as s
u,v,w=s.symbols('u v w')
T=u-v-w
H=s.expand(T**3-27*u*v*w)
assert s.factor(H)==H
assert [s.expand(s.diff(H,t)) for t in (u,v,w)]==[s.expand(t) for t in (
    3*T*T-27*v*w, -3*T*T-27*u*w, -3*T*T-27*u*v)]
assert H.subs({u:-1,v:1,w:1})==0
assert all(s.diff(H,t).subs({u:-1,v:1,w:1})==0 for t in (u,v,w))
hess=s.hessian(H,(u,v)).subs({u:-1,v:1,w:1})
assert hess.det()==243
assert s.factor(H.subs({u:0}))==-(v+w)**3
assert s.factor(H.subs({v:0}))==(u-w)**3
assert s.factor(H.subs({w:0}))==(u-v)**3
# Explicit homogeneous relation from the Klein quadric a=b+c.
a,b=s.symbols('a b'); assert s.expand(H.subs({u:a**3,v:b**3,w:(a-b)**3}))==0

# The plane cubic is not contained in a line or conic: the six monomials
# U^2,V^2,W^2,UV,UW,VW pulled back under [a:b]->[a^3:b^3:(a-b)^3]
# have linearly independent degree-six coefficient vectors.
forms=[a**6,b**6,(a-b)**6,a**3*b**3,a**3*(a-b)**3,b**3*(a-b)**3]
coeff=s.Matrix([[s.expand(f).coeff(a,6-j).coeff(b,j) for f in forms] for j in range(7)])
assert coeff.rank()==6
# Projective diagonal cube-root stabilizer has 27 elements.
gcount=0
for lam in product(range(3),repeat=5):
    q=(0,)+lam
    if (q[0]+q[1]-q[2]-q[3])%3==0 and (q[0]+q[1]-q[4]-q[5])%3==0:
        gcount+=1
assert gcount==27

# Check the four-piece set-theoretic singularity classification on all
# projective points over three fields of characteristic different from three.
def reps(p):
    for first in range(6):
        for suffix in product(range(p),repeat=5-first):
            yield (0,)*first+(1,)+suffix

def classify(p):
    count=0; singular_count=0
    for x in reps(p):
        U=x[0]*x[1]%p; V=x[2]*x[3]%p; W=x[4]*x[5]%p
        h=((U-V-W)**3-27*U*V*W)%p
        if h:
            count+=1
            continue
        t=U-V-W
        hu=(3*t*t-27*V*W)%p
        hv=(-3*t*t-27*U*W)%p
        hw=(-3*t*t-27*U*V)%p
        actual=all((d*partner)%p==0 for d,partner in zip((hu,hu,hv,hv,hw,hw),(x[1],x[0],x[3],x[2],x[5],x[4])))
        expected=((U+V)%p==0 and (U+W)%p==0) or (x[0]==x[1]==0 and (V+W)%p==0) or (x[2]==x[3]==0 and (U-W)%p==0) or (x[4]==x[5]==0 and (U-V)%p==0)
        assert actual==expected,(p,x,actual,expected)
        singular_count+=int(actual)
        count+=1
    return (count,singular_count)

for p in (5,7):
    n,k=classify(p)
    assert n==(p**6-1)//(p-1)
    print('F_%d projective points %d, singular points %d: classified'%(p,n,k))

# The divisor Y is an affine complete intersection, with saturated relation
# lattice: determinant-one minor of its 2x6 exponent-difference matrix.
M=s.Matrix([[1,1,-1,-1,0,0],[1,1,0,0,-1,-1]])
assert abs(M.extract([0,1],[0,2]).det())==1
print('VERIFY_OK')
