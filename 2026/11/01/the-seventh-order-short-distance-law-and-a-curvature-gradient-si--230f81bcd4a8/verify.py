"""Numerical and exact checks for the isotropic short-distance curvature law.
Uses the Python standard library only. Finite checks do not prove the theorem.
"""
from fractions import Fraction
from math import pi, sin, cos, sqrt, acos, isclose

checks = 0

def close(a, b, tol=2e-9):
    global checks
    assert abs(a-b) <= tol*max(1.0,abs(a),abs(b)), (a,b)
    checks += 1

def simpson(f, n=16384):
    assert n % 2 == 0
    h=2*pi/n
    acc=f(0.0)+f(2*pi)
    for j in range(1,n):
        acc+=(4 if j%2 else 2)*f(j*h)
    return acc*h/3

# Unit disk: exact covariogram Taylor coefficients.
def disk_cov(t):
    return 2*acos(t/2)-0.5*t*sqrt(4-t*t)

for t in (0.2,0.1,0.05):
    polynomial=pi-2*t+t**3/12+t**5/320
    assert abs(disk_cov(t)-polynomial)< t**7
    checks += 1

# Elliptic domains: independent affine transform of circle covariogram.
# Therefore the angular average of its fifth-order directional coefficient
# must agree with the differential-geometric boundary integral.
for a,b in ((1.,1.),(2.,1.),(3.,2.),(4.,1.5)):
    def I_integrand(th):
        ss=a*a*sin(th)**2+b*b*cos(th)**2
        speed=sqrt(ss)
        kappa=a*b/ss**1.5
        derivative= -3*a*b*(a*a-b*b)*sin(th)*cos(th)/ss**3
        return (9*kappa**4-8*derivative**2)*speed
    I=simpson(I_integrand)
    def independent(th):
        q=sqrt(cos(th)**2/a**2+sin(th)**2/b**2)
        return 9*a*b*q**5
    J=simpson(independent)
    close(I,J,2e-10)
    if a==b==1.: close(I,18*pi)

# Explicit support family with curvature radius 1+a*cos(k theta).
# One calculation is through curvature and its arc-length derivative,
# the other through the rational closed formula.
for k in (2,3,4,7):
    for amp in (0.,0.2,0.5,0.8):
        def integrand(th):
            radius=1+amp*cos(k*th)
            dr=-k*amp*sin(k*th)
            return 9/radius**3-8*dr*dr/radius**5
        I=simpson(integrand)
        J=pi*(18-(9+8*k*k)*amp**2-(9+2*k*k)*amp**4)/(1-amp**2)**3.5
        close(I,J,5e-10)

# Rational checks of the k=3, a=1/2 exact polynomial and area.
k=3
amp=Fraction(1,2)
poly=18-(9+8*k*k)*amp**2-(9+2*k*k)*amp**4
assert poly==Fraction(-63,16)
checks+=1
area_over_pi=1-amp**2/Fraction(2*(k*k-1))
assert area_over_pi==Fraction(63,64)
checks+=1
close(float(poly)*pi/(1-float(amp)**2)**3.5,-56*pi/(3*sqrt(3)))
for k in (2,3,5,10):
    poly0=18
    poly1=18-(9+8*k*k)-(9+2*k*k)
    assert poly0>0 and poly1<0
    checks+=1

# Recompute normalized disk coefficient from radial covariogram:
# D(rho)=rho^2-4/(3pi)rho^3+rho^5/(30pi)+rho^7/(1120pi).
I_2=2*pi
I_4=18*pi
c5=sqrt(pi)/(60*pi**2.5)*I_2
c7=pi**1.5/(20160*pi**3.5)*I_4
close(c5,1/(30*pi))
close(c7,1/(1120*pi))
print('FINITE_GEOMETRIC_CHECKS_OK',checks)
