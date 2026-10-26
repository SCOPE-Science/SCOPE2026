"""Reproducibility checks for sharp endpoint affine projection on concentric shells.
All data and calculations concern a self-contained mathematical assertion.
"""
from math import acos, sqrt, pi, gamma, isclose, cos, sin
from scipy.integrate import quad
from scipy.optimize import brentq


def ball_volume(d):
    return pi**(d/2)/gamma(d/2+1)

def q(d,r):
    return (1-r**(d+2))/((d+2)*(1-r**d)) if r!=1 else 1/d

def F(d,R,z):
    if R<=z: return 0.
    cd=ball_volume(d-1)
    a=(d-1)/2
    return cd*quad(lambda t: (t/z-1)*(R*R-t*t)**a,z,R,epsabs=1.e-12,epsrel=2.e-12)[0]

def F2(R,z):
    if R<=z: return 0.
    h=sqrt(R*R-z*z)
    return -R*R*acos(z/R)+z*h+2*h**3/(3*z)

def norm(d,r):
    z=q(d,r)
    return 1+2*(F(d,1,z)-F(d,r,z))/(ball_volume(d)*(1-r**d))

def norm2(r):
    z=q(2,r)
    return 1+2*(F2(1,z)-F2(r,z))/(pi*(1-r*r))

def direct2(r):
    z=q(2,r)
    # independent angular integration of unmodified kernel, then radial integration
    def ang(rad):
        s=rad/z
        return quad(lambda t: abs(1+s*cos(t)),0,2*pi,
                    epsabs=1e-11,limit=250)[0]/(2*pi)
    return quad(lambda rad: 2*rad*ang(rad)/(1-r*r),r,1,
                epsabs=5e-8,limit=250)[0]

number=0
for d in range(2,10):
    threshold=brentq(lambda r: r-q(d,r),0.000001,.999999,xtol=1e-14)
    assert 1/(d+2)<threshold<1/d
    number+=1
    for r in (0,.03,.19,.31,.5,.72,.93):
        z=q(d,r)
        val=norm(d,r)
        assert val>1 and val<d+1
        assert isclose(q(d,0),1/(d+2),rel_tol=1.e-12)
        assert isclose(F(d,r,z),0,abs_tol=1.e-14) if r<=z else F(d,r,z)>0
        number+=3
for R in (.32,.51,1):
    for z in (.17,.22,.3,.49,.64):
        if z>=R: continue
        assert abs(F(2,R,z)-F2(R,z))<2e-12
        number+=1
for r in (0,.05,.2,2-sqrt(3),.3,.5,.85):
    assert abs(norm(2,r)-norm2(r))<1e-10
    assert abs(norm2(r)-direct2(r))<7e-8
    number+=2
rc=2-sqrt(3)
assert abs(rc-q(2,rc))<1e-14
circle=1/3+2*sqrt(3)/pi
assert abs(norm2(1-1.e-5)-circle)<2e-5
assert abs(norm2(0)-(1-2/pi*acos(.25)+11*sqrt(15)/(8*pi)))<2e-12
number+=3
print('PASS',number,'independent quadrature and formula assertions')
print('threshold 2D',rc,'disk norm',norm2(0),'circle norm',circle)
for d in (2,3,4,5,8):
 rc=brentq(lambda r: r-q(d,r),1e-8,.9)
 # approximate derivative
 qprime=(q(d,rc+1e-5)-q(d,rc-1e-5))/(2e-5)
 exponent=(d+3)/2
 Cd=(8*ball_volume(d-1)*2**((d-1)/2)*rc**((d-3)/2)/
     (ball_volume(d)*(1-rc**d)*(d+1)*(d+3)))*(1-qprime)**exponent
 print('d=',d,'r*=',rc,'exponent=',exponent,'C=',Cd)

# High-precision independent cap integrations verify the contact exponent and coefficient.
import mpmath as mp
mp.mp.dps=65
cusp_checks=0
for d in (2,3,4,5):
    vd=lambda j: mp.pi**(mp.mpf(j)/2)/mp.gamma(mp.mpf(j)/2+1)
    qq=lambda rad:(1-rad**(d+2))/((d+2)*(1-rad**d))
    root=mp.findroot(lambda rad:rad-qq(rad),1/mp.mpf(d+2))
    qp=mp.diff(qq,root)
    exponent=mp.mpf(d+3)/2
    const=8*vd(d-1)*2**(mp.mpf(d-1)/2)*root**(mp.mpf(d-3)/2)/\
          (vd(d)*(1-root**d)*(d+1)*(d+3))*(1-qp)**exponent
    for eps in (mp.mpf('0.003'),mp.mpf('0.0007')):
        rad=root+eps
        zz=qq(rad)
        missing=vd(d-1)*mp.quad(lambda x:(x/zz-1)*(rad*rad-x*x)**(mp.mpf(d-1)/2),[zz,rad])
        normalized=2*missing/(vd(d)*(1-rad**d)*eps**exponent)
        assert abs(normalized/const-1)<mp.mpf('.06')
        cusp_checks+=1
print('CUSP PASS',cusp_checks,'high-precision scaling assertions')
