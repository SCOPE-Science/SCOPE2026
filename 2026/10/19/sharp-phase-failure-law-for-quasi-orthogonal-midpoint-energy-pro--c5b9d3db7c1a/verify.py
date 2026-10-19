"""Reproduce identities and numerical checks for the quadratic-invariant
projection solvability theorem. Requires Python >=3.9; standard library only.
Every numeric test is supplementary to the displayed analytic proof.
"""
from fractions import Fraction
import math
import random

CHECKS = 0

def check(condition, reason):
    global CHECKS
    assert condition, reason
    CHECKS += 1

def close(a, b, tol=1.e-10):
    check(abs(a-b) <= tol*max(1.,abs(a),abs(b)), f"{a!r} != {b!r}")

def energy(q, k):
    return q[0]**2 + k*k*q[1]**2

def midpoint(q, k, h):
    a = 1. - (k*h)**2/2.
    return (a*q[0]+h*k*k*q[1], -h*q[0]+a*q[1])

def min_line_energy(y, k):
    a=y[0]**2
    b=(k*y[1])**2
    r=k*k
    return a+b-(a+r*b)**2/(a+r*r*b)

def g(r, u):
    return (r-1.)**2*u*(1-u)/(1+(r*r-1.)*u)

def d(k,h):
    return 1+(k*h)**4/4

def hc(k):
    return 2/math.sqrt(k*(k*k-1))

def failure_probability(k,h):
    r=k*k
    D=d(k,h)
    H=D*(r-1.)**2
    crit=(r+1.)**2
    if H <= crit*(1+4.e-15):  # suppress roundoff at the exact contact point
        return 0.
    discr=(H-(r+1.)**2)*(H-(r-1.)**2)
    root=math.sqrt(discr)
    lo=(H-r*r+1.-root)/(2*H)
    hi=(H-r*r+1.+root)/(2*H)
    return (2/math.pi)*(math.asin(math.sqrt(hi))-math.asin(math.sqrt(lo)))

# An exact counterexample independent of floating arithmetic.
r=Fraction(4)
h=Fraction(2)
q=(Fraction(1),Fraction(1,2))
alpha=1-r*h*h/2
y=(alpha*q[0]+h*r*q[1],-h*q[0]+alpha*q[1])
check(y==(Fraction(-3),Fraction(-11,2)), 'midpoint output')
A=y[0]**2; B=r*y[1]**2
E_min=A*B*(r-1)**2/(A+r*r*B)
check(E_min==Fraction(9801,1945), 'exact minimum')
check(E_min>energy(q,Fraction(2)), 'empty projection line')

# Matrix mapping, its weighted energy gain, completion of squares,
# phase dependence and equality of the universal extremizer.
rng=random.Random(240918328)
for _ in range(1600):
    k=1.03+9*rng.random()
    h=0.01+10*rng.random()
    theta=2*math.pi*rng.random()
    q=(math.cos(theta),math.sin(theta)/k)
    y=midpoint(q,k,h)
    D=d(k,h)
    close(energy(y,k),D*energy(q,k),2e-11)
    s=k*k*y[1]**2/energy(y,k)
    close(min_line_energy(y,k),energy(y,k)*g(k*k,s),3e-10)
    # Independently minimize the quadratic line using exact coefficients.
    a=y[0]**2; b=(k*y[1])**2; r=k*k
    lam=-(a+r*b)/(a+r*r*b)
    close((1+lam)**2*a+(1+r*lam)**2*b,min_line_energy(y,k),3e-10)
    close(g(r,1/(r+1)),((r-1)/(r+1))**2,1e-11)

# Sharp worst-phase witness constructed by inverting the midpoint matrix.
for k in (1.1,1.4,2.,3.,7.):
    r=k*k
    h=hc(k)
    for mult in (.5,.9,1.,1.00001,1.2,2.0,8.0):
        hh=h*mult
        D=d(k,hh)
        alpha=1-r*hh*hh/2
        yy1=math.sqrt(D*r/(r+1))
        yy2=math.sqrt(D/(r+1))/k
        qq=((alpha*yy1-hh*r*yy2)/D,(hh*yy1+alpha*yy2)/D)
        close(energy(qq,k),1.,1e-11)
        y=midpoint(qq,k,hh)
        close(y[0],yy1,2e-11)
        close(y[1],yy2,2e-11)
        minimum=min_line_energy(y,k)
        target=energy(qq,k)
        if mult<1:
            check(minimum<target, 'below threshold')
        if mult>1:
            check(minimum>target, 'above threshold')
        if mult==1:
            close(minimum,target,1e-10)

# Failure-phase probability by independent midpoint counting on the energy ellipse.
for k,h_factor in ((1.2,1.2),(2.,1.02),(2.,1.4),(3.,2.),(5.,1.5)):
    h=hc(k)*h_factor
    n=300000
    count=0
    for j in range(n):
        th=2*math.pi*(j+.5)/n
        q=(math.cos(th),math.sin(th)/k)
        y=midpoint(q,k,h)
        if min_line_energy(y,k)>energy(q,k):
            count+=1
    close(count/n,failure_probability(k,h),2.e-5)

# Critical square-root onset and high-step successful-phase tail.
for k in (1.3,2.,4.):
    r=k*k
    Dcrit=((r+1)/(r-1))**2
    crit_const=2*(r-1)/(math.pi*(r+1))
    for eps in (1e-4,1e-5,1e-6):
        h=hc(k)*(1+eps)
        p=failure_probability(k,h)
        approx=crit_const*math.sqrt(d(k,h)-Dcrit)
        check(abs(p/approx-1)<.015, 'critical square-root law')
    asympt=4*(r+1)/(math.pi*r*(r-1))
    for h in (30.,100.):
        success=1-failure_probability(k,h)
        check(abs(success*h*h/asympt-1)<.035, 'large-step phase law')

print(f'PASS: {CHECKS} exact/numerical assertions')
print('Exact witness: kappa=2, h=2, start=(1,1/2), prediction=(-3,-11/2), minimum=9801/1945>2')
print(f'Uniform threshold for kappa=2: h={hc(2):.15f}')
for mult in (0.9,1.0,1.1,1.5,2.,5.):
    hh=hc(2)*mult
    print(f'  h/h_crit={mult:.1f}, failed initial-phase fraction={failure_probability(2,hh):.12f}')
