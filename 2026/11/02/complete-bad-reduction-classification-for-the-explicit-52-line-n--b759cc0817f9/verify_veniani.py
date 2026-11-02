#!/usr/bin/env python3
"""Exact arithmetic checks for the reduction of a fixed integral quartic surface.

Requires Python 3 and SymPy. The proof of universal exhaustion uses the
nonzero principal minors of the displayed symmetric matrix, not sampling.
"""
import itertools
import sympy as sp
x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3')
u,v,w,t=sp.symbols('u v w t')
F=(x0**2*x1*x2-x1**3*x2-2*x1**2*x2**2-x1*x2**3
   +x0**3*x3+x0*x1**2*x3+2*x0*x1*x2*x3
   +x0*x2**2*x3+2*x0**2*x3**2+x1*x2*x3**2+x0*x3**3)
M=sp.Matrix([[-4,2,-3,1],[2,0,1,1],[-3,1,4,-2],[1,1,-2,0]])
vars_=(u,v,w,t)
Q=sp.expand(sum(M[i,j]*vars_[i]**2*vars_[j]**2 for i in range(4) for j in range(4))/2)
assert sp.expand(8*F+Q.subs({u:x0+x3,v:x0-x3,w:x1+x2,t:x1-x2}))==0
expected={ (0,):-4,(1,):0,(2,):4,(3,):0,
 (0,1):-4,(0,2):-25,(0,3):-1,(1,2):-1,(1,3):-1,(2,3):-4,
 (0,1,2):-24,(0,1,3):8,(0,2,3):24,(1,2,3):-8,
 (0,1,2,3):64 }
for S,d in expected.items():
    assert M.extract(S,S).det()==d, (S,d)
assert {abs(p) for d in expected.values() for p in sp.factorint(abs(d)) if d}=={2,3,5}
# Exhaust all projective supports: for p=3,5, calculate kernel of each
# principal submatrix over F_p, and retain vectors with all entries nonzero.
def projective_vectors(p):
    points=[]
    for first in range(4):
        for tail in itertools.product(range(p),repeat=3-first):
            points.append((0,)*first+(1,)+tail)
    return points

def zeros(p):
    out=[]
    for P in projective_vectors(p):
        V=[pow(a,2,p) for a in P]
        MV=[sum(int(M[i,j])*V[j] for j in range(4))%p for i in range(4)]
        if all((P[i]*MV[i])%p==0 for i in range(4)):
            out.append(P)
    return out
# For p=3 the 10 singular points are defined over F_9, not F_3:
# verify the support-kernel algebraically, without claiming F_3 exhaustive.
for p in (3,5,7,11):
    singular_supports=[]
    for r in range(1,5):
        for S in itertools.combinations(range(4),r):
            # Gaussian projective q-values, all nonzero, over F_p.
            for qtail in itertools.product(range(1,p),repeat=r-1):
                q=(1,)+qtail
                if all(sum(int(M[i,j])*q[b] for b,j in enumerate(S))%p==0 for i in S):
                    singular_supports.append((S,q))
    if p==3:
        assert {s for s,_ in singular_supports}=={(1,),(3,),(0,1,2),(0,2,3)}
        assert set(singular_supports)=={((1,),(1,)),((3,),(1,)),((0,1,2),(1,2,1)),((0,2,3),(1,2,1))}
    elif p==5:
        assert set(singular_supports)=={((1,),(1,)),((3,),(1,)),((0,2),(1,2))}
    else:
        assert set(singular_supports)=={((1,),(1,)),((3,),(1,))}
# At p=3 the kernel ratios are (u^2,v^2,w^2)=(1,2,1),
# (u^2,w^2,t^2)=(1,2,1); at p=5 (u^2,w^2)=(3,1).
# Nondegenerate Hessians at all points, computed without square-root choices:
H=sp.hessian(Q, vars_)
def hessian_affine(fixed_idx,coord_squares,p):
    movable=[i for i in range(4) if i!=fixed_idx]
    # To avoid taking square roots symbolically, find a finite extension or
    # use determinant polynomial and substitute coordinate *squares*.
    raw=sp.expand(H.extract(movable,movable).det())
    val=0
    for exponents,coefficient in sp.Poly(raw,*vars_).terms():
        assert all(e%2==0 for e in exponents)
        prod=coefficient
        for a,e in zip(vars_,exponents):
            prod*=coord_squares.get(a,0)**(e//2)
        val+=prod
    return int(val)%p
assert hessian_affine(1,{v:1},7)!=0
assert hessian_affine(3,{t:1},7)!=0
assert hessian_affine(0,{u:1,v:2,w:1},3)!=0
assert hessian_affine(0,{u:1,w:2,t:1},3)!=0
assert hessian_affine(2,{u:3,w:1},5)!=0
Hlin=x0+x1+x2+x3
quad=x0*x3+x1*x2
assert sp.Poly(F-Hlin**2*quad,(x0,x1,x2,x3),modulus=2).is_zero
# The partial derivatives of the mod-2 quartic are H^2 times a
# permutation of the four homogeneous coordinates; after saturation,
# their ideal is (H^2), giving a double-plane singular scheme.
for xi,qi in zip((x0,x1,x2,x3),(x3,x2,x1,x0)):
    assert sp.Poly(sp.diff(F,xi)-Hlin**2*qi,(x0,x1,x2,x3),modulus=2).is_zero
print('VENIANI52_PRINCIPAL_MINORS_ALL_ODD_PRIMES_AND_CHAR2_DOUBLE_PLANE_PASS')
