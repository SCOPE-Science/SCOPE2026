#!/usr/bin/env python3
"""Exact checks for the discriminant stratification of a cubic net."""
from sympy import symbols, Matrix, expand, factor, diff, groebner, simplify
from itertools import combinations

x,y,z,a,b,c,u,v,t = symbols('x y z a b c u v t')
f= y*z*(y-z)
g= x*z*(z-x)
h= x*y*(x-y)
G=a*f+b*g+c*h
assert expand(Matrix([[diff(q,r) for r in (x,y,z)] for q in (f,g,h)]).det()+6*x*y*z*(x-y)*(x-z)*(y-z)) == 0
assert expand(G.subs({a:0,b:u,c:v})-x*(u*z*(z-x)+v*y*(x-y))) == 0
assert expand(G.subs({a:u,b:u,c:v})-(x-y)*(v*x*y-u*z*(x+y)+u*z*z)) == 0
assert [factor(diff(G,k).subs(x,0)) for k in (x,y,z)] == [b*z*z-c*y*y,a*z*(2*y-z),a*y*(y-2*z)]
assert [expand(diff(G,k).subs({x:t,y:t})) for k in (x,y,z)] == [expand(-2*b*t*z+b*z*z+c*t*t),expand(2*a*t*z-a*z*z-c*t*t),expand((a-b)*t*(t-2*z))]
assert factor(Matrix([[0,v/2,-u/2],[v/2,0,-u/2],[-u/2,-u/2,u]]).det())==u*v*(u-v)/4
assert factor(Matrix([[0,v/2,-u/2],[v/2,-v,0],[-u/2,0,u]]).det())==u*v*(u-v)/4
assert expand(G.subs({a:1,b:1,c:0})+z*(x-y)*(x+y-z))==0
assert expand(G.subs({a:0,b:0,c:1})-x*y*(x-y))==0
assert expand(G.subs({a:1,b:1,c:1})-(x-y)*(x-z)*(y-z))==0
assert expand(G.subs({x:y,y:x}, simultaneous=True)+G.subs({a:b,b:a},simultaneous=True)) == 0
for var in (x,y,z):
    p=expand(G.subs({a:1,b:2,c:3,var:1}))
    remain=[q for q in (x,y,z) if q!=var]
    gb=groebner([diff(p,q) for q in remain]+[p],*remain,order='lex')
    assert len(gb.polys)==1 and gb.polys[0].as_expr()==1, (var,gb)
# The arrangement a*b*c*(a-b)*(a-c)*(b-c) has four triple points and three double points.
pts={(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,1,0),(1,0,1),(0,1,1)}
lines=lambda A,B,C: [A,B,C,A-B,A-C,B-C]
assert sorted([sum(w==0 for w in lines(*p)) for p in pts])==[2,2,2,3,3,3,3]
print('VERIFY_OK: gradient determinant, six lines, conic nodes, 7 crossings, three affine Gröbner certificates')
