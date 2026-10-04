#!/usr/bin/env python3
from itertools import product
import sympy as sp

x1,x2,x3,x4 = sp.symbols('x1 x2 x3 x4')
xs=(x1,x2,x3,x4)
z=(-(x1+x2+x3+x4),x1,x2,x3,x4)
c=(1,2,3,5,7)
a=tuple(sp.Rational(1,ci) for ci in c)

g=sp.expand(sum(a[i]*z[i]**3 for i in range(5)))
h=sp.expand(sum(c[i]*sp.prod(z[j] for j in range(5) if j != i) for i in range(5)))
H=sp.hessian(g,xs)
detH=sp.expand(H.det())
assert sp.expand(detH-sp.Rational(216,35)*h)==0

grad=[sp.expand(sp.diff(h,x)) for x in xs]

# The ten vertices of the standard Sylvester pentahedron in the chosen chart.
nodes=[
(-1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1),
(1,-1,0,0),(1,0,-1,0),(1,0,0,-1),(0,1,-1,0),(0,1,0,-1),(0,0,1,-1)
]
assert len(set(nodes))==10
for p in nodes:
    sub=dict(zip(xs,p))
    assert h.subs(sub)==0
    assert all(q.subs(sub)==0 for q in grad)
    HH=sp.Matrix([[sp.diff(h,xi,xj).subs(sub) for xj in xs] for xi in xs])
    assert HH.rank()==3

# The witness cubic surface is smooth: the four affine projective charts of its gradient are empty.
gg=[sp.diff(g,x) for x in xs]
for j,x in enumerate(xs):
    G=sp.groebner(gg+[x-1],*xs,order='grevlex')
    assert len(G.polys)==1 and G.polys[0].as_expr()==1

# Hilbert function of R/K, K the gradient ideal of the quartic h.
GK=sp.groebner(grad,*xs,order='grevlex')
lms=[tuple(p.LM(order=GK.order).exponents) for p in GK.polys]
def comps(n,k):
    if k==1:
        yield (n,)
    else:
        for i in range(n+1):
            for t in comps(n-i,k-1):
                yield (i,)+t
def divides(a,b):
    return all(u<=v for u,v in zip(a,b))
def hf_quotient(maxd):
    return [sum(1 for e in comps(d,4) if not any(divides(m,e) for m in lms)) for d in range(maxd+1)]
hfK=hf_quotient(8)
assert hfK==[1,4,10,16,19,16,10,10,10], hfK

# Hilbert function of the reduced ten-point scheme, by exact evaluation ranks.
def monomial_exponents(d):
    return list(comps(d,4))
def ev_rank(d):
    exps=monomial_exponents(d)
    M=[]
    for p in nodes:
        row=[]
        for e in exps:
            v=1
            for pi,ei in zip(p,e): v*=pi**ei
            row.append(v)
        M.append(row)
    return sp.Matrix(M).rank()
hfI=[ev_rank(d) for d in range(9)]
assert hfI==[1,4,10,10,10,10,10,10,10], hfI

defect=[u-v for u,v in zip(hfK,hfI)]
assert defect==[0,0,0,6,9,6,0,0,0], defect
assert sum(defect)==21

# A dehomogenizing form avoiding all ten nodes gives an exact length-ten projective Jacobian scheme.
L=x1+2*x2+4*x3+8*x4
for p in nodes:
    assert L.subs(dict(zip(xs,p))) != 0
GP=sp.groebner(grad+[L-1],*xs,order='grevlex')
lmp=[tuple(p.LM(order=GP.order).exponents) for p in GP.polys]
std=[]
for d in range(10):
    for e in comps(d,4):
        if not any(divides(m,e) for m in lmp): std.append(e)
assert len(std)==10, len(std)

print('VERIFY_OK')
print('hessian_scalar=216/35')
print('nodes=10 ordinary')
print('HF_R_over_K=' + ','.join(map(str,hfK)))
print('HF_nodes=' + ','.join(map(str,hfI)))
print('saturation_defect=' + ','.join(map(str,defect)) + '; length=21')
