"""Exact verification of the characteristic-three special fibre of the twelve-conic Hesse arrangement.

Requires Python 3.11+ and SymPy 1.13+. All symbolic identities use GF(3)[t,x,y,z].
Run: python verify_hesse_char3.py
"""
import itertools
import sympy as sp

x,y,z,t,w = sp.symbols('x y z t w')
w2 = -w-1
source = [
 x**2+(t+1)*(w*x*y+w2*x*z+y*z)+w2*y**2+w*z**2,
 x**2+(t+1)*(w2*x*y+w*x*z+y*z)+w*y**2+w2*z**2,
 x*y-t*z**2,
 x**2+(w*t+1)*(x*y+w*x*z+w*y*z)+y**2+w2*z**2,
 x**2+(w2*t+1)*(x*y+w2*x*z+w2*y*z)+y**2+w*z**2,
 x**2+(w*t+w2)*(x*y+y*z+w*x*z)+w*y**2+z**2,
 x*z-t*y**2,
 x**2+(w2*t+w)*(x*y+y*z+w2*x*z)+w2*y**2+z**2,
 x**2+(t+w2)*(x*y+x*z+w2*y*z)+w*y**2+w*z**2,
 x**2+(t+w)*(x*y+x*z+w*y*z)+w2*(y**2+z**2),
 t*x**2-y*z,
 x**2+(t+1)*(x*y+x*z+y*z)+y**2+z**2
]
A=x*y-t*z**2
B=x*z-t*y**2
C=y*z-t*x**2
D=x**2+y**2+z**2+(t+1)*(x*y+y*z+z*x)
components = [A,B,C,D]

def gf3(expr,*gens):
    return sp.Poly(sp.expand(expr), *(gens or (t,x,y,z)), modulus=3)

# In the cyclotomic residue field at 3, omega maps to 1.
expected = [D,D,A,D,D,D,B,D,D,D,-C,D]
for j,(f,g) in enumerate(zip(source,expected),1):
    assert gf3(f.subs(w,1)) == gf3(g), f'specialization of conic {j}'
assert len(source)==12 and len(expected)==12

# Conics are smooth for t different from 0,1.
for f,det in zip(components,[-t,-t,-t,1-t**3]):
    assert gf3(sp.det(sp.hessian(f,(x,y,z))))==gf3(det)

# The six predicted pairwise intersections, using multiplicity and component labels.
E=[(1,0,0),(0,1,0),(0,0,1)]
P=[(t,1,1),(1,t,1),(1,1,t)]
for p in E+P:
    vals=[gf3(f.subs(dict(zip((x,y,z),p)),simultaneous=True)) for f in components]
    count=sum(v.is_zero for v in vals)
    assert count==(2 if p in E else 3), (p,vals)

# The symmetric group on x,y,z permutes A,B,C, while D is invariant.
for perm in itertools.permutations((x,y,z)):
    subs=dict(zip((x,y,z),perm))
    image={gf3(f.subs(subs,simultaneous=True)).as_expr() for f in (A,B,C)}
    assert image=={gf3(f).as_expr() for f in (A,B,C)}
    assert gf3(D.subs(subs,simultaneous=True))==gf3(D)

# At [1:0:0], A and B are transverse.
point={x:1,y:0,z:0}
Ga=[gf3(sp.diff(A,j).subs(point)).as_expr() for j in (x,y,z)]
Gb=[gf3(sp.diff(B,j).subs(point)).as_expr() for j in (x,y,z)]
assert Ga==[0,1,0] and Gb==[0,0,1]

# At [t:1:1], work on z=1 and set x=t+u,y=1+v.
u,v=sp.symbols('u v')
local={x:t+u,y:1+v,z:1}
a=gf3(A.subs(local),t,u,v)
b=gf3(B.subs(local),t,u,v)
d=gf3(D.subs(local),t,u,v)
assert a == gf3(u+t*v+u*v,t,u,v)
assert b == gf3(u+t*v-t*v*v,t,u,v)
assert d == gf3((t-1)*(u+t*v)+u*u+v*v+(t+1)*u*v,t,u,v)
# On A: u=-t*v/(1+v). On B: u=-t*v+t*v*v.
uA=-t*v/(1+v)
uB=-t*v+t*v*v

def rational_mod(expr):
    num,den=sp.fraction(sp.cancel(expr))
    return gf3(num,t,v),gf3(den,t,v)

assert rational_mod(B.subs(local).subs(u,uA)) == (
    gf3(-t*v**3,t,v),gf3(1+v,t,v))
assert rational_mod(A.subs(local).subs(u,uB)) == (
    gf3(t*v**3,t,v),gf3(1,t,v))
assert rational_mod(D.subs(local).subs(u,uA)) == (
    gf3(v*v*((t-1)**2+(t-1)*v+v*v),t,v),gf3((1+v)**2,t,v))
assert rational_mod(D.subs(local).subs(u,uB)) == (
    gf3(v*v*((t-1)**2+(t-t*t)*v+t*t*v*v),t,v),gf3(1,t,v))
# The leading coefficients of the three restrictions are t, (t-1)^2, (t-1)^2.
# Thus the pairwise local intersection multiplicities are exactly 3,2,2.
# Bezout's bound 4 for each distinct conic pair makes this the entire incidence list.

# Direct independent point census over F3 and F9 (GF9 = GF3[a]/(a*a+1)).
def add(a,b): return ( (a%3+b%3)%3 )+3*((a//3+b//3)%3)
def neg(a): return (-a%3)+3*((-(a//3))%3)
def mul(a,b):
    a0,a1=a%3,a//3;b0,b1=b%3,b//3
    return ((a0*b0+2*a1*b1)%3)+3*((a0*b1+a1*b0)%3)
def pwr(a,n):
    out=1
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n>>=1
    return out
def inv(a):
    assert a!=0
    return pwr(a,7)
def squared(a):return mul(a,a)
def sub(a,b):return add(a,neg(b))
def projectively_normalize(q):
    for k,c in enumerate(q):
        if c!=0:
            sc=inv(c)
            return tuple(mul(sc,entry) for entry in q)
    raise ValueError('zero vector')
def conic_evals(q,param):
    xx,yy,zz=q
    ab=mul(xx,yy);ac=mul(xx,zz);bc=mul(yy,zz)
    sqx,sqy,sqz=map(squared,q)
    return [sub(ab,mul(param,sqz)),sub(ac,mul(param,sqy)),sub(bc,mul(param,sqx)),
            add(add(add(sqx,sqy),sqz),mul(add(param,1),add(add(ab,ac),bc)))]
for k in [3,9]:
    elements = list(range(k)) if k==9 else [0,1,2]
    # Every element in the q-subfield is represented by 0,1,2 for F3.
    pts=set()
    for yy in elements:
        for zz in elements:pts.add((1,yy,zz))
    for zz in elements:pts.add((0,1,zz))
    pts.add((0,0,1))
    assert len(pts)==k*k+k+1
    for param in elements:
        if param in [0,1]:continue
        predicted={projectively_normalize(p) for p in [(1,0,0),(0,1,0),(0,0,1),
            (param,1,1),(1,param,1),(1,1,param)]}
        observed={q for q in pts if conic_evals(q,param).count(0)>=2}
        assert predicted==observed, (k,param,predicted,observed)
        assert len(observed)==6

print('VERIFY_OK: twelve-conic specialization, smoothness, six points, local contacts, Bezout and F3/F9 census')
