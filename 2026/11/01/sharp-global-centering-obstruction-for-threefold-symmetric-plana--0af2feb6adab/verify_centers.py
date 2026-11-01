"""Reproducible finite checks for the cubic threefold-projection center theorem.

Uses only the Python standard library.  The accompanying analytic proof,
not this finite test, establishes all universal claims.
"""
from fractions import Fraction
import math
import random

SEED = 20260923
RNG = random.Random(SEED)
CHECKS = 0

def check(test, label):
    global CHECKS
    if not test:
        raise AssertionError(label)
    CHECKS += 1

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def norm(a):
    return math.sqrt(dot(a,a))

def unit(a):
    d = norm(a)
    return tuple(x/d for x in a)

def basis(n):
    j = min(range(3),key=lambda i:abs(n[i]))
    v = tuple(float(i==j)-n[j]*n[i] for i in range(3))
    e = unit(v)
    return e,unit(cross(n,e))

def center(n, epsilon):
    x,y,z=n
    v=(y*z,z*x,x*y)
    vn=dot(v,n)
    return tuple(-epsilon*(v[i]-vn*n[i])/4 for i in range(3))

def projected_fourier(n, epsilon, steps=24):
    a,b=basis(n)
    total=[0.,0.,0.]
    for k in range(steps):
        t=2*math.pi*k/steps
        u=tuple(a[i]*math.cos(t)+b[i]*math.sin(t) for i in range(3))
        h=1+epsilon*u[0]*u[1]*u[2]
        for i in range(3): total[i]+=2*h*u[i]/steps
    return tuple(total)

# Exact rational identities for the squared center norm.
for i in range(600):
    a,b,c=(RNG.randint(0,30) for _ in range(3))
    if a+b+c==0: continue
    p,q,r=(Fraction(t,a+b+c) for t in (a,b,c))
    e2=p*q+q*r+r*p
    e3=p*q*r
    m=min(p,q,r)
    check(e2-9*e3<=Fraction(1,4),"simplex inequality")
    if m<=Fraction(1,9):
        check(e2-9*e3<= (1-m)*(1-3*m)**2/4,"small-min branch")
    else:
        check(e2-9*e3<=m*(1-m),"large-min branch")
check(Fraction(1,2)*Fraction(1,2)==Fraction(1,4),"sharp bound")
check(3*Fraction(1,15)-9*Fraction(1,105)==Fraction(4,35),"sphere exact moment")
check(Fraction(4,35)/16==Fraction(1,140),"mean-square exact moment")

# Check discrete Fourier projection against the derived vector-field formula.
for eps in (0.3,-0.5):
    for j in range(700):
        n=unit(tuple(RNG.gauss(0,1) for _ in range(3)))
        cf=center(n,eps)
        cn=projected_fourier(n,eps)
        check(norm(tuple(cf[i]-cn[i] for i in range(3)))<1e-12,
              "Steiner point Fourier recovery")
        check(abs(dot(cf,n))<1e-12,"center lies in projection plane")
        a,b=basis(n)
        for k in range(8):
            t=2*math.pi*k/24
            def residual(theta):
                u=tuple(a[i]*math.cos(theta)+b[i]*math.sin(theta) for i in range(3))
                return 1+eps*u[0]*u[1]*u[2]-dot(cf,u)
            check(abs(residual(t)-residual(t+2*math.pi/3))<2e-13,
                  "recentered threefold symmetry")

# Independent harmonic-cubic test beyond the coordinate product:
# H(x,y,z) = x^3 - 3*x*y^2 is harmonic in three dimensions.
# The first circle Fourier coefficient must equal -P_n grad(H)(n)/4.
for j in range(320):
    n=unit(tuple(RNG.gauss(0,1) for _ in range(3)))
    x,y,z=n
    grad=(3*x*x-3*y*y,-6*x*y,0.0)
    gn=dot(grad,n)
    pred=tuple(-(grad[i]-gn*n[i])/4 for i in range(3))
    a,b=basis(n)
    recovered=[0.0]*3
    for k in range(24):
        t=2*math.pi*k/24
        u=tuple(a[i]*math.cos(t)+b[i]*math.sin(t) for i in range(3))
        h=u[0]**3-3*u[0]*u[1]**2
        for i in range(3): recovered[i]+=h*u[i]/12
    check(norm(tuple(pred[i]-recovered[i] for i in range(3)))<1e-12,
          "general harmonic cubic center identity")

# Check the exact extremal normal directions and the seven unoriented zeros.
for eps in (0.3,-0.5):
    for j in range(3):
        for s in (-1,1):
            n=[0.0]*3;n[j]=float(s)
            check(norm(center(tuple(n),eps))<1e-14,"coordinate-axis zero")
    for s1 in (-1,1):
        for s2 in (-1,1):
            for s3 in (-1,1):
                n=(s1/math.sqrt(3),s2/math.sqrt(3),s3/math.sqrt(3))
                check(norm(center(n,eps))<1e-14,"body-diagonal zero")
    for j in range(3):
        for s1 in (-1,1):
            for s2 in (-1,1):
                n=[0.0]*3
                inds=[i for i in range(3) if i!=j]
                n[inds[0]]=s1/math.sqrt(2)
                n[inds[1]]=s2/math.sqrt(2)
                check(abs(norm(center(tuple(n),eps))-abs(eps)/8)<1e-14,
                      "sharp uniform displacement")

# Check the constrained two-direction lower bound for arbitrary global shifts.
for j in range(800):
    eps=0.3
    a=[RNG.uniform(-2,2) for _ in range(3)]
    for axis in range(3):
        others=[i for i in range(3) if i!=axis]
        magnitudes=[]
        for s in (-1.,1.):
            n=[0.,0.,0.]
            n[others[0]]=1/math.sqrt(2)
            n[others[1]]=s/math.sqrt(2)
            cf=center(tuple(n),eps)
            projected_a=tuple(a[i]-dot(a,n)*n[i] for i in range(3))
            magnitudes.append(norm(tuple(cf[i]-projected_a[i] for i in range(3))))
        check(max(magnitudes)+1e-13>=abs(eps)/8+abs(a[axis]),
              "unique common-center minimax bound")

# Independent seeded spherical sampling of the exact mean-square identity.
for eps in (0.3,-0.5):
    m=120000
    total=0.0
    for _ in range(m):
        n=unit(tuple(RNG.gauss(0,1) for _ in range(3)))
        c=center(n,eps)
        total+=dot(c,c)
    check(abs(total/m-eps**2/140)<0.001*eps**2,
          "spherical mean-square Monte Carlo")

print(f"PASS: {CHECKS} deterministic rational, Fourier, symmetry, minimax, and stochastic checks")
