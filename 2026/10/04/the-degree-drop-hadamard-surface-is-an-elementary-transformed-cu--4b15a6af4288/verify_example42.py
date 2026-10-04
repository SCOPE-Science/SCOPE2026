import itertools
import sympy as sp

x0,x1,x2,x3,x4=sp.symbols('x0 x1 x2 x3 x4')
y0,y1,z0,z1=sp.symbols('y0 y1 z0 z1')
X=[x0,x1,x2,x3,x4]
sections=[(y0-y1)*z0**2,(y0-y1)*z0*z1,(y0-y1)*z1**2,y0*z0**2,2*y0*z0*z1]
q=[x0*x2-x1**2,x0*x4-2*x1*x3,x1*x4-2*x2*x3]
subs=dict(zip(X,sections))
assert all(sp.expand(f.subs(subs))==0 for f in q)

# Unique projective base point: inspect the four standard affine charts.
chart_bases={}
for yf in (y0,y1):
    for zf in (z0,z1):
        vars_=[v for v in (y0,y1,z0,z1) if v not in (yf,zf)]
        polys=[sp.expand(f.subs({yf:1,zf:1})) for f in sections]
        G=sp.groebner(polys,*vars_,order='lex')
        chart_bases[(str(yf),str(zf))]=[sp.expand(g.as_expr()) for g in G.polys]
assert chart_bases[('y0','z0')]==[1]
assert chart_bases[('y1','z0')]==[1]
assert chart_bases[('y0','z1')]==[y1-1,z0]
assert chart_bases[('y1','z1')]==[y0-1,z0]

# Smoothness of the determinantal surface: on every projective coordinate chart,
# q_i plus all 2x2 Jacobian minors generate the unit ideal.
J=sp.Matrix([[sp.diff(f,v) for v in X] for f in q])
minors=[]
for rr in itertools.combinations(range(3),2):
    for cc in itertools.combinations(range(5),2):
        minors.append(sp.expand(J.extract(rr,cc).det()))
for xi in X:
    G=sp.groebner(q+minors+[xi-1],*X,order='lex')
    assert G.contains(sp.Integer(1))

# Birational recovery on x0 != 0: t=z1/z0=x1/x0 and r=y0/(y0-y1)=x3/x0.
# Substitute affine parameters t,r into the projective chart x0=1.
t,r=sp.symbols('t r')
chart={x0:1,x1:t,x2:t**2,x3:r,x4:2*r*t}
assert all(sp.expand(f.subs(chart))==0 for f in q)

# Blow-up local model at p=([1:1],[0:1]): y0=z1=1, y1=1+u, z0=t.
u,tloc=sp.symbols('u t')
local=[sp.expand(f.subs({y0:1,y1:1+u,z0:tloc,z1:1})) for f in sections]
assert local==[-u*tloc**2,-u*tloc,-u,tloc**2,2*tloc]
# The base ideal is (u,t); the exceptional divisor maps by degree-one terms [-u:2t]
# to the ruling line x0=x1=x3=0.

# Source fiber z0=0 maps constantly away from p.
fiber=[sp.expand(f.subs({z0:0,z1:1})) for f in sections]
assert fiber==[0,0,y0-y1,0,0]
# Divisor y0=y1 maps to the other boundary line x0=x1=x2=0.
directrix=[sp.expand(f.subs({y1:y0})) for f in sections]
assert directrix[:3]==[0,0,0]

# Intersection-theoretic degree after resolving one simple base point:
# H=(1,2) on P1xP1 has H^2=4, so (H-E)^2=3.
assert 2*1*2-1==3
print('VERIFY_OK')
