#!/usr/bin/env python3
"""Exact finite-characteristic algebra for a genus-five generalized Howe family.

This checks coefficient extraction, relevant factorizations, special fibers,
and the finite intersections governing the low-rank strata.
"""
import sympy as s
p=11
x,u,v=s.symbols('x u v')
Q=lambda a:x*x-a*x+1
F=s.Poly(s.expand((x**4-1)*Q(u)),x)
P=F**5
M=s.Matrix([[P.nth(p*i-j) for j in (1,2)] for i in (1,2)])
expected=s.Matrix([[3*u**4-5*u**2-1,-5*u**5-u**3+4*u],
                   [5*u**5+u**3-4*u,-3*u**4+5*u**2+1]])
def zero(q,*vars):
    return s.Poly(s.expand(q), *vars, modulus=p).is_zero
assert all(zero(M[i,j]-expected[i,j],u) for i in range(2) for j in range(2))
assert zero(s.expand(M.det()-3*(u*u-3)**2*(u*u-4)**3),u)
assert all(zero(M[i,j].subs(u,w),u) for w in (5,6) for i in range(2) for j in range(2))
G=s.Poly(s.expand(Q(u)*Q(v)),x)
H=(G**5).nth(10)
assert s.Poly(H,u,v,modulus=p).total_degree()==10
assert zero(H.subs({u:5,v:6})-4,u,v)
for w, fac in [
  (5,-2*(v-4)*(v-3)*(v*v+4*v+2)),
  (6,-2*(v+3)*(v+4)*(v*v-4*v+2))]:
    assert zero(H.subs(u,w)-fac,v)
    poly=s.Poly(fac,v,modulus=p)
    forbidden=s.Poly(v*(v*v-4)*(v-w)*(v-(11-w)),v,modulus=p)
    assert s.gcd(poly,forbidden).degree()==0
    assert s.gcd(poly,poly.diff()).degree()==0
for a,b,pr in [(1,8,5),(1,3,4),(5,1,3),(5,3,2),(5,6,1)]:
    assert a not in (0,2,9) and b not in (0,2,9) and a!=b
    h0=(int(H.subs({u:a,v:b}))%p==0)
    rs=5-2*(a in (5,6))-2*(b in (5,6))-h0
    assert rs==pr, (a,b,rs,pr)
print('EXACT_CHAR11_GENUS5_HOWE_CARTIER_FACTORS_16_2_OK')
print('M_11=',s.Matrix(2,2,lambda i,j:s.Poly(M[i,j],u,modulus=11).as_expr()))
print('H_11=',s.Poly(H,u,v,modulus=11).as_expr())
