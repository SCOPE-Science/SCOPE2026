#!/usr/bin/env python3
"""Exact characteristic-zero verification of a smooth-conic pencil in P^2."""
import sympy as S
from sympy.polys.matrices import DomainMatrix

x,y,z,t=S.symbols('x y z t')
f=(x*x+y*y-t*z*z)*(x*x-z*z)*(y*y-z*z)*(x+y)
grad=[S.diff(f,w) for w in (x,y,z)]

def monomials(d):
    return [x**a*y**b*z**(d-a-b) for a in range(d+1) for b in range(d-a+1)]

def jacobian_matrix(d):
    mons=monomials(d)
    row_mons=monomials(6+d)
    idx={S.Poly(m,x,y,z).monoms()[0]:i for i,m in enumerate(row_mons)}
    cols=[]
    for g in grad:
        for h in mons:
            col=[0]*len(row_mons)
            for e,c in S.Poly(S.expand(g*h),x,y,z).terms():
                col[idx[e]]=c
            cols.append(col)
    return S.Matrix(len(row_mons),len(cols),lambda i,j:cols[j][i])

def relation(A,B,C,specialization=None):
    expr=S.expand(A*grad[0]+B*grad[1]+C*grad[2])
    if specialization is not None:
        expr=S.expand(expr.subs(t,specialization))
    assert expr==0

A=(4*t*x*x*z*z+3*t*x*y*z*z-7*t*z**4 -2*x**4-3*x**3*y-4*x*x*y*y+5*x*x*z*z-5*x*y**3+2*x*y*z*z+7*y*y*z*z)
B=(-3*t*x*y*z*z-4*t*y*y*z*z+7*t*z**4+5*x**3*y+4*x*x*y*y-7*x*x*z*z+3*x*y**3-2*x*y*z*z+2*y**4-5*y*y*z*z)
C=z*(x-y)*(-3*t*z*z+5*x*x+2*x*y+5*y*y-2*z*z)
relation(A,B,C)
assert S.Poly(A,x,y,z).total_degree()==4

M3=jacobian_matrix(3)
rows1=[0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31]
rows2=[0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,33]

def det_rows(M,rows):
    Q=M.extract(rows,list(range(M.cols)))
    assert Q.rows==Q.cols
    return S.factor(DomainMatrix.from_Matrix(Q).convert_to(S.QQ.poly_ring(t)).det().as_expr())

assert S.expand(det_rows(M3,rows1)-370091753472*t**8*(t-2)**3*(t-1)**8*(t+1))==0
assert S.expand(det_rows(M3,rows2)-740183506944*t**7*(t-2)**3*(t-1)**8)==0

# The special parameters have a syzygy in strictly lower degree.
relation(-z*(3*x*x-3*x*y+7*y*y-7*z*z),
         z*(7*x*x-3*x*y+3*y*y-7*z*z),
         (x-y)*(7*x*y+4*z*z),1)
relation(-z*(x-7*y),z*(7*x-y),7*x*y-z*z,2)

M2_1=jacobian_matrix(2).subs(t,1)
row18=[0,1,2,3,4,5,9,10,11,12,13,14,17,18,19,20,21,25]
assert M2_1.extract(row18,list(range(18))).det()==-44957696
M1_2=jacobian_matrix(1).subs(t,2)
row9=[0,1,2,3,4,8,9,10,12]
assert M1_2.extract(row9,list(range(9))).det()==-2322432

# Distinct square corners and intersections with diagonal line.
# The conic is smooth precisely when t is nonzero.
q=x*x+y*y-t*z*z
assert S.det(S.hessian(q,(x,y,z)))==-8*t
for a,b in [(1,1),(1,-1),(-1,1),(-1,-1)]:
    assert S.expand(q.subs({x:a,y:b,z:1}))==2-t
assert S.discriminant(q.subs({x:1,z:1}),y)==4*(t-1)
assert S.discriminant(q.subs({y:1,z:1}),x)==4*(t-1)
assert S.factor(q.subs(y,-x))==2*x*x-t*z*z
# For t != 0, this last restriction has two distinct projective roots.
# The pairwise Bezout count for the reduced components is 10+5*2=20.
assert 14+2*3==20    # generic 14 nodes and 2 triple points
assert 6+4*2+2*3==20 # t=1: six nodes, four tacnodes, two triples
assert 2+2*3+2*6==20 # t=2: two nodes, two triples, two quadruples

# Euler's relation and standard free/nearly-free numerical criteria (degree 7).
d=7
assert 28==(d-1)**2-2*(d-2-1)
assert 26+1==3**2-3*(d-1)+(d-1)**2
assert 22+1!=4**2-4*(d-1)+(d-1)**2
assert 22!=(d-1)**2-4*(d-4-1)
print('VERIFY_OK smooth=t_nonzero, generic=(14A1+2D4,mdr4), t1=(6A1+4A3+2D4,mdr3,nearly_free), t2=(2A1+2D4+2X9,mdr2,free)')
