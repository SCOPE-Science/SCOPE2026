#!/usr/bin/env python3
"""Exact icosahedral sign-cell checks and independent dodecahedral shadow tests.

Uses only Python's standard library. Coordinates lie in Z[phi], phi^2=phi+1.
The finite checks are exhaustive after the six-great-circle reduction.
"""
from itertools import combinations, product
from math import sqrt, pi, acos, asin, atan, tan, sin, cos, fsum
import random

Z=(0,0); ONE=(1,0); PHI=(0,1)
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[0],-x[1]
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x;c,d=y
    return a*c+b*d,a*d+b*c+b*d
def sgn(x):
    # Decide sign of (2a+b)+b sqrt(5) by INTEGER comparisons only.
    a,b=x; A=2*a+b; B=b
    if not B: return (A>0)-(A<0)
    if not A: return (B>0)-(B<0)
    if A*B>0: return (A>0)-(A<0)
    if A>0: return (A*A>5*B*B)-(A*A<5*B*B)
    return (5*B*B>A*A)-(5*B*B<A*A)
def scal(k,x): return k*x[0],k*x[1]
def vecadd(x,y): return tuple(add(a,b) for a,b in zip(x,y))
def vecneg(x): return tuple(neg(a) for a in x)
def vecscale(k,x): return tuple(scal(k,a) for a in x)
def dot(x,y):
    out=Z
    for a,b in zip(x,y):out=add(out,mul(a,b))
    return out
def cross(x,y):
    return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
            sub(mul(x[2],y[0]),mul(x[0],y[2])),
            sub(mul(x[0],y[1]),mul(x[1],y[0])))
def check(x,y,label):
    assert x==y, (label,x,y)
def fl(x): return x[0]+x[1]*(1+sqrt(5))/2

# Six chosen representatives of the opposite face-normal pairs.
S=((Z,neg(ONE),neg(PHI)),(Z,neg(ONE),PHI),
   (neg(ONE),neg(PHI),Z),(neg(ONE),PHI,Z),
   (neg(PHI),Z,neg(ONE)),(neg(PHI),Z,ONE))
R2=add(PHI,scal(2,ONE))
assert all(dot(v,v)==R2 for v in S)
assert all(abs(fl(dot(S[i],S[j])))>0 for i,j in combinations(range(6),2))
assert all(sgn(dot(S[i],cross(S[j],S[k])))!=0
           for i,j,k in combinations(range(6),3))
assert all(dot(S[i],S[j]) in (PHI,neg(PHI))
           for i,j in combinations(range(6),2))

results=[]; triangle_mask=[]; pentagon_mask=[]
for bits in product((-1,1),repeat=6):
    c=[]
    for i,j in combinations(range(6),2):
        cp=cross(S[i],S[j])
        for k in (-1,1):
            ray=vecscale(k,cp)
            if all(sgn(dot(vecscale(bits[z],S[z]),ray))>=0 for z in range(6)):
                c.append((i,j,ray))
    if not c: continue
    assert len(c) in (3,5)
    n=0
    for i,j in combinations(range(6),2):
        if bits[i]*bits[j] != sgn(dot(S[i],S[j])):
            n+=2
    assert (len(c),n) in ((3,12),(5,10))
    counts=[sum(int(z in (i,j)) for i,j,_ in c) for z in range(6)]
    act=[z for z,ct in enumerate(counts) if ct>0]
    assert len(act)==len(c) and all(counts[z] in (0,2) for z in range(6))
    for i,j,_ in c:
        q=sgn(dot(vecscale(bits[i],S[i]),vecscale(bits[j],S[j])))
        assert q==(-1 if len(c)==3 else 1)
    if len(c)==3:
        triangle_mask.append(bits)
        s=tuple(Z for _ in range(3))
        for z in range(6):s=vecadd(s,vecscale(bits[z],S[z]))
        # s_raw^2=12 phi^2=12(phi+1), and s_raw dot each active normal=2.
        check(dot(s,s),(12,12),'triangle intensity squared')
        for z in act:check(dot(s,vecscale(bits[z],S[z])),(2,0),'triangle side normal')
        # Each corner has exactly the same normalized intensity c>0.
        for _,_,ray in c:
            t=dot(s,ray)
            assert sgn(t)>0
            check(mul(t,t),mul((8,12),dot(ray,ray)),'triangle corner intensity')
    else:pentagon_mask.append(bits)
    results.append((bits,len(c),n))
assert len(results)==32
assert len(triangle_mask)==20 and len(pentagon_mask)==12
assert 20*3+12*5==120
print('EXACT_DODECA_SHADOW_CELLS_OK chambers=32 triangles=20 pentagons=12')

# Analytic value and sign of the new mixed moments.
theta=acos(1/sqrt(5));p12=15*theta/pi-5
M12=1.5-0.3*sqrt(5)
M10=3-M12
s2=6+6/sqrt(5)
T=3*theta-pi
D=1-1/sqrt(5)
C=sqrt(4+8/sqrt(5))
J12=(5/pi)*(s2*T/3+2*D*C*tan(pi/10))
Jall=2+20/(pi*sqrt(5))*(2+asin(1/sqrt(5)))
J10=Jall-J12
assert abs(20*T+12*(2*pi-5*theta)-4*pi)<1e-12
assert 0<p12<1
assert M12<3*p12
print('ANALYTIC_MOMENTS_OK',
      f'p12={p12:.15f}', f'M12={M12:.15f}',
      f'J12={J12:.15f}',f'Jall={Jall:.15f}')

# Independent geometry: reconstruct polar dodecahedron vertices from 20 faces
# of the icosahedron and evaluate planar convex hulls against the face-normal
# Cauchy formula. This is independent of the chamber count and area integrals.
N=[tuple(fl(x) for x in v) for v in S]+[tuple(-fl(x) for x in v) for v in S]

def d3(a,b,c):return (a[0]*(b[1]*c[2]-b[2]*c[1])-
                           a[1]*(b[0]*c[2]-b[2]*c[0])+
                           a[2]*(b[0]*c[1]-b[1]*c[0]))
def vcross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def vdot(a,b):return sum(x*y for x,y in zip(a,b))
def norm(x):return sqrt(vdot(x,x))
def unit(x):return tuple(y/norm(x) for y in x)
faces=[]
for i,j,k in combinations(range(12),3):
    if all(abs(vdot(N[a],N[b])-((1+sqrt(5))/2))<1e-9
           for a,b in ((i,j),(i,k),(j,k))):
        faces.append((i,j,k))
assert len(faces)==20
V=[]
for a,b,c in faces:
    det=d3(N[a],N[b],N[c]); assert abs(det)>1e-10
    V.append(tuple((vcross(N[b],N[c])[i]+vcross(N[c],N[a])[i]
                    +vcross(N[a],N[b])[i])/det for i in range(3)))
assert len(V)==20 and all(max(vdot(n,x) for n in N)<=1+1e-9 for x in V)

def hull(points):
    ss=sorted(set(points))
    def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lower=[]
    for p in ss:
        while len(lower)>=2 and turn(lower[-2],lower[-1],p)<=1e-10:lower.pop()
        lower.append(p)
    upper=[]
    for p in ss[::-1]:
        while len(upper)>=2 and turn(upper[-2],upper[-1],p)<=1e-10:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]
def polygon_area(h):
    return abs(sum(h[i][0]*h[(i+1)%len(h)][1]-h[i][1]*h[(i+1)%len(h)][0]
                   for i in range(len(h)))/2)
def projected(u):
    v=unit(vcross(u,(1.,0.,0.)) if abs(u[0])<0.85 else vcross(u,(0.,1.,0.)))
    w=vcross(u,v)
    h=hull([(vdot(x,v),vdot(x,w)) for x in V])
    return len(h),polygon_area(h)
# One face n_0·x=1 is a regular pentagon, recover its exact numerical area.
fv=[x for x in V if abs(vdot(N[0],x)-1)<1e-9]
assert len(fv)==5
nv=unit(N[0]);b=unit(vcross(nv,(1.,0.,0.)))
crossnv=vcross(nv,b)
F=polygon_area(hull([(vdot(x,b),vdot(x,crossnv)) for x in fv]))
assert F>0
rng=random.Random(45091)
for j in range(400):
    u=unit([rng.gauss(0,1) for _ in range(3)])
    vnum,area=projected(u)
    cut=sum(2 for i,k in combinations(range(6),2)
            if (vdot(N[i],u)*vdot(N[k],u)>0) !=
                 (sgn(dot(S[i],S[k]))>0))
    assert vnum==cut,(j,vnum,cut)
    bright=F*sum(abs(vdot(N[i],u))/sqrt(float(fl(R2))) for i in range(6))
    assert abs(area-bright)<1e-8,(area,bright)
print('DIRECT_DODECA_PROJECTED_HULL_OK hulls=400 faces=12 vertices=20')

# Independent deterministic sphere area quadrature of all three first and
# second weighted moments; these are numerical checks, not infinite proofs.
NGRID=240000
sumw12=sumw10=sumw2_12=sumw2_10=0.
nh12=0
for k in range(NGRID):
    z=1-2*(k+.5)/NGRID
    azi=k*pi*(3-sqrt(5))
    r=sqrt(1-z*z)
    u=(r*cos(azi),r*sin(azi),z)
    signs=[1 if vdot(N[i],u)>0 else -1 for i in range(6)]
    ct=2*sum(signs[i]*signs[j]!=sgn(dot(S[i],S[j]))
             for i,j in combinations(range(6),2))
    w=sum(abs(vdot(N[i],u))/sqrt(fl(R2)) for i in range(6))
    if ct==12:nh12+=1;sumw12+=w;sumw2_12+=w*w
    else:assert ct==10;sumw10+=w;sumw2_10+=w*w
errp=abs(nh12/NGRID-p12)
errm=abs(sumw12/NGRID-M12)
errj=abs(sumw2_12/NGRID-J12)
assert errp<0.002 and errm<0.006 and errj<0.02,(errp,errm,errj)
assert abs(sumw10/NGRID-M10)<0.006
assert abs((sumw2_12+sumw2_10)/NGRID-Jall)<0.02
print('INDEPENDENT_SPHERICAL_QUADRATURE_OK directions=',NGRID,
      'p_err=',round(errp,7),'m1_err=',round(errm,7),'m2_err=',round(errj,7))
