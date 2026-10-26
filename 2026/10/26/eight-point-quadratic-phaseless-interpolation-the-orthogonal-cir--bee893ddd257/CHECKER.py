"""Exact supplementary algebra for eight-point quadratic phaseless interpolation."""
import sympy as s
from itertools import combinations

I=s.I
x,y,a,t,u,v=s.symbols('x y a t u v', real=True)
z=x+I*y
H=s.Matrix([[a,u+I*v,0],[u-I*v,t-a,-u-I*v],[0,-u+I*v,-t]])
V=s.Matrix([1,z,z*z])
F=s.expand((s.conjugate(V).T*H*V)[0]); rhs=s.expand((1-x*x-y*y)*(a+t*(x*x+y*y)+2*u*x-2*v*y))
assert s.simplify(F-rhs)==0
assert s.simplify(H.det()-(t-a)*(u*u+v*v-a*t))==0
checks=2

def row(w):
    w=s.sympify(w)
    X,Y=s.re(w).expand(complex=True),s.im(w).expand(complex=True)
    return [1,s.simplify(X*X+Y*Y),2*X,-2*Y]

def audit(wpts, expected):
    global checks
    mat=s.Matrix([row(w) for w in wpts]); assert mat.rank()==3,(wpts,mat.rank())
    vec=mat.nullspace()[0]
    aa,tt,uu,vv=vec
    DD=s.factor((tt-aa)*(uu*uu+vv*vv-aa*tt))
    assert s.simplify(uu*uu+vv*vv-aa*tt)>0,(wpts,vec)
    assert (s.simplify(DD)!=0)==expected,(wpts,vec,DD)
    assert s.simplify(H.subs({a:aa,t:tt,u:uu,v:vv}).det()-DD)==0
    for w in wpts:
        X,Y=s.re(w).expand(complex=True),s.im(w).expand(complex=True)
        assert s.simplify(rhs.subs({x:X,y:Y,a:aa,t:tt,u:uu,v:vv}))==0
        checks+=1
    checks+=4

# Nonorthogonal unit-centered and translated circles; collinear off-center and through origin.
for pts,exp in [([0,2,2*I],True),([2,3,4],True),([2,3,4+I],True),([2,3,3+I],True),([0,2,3],False),([2,3,5],True),([2*I,3*I,4*I],True),([0,2*I,3*I],False),([2,2*I,3+I],True)]:
    # Collinear 2,3,4 has line y=0 -> expected False, while x=const and y=const non-origin True.
    if pts == [2,3,4]: exp=False
    if pts == [2,3,5]: exp=False
    if pts == [2*I,3*I,4*I]: exp=False
    audit(pts,exp)

# Ordinary circle orthogonal to unit circle: center 2, radius sqrt(3).
r=s.sqrt(3)
audit([2+r,2+I*r,2-r],False)
# An ordinary translated circle, center 2 and radius 1 (not orthogonal).
audit([3,2+I,1],True)
# A diameter-line witness, valid on the whole real axis and the whole unit circle.
z0=s.symbols('z0',real=True)
p=z0+I*(1+z0*z0);q=z0-I*(1+z0*z0)
assert s.simplify(s.expand_complex(p*s.conjugate(p)-q*s.conjugate(q)))==0
checks+=1
# For the unit circle, conjugate-reciprocal condition implies equality exactly.
theta=s.symbols('theta',real=True)
zet=s.exp(I*theta)
P=zet+I*(1+zet*zet); Q=zet-I*(1+zet*zet)
assert s.trigsimp(s.expand_complex(P*s.conjugate(P)-Q*s.conjugate(Q)))==0
checks+=1
assert s.simplify(p/q-1)!=0
checks+=1
# 5 roots make evaluation of a trig polynomial of Laurent degree 2 injective.
omega=s.exp(2*s.pi*I/5)
assert s.Matrix([[s.exp(2*s.pi*I*k*j/5) for j in range(-2,3)] for k in range(5)]).det()!=0
checks+=1
# Example: determinant +2, corresponding to w=0,2,2i.
M=s.Matrix([row(w) for w in [0,2,2*I]])
assert M.rank()==3
assert H.subs({a:0,t:1,u:-1,v:1}).det()==2
checks+=2
print('PASS:',checks,'exact symbolic and geometric assertions')
