"""Reproducibility checks for the three-line Gaussian interference spectrum.

Uses only Python's standard library except an optional mpmath quadrature test.
Finite numerical checks do not replace the proofs in RESULT.md.
"""
from math import cos, sin, pi, sqrt, floor, isclose
import cmath

def eig_formula(t,rho):
    s=1+cmath.exp(2j*pi*t)+cmath.exp(2j*pi*rho*t)
    return (3-abs(s))/2,(3+abs(s))/2

def eig_direct(t,rho):
    theta=[0,pi*t,pi*rho*t]
    row=[(cos(x),-sin(x)) for x in theta]
    a=sum(x*x for x,y in row)
    b=sum(x*y for x,y in row)
    c=sum(y*y for x,y in row)
    d=sqrt((a-c)**2+4*b*b)
    return (a+c-d)/2,(a+c+d)/2

def torus_distance(x):
    return abs(x-round(x))

def assert_close(x,y,tol=1e-10):
    assert abs(x-y)<=tol*max(1,abs(x),abs(y)),(x,y)

def gauss_stft(a,b,nu,x,w):
    return 2**(-0.5)*cmath.exp(-1j*pi*x*w-0.5*pi*(x*x+w*w+nu*nu))* (a*cmath.exp(pi*nu*w+1j*pi*nu*x)+b*cmath.exp(-pi*nu*w-1j*pi*nu*x))

def gauss_intensity(a,b,nu,x,w):
    C=a*b.conjugate()
    return 0.5 * __import__('math').exp(-pi*(x*x+w*w+nu*nu))*(abs(a)**2*__import__('math').exp(2*pi*nu*w)+abs(b)**2*__import__('math').exp(-2*pi*nu*w)+2*(C*cmath.exp(2j*pi*nu*x)).real)

checks=0
for rho in (sqrt(2), (1+sqrt(5))/2, 1.5,2.,pi):
 for k in range(1,181):
    t=k/17
    a=eig_formula(t,rho); b=eig_direct(t,rho)
    assert_close(a[0],b[0]); assert_close(a[1],b[1]); checks+=2
    dist2=torus_distance(t)**2+torus_distance(rho*t)**2
    assert a[0]+1e-11>=4*dist2/3
    assert a[0]<=2*pi*pi*dist2+1e-11
    checks+=2
for a,b,nu,x,w in ((1+.5j,.3-1j,.7,0.4,.2), (.8+.3j,2-1j,0.25,1.1,-1.2), (1+2j,-2+.4j,1.5,-.25,.1)):
    assert_close(abs(gauss_stft(a,b,nu,x,w))**2,gauss_intensity(a,b,nu,x,w)); checks+=1
# Exact resonance for rational rho and t integer multiple of denominator.
assert eig_formula(2,1.5)[0]<1e-13; checks+=1
# Exact normal-form phase extraction: 3 real measurements recover two coordinates.
rho=sqrt(2); t=3.17; C=.4-.7j
rows=[(cos(pi*v),-sin(pi*v)) for v in [0,t,rho*t]]
y=[u*C.real+v*C.imag for u,v in rows]
a=sum(u*u for u,v in rows); b=sum(u*v for u,v in rows); c=sum(v*v for u,v in rows)
rhs1=sum(u*z for (u,v),z in zip(rows,y)); rhs2=sum(v*z for (u,v),z in zip(rows,y))
det=a*c-b*b
Crec=complex((c*rhs1-b*rhs2)/det,(a*rhs2-b*rhs1)/det)
assert_close(Crec.real,C.real);assert_close(Crec.imag,C.imag); checks+=2
# Golden-ratio convergents: worst-case q^-2 degeneration at infinitely many q.
f0,f1=1,1
for k in range(2,25):
    f0,f1=f1,f0+f1
    q=f1
    val=eig_formula(q,(1+sqrt(5))/2)[0]
    if k>=8:
        assert q*q*val<50
        checks+=1
# Optional direct integral, independent of closed expression.
try:
 import mpmath as mp
 mp.mp.dps=38
 z=mp.mpc(.45,-.7); v=mp.mpc(.3,.2); nu=mp.mpf('.4'); x=mp.mpf('.25'); w=mp.mpf('-.45')
 direct=mp.quad(lambda s:(z*mp.exp(2j*mp.pi*nu*s)+v*mp.exp(-2j*mp.pi*nu*s))*mp.exp(-mp.pi*s*s-mp.pi*(s-x)**2-2j*mp.pi*w*s),[-mp.inf,mp.inf])
 closed=gauss_stft(complex(z),complex(v),float(nu),float(x),float(w))
 assert abs(complex(direct)-closed)<1e-12
 checks+=1
except ImportError:
 print('Optional mpmath integral unavailable; algebraic checks still completed.')
print('PASS: %d independent finite comparison/inequality assertions.'%checks)
