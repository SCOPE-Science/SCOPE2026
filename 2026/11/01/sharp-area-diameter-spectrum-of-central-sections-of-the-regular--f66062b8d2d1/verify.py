"""Independent exact and numerical checks for the central octahedron area-diameter spectrum.
Requires SymPy (see requirements.txt); run python3 verify.py.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, isclose, atan2
import random
import sympy as S

q,t=S.symbols('q t', real=True)
A2=4*(1+q*q+t*t)*(q*t+q+t)**2/((q+t)**2*(1+q)**2*(1+t)**2)
P=-(q*q+q+1)*t*t+(1-q)**2*(q+1)*t+q*(2*q*q-q+2)
D2=4*(1+q*q)/(1+q)**2
checks=0

def confirm(cond,label):
    global checks
    if not cond: raise AssertionError(label)
    checks+=1

confirm(S.simplify(S.diff(A2,t)+8*t*(q*t+q+t)*P/((1+q)**2*(q+t)**3*(1+t)**3))==0, 'derivative identity')
confirm(S.factor(P.subs(t,q)-3*q*(1-q))==0,'left endpoint derivative sign')
confirm(S.factor(P.subs(t,1)+3*q*q*(1-q))==0,'right endpoint derivative sign')
confirm(S.factor(A2.subs(t,q)-(q+2)**2*(2*q*q+1)/(q+1)**4)==0,'upper endpoint')
confirm(S.factor(A2.subs(t,1)-(2*q+1)**2*(q*q+2)/(q+1)**4)==0,'other endpoint')
confirm(S.factor(A2.subs(t,q)-A2.subs(t,1)-2*(1-q)**3/(1+q)**3)==0,'endpoint comparison')
confirm(S.factor(S.diff(4*(1+t*t)/(1+t)**2,t)-8*(t-1)/(1+t)**3)==0,'q=0 boundary')


def cross(u,v):
    return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])

def add(u,v):return tuple(x+y for x,y in zip(u,v))

def dot(u,v):return sum(x*y for x,y in zip(u,v))

# An independent area-vector computation from the actual six intersection vertices.
def exact_area_sq_and_diameter_sq(x,y):
    if x==0 and y==0: return F(4),F(4)
    v12=(y/(x+y),-x/(x+y),F(0))
    v13=(F(1)/(1+x),F(0),-x/(1+x))
    v23=(F(0),F(1)/(1+y),-y/(1+y))
    av=add(add(cross(v12,v13),cross(v13,v23)),cross(v12,v23))
    # Polygon area-vector is parallel to the normal; squared norm equals area squared.
    area_sq=dot(av,av)
    d_sq=max(4*dot(v,v) for v in (v12,v13,v23))
    return area_sq,d_sq

for a in range(0,14):
    for b in range(a,14):
        x,y=F(a,13),F(b,13)
        if x==0 and y==0:
            asq,dsq=exact_area_sq_and_diameter_sq(x,y)
            confirm(asq==4 and dsq==4, 'coordinate section')
            continue
        av,dv=exact_area_sq_and_diameter_sq(x,y)
        expected=4*(1+x*x+y*y)*(x*y+x+y)**2/((x+y)**2*(1+x)**2*(1+y)**2)
        confirm(av==expected,('exact area',a,b))
        confirm(dv==4*(1+x*x)/(1+x)**2,('exact diameter',a,b))

# Independently enumerate all 12 octahedron edges and intersect with the plane.
def enumerate_polygon_area(x,y):
    n=(x,y,1.0)
    verts=[]
    for i in range(3):
        for j in range(i+1,3):
            for si in (-1.0,1.0):
                for sj in (-1.0,1.0):
                    z0=n[i]*si; z1=n[j]*sj
                    if z0*z1>1e-15: continue
                    if abs(z1-z0)<1e-13:
                        continue
                    w=z1/(z1-z0); v=-z0/(z1-z0)
                    point=[0.0]*3
                    point[i]=si*w; point[j]=sj*v
                    if all(sum((point[k]-p[k])**2 for k in range(3))>1e-18 for p in verts):
                        verts.append(tuple(point))
    norm=sqrt(sum(v*v for v in n)); nn=tuple(v/norm for v in n)
    base=(1.,0.,0.)
    if abs(sum(base[i]*nn[i] for i in range(3)))>.95: base=(0.,1.,0.)
    basis=cross(nn,base); bn=sqrt(dot(basis,basis)); basis=tuple(v/bn for v in basis)
    basis2=cross(nn,basis)
    coords=[(dot(v,basis),dot(v,basis2)) for v in verts]
    coords.sort(key=lambda p:atan2(p[1],p[0]))
    return abs(sum(coords[i][0]*coords[(i+1)%len(coords)][1]-coords[i][1]*coords[(i+1)%len(coords)][0] for i in range(len(coords))))/2

rng=random.Random(20261031)
for k in range(2500):
    x=rng.uniform(.0001,1.0)
    y=rng.uniform(x,1.0)
    formula=2*sqrt(1+x*x+y*y)*(x*y+x+y)/((x+y)*(1+x)*(1+y))
    area=enumerate_polygon_area(x,y)
    confirm(isclose(formula,area,rel_tol=1e-10,abs_tol=1e-10),('edge enumeration',x,y,area,formula))
    coeff=(1-x)**2*(1+x); lead=1+x+x*x; constant=x*(2*x*x-x+2)
    root=(coeff+sqrt(coeff*coeff+4*lead*constant))/(2*lead)
    confirm(x<=root<=1,('unique critical',x,root))
    def areav(y): return 2*sqrt(1+x*x+y*y)*(x*y+x+y)/((x+y)*(1+x)*(1+y))
    am=areav(root); ap=areav(x)
    confirm(all(am-1e-10<=areav(x+(1-x)*j/40)<=ap+1e-10 for j in range(41)),('sharp bounds',x))
    r=sqrt(1+x*x)/(1+x)
    recovery=(1-r*r)/(r*r+sqrt(2*r*r-1))
    confirm(isclose(recovery,x,rel_tol=1e-10,abs_tol=1e-10),('diameter inversion',x))
confirm(exact_area_sq_and_diameter_sq(F(1),F(1))==(F(27,16),F(2)),'face normal endpoint')
confirm(exact_area_sq_and_diameter_sq(F(0),F(1))==(F(2),F(4)),'square endpoint')
print('VERIFY_OK',checks,'checks')
