#!/usr/bin/env python3
"""Exact consistency checks for fourth-degree volume moments of Platonic bodies.

Only polynomial identities and elementary geometric reductions certify the formulas;
finite sampling is a supplementary cross-check, not a quantified proof.
"""
import itertools
import math
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull

S=sp.sqrt(5)
phi=(1+S)/2
bI=sp.simplify(sp.Rational(4,3)/(phi+2))
bD=sp.simplify(1/(3*phi**2*sp.sin(sp.pi/5)**2))
beta=sp.Rational(2,3)-2*S/15
assert sp.simplify(bI-beta)==0
assert sp.simplify(sp.trigsimp(bD-beta))==0

# Exact moments of the uniform triangular facet about its circumcenter.
c=sp.symbols('c',real=True)
def bary(a,b):
    return sp.factor(2*sp.factorial(a)*sp.factorial(b)/sp.factorial(a+b+2))
q=sp.expand((sp.Symbol('a')**2+sp.Symbol('b')**2+2*c*sp.Symbol('a')*sp.Symbol('b'))**2)
a,b=sp.symbols('a b')
face_four=sum(coeff*bary(i,j) for (i,j),coeff in sp.Poly(q,a,b).terms())
face_two=bary(2,0)+bary(0,2)+2*c*bary(1,1)
assert sp.simplify(face_two-(2+c)/6)==0
assert sp.simplify(face_four-(7+6*c+2*c**2)/45)==0

# Every regular solid decomposes into congruent cones over its faces.
# The normalized radial moment depends only on face angle cosine and beta=rho^2/R^2.
def radial_k(c0,b):
    z=1-b+b*(2+c0)/6
    second=sp.Rational(3,5)*z
    fourth=sp.Rational(3,7)*((1-b)**2+2*(1-b)*b*(2+c0)/6+b**2*(7+6*c0+2*c0**2)/45)
    k=sp.simplify(sp.radsimp(fourth/second**2))
    return k

expected={
 'tetrahedron':sp.Rational(95,63),
 'cube':sp.Rational(19,15),
 'octahedron':sp.Rational(80,63),
 'dodecahedron':(338875-37475*S)/211722,
 'icosahedron':sp.Rational(185,126)-5*S/42,
}
data={
 'tetrahedron':(-sp.Rational(1,2),sp.Rational(8,9)),
 'cube':(sp.Integer(0),sp.Rational(2,3)),
 'octahedron':(-sp.Rational(1,2),sp.Rational(2,3)),
 'dodecahedron':((S-1)/4,beta),
 'icosahedron':(-sp.Rational(1,2),beta),
}
for k,(c0,b0) in data.items():
    got=radial_k(c0,b0)
    assert sp.simplify(got-expected[k])==0,(k,got)

# Independent exact Dirichlet proofs for all cubic/tetrahedral tensor ratios.
y=sp.symbols('y',real=True)
qT=sp.integrate((2*y-1)**4*6*y*(1-y),(y,0,1))
assert qT==sp.Rational(3,35)
# x+y=2(lambda_1-lambda_4) with uniform Dirichlet(1,1,1,1).
def dir4(i,j):
    return sp.factorial(i)*sp.factorial(j)/sp.prod(range(4,4+i+j))
sum4=16*(2*dir4(4,0)-8*dir4(3,1)+6*dir4(2,2))
pT=sp.factor((sum4-2*qT)/6)
assert pT==sp.Rational(1,21)

moments={
 'tetrahedron':(qT,pT,sp.Rational(19,35)),
 'cube':(sp.Rational(1,5),sp.Rational(1,9),sp.Rational(19,15)),
 'octahedron':(sp.Rational(1,35),sp.Rational(1,210),sp.Rational(4,35)),
}
coefficient={'tetrahedron':-sp.Rational(10,19),'cube':-sp.Rational(10,19),'octahedron':sp.Rational(5,8)}
for name,(q4,p22,r4) in moments.items():
    assert sp.simplify(r4-3*q4-6*p22)==0
    assert sp.simplify(5*(q4-3*p22)/r4-coefficient[name])==0

# The character projection of icosahedral harmonics H_2 and H_4 is zero.
angles=[sp.Integer(0),sp.pi,2*sp.pi/3,2*sp.pi/5,4*sp.pi/5]
counts=[1,15,20,12,12]
def ch(degree,theta):
    if theta==0:return 2*degree+1
    return sp.simplify(1+2*sum(sp.cos(k*theta) for k in range(1,degree+1)))
for degree in (2,4):
    assert sp.simplify(sum(num*ch(degree,theta) for num,theta in zip(counts,angles)))==0

# Exact angular extrema and quartic shape coincidence.
axis=sp.Integer(1); diagonal=sp.Rational(1,3)
assert 1+coefficient['cube']*(axis-sp.Rational(3,5))==sp.Rational(15,19)
assert 1+coefficient['cube']*(diagonal-sp.Rational(3,5))==sp.Rational(65,57)
assert 1+coefficient['octahedron']*(axis-sp.Rational(3,5))==sp.Rational(5,4)
assert 1+coefficient['octahedron']*(diagonal-sp.Rational(3,5))==sp.Rational(5,6)

# Truly independent volume sampling: build the solids from vertices, triangulate
# all hull facets, choose each center-to-facet tetrahedron with volume weights,
# then use Dirichlet barycentric points in each tetrahedron.
f=float(phi)
vertices={}
vertices['tetrahedron']=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)
vertices['cube']=np.array(list(itertools.product([-1,1],repeat=3)),dtype=float)
vertices['octahedron']=np.array([[z if i==j else 0 for i in range(3)] for j in range(3) for z in [-1,1]],dtype=float)
vertices['icosahedron']=np.array([p for x,y in itertools.product([-1,1],repeat=2) for p in [(0,x,y*f),(x,y*f,0),(y*f,0,x)]],dtype=float)
vertices['dodecahedron']=np.array(list(itertools.product([-1,1],repeat=3))+[p for x,y in itertools.product([-1,1],repeat=2) for p in [(0,x/f,y*f),(x/f,y*f,0),(y*f,0,x/f)]],dtype=float)

rng=np.random.default_rng(1729)
N=90000
max_err=0.0
for name,V in vertices.items():
    h=ConvexHull(V)
    triangles=V[h.simplices]
    tetra_vol=np.abs(np.linalg.det(triangles))/6
    face_choice=rng.choice(len(tetra_vol),size=N,p=tetra_vol/tetra_vol.sum())
    b=rng.dirichlet([1,1,1,1],size=N)
    x=np.einsum('ni,nij->nj',b[:,1:],triangles[face_choice])
    squared=np.sum(x*x,axis=1)
    r2=np.mean(squared)
    r4=np.mean(squared**2)
    k_mc=r4/r2**2
    k_true=float(expected[name])
    assert abs(k_mc-k_true)<0.022,(name,k_mc,k_true)
    for U in [np.array([1.,0,0]),np.array([1.,1,1])/math.sqrt(3)]:
        F_mc=5*np.mean((x@U)**4)/r4
        sigma=np.sum(U**4)
        F_true=1+float(coefficient.get(name,0))*(sigma-3/5)
        err=abs(F_mc-F_true)
        max_err=max(max_err,err)
        assert err<0.08,(name,U,F_mc,F_true)

print('VERIFY_OK')
print('exact_face_moments = passed')
print('exact_polyhedral_radial_moments = passed')
print('exact_tetrahedral_and_cubic_quartic_tensors = passed')
print('icosahedral_character_projection_H2_H4 = passed')
print('numerical_volumetric_tetrahedralization_samples_per_solid =',N)
print('numerical_max_F_discrepancy =',round(max_err,8))
for name in expected:
    print(name,'radial_shape',sp.sstr(expected[name]),'numeric',float(expected[name]))
