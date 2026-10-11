"""Numerical and rational-identity checks for a sharp Hilbert-block Birkhoff symmetry theorem.
No finite computation replaces the analytic proof.
"""
import math
import random

rng=random.Random(20261008)

def defect(p,z):
    if abs(p-2)<1e-14:
        return 0.0
    a=abs(p-2)*z
    den=math.exp(math.log(math.cosh(z))/p
                 +(p-1)*math.log(math.cosh((p-1)*z))/p)
    return math.sinh(a)/den

def scalar(p,t):
    return (t**(1/p)*abs(t**(p-2)-1)
           / ((1+t)**(1/p)*(1+t**(p-1))**((p-1)/p)))

def golden_max(func,left,right):
    q=(5**0.5-1)/2
    a,b=left,right
    c=b-q*(b-a); d=a+q*(b-a)
    fc,fd=func(c),func(d)
    for _ in range(160):
        if fc<fd:
            a,c,fc=c,d,fd
            d=a+q*(b-a);fd=func(d)
        else:
            b,d,fd=d,c,fc
            c=b-q*(b-a);fc=func(c)
    x=(a+b)/2
    return x,func(x)

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def norm(x):
    return math.sqrt(dot(x,x))

def unit(n):
    x=[rng.gauss(0,1) for _ in range(n)]
    s=norm(x)
    return [v/s for v in x]

checks=0
for p in (1.15,1.4,1.6,1.9,2.1,2.4,3,4,7,12):
    for z in (0.0,0.05,0.2,0.75,1,1.4,2.5,3.4):
        t=math.exp(2*z)
        assert abs(defect(p,z)-scalar(p,t))<3e-11
        checks+=1
        q=p/(p-1)
        assert abs(defect(p,z)-defect(q,(p-1)*z))<3e-10
        checks+=1
    for j in range(250):
        t=math.exp(rng.uniform(-4,4))
        w=rng.uniform(0.0001,0.9999)
        A=t**p-1
        z=(min(w*t,1-w))/(1+w*A)**((p-1)/p)
        wopt=1/(1+t)
        bound=min(wopt*t,1-wopt)/(1+wopt*A)**((p-1)/p)
        assert z<=bound+3e-13,(p,t,w,z,bound)
        assert 1+w*A/p>0 and 1+A*(p-1+w)/p>0
        checks+=1

# Reconstruct the exact attaining pair for each exponent using unit Hilbert vectors.
for p in (1.2,1.5,2.4,3,5,10):
    zmax,D=golden_max(lambda z:defect(p,z),0,7)
    t=math.exp(2*zmax)
    w=1/(1+t)
    a=w**(1/p); b=(1-w)**(1/p)
    rho=(1+w*(t**p-1))**(-1/p)
    c=a*t*rho;d=b*rho
    assert abs(a**p+b**p-1)<1e-12
    assert abs(c**p+d**p-1)<1e-12
    for dim_h,dim_k in ((1,1),(2,3),(9,5)):
        h=unit(dim_h);k=unit(dim_k)
        u=[a*v for v in h];v=[b*e for e in k]
        xi=[c*e for e in h];ze=[-d*e for e in k]
        forward=a**(p-2)*dot(u,xi)+b**(p-2)*dot(v,ze)
        reverse=c**(p-2)*dot(xi,u)+d**(p-2)*dot(ze,v)
        assert abs(forward)<3e-12
        assert abs(abs(reverse)-D)<3e-10
        checks+=1

# Non-collinear admissible vectors by explicit orthogonal projection at x.
for p in (1.4,1.9,2.1,3,4,7):
    zmax,D=golden_max(lambda z:defect(p,z),0,8)
    for _ in range(300):
        a=rng.uniform(.05,.995)**(1/p)
        b=(1-a**p)**(1/p)
        u=[a*v for v in unit(3)]
        v=[b*t for t in unit(4)]
        xi=unit(3); ze=unit(4)
        lhs=a**(p-2)*dot(u,xi)+b**(p-2)*dot(v,ze)
        f=[(a**(p-2))*e for e in u]+[(b**(p-2))*e for e in v]
        f2=dot(f,f)
        trial=xi+ze
        yy=[e-lhs*f0/f2 for e,f0 in zip(trial,f)]
        cc=norm(yy[:3]); dd=norm(yy[3:]); r=(cc**p+dd**p)**(1/p)
        yy=[e/r for e in yy]
        fwd=a**(p-2)*dot(u,yy[:3])+b**(p-2)*dot(v,yy[3:])
        c=norm(yy[:3]);d=norm(yy[3:])
        rev=c**(p-2)*dot(yy[:3],u)+d**(p-2)*dot(yy[3:],v)
        assert abs(fwd)<4e-12
        assert abs(rev)<=D+6e-11,(p,rev,D)
        checks+=1

z0=1.1996786402577338339
kappa=z0/math.cosh(z0)
assert abs(z0*math.tanh(z0)-1)<1e-14
for p in (1.9995,1.999,2.0005,2.001):
    zmax,D=golden_max(lambda z:defect(p,z),0,6)
    assert abs(zmax-z0)<0.012
    assert abs(D/abs(p-2)-kappa)<0.002
    checks+=1

print(f'VERIFY_OK checks={checks} hilbert_fibers=1,2,3,4,5,9 sharp_slope={kappa:.17g} phi=hyperbolic')
