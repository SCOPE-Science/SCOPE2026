#!/usr/bin/env python3
"""Exact finite-characteristic polynomial checks for the B3 quartic.
Requires Python 3.10+ and SymPy. Checks identities, not historical novelty.
"""
import sympy as s
from itertools import combinations
x,y,z,a,b,c,u,v=s.symbols('x y z a b c u v')

def zero(f,variables=(x,y,z,a,b,c)):
    return s.Poly(s.expand(f), *variables, modulus=3).is_zero

QZ=(3*a*(b*b-c*c)*x*x*y*z + 3*b*(c*c-a*a)*x*y*y*z
    +3*c*(a*a-b*b)*x*y*z*z+a**3*(y**3*z-y*z**3)
    +b**3*(x*z**3-x**3*z)+c**3*(x**3*y-x*y**3))
Q=a**3*(y**3*z-y*z**3)+b**3*(x*z**3-x**3*z)+c**3*(x**3*y-x*y**3)
assert zero(QZ-Q)
ells=[b*z-c*y,c*x-a*z,a*y-b*x]
for var,L in zip([x,y,z],ells):
    assert zero(s.diff(Q,var)-L**3)
assert zero(Q.subs({x:a,y:b,z:c}))
assert zero(Q.subs({x:a**3,y:b**3,z:c**3}))
# Frobenius-twisted strange point is on every smooth-point tangent.
assert zero(a**3*s.diff(Q,x)+b**3*s.diff(Q,y)+c**3*s.diff(Q,z))

Qa=Q.subs(c,1)
local=s.expand(Qa.subs({x:a+u,y:b+v,z:1}))
A=a**3-a
B=b-b**3
pred=B*u**3+A*v**3+u**3*v-u*v**3
assert zero(local-pred,(a,b,u,v))
assert zero(s.diff(local,u)+v**3,(a,b,u,v))
assert zero(s.diff(local,v)-u**3,(a,b,u,v))

# The nine base-point evaluation conditions remain independent modulo three.
points=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)]
monomials4=[x**i*y**j*z**(4-i-j) for i in range(5) for j in range(5-i)]
eval_matrix=s.Matrix([[int(f.subs({x:X,y:Y,z:Z})) % 3 for f in monomials4] for X,Y,Z in points])
assert len(s.polys.matrices.DomainMatrix.from_Matrix(eval_matrix).convert_to(s.GF(3)).rref()[1])==9

# The B3 nine-point linear system has dimension 6 in characteristic three,
# and imposing a triple point gives a 6x6 jet matrix with a nonzero 5x5 minor.
base=[x**3*y-x*y**3,x**3*z-x*z**3,y**3*z-y*z**3,x*x*y*z,x*y*y*z,x*y*z*z]
monomials=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
cols=[]
for f in base:
    fuv=s.Poly(s.expand(f.subs({x:a+u,y:b+v,z:1})),u,v)
    cols.append([s.Poly(fuv.coeff_monomial(u**i*v**j),a,b,modulus=3).as_expr() for i,j in monomials])
M=s.Matrix(cols).T
assert zero(s.det(M),(a,b))
assert zero(s.det(M.minor_submatrix(0,0))+a*b,(a,b))

# The open A B(A^2-B^2) !=0 is nonempty, using F_27 = F_3[t]/(t^3-t-1).
# Polynomial representatives are tuples of three coefficients of 1,t,t^2.
def fm(p,q):
    t=[0]*5
    for i,pi in enumerate(p):
        for j,qj in enumerate(q):t[i+j]=(t[i+j]+pi*qj)%3
    for i in (4,3):
        t[i-3]=(t[i-3]+t[i])%3
        t[i-2]=(t[i-2]+t[i])%3
    return tuple(t[:3])
def fa(p,q):return tuple((i+j)%3 for i,j in zip(p,q))
def fn(p):return tuple((-i)%3 for i in p)
def fs(p,q):return fa(p,fn(q))
def fp(p,n):
    r=(1,0,0)
    for _ in range(n):r=fm(r,p)
    return r
one=(1,0,0); aa=(0,1,0); bb=(0,0,1)
AA=fs(fp(aa,3),aa)
BB=fs(bb,fp(bb,3))
Delta=fm(fm(AA,BB),fs(fp(AA,2),fp(BB,2)))
assert AA==(1,0,0) and BB==(2,1,0) and Delta!=(0,0,0), (AA,BB,Delta)
print('B3_CHAR3_FROBENIUS_GRADIENT_LENGTH9_UNIQUE_JET_AND_WILD_CUSP_OPEN_PASS')
print('rank5_minor=-ab; F27_witness_delta=',Delta)
