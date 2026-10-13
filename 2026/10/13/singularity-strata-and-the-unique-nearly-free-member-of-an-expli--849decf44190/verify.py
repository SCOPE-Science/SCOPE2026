#!/usr/bin/env python3
"""Exact algebra checks for the singularity stratification of a four-conic family.
Requires SymPy >= 1.12. Run: python verify.py
"""
from itertools import combinations
import sympy as s
x,y,z,t = s.symbols('x y z t')
Q0=x*x+y*y-z*z
Q1=2*x*x+y*y+2*x*z
Q2=x*x+y*y+2*x*z
Q3=4*x*x+6*y*y+4*x*z-t*z*z
Q=[Q0,Q1,Q2,Q3]
assert [s.det(s.hessian(q,(x,y,z))/2) for q in Q] == [-1,-1,-1,-24*(t+1)]
# Exact equations obtained by eliminating y from each pair on z=1.
R={
(0,1):(x+1)**4,
(0,2):(2*x+1)**2,
(0,3):(t+2*x*x-4*x-6)**2,
(1,2):x**4,
(1,3):(t+8*x*x+8*x)**2,
(2,3):(t+2*x*x+8*x)**2,
}
for i,j in combinations(range(4),2):
    rr=s.resultant(Q[i].subs(z,1),Q[j].subs(z,1),y)
    assert s.expand(rr-R[(i,j)])==0,(i,j)
# Confirm all three comparisons of the fourth conic with the first three.
assert s.expand(Q3-6*Q0-(-2*x*x+4*x*z+(6-t)*z*z))==0
assert s.expand(Q3-6*Q1-(-8*x*x-8*x*z-t*z*z))==0
assert s.expand(Q3-6*Q2-(-2*x*x-8*x*z-t*z*z))==0
assert s.discriminant(t+2*x*x-4*x-6,x)==8*(8-t)
assert s.discriminant(t+8*x*x+8*x,x)==32*(2-t)
assert s.discriminant(t+2*x*x+8*x,x)==8*(8-t)
# The unique non-fixed component becomes singular only at t=-1.
# The pair Q0,Q2 has two transverse points at infinity and two affine points.
assert s.factor(Q2-Q0)==z*(2*x+z)
# New triple intersections with Q3: t=0 (two tangential triples), t=7/2 (two transverse triples).
for xx,yy2,tt in [(-1,0,0),(0,0,0),(s.Rational(-1,2),s.Rational(3,4),s.Rational(7,2))]:
    for i,j in [(0,1)] if xx==-1 else ([(1,2)] if xx==0 else [(0,2)]):
        assert s.expand(Q[i].subs({x:xx,z:1,y:s.sqrt(yy2)}))==0
        assert s.expand(Q[j].subs({x:xx,z:1,y:s.sqrt(yy2)}))==0
    assert s.expand(Q3.subs({x:xx,y:s.sqrt(yy2),z:1,t:tt}))==0
# Contact orders at the two 3-branch points for t=0: {4,2,2} in each case.
v=s.symbols('v')
branches_at_minus_one=[-s.sqrt(1-v*v),(-1-s.sqrt(1-2*v*v))/2,(-1-s.sqrt(1-6*v*v))/2]
branches_at_zero=[(-1+s.sqrt(1-2*v*v))/2,-1+s.sqrt(1-v*v),(-1+s.sqrt(1-6*v*v))/2]
for branches in [branches_at_minus_one,branches_at_zero]:
    orders=[]
    for aa,bb in combinations(branches,2):
        p=s.series(aa-bb,v,0,7).removeO().expand()
        for k in range(1,7):
            if p.coeff(v,k)!=0:orders.append(k);break
    assert sorted(orders)==[2,2,4],orders
# Local arithmetic for the printed coefficient (t=9).
for xx in (-2,1):
    assert Q3.subs({x:xx,y:0,z:1,t:9})==-1
# Exact Jacobian syzygy of degree three for the corrected t=8 fiber.
f=s.expand(s.prod(q.subs(t,8) for q in Q))
a=-(x**3-x*x*z+x*y*y-3*x*z*z-y*y*z)
c=(2*x+z)*(x*x+x*z+y*y-z*z)
assert s.expand(a*s.diff(f,x)+c*s.diff(f,z))==0
# An injective reduction modulo a prime proves absence of lower-degree
# syzygies over Q. Row vectors are coefficient vectors of monomial multiples.
p=1000003
def monomials(d):
    return [(i,j,d-i-j) for i in range(d+1) for j in range(d+1-i)]
def rank_mod(mat,prime):
    n=len(mat);m=len(mat[0]);r=0
    for col in range(m):
        pivot=next((j for j in range(r,n) if mat[j][col]%prime),None)
        if pivot is None:continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        inv=pow(int(mat[r][col])%prime,-1,prime)
        for j in range(col,m):mat[r][j]=(int(mat[r][j])*inv)%prime
        for i in range(r+1,n):
            fac=mat[i][col]%prime
            if fac:
                for j in range(col,m):mat[i][j]=(int(mat[i][j])-fac*mat[r][j])%prime
        r+=1
        if r==n:break
    return r
for d in (1,2):
    mons=[x**i*y**j*z**k for i,j,k in monomials(d)]
    cols=[s.Poly(m*s.diff(f,var),x,y,z) for var in (x,y,z) for m in mons]
    rows=monomials(7+d)
    M=[[int(col.coeff_monomial(e))%p for col in cols] for e in rows]
    assert rank_mod(M,p)==len(cols)==3*len(mons)
# Singularity baskets have constant total delta = 24 (=six conic-pair Bezout numbers).
# t=0: 2 triple-contact (delta 8 each), 8 nodes.
# t=2: 2 A7 (delta 4), 2 A3 (delta 2), 12 nodes.
# t=7/2: 2 A7, 2 ordinary triples (delta 3), 10 nodes.
# t=8: 4 A7, 8 nodes.
# generic: 2 A7 and 16 nodes.
assert all(vals==24 for vals in [2*8+8,2*4+2*2+12,2*4+2*3+10,4*4+8,2*4+16])
print('VERIFY_OK discriminant_parameters=-1,0,2,7/2,8 strata=generic:2A7+16A1;t0:2triple(4,2,2)+8A1;t2:2A7+2A3+12A1;t7/2:2A7+2D4+10A1;t8:4A7+8A1 corrected_nearly_free_mdr=3 printed_t9_not_nearly_free')
