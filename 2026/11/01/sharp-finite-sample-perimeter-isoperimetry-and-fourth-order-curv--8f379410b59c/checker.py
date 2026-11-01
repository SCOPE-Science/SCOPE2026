#!/usr/bin/env python3
"""Standalone finite diagnostics for the random inscribed-polygon area formulas.
Scientific conclusions rely on the separate analytic proof, not these checks.
"""
from fractions import Fraction
import cmath, math, random

PI = math.pi

def beta_polynomial(m,k):
    w=2*PI*k
    ans=0.0
    for j in range((m-3)//2+1):
        ans+=(-1)**j*math.factorial(m-1)/math.factorial(m-2-2*j)/w**(2*j+1)
    return ans

def beta_integral(m,k,N=12000):
    assert N%2==0
    f=lambda t:(m-1)*(1-t)**(m-2)*math.sin(2*PI*k*t)
    acc=f(0)+f(1)
    for j in range(1,N): acc+=(4 if j%2 else 2)*f(j/N)
    return acc/(3*N)

checks=0
for m in range(3,12):
    for k in range(1,9):
        a=beta_polynomial(m,k); b=beta_integral(m,k)
        assert abs(a-b)<2e-10,(m,k,a,b)
        checks+=1
    for k in range(2,13):
        assert 0<beta_polynomial(m,k)<k*beta_polynomial(m,1)
        checks+=1

# An independent exact geometric calculation for the unit square, three samples.
# Probability of a (2+1)-edge occupancy is 9/16, its conditional area is 1/9.
# Probability of three distinct occupied edges is 3/8, conditional area is 1/4.
assert Fraction(9,16)*Fraction(1,9)+Fraction(3,8)*Fraction(1,4)==Fraction(5,32)
checks+=1

# Exact integration of the boundary Fourier coefficients of the square.
# This test compares an infinite-series formula (truncated with a rapidly
# decaying tail) to the independent rational side-occupancy computation.
verts=[0j,1+0j,1+1j,1j,0j]
omega=PI/2

def c_square(n):
    x=0j
    for j in range(4):
        tangent=verts[j+1]-verts[j]
        x+=tangent*(cmath.exp(-1j*n*omega*j)-cmath.exp(-1j*n*omega*(j+1)))
    return x/((1j*n*omega)**2*4)

modes=range(1,1201)
area=PI*sum(k*(abs(c_square(k))**2-abs(c_square(-k))**2) for k in modes)
E3=1.5*sum((abs(c_square(k))**2-abs(c_square(-k))**2)*beta_polynomial(3,k) for k in modes)
E4=2*sum((abs(c_square(k))**2-abs(c_square(-k))**2)*beta_polynomial(4,k) for k in modes)
assert abs(area-1)<5e-10,area
assert abs(E3-5/32)<2e-10,E3
assert abs(E4-5/16)<4e-10,E4
checks+=3

# Independent seeded Monte Carlo checks for unit-circle expectations.
rng=random.Random(271828)
for m in (3,4,5,7):
    expected=(m/2)*beta_polynomial(m,1)
    sample=[]
    for rep in range(15000):
        angles=sorted(rng.random()*2*PI for _ in range(m))
        points=[complex(math.cos(t),math.sin(t)) for t in angles]
        ar=.5*sum((points[j].conjugate()*points[(j+1)%m]).imag for j in range(m))
        sample.append(ar)
    mean=sum(sample)/len(sample)
    assert abs(mean-expected)<0.025,(m,mean,expected)
    checks+=1

# First curvature-dependent coefficient in the high-sample asymptotics;
# for a unit circle, curvature-cube integral is 2*pi and L=2*pi.
L=2*PI
for m in (50,80,120):
    exact=PI-(m/2)*beta_integral(m,1,18000)
    approx=PI*L**2/((m+1)*(m+2)) - L**4*PI/((m+1)*(m+2)*(m+3)*(m+4))
    assert abs(exact-approx)<0.00001/(m/50)**5,(m,exact,approx)
    checks+=1

# Gauss--Bonnet and Jensen for a noncircular ellipse.
a,b=2.0,1.0
N=16384
speed=lambda t:math.hypot(a*math.sin(t),b*math.cos(t))
kappa=lambda t:a*b/speed(t)**3
Lellipse=sum(speed(2*PI*i/N) for i in range(N))*2*PI/N
curv_mass=sum(kappa(2*PI*i/N)*speed(2*PI*i/N) for i in range(N))*2*PI/N
curv_cube=sum(kappa(2*PI*i/N)**3*speed(2*PI*i/N) for i in range(N))*2*PI/N
assert abs(curv_mass-2*PI)<1e-10
assert curv_cube>8*PI**3/Lellipse**2
checks+=2
print('PASS',checks,'independent finite diagnostics')
print('square exact E3=5/32, E4=5/16; spectral:',E3,E4)
print('ellipse length=',Lellipse,'curvature cube=',curv_cube)
