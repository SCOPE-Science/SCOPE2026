#!/usr/bin/env python3
"""Exact rational and Monte Carlo checks of a Poisson angular-reset colloid."""
from fractions import Fraction as F
from math import cos, sin, sqrt
from random import Random


def moments_from_laplace(r):
    r=F(r)
    c1=r/(r+1)
    c2=r/(r+4)
    es=1/r
    es2=2/r**2
    ex=c1-1
    ex2=(F(3)+c2-4*c1)/2
    exs=r/(r+1)**2-1/r
    ey2=(1-c2)/2
    v=ex/es
    par=(ex2-2*v*exs+v*v*es2)/(2*es)
    perp=ey2/(2*es)
    return v,par,perp

def closed(r):
    r=F(r)
    return (-r/(r+1),
            r*(2*r**2+2*r+3)/((r+1)**3*(r+4)),
            r/(r+4))

count=0
for num in range(1,101):
    for den in (1,3,7,17,37):
        r=F(num,den)
        assert moments_from_laplace(r)==closed(r),r
        count+=3

def p(r):return 2*r**3+4*r**2-r+6
def crossing(r):return r**3+r**2+r-2
assert p(F(0))>0
for j in range(1,300):
    r=F(j,20)
    assert p(r)>0
    count+=1
assert crossing(F(8105,10000))<0<crossing(F(8106,10000))
assert closed(F(2))[1]==F(5,27)
assert closed(F(2))[2]==F(1,3)
count+=4

def simulate(r,n=75000,seed=7):
    gen=Random(seed)
    t=xx=yy=x2=y2=xy=0.0
    v,par,perp=map(float,closed(F(str(r))))
    for _ in range(n):
        s=gen.expovariate(r)
        phi=gen.gauss(0.0,sqrt(2*s))
        x=cos(phi)-1-v*s
        y=sin(phi)
        t+=s
        xx+=x
        yy+=y
        x2+=x*x
        y2+=y*y
        xy+=x*y
    # Renewal reward samples estimate the centered diffusion rates.
    gotpar=x2/(2*t); gotperp=y2/(2*t)
    assert abs(gotpar-par)<0.018,(r,gotpar,par)
    assert abs(gotperp-perp)<0.018,(r,gotperp,perp)
    assert abs(xy/t)<0.024,(r,xy/t)
    assert abs(xx/t)<0.018,(r,xx/t)
    return gotpar,gotperp,xx/t

for i,r in enumerate((0.1,0.5,1,2,5,20)):
    vals=simulate(r,seed=519+i)
    print(f'r={r:<4}: simulated (parallel,perpendicular,centered speed)={vals}')
    count+=4
print(f'PASS: {count} exact and stochastic checks; simulations 450,000 complete renewal excursions')

# An independent vector/matrix moment reconstruction for generic couplings.
def matrix_from_moments(r, a, E):
    r=F(r); a=tuple(map(F,a))
    E=[[F(z) for z in line] for line in E]
    c1=r/(r+1); c2=r/(r+4)
    u=(1-c2)/2
    w=1+c2-2*c1
    exs=r/(r+1)**2-1/r
    v=[-r*z/(r+1) for z in a]
    s2=2/r**2
    norm=sum(z*z for z in a)
    ans=[]
    for i in range(2):
        row=[]
        for j in range(2):
            dij=F(int(i==j))
            # Centered reward covariance per mean cycle time, divided by two.
            ey2=u*norm*dij + w*a[i]*a[j]
            mixed=-(v[i]*a[j]+a[i]*v[j])*exs
            slow=v[i]*v[j]*s2
            geom=r/2*(ey2+mixed+slow)
            isotropic=(E[0][0]+E[1][1])/2
            trans=isotropic*dij+r/(r+4)*(E[i][j]-isotropic*dij)
            row.append(geom+trans)
        ans.append(row)
    return ans

def matrix_closed(r,a,E):
    r=F(r); a=tuple(map(F,a)); E=[[F(z) for z in line] for line in E]
    _,fp,ft=closed(r)
    norm=sum(z*z for z in a)
    isotropic=(E[0][0]+E[1][1])/2
    return [[isotropic*int(i==j)+r/(r+4)*(E[i][j]-isotropic*int(i==j))+
             norm*ft*int(i==j)+(fp-ft)*a[i]*a[j]
             for j in range(2)] for i in range(2)]

extra=0
for r in (F(1,7),F(1,2),F(1),F(2),F(9,2),F(35)):
    for a in ((1,0),(2,3),(-1,4),(F(3,5),F(-7,8))):
        for E in (((1,0),(0,1)),((3,1),(1,2)),((7,-2),(-2,5))):
            assert matrix_from_moments(r,a,E)==matrix_closed(r,a,E)
            extra+=4
assert matrix_closed(F(0)+F(1,10**6),(0,0),((3,1),(1,2)))[0][1] == F(1,10**6)/(F(1,10**6)+4)
print(f'PASS: {extra+1} further generic-mobility exact matrix identities')

# A separate Euler-path witness with genuinely anisotropic body diffusion.
# This tests the spatial and angular covariance without sampling from the
# derived closed-form Gaussian renewal rewards.
from math import sin as _sin, cos as _cos

def generic_path_check(rate,n,seed):
    rng=Random(seed)
    a=(2.,-1.)
    E=((3,1),(1,2))
    target=matrix_closed(F(str(rate)),a,E)
    sx2=sxy=sy2=total=0.0
    vel=[-rate*z/(rate+1) for z in a]
    for _ in range(n):
        s=rng.expovariate(rate)
        ds=s/28
        z=sqrt(2*ds)
        theta=0.0
        bx=by=0.0
        for _ in range(28):
            n1=rng.gauss(0,1); n2=rng.gauss(0,1)
            dx=z*sqrt(3)*n1
            dy=z*(n1/sqrt(3)+sqrt(5/3)*n2)
            bx+=_cos(theta)*dx-_sin(theta)*dy
            by+=_sin(theta)*dx+_cos(theta)*dy
            theta+=z*rng.gauss(0,1)
        xx=bx+a[0]*(_cos(theta)-1)-a[1]*_sin(theta)-vel[0]*s
        yy=by+a[0]*_sin(theta)+a[1]*(_cos(theta)-1)-vel[1]*s
        sx2+=xx*xx; sxy+=xx*yy; sy2+=yy*yy; total+=s
    estimates=((sx2/(2*total),sxy/(2*total)),(sxy/(2*total),sy2/(2*total)))
    for i in range(2):
        for j in range(2):
            assert abs(estimates[i][j]-float(target[i][j]))<0.085, (rate,i,j,estimates,target)
    print(f'anisotropic-body path test at rate {rate}: {estimates}')

for j,rate in enumerate((0.5,2.,8.)):
    generic_path_check(rate,27000,72+int(rate*10))
print('PASS: 12 anisotropic-path covariance checks across three reset rates')

# Exact coefficient-level verification of the longitudinal derivative factor.
def poly_mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a0 in enumerate(p):
        for j,b0 in enumerate(q):
            out[i+j]+=a0*b0
    return out

def poly_add(p,q):
    return [(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
            for i in range(max(len(p),len(q)))]

def poly_neg(p):return [-x for x in p]
def poly_der(p):return [(i+1)*p[i+1] for i in range(len(p)-1)]
N=[0,3,2,2]
A=poly_mul(poly_mul([1,1],[1,1]),[1,1])
Den=poly_mul(A,[4,1])
num=poly_add(poly_mul(poly_der(N),Den),poly_neg(poly_mul(N,poly_der(Den))))
P=[6,-1,4,2]
expected=poly_neg(poly_mul(poly_mul([-2,1],P),poly_mul([1,1],[1,1])))
assert num==expected,(num,expected)
print('PASS: exact polynomial-coefficient identity for the sharp derivative')
