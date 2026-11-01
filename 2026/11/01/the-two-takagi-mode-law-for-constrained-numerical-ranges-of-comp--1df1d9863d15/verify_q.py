"""Supplementary finite tests of the affine q-radius law for symmetric antilinear maps.
Uses only the Python standard library; not a substitute for the proof.
"""
import cmath
import math
import random

rng = random.Random(91730419)
checks = 0

def inner(x, y):
    return sum(a*b.conjugate() for a,b in zip(x,y))

def norm(x):
    return math.sqrt(inner(x,x).real)

def unit(n):
    v=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(n)]
    z=norm(v)
    return [a/z for a in v]

def apply(sigma,x):
    return [d*z.conjugate() for d,z in zip(sigma,x)]

def radial(sigma,rho):
    return (1+rho)*sigma[0]/2+(1-rho)*sigma[1]/2

# All hypotheses and extremes are tested in several ranks and dimensions.
for n in (2,3,5,9):
    for case in range(16):
        sigmas=sorted([rng.uniform(0,4) for _ in range(n)],reverse=True)
        if case % 4 == 0: sigmas[1]=0;sigmas[2:]=[0]*(n-2)
        if case % 4 == 1: sigmas[1]=sigmas[0]
        for rho in (0.0,0.08,0.3,0.5,0.8,0.999,1.0):
            theta=rng.uniform(-math.pi, math.pi)
            q=rho*cmath.exp(1j*theta)
            R=radial(sigmas,rho)
            b_plus=(1+rho)/2;b_minus=(1-rho)/2
            x=[complex(0) for _ in range(n)]
            y=[complex(0) for _ in range(n)]
            x[0]=math.sqrt(b_plus);x[1]=1j*math.sqrt(b_minus)
            y[0]=math.sqrt(b_plus)*cmath.exp(-1j*theta)
            y[1]=-1j*math.sqrt(b_minus)*cmath.exp(-1j*theta)
            assert abs(norm(x)-1)<2e-12
            assert abs(norm(y)-1)<2e-12
            assert abs(inner(x,y)-q)<2e-12
            assert abs(abs(inner(apply(sigmas,x),y))-R)<2e-12
            checks+=4
            for _ in range(60):
                a=unit(n)
                z=unit(n)
                coeff=inner(z,a)
                z=[zj-coeff*aj for zj,aj in zip(z,a)]
                z=[zj/norm(z) for zj in z]
                eta=math.sqrt(max(0,1-rho*rho))
                b=[q.conjugate()*aj+eta*zj for aj,zj in zip(a,z)]
                assert abs(inner(a,b)-q)<2e-12
                assert abs(norm(b)-1)<2e-12
                assert abs(inner(apply(sigmas,a),b))<=R+2e-12
                checks+=3
            # Zero-radius witnesses for the disk centered at the origin.
            if sigmas[0]==0 or sigmas[1]==0:
                zx=[0j]*n;zx[1]=1
                zb=[0j]*n;zb[1]=q.conjugate();zb[0]=math.sqrt(1-rho*rho)
                assert abs(inner(zx,zb)-q)<2e-12
                assert abs(inner(apply(sigmas,zx),zb))<2e-12
                checks+=2
            elif rho==0:
                zx=[0j]*n;zx[0]=1
                zb=[0j]*n;zb[1]=1
                assert abs(inner(zx,zb)-q)<2e-12
                assert abs(inner(apply(sigmas,zx),zb))<2e-12
                checks+=2
            elif rho==1:
                a,b=sigmas[:2]
                zx=[0j]*n;zx[0]=math.sqrt(b/(a+b));zx[1]=1j*math.sqrt(a/(a+b))
                zb=[z*cmath.exp(-1j*theta) for z in zx]
                assert abs(inner(zx,zb)-q)<2e-12
                assert abs(inner(apply(sigmas,zx),zb))<2e-12
                checks+=2
            else:
                a,b=sigmas[:2]; eta=math.sqrt(1-rho*rho)
                hi=math.atan(math.sqrt(a/b));lo=0.0
                def vals(z):
                    c=math.cos(z);t=math.sin(z)
                    u=a*c*c-b*t*t
                    d=-1j*(a+b)*c*t
                    return u,d
                for _ in range(70):
                    m=(lo+hi)/2
                    u,d=vals(m)
                    if rho*abs(u)>eta*abs(d): lo=m
                    else: hi=m
                z=(lo+hi)/2;u,d=vals(z)
                zx=[0j]*n;zx[0]=math.cos(z);zx[1]=1j*math.sin(z)
                v=[0j]*n;v[0]=-zx[1].conjugate();v[1]=zx[0].conjugate()
                # Need y = bar(q) x + eta*t*v, with conj(t) chosen to cancel.
                rhs=-(q*u)/(eta*d)
                t=rhs.conjugate()/abs(rhs)
                zb=[q.conjugate()*xx+eta*t*vv for xx,vv in zip(zx,v)]
                assert abs(inner(zx,zb)-q)<2e-12
                assert abs(norm(zb)-1)<2e-12
                assert abs(inner(apply(sigmas,zx),zb))<2e-11
                checks+=3
print('PASS',checks,'finite assertions across dimensions, q values, sharp frames and zero witnesses')
