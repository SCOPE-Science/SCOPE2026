#!/usr/bin/env python3
"""Exact arithmetic spot checks for the two-parallel-line quadratic phase-retrieval theorem.
The printed rank tests are finite checks; the proof in RESULT.md covers arbitrary nodes.
"""
from sympy import Matrix, I, symbols, expand, Poly, det, factor, simplify
x, y, h = symbols('x y h', real=True)
a,b,c,u,v,s,t,w,k = symbols('a b c u v s t w k', real=True)
unknowns = (a,b,c,u,v,s,t,w,k)
q = a + b*(x*x+y*y)+c*(x*x+y*y)**2 + 2*(u*x-v*y)+2*(s*(x*x-y*y)-2*t*x*y)+2*(w*x-k*y)*(x*x+y*y)
assert expand(q.subs(y,0)).coeff(x,4)==c
assert expand(q.subs(y,h)).coeff(x,3)==2*w
H = Matrix([[0,-2*I*h,1],[2*I*h,-2,0],[1,0,0]])
assert simplify(det(H)-2)==0
assert simplify(q.subs({a:0,b:-2,c:0,u:0,v:-2*h,s:1,t:0,w:0,k:0})-4*y*(h-y))==0
count=0
sets=[
  ([0,1,2,3],[0,1,2,4],1,8),
  ([0,1,2,3],[0,1,2,3],1,7),
  ([-2,0,4,7],[-10,2,6,13],2,8),
  ([-3,0,1,7],[-5,1,3,6],-3,7),
  ([1,2,4,8],[0,4,5,9],2,8),
  ([-10,2,3,7],[-5,-2,2,5],1,8),
]
for r, ss, height, expected in sets:
    pts=[(z,0) for z in r]+[(z,height) for z in ss]
    A=Matrix([[expand(q.subs({x:xi,y:yi})).coeff(z) for z in unknowns] for xi,yi in pts])
    rk=A.rank()
    assert rk==expected,(r,ss,rk,expected)
    assert (rk==8)==(sum(r)!=sum(ss))
    if rk==8:
        assert len(A.nullspace())==1
        vec=A.nullspace()[0]
        assert simplify(vec[2])==0
        mat=Matrix([[vec[0],vec[3]+I*vec[4],vec[5]+I*vec[6]],
                    [vec[3]-I*vec[4],vec[1],vec[7]+I*vec[8]],
                    [vec[5]-I*vec[6],vec[7]-I*vec[8],vec[2]]])
        assert simplify(det(mat))!=0
    else:
        assert len(A.nullspace())==2
    count+=1
print('Exact symbolic identity, full-rank kernel, and determinant assertions: PASS')
print(f'Finite sample-array rank and nullity cases: {count} PASS')
print('Universal two-line criterion relies on the written proof, not these finite tests.')
