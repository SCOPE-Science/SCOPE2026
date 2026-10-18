"""Reproduce diagnostic geometry and moment checks for ellipsoidal section profiles.

Python 3.10+; standard library only. The universal theorem is proved analytically.
"""
import math
from fractions import Fraction as F


def close(actual, target, tolerance=2e-8):
    assert math.isfinite(actual), (actual, target)
    assert abs(actual-target) <= tolerance*max(1.0, abs(target)), (actual, target)


def simpson(fn, a=0., b=1., n=40000):
    assert n % 2 == 0
    h=(b-a)/n
    acc=fn(a)+fn(b)
    for k in range(1,n):
        acc+=(4 if k % 2 else 2)*fn(a+h*k)
    return acc*h/3


def moments(L, kind):
    if L==1:
        return (1., 1., 1.)
    if kind=='prolate':
        p=math.sqrt(L*L-1)
        a1=math.atan(p)/p
        a2=(a1+1/(L*L))/2
        a3=(3*a2+1/(L**4))/4
    else:
        a1=math.acosh(L)/(L*math.sqrt(L*L-1))
        a2=(a1+1)/(2*L*L)
        a3=(3*a2+1)/(4*L*L)
    return a1,a2,a3


def defect(m):
    a,b,c=m
    s=a-F(2,3)*b+F(1,5)*c
    d=max(0.,a*c-b*b)
    # stable form for small D, avoiding loss in 1-sqrt(1-x)
    v=float(F(16,45))*d/s**2
    assert 0<=v<=1+1e-12, (m,v)
    return 0.5*v/(1+math.sqrt(max(0,1-v)))


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def norm(a):
    return math.sqrt(dot(a,a))


def actual_section_area(diagonal_Q, normal, offset):
    u=tuple(t/norm(normal) for t in normal)
    p=(1.,0.,0.) if abs(u[0])<.8 else (0.,1.,0.)
    v=cross(u,p); v=tuple(t/norm(v) for t in v)
    w=cross(u,v)
    inv=tuple(1/t for t in diagonal_Q)
    def quadratic(x,y):
        return sum(s*xk*yk for s,xk,yk in zip(inv,x,y))
    a=quadratic(v,v); b=quadratic(v,w); c=quadratic(w,w)
    det=a*c-b*b
    d=offset*quadratic(u,v); e=offset*quadratic(u,w)
    residual=1-offset**2*quadratic(u,u)+(c*d*d-2*b*d*e+a*e*e)/det
    return math.pi*residual/math.sqrt(det)


def theory_section_area(diagonal_Q, normal, offset):
    u=tuple(t/norm(normal) for t in normal)
    s=sum(v*t*t for v,t in zip(diagonal_Q,u))
    return math.pi*math.sqrt(math.prod(diagonal_Q))/math.sqrt(s)*(1-offset**2/s)


def check():
    h_det=F(1,5)-F(1,9)
    assert h_det==F(4,45)
    assert F(1)-F(2,3)+F(1,5)==F(8,15)
    close(defect((1,1,1)),0)
    # Two equivalent traces for the nonzero singular-value Gram matrix.
    for kind in ('prolate','oblate'):
        for L in (1.02,1.1,1.4,2.,3.,6.):
            m=moments(L,kind)
            for j in (1,2,3):
                v=simpson(lambda z: (1+(L*L-1)*(z*z if kind=='prolate' else 1-z*z))**(-j))
                close(m[j-1],v,2e-8)
            aa,bb,cc=m
            tr=aa-F(2,3)*bb+F(1,5)*cc
            det=float(h_det)*(aa*cc-bb*bb)
            lamlo=(tr-math.sqrt(max(0.,tr*tr-4*det)))/2
            close(defect(m),lamlo/tr,2e-9)
            assert 0<=defect(m)<.5
    for diag in [(4.,1.,1.),(4.,4.,1.),(3.,2.,1.),(8.,3.,1.)]:
        for k in range(1,70):
            u=(math.sin(1.17*k),math.cos(.37*k),math.sin(.43*k)+.2)
            t=.8*math.sin(1.77*k)
            area=actual_section_area(diag,u,t)
            geometric=theory_section_area(diag,u,t)
            close(area,geometric,3e-12)
    # Q=I+eps*diag(1,0,0) or I+eps*diag(1,1,0):
    # traceless Frobenius norm squared =2/3, predicted coefficient=1/36.
    for kind in ('prolate','oblate'):
        for eps in (.04,.02,.01,.004):
            e=defect(moments(math.sqrt(1+eps),kind))
            ratio=e/(eps*eps)
            assert abs(ratio-F(1,36))<.0035, (kind,eps,ratio)
    target=.5*(1-math.sqrt(7281)/89)
    for L in (20.,100.,1000.):
        err=defect(moments(L,'prolate'))
        assert err>0 and abs(err-target)<.004
    for L in (100.,1000.,100000.):
        err=defect(moments(L,'oblate'))
        assert err>0
        assert abs(45*math.log(L)*err-1)<.3, (L,err,45*math.log(L)*err)
    print('VERIFY_OK')

if __name__=='__main__':
    check()
