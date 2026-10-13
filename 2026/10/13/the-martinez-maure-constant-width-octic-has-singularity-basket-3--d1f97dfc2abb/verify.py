import sympy as sp

I=sp.I
x,y,w,z,u,v,h,r=sp.symbols('x y w z u v h r')
s=x**2+y**2
q=y*(y**2-3*x**2)
F=sp.expand((s**2+8*q)**2 + 432*q*(351-10*s) - 567**3 - 28*s**3 - 486*s*(67*s-567*18))
assert sp.Poly(F,x,y).total_degree()==8

# C3 symmetry.
r3=sp.sqrt(3)
Rx=-x/sp.Integer(2)-r3*y/sp.Integer(2)
Ry=r3*x/sp.Integer(2)-y/sp.Integer(2)
assert sp.expand(F.subs({x:Rx,y:Ry}, simultaneous=True)-F)==0

# Rational normalization parameter in complex coordinates u=x+iy, v=x-iy.
upar=-I*z**4+8*z-2*I*z**-2
vpar=2*I*z**2+8*z**-1+I*z**-4
xpar=sp.cancel((upar+vpar)/2)
ypar=sp.cancel((upar-vpar)/(2*I))
assert sp.cancel(F.subs({x:xpar,y:ypar}))==0
p1=sp.expand(u*z**2 + I*z**6 - 8*z**3 + 2*I)
p2=sp.expand(v*z**4 - 2*I*z**6 - 8*z**3 - I)
res=sp.factor(sp.resultant(p1,p2,z))
Fuv=sp.factor(F.subs({x:(u+v)/2,y:(u-v)/(2*I)}))
assert sp.expand(res-Fuv)==0
subs=sp.subresultants(p1,p2,z)
lin=subs[-2]
assert sp.degree(lin,z)==1
coef=sp.Poly(lin,z).coeff_monomial(z)
u1=sp.simplify(upar.subs(z,1)); v1=sp.simplify(vpar.subs(z,1))
assert sp.simplify(coef.subs({u:u1,v:v1}))==151552
# Hence the generic common root z is unique: the parametrization is birational.

# Projective parametrization and no base points.
S,T=sp.symbols('S T')
U=-I*S**8+8*S**5*T**3-2*I*S**2*T**6
V=2*I*S**6*T**2+8*S**3*T**5+I*T**8
W=S**4*T**4
assert sp.simplify(V.subs(S,0))==I*T**8
assert sp.simplify(U.subs(T,0))==-I*S**8
# Homogenized equation vanishes identically.
P=sp.Poly(F,x,y)
Fh=sp.expand(sum(c*x**a*y**b*w**(8-a-b) for (a,b),c in P.terms()))
Xsub=(U+V)/2; Ysub=(U-V)/(2*I)
assert sp.expand(Fh.subs({x:Xsub,y:Ysub,w:W}))==0
assert sp.factor(Fh.subs(w,0))==(x**2+y**2)**4

# Exact affine singular set: nine points, organized as 3 real cusps + two C3 node orbits.
Fx,Fy=sp.diff(F,x),sp.diff(F,y)
sol=sp.solve_poly_system([F,Fx,Fy],x,y)
assert len(sol)==9

def R(P):
    a,b=P
    return (sp.simplify(-a/2-r3*b/2), sp.simplify(r3*a/2-b/2))
Pc=(sp.Integer(0),sp.Integer(9))
Pn=(sp.Integer(0),-sp.Integer(9)+6*I*r3)
Pnb=(sp.Integer(0),-sp.Integer(9)-6*I*r3)
expected=[]
for P0 in (Pc,Pn,Pnb):
    P=P0
    for _ in range(3):
        expected.append(P)
        P=R(P)
assert len(expected)==9
nums=[(complex(sp.N(a,20)),complex(sp.N(b,20))) for a,b in expected]
for i in range(9):
    for j in range(i):
        assert abs(nums[i][0]-nums[j][0])+abs(nums[i][1]-nums[j][1])>1e-8
for a,b in expected:
    assert sp.simplify(F.subs({x:a,y:b}))==0
    assert sp.simplify(Fx.subs({x:a,y:b}))==0
    assert sp.simplify(Fy.subs({x:a,y:b}))==0

# Node representative: nondegenerate quadratic term.
H=sp.hessian(F,(x,y))
hdet=sp.simplify(H.det().subs({x:Pn[0],y:Pn[1]}))
assert hdet!=0

# E6 representative: normalization parameter near z=i has valuations (3,4).
xs=sp.series(xpar.subs(z,I+h),h,0,7).removeO().expand()
ys=sp.series(ypar.subs(z,I+h)-9,h,0,7).removeO().expand()
assert sp.Poly(xs,h).as_dict().get((3,))==12
assert sp.Poly(ys,h).as_dict().get((4,))==-9
assert min(k[0] for k,c in sp.Poly(xs,h).terms() if c)!=0
assert min(k[0] for k,c in sp.Poly(ys,h).terms() if c)!=0
# Check exact orders directly.
def valuation(poly,var):
    P=sp.Poly(sp.expand(poly),var)
    return min(mon[0] for mon,c in P.terms() if c!=0)
assert valuation(xs,h)==3 and valuation(ys,h)==4

# One point at infinity in chart V=1; after removing the tangent term, valuations are (2,7), hence A6.
U0=-I*r**8+8*r**5-2*I*r**2
V0=2*I*r**6+8*r**3+I
W0=r**4
a=sp.series(U0/V0,r,0,12).removeO().expand()
b=sp.series(W0/V0,r,0,12).removeO().expand()
c=sp.series(b+I*a**2/4,r,0,12).removeO().expand()
assert valuation(a,r)==2 and valuation(c,r)==7
# The conjugate point has the same analytic type.

# Delta-genus exhausts the plane-octic arithmetic genus.
pa=(8-1)*(8-2)//2
Delta=3*3 + 6*1 + 2*3
assert pa==21 and Delta==21
print('VERIFY_OK')
print('affine_singularities=3_E6_plus_6_A1')
print('infinity_singularities=2_A6')
print('normalization=P1')
print('delta_total=21=arithmetic_genus')
