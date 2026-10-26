#!/usr/bin/env python3
"""Standalone arithmetic and quadrature checks for the stated polar scaling law."""
from fractions import Fraction as F
from math import pi, sqrt, cos, cosh, sinh, exp, gamma

checks=0
def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def beta_moment(p,c):
    return gamma(p+1)*gamma(c+1)/gamma(p+c+1)

def q(theta,h,d):
    a=sqrt(h/d)
    return a*cosh(a*(pi-abs(theta)))/(2*sinh(a*pi))

def simpson(f,a,b,n=4096):
    assert n%2==0
    dt=(b-a)/n
    z=f(a)+f(b)
    for j in range(1,n):
        z+=(4 if j%2 else 2)*f(a+dt*j)
    return z*dt/3

for h,d in [(1.,1.),(2.,3.),(.3,1.2),(4.,1.)]:
    kappa=sqrt(h/d)
    check(abs(simpson(lambda z:q(z,h,d),-pi,pi)-1)<3e-7, 'orientation normalization')
    check(abs((q(1.e-8,h,d)-q(0,h,d))/1.e-8 - (-kappa*kappa/2))<2e-6,'right cusp')
    for m in range(1,8):
        approx=simpson(lambda z:q(z,h,d)*cos(m*z),-pi,pi)
        exact=h/(h+d*m*m)
        check(abs(approx-exact)<1e-6,'orientation Fourier coefficient '+str(m))
for c in [0.4,1.,1.7,3.,6.]:
    for p in range(1,7):
        # R=1-U^(1/c), U uniform: nonsingular quadrature for moments
        approx=simpson(lambda t:(1-t**(12/c))**p*12*t**11,0,1,8192)
        exact=beta_moment(p,c)
        check(abs(approx-exact)<2e-5, 'radial beta moment')
    for rr in [0.01,0.2,0.7,0.97]:
        cdf=1-(1-rr)**c
        check(0<cdf<1, 'radial CDF')
        den=c*(1-rr)**(c-1)
        d_cdf=(1-(1-(rr+1e-6))**c-(1-(1-(rr-1e-6))**c))/(2e-6)
        check(abs(d_cdf-den)<max(1e-7,den*5e-6), 'radial density')

for k in [F(1),F(7),F(23),F(101)]:
    for c in [F(1,3),F(1),F(2),F(4)]:
        for h,d in [(F(1),F(2)),(F(3),F(1)),(F(1,2),F(4))]:
            r=c*k
            m1=h/(h+d); m2=h/(h+4*d)
            ey=m1/(1+c)
            # Exact stationary mean after independent position resets:
            ez=ey/k  # active speed v=1
            check((k+r)*ez==m1, 'stationary mean generator')
            # Position-orientation mixed observables from stationary generator:
            zu_bar=(1+h*ez)/(k+r+d+h)
            zu=(m2+h*ez)/(k+r+d+h)
            ezzbar=2*zu_bar/(2*k+r)
            ezz=2*zu/(2*k+r)
            check((k+r+d+h)*zu_bar==1+h*ez,'mixed z-ubar generator')
            check((k+r+d+h)*zu==m2+h*ez,'mixed z-u generator')
            check((2*k+r)*ezzbar==2*zu_bar,'squared modulus generator')
            check((2*k+r)*ezz==2*zu,'squared complex generator')
            # Nonasymptotic position second moments and limiting Beta moments:
            ynorm2=k*k*ezzbar
            ynormsq=k*k*ezz
            limitr2=F(2,1)/((c+1)*(c+2))
            check(ynorm2<=1 and ynorm2>=0,'finite-k support bound')
            # Quantitative coupling forces second moment convergence at O(k^-1/2):
            error=sqrt(float((2*d+4*h)/k))
            check(abs(float(ynorm2-limitr2))<=2*error+1e-12,'moment W2 bound')
            check(abs(float(ynormsq-m2*limitr2))<=2*error+1e-12,'complex moment W2 bound')
            # Recover c from the radial second moment and h/d from mean:
            calc_c=(-3+sqrt(1+8/float(limitr2)))/2
            check(abs(calc_c-float(c))<1e-12,'c recovery')
            omega=float(ey)*(1+float(c))
            check(abs(omega/(1-omega)-float(h/d))<1e-12,'angular rate recovery')

for c in [0.2,1.0,2.5]:
    check(beta_moment(0,c)==1,'probability normalization')
    for p in range(1,9):
        check(abs(beta_moment(p,c)-beta_moment(p-1,c)*p/(p+c))<2e-12,'beta recurrence')
print('PASS', checks, 'deterministic checks')

def covariance_k(k,c,h,d,lag):
    """Exact complex stationary two-time covariance of Y=kX/v for v=1."""
    r=c*k; alpha=k+r; beta=d+h
    m1=h/beta
    Ez=m1/alpha
    Ezu=(1+h*Ez)/(alpha+beta)
    Ez2=2*Ezu/(2*k+r)
    if abs(alpha-beta)<1e-12:
        kernel=lag*exp(-alpha*lag)
    else:
        kernel=(exp(-beta*lag)-exp(-alpha*lag))/(alpha-beta)
    C=(exp(-alpha*lag)*Ez2
       +m1*(1-exp(-alpha*lag))*Ez/alpha
       +(Ezu-m1*Ez)*kernel)
    return k*k*C

for c,h,d in [(0.3,1.2,0.7),(1.,3.,2.),(4.,1.,4.)]:
    mu=1/(1+c); va=c/((1+c)**2*(2+c)); m=h/(h+d)
    for s in [0.,0.4,1.5,7.]:
        target=mu**2+va*exp(-(1+c)*s)
        check(abs(covariance_k(300000,c,h,d,s/300000)-target)<1e-4,'fast time covariance')
    for lag in [0.2,1.,5.]:
        target=mu*mu*(m*m+(1-m*m)*exp(-(h+d)*lag))
        check(abs(covariance_k(300000,c,h,d,lag)-target)<1e-4,'positive physical lag covariance')
    check(abs(covariance_k(10000,c,h,d,0)-2/((1+c)*(2+c)))<1e-3,'zero-lag variance')
    check(va>0,'positive fast-layer covariance jump')

print('PASS', checks, 'total deterministic checks including time-covariance limits')
