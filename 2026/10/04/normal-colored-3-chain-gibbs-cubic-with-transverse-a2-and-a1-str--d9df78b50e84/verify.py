import sympy as sp
from itertools import combinations
x11,x12,x13,x22,x23,x33=sp.symbols("x11 x12 x13 x22 x23 x33")
vs=[x11,x12,x13,x22,x23,x33]
f=x11*x13*x23-x12**2*x23+x12*x22*x13-x12*x13**2-x12*x13*x33+x12*x23**2-x22*x13*x23+x13**2*x23
g=[sp.factor(sp.diff(f,v)) for v in vs]
assert g[0]==x13*x23 and g[5]==-x12*x13 and g[3]==x13*(x12-x23)
y,w,z=sp.symbols("y w z")
assert sp.expand(g[1].subs({x13:0,x12:y,x23:w})-w*(-2*y+w))==0
assert sp.expand(g[4].subs({x13:0,x12:y,x23:w})-y*(-y+2*w))==0
assert all(sp.expand(q.subs({x12:0,x13:0,x23:0}))==0 for q in g)
q,s=sp.symbols("q s")
L={x11:q,x12:0,x13:s,x22:q+s,x23:0,x33:q}
assert all(sp.expand(h.subs(L))==0 for h in g)
assert sp.expand(g[1].subs({x12:0,x23:0})-x13*(-x13+x22-x33))==0
assert sp.expand(g[4].subs({x12:0,x23:0})-x13*(x11+x13-x22))==0
H=sp.hessian(f,vs); HL=H.subs(L)
assert sp.factor(HL.extract([0,1,2,4],[0,1,2,4]).det())==s**4
for I in combinations(range(6),5):
 for J in combinations(range(6),5): assert sp.expand(HL.extract(I,J).det())==0
a,b,c,t=sp.symbols("a b c t")
normal=sp.expand(f.subs({x11:a,x12:y,x13:z,x22:b,x23:w,x33:c}))
expected=(a-b)*z*w+(b-c)*y*z-y**2*w-y*z**2+y*w**2+z**2*w
assert sp.expand(normal-expected)==0
A=a-b; B=b-c; Hn=sp.hessian(normal,(y,z,w)).subs({y:0,z:0,w:0}); k=sp.Matrix([A,0,-B])
assert all(sp.simplify(v)==0 for v in Hn*k)
assert sp.factor(normal.subs({y:A*t,z:0,w:-B*t}))==A*B*(a-c)*t**3
print("VERIFY_OK")
