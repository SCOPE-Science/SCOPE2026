#!/usr/bin/env python3
"""Reproducibility checks for Euclidean chord moments of ring torus surfaces.

Requires only the Python 3 standard library. The written proof establishes the
infinite assertions; these independent quadratures and rational checks expose
normalization or polynomial transcription mistakes, not a substitute for proof.
"""
from fractions import Fraction as F
from math import cos, sin, pi, isclose


def add(a,b):
    return [F((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)) for i in range(max(len(a),len(b)))]

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out

def scale(a,q):return [q*v for v in a]
def deriv(a):return [i*a[i] for i in range(1,len(a))]

# Exact polynomial identities after clearing positive denominators.
N4=[F(12),F(52),F(39)]
N6=[F(40),F(312),F(516),F(187)]
one_two=[F(1),F(2)]
assert add(mul(deriv(N4),one_two),scale(N4,-4))==[F(4),F(-26),F(0)]
NT=add(N6,scale(mul(N4,one_two),-12))
assert NT==[F(-104),F(-600),F(-1200),F(-749)]
assert add(mul(deriv(NT),one_two),scale(NT,-6))==[F(24),F(0),F(153),F(0)]

def k4(x):return (12+52*x+39*x*x)/(8*(1+2*x)**2)
def k6(x):return (40+312*x+516*x*x+187*x**3)/(16*(1+2*x)**3)
def contrast(x):return k6(x)-6*k4(x)
def moment2(R,r):return 2*(R*R+2*r*r)
def moment4(R,r):return (12*R**4+52*R*R*r*r+39*r**4)/2
def moment6(R,r):return (40*R**6+312*R**4*r*r+516*R*R*r**4+187*r**6)/2

assert k4(F(2,13))==F(26,17)
assert k4(F(1))==F(103,72)
assert k4(F(4,9))==F(3,2)
assert contrast(F(0))==F(-13,2)
assert contrast(F(1))==F(-2653,432)
assert F(59,432)==F(3)*(51*F(1)**2+8)/(16*(1+2*F(1))**4)

# Exact two-moment camouflage with different squared aspect ratios.
x=F(1,16)
y=(4-9*x)/(52*x+9)
assert y==F(55,196) and x!=y
assert k4(x)==k4(y)==F(3943,2592)
assert k6(x)!=k6(y)
R1_sq,r1_sq=F(8,9),F(1,18)
R2_sq,r2_sq=F(98,153),F(55,306)
assert r1_sq/R1_sq==x and r2_sq/R2_sq==y
assert 2*(R1_sq+2*r1_sq)==2*(R2_sq+2*r2_sq)==2
assert (12*R1_sq**2+52*R1_sq*r1_sq+39*r1_sq**2)/2==(12*R2_sq**2+52*R2_sq*r2_sq+39*r2_sq**2)/2

# Independent pairwise-angle quadrature. The angular-difference average
# is evaluated directly: E_phi[D^2]=A, E_phi[D^4]=A^2+B^2/2,
# E_phi[D^6]=A^3+3AB^2/2.  The theta/eta quadrature is a full
# trigonometric integration rather than a repeat of the tensor calculation.
def angular_quadrature(R,r,N=64):
    theta=[2*pi*i/N for i in range(N)]
    xy=[R+r*cos(v) for v in theta]
    zz=[r*sin(v) for v in theta]
    w=[v/R for v in xy]
    out=[0.,0.,0.]
    for i in range(N):
        for j in range(N):
            A=xy[i]*xy[i]+xy[j]*xy[j]+(zz[i]-zz[j])**2
            B=2*xy[i]*xy[j]
            wt=w[i]*w[j]/(N*N)
            out[0]+=wt*A
            out[1]+=wt*(A*A+B*B/2)
            out[2]+=wt*(A**3+1.5*A*B*B)
    return out

count=0
for R,r in [(3.,1.),(1.,.2),(2.,1.8),(1.,.99),(1.,.001),
            (5.,.5),(.8,.7),(7.,6.9),(4.,3.),(3.5,1.25)]:
    direct=angular_quadrature(R,r)
    formula=(moment2(R,r),moment4(R,r),moment6(R,r))
    for obs,ex in zip(direct,formula):
        assert isclose(obs,ex,rel_tol=2e-11,abs_tol=2e-11),(R,r,obs,ex)
        count+=1

# Rational parameter checks for the exact ambiguity involution, whenever
# the partner remains positive; these are diagnostic, not the general proof.
for i in range(1,177):
    x=F(i,400)
    y=(4-9*x)/(52*x+9)
    if y>0:
        assert k4(x)==k4(y)
        count+=1

# A global inverse inequality for the squared aspect ratio.
xs=[F(i,100) for i in range(1,100)]
for i in range(len(xs)-1):
    a,b=xs[i],xs[i+1]
    assert b-a <= F(432,59)*(contrast(b)-contrast(a))
    count+=1

print('VERIFY_OK independent_angle_moments=30 rational_and_inverse_checks='+str(count-30))
