#!/usr/bin/env python3
"""Exact rational/two-prime rank certificates for a 16-nodal Kummer quartic.

Requirements: Python 3, sympy, numpy.  No remote services or external data.
The modular calculations certify LOWER bounds over Q, combined in the
mathematical argument with explicit rational inclusions for UPPER bounds.
"""
from itertools import product
from collections import Counter, defaultdict
from math import prod
import sympy as S
import numpy as np

X,Y,Z,W=S.symbols('X Y Z W')
variables=(X,Y,Z,W)
faces=(W+X+Y+Z,W+X-Y-Z,W-X+Y-Z,W-X-Y+Z)
F=S.expand(3*(2*X**2+2*Y**2+2*Z**2-3*W**2)**2-28*prod(faces))
grad=[S.diff(F,t) for t in variables]
points=[]
for a,b,c in product((1,-1),repeat=3):
    if a*b*c==1: points.append((a,b,c,4))
for axis in range(3):
    for sign in (1,-1):
        for t in (2,-2):
            a=[0,0,0,4]
            a[axis]=4*sign
            others=[i for i in range(3) if i!=axis]
            a[others[0]]=t
            a[others[1]]=t*sign
            points.append(tuple(a))
assert len(points)==len(set(points))==16
for pt in points:
    sub=dict(zip(variables,pt))
    assert F.subs(sub)==0 and all(g.subs(sub)==0 for g in grad)
hessian=S.hessian(F,(X,Y,Z))
hess_data=Counter(int(hessian.det().subs(dict(zip(variables,pt)))) for pt in points)
assert hess_data=={-11098128384:12,-693633024:4}

# The affine gradient ideal (W=1) has a reduced length-16 zero scheme.
gb=S.groebner([g.subs(W,1) for g in grad],X,Y,Z,order='lex')
assert [S.LM(p.as_expr(),X,Y,Z) for p in gb.polys]==[X,Y**4,Y**2*Z**2,Z**6]
for chart in (X,Y,Z):
    other=[t for t in (X,Y,Z) if t!=chart]
    gbinf=S.groebner([g.subs({W:0,chart:1}) for g in grad],*other,order='lex')
    assert len(gbinf.polys)==1 and gbinf.polys[0].as_expr()==1


def monomials(d):
    return [(a,b,c,d-a-b-c) for a in range(d+1) for b in range(d-a+1) for c in range(d-a-b+1)]

def evaluations(d, jet=False):
    rows=[]
    for pt in points:
        for deriv in ((None,0,1,2) if jet else (None,)):
            row=[]
            for exp in monomials(d):
                ee=list(exp)
                co=1
                if deriv is not None:
                    co=ee[deriv]
                    ee[deriv]-=1
                row.append(co*prod(pt[j]**ee[j] for j in range(4)) if co else 0)
            rows.append(row)
    return S.Matrix(rows)

def rank_mod(matrix,prime):
    if isinstance(matrix,S.MatrixBase):
        it=matrix.tolist()
    else:it=matrix
    a=np.array([[int(S.Rational(q).p)*pow(int(S.Rational(q).q),-1,prime)%prime for q in row] for row in it],dtype=np.int64)
    rows,cols=a.shape
    rk=0
    for j in range(cols):
        if rk==rows:break
        nz=np.flatnonzero(a[rk:,j])
        if nz.size==0:continue
        k=int(nz[0])+rk
        if k!=rk:a[[rk,k]]=a[[k,rk]]
        a[rk]=(a[rk]*pow(int(a[rk,j]),-1,prime))%prime
        idx=np.flatnonzero(a[:,j]);idx=idx[idx!=rk]
        if idx.size:a[idx]=(a[idx]-a[idx,j,None]*a[rk])%prime
        rk+=1
    return rk

def from_polynomial(poly,degree):
    pp=S.Poly(poly,*variables)
    return S.Matrix([pp.coeff_monomial(prod(t**e for t,e in zip(variables,exp))) for exp in monomials(degree)])

def as_terms(vec,degree):
    return {a:S.Rational(c) for a,c in zip(monomials(degree),vec) if c}

def times(vec,degree,other,otherdegree):
    vals=defaultdict(lambda:S.Integer(0))
    for a,u in as_terms(vec,degree).items():
        for b,v in as_terms(other,otherdegree).items():
            vals[tuple(x+y for x,y in zip(a,b))]+=u*v
    return S.Matrix([vals.get(e,0) for e in monomials(degree+otherdegree)])

def monvec(d,exponent):
    return S.Matrix([int(e==exponent) for e in monomials(d)])

assert evaluations(2).rank()==10
M3=evaluations(3)
M4=evaluations(4)
I3=M3.nullspace()
I4=M4.nullspace()
assert len(I3)==4 and len(I4)==19
G3=[from_polynomial(g,3) for g in grad]
assert S.Matrix.hstack(*G3).rank()==4
assert M3*S.Matrix.hstack(*G3)==S.zeros(16,4)

F4=from_polynomial(F,4)
P6=[times(G3[i],3,G3[j],3) for i in range(4) for j in range(i,4)]
P6Q=[times(v,6,monvec(1,e),1) for v in P6 for e in monomials(1)]
FR2=[times(F4,4,monvec(2,e),2) for e in monomials(2)]
FR3=[times(F4,4,monvec(3,e),3) for e in monomials(3)]
E3=[times(v,3,monvec(1,e),1) for v in I3 for e in monomials(1)]
assert S.Matrix.hstack(*E3).rank()==16
extras=[]
span=E3[:]
current=16
for v in I4:
    if S.Matrix.hstack(*(span+[v])).rank()>current:
        extras.append(v);span.append(v);current+=1
assert len(extras)==3 and current==19

# Exact Q-rank in degree 7 for the ordinary square.
ordinary7=[times(u,6,monvec(1,e),1) for u in [times(I3[i],3,I3[j],3) for i in range(4) for j in range(i,4)] for e in monomials(1)]
ordinary7 += [times(u,3,v,4) for u in I3 for v in I4]
assert S.Matrix.hstack(*ordinary7).rank()==52

# Degree 8 ordinary-square spanning vectors, using the 4+3 generators of I.
I3pairs=[times(I3[i],3,I3[j],3) for i in range(4) for j in range(i,4)]
ordinary8=[times(u,6,monvec(2,e),2) for u in I3pairs for e in monomials(2)]
ordinary8 += [times(times(u,3,v,4),7,monvec(1,e),1) for u in I3 for v in extras for e in monomials(1)]
ordinary8 += [times(extras[i],4,extras[j],4) for i in range(3) for j in range(i,3)]

expected={
    'I3':16, 'I4':16,
    'jet3':20, 'jet4':34, 'jet5':52, 'jet6':64,
    'jet7':64, 'jet8':64,
    'square6':20, 'square7':56, 'ordinary8':101,
}
for prime in (1009,1013):
    ranks={
        'I3':rank_mod(M3,prime),'I4':rank_mod(M4,prime),
        'jet3':rank_mod(evaluations(3,True),prime),
        'jet4':rank_mod(evaluations(4,True),prime),
        'jet5':rank_mod(evaluations(5,True),prime),
        'jet6':rank_mod(evaluations(6,True),prime),
        'jet7':rank_mod(evaluations(7,True),prime),
        'jet8':rank_mod(evaluations(8,True),prime),
        'square6':rank_mod(S.Matrix.hstack(*(P6+FR2)),prime),
        'square7':rank_mod(S.Matrix.hstack(*(P6Q+FR3)),prime),
        'ordinary8':rank_mod(S.Matrix.hstack(*ordinary8),prime),
    }
    assert ranks==expected,(prime,ranks)
    print('prime',prime,'ranks',ranks)

print('node_count=16; Hessian determinant multiplicities=',sorted(hess_data.items()))
print('affine_gradient_leading_monomials=X,Y^4,Y^2 Z^2,Z^6; quotient_length=16; no nodes at infinity')
print('reduced_hilbert=[1,4,10,16,...]')
print('double_hilbert=[1,4,10,20,34,52,64,64,...]')
print('symbolic_square_generators=quartic_F + ten_products_of_gradient_cubics')
print('ordinary_symbolic_defect_dimensions_by_degrees_4_to_7=[1,4,10,4]')
print('VERIFY_OK')
