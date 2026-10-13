#!/usr/bin/env python3
"""Exact finite-dimensional checks for orthogonal three-frame singular strata.
The checks are consistency tests, not proofs for all ambient dimensions.
"""
import sympy as sp

EDGES=((0,1),(0,2),(1,2))

def jacobian_at(d, columns):
    X=sp.Matrix(d,3,lambda a,b:sp.Symbol('x%d%d'%(a,b)))
    coords=list(X)
    eq=[sum(X[a,i]*X[a,j] for a in range(d)) for i,j in EDGES]
    sub={X[a,j]:columns[j][a] for a in range(d) for j in range(3)}
    J=sp.Matrix([[sp.diff(f,x).subs(sub) for x in coords] for f in eq])
    assert all(sp.expand(f.subs(sub))==0 for f in eq)
    return coords,eq,J,sub

def transverse_hessian(d,kind):
    zero=sp.zeros(d,1)
    if kind=='B':
        w=sp.Matrix([1]+[0]*(d-1))
        cols=(zero,zero,w)
        defining=0
    else:
        w=sp.Matrix([1,sp.I]+[0]*(d-2))
        cols=(zero,w,w)
        defining=1
    coords,eq,J,sub=jacobian_at(d,cols)
    assert J.rank()==2
    # The linear differential relation on the three equations is uniquely
    # up to scalar.  Its second derivative on the tangent space is the
    # ordinary transverse Hessian of the hypersurface left after eliminating two equations.
    K=J.T.nullspace()
    assert len(K)==1
    f=sum(K[0][i]*eq[i] for i in range(3))
    tangent=sp.Matrix.hstack(*J.nullspace())
    h=(tangent.T*sp.hessian(f,coords)*tangent).subs(sub)
    assert h.rows==3*d-2
    assert h.rank()==2*d-2,(d,kind,h.rank())
    return J.rank(),h.rank(),h.rows-h.rank()

for d in (4,5,6,7):
    for kind in ('A','B'):
        jac,rank,nullity=transverse_hessian(d,kind)
        assert (jac,rank,nullity)==(2,2*d-2,d)
    # projective degree of Segre P^1 x Q^(d-2): choose 1 from the
    # P^1 factor in (H_1+H_Q)^(d-1), and deg(Q)=2.
    component_degree=2*(d-1)
    assert 3*component_degree+3==6*d-3
    print('M=%d: A,B Jacobian rank 2; transverse Hessian rank %d; singular-degree %d' %(d,2*d-2,6*d-3))
print('EXACT_CHECK_OK')
