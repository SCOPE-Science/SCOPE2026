"""Exact reproducibility checks for a planar residual-sketch projection theorem.

Requires Python 3.9+ standard library only. Finite checks support, but do not
replace, the general algebra and angular integral given in the proof.
"""
from fractions import Fraction as Q
from math import sqrt, atan, pi

checks = 0

def eq(actual, expected):
    global checks
    assert actual == expected, (actual, expected)
    checks += 1

def actual_ratio_squared(a, b, t, sign1=1, sign2=1):
    # x=(1,t), A=diag(sign1*a,sign2*b), B=I, sketch s=x.
    x = (Q(1), t)
    d = a*a*x[0]*x[0] + b*b*x[1]*x[1]
    lam = (x[0]*x[0] + x[1]*x[1])/d
    v = (x[0] * (1-lam*a*a), x[1] * (1-lam*b*b))
    rnorm = x[0]*x[0]+x[1]*x[1]
    return (v[0]*v[0]+v[1]*v[1])/rnorm

# Equivalent algebraic formula for the squared amplification.
for a in (Q(1), Q(2), Q(3), Q(7), Q(11)):
    for b in (Q(1), Q(2), Q(5)):
        for numerator in range(-9,10):
            t=Q(numerator,7)
            predicted=(a*a-b*b)**2*t*t / (a*a+b*b*t*t)**2
            for s1 in (-1,1):
                for s2 in (-1,1):
                    eq(actual_ratio_squared(a,b,t,s1,s2),predicted)

# The two exact threshold inequalities are equivalent to factor signs.
for a in range(1,19):
    for b in range(1,13):
        lo,hi=Q(min(a,b)),Q(max(a,b))
        kap=hi/lo
        worst=(kap-1/kap)/2
        mean=(kap-1)**2/(2*kap)
        eq((worst<=1), (kap*kap-2*kap-1<=0))
        eq((mean<=1), (kap*kap-4*kap+1<=0))

# Exact 2-step finite termination on a non-eigenvector (also for indefinite A).
# Second sketch is the first residual, perpendicular to the first sketch.
for a in range(1,10):
    for b in range(1,8):
        if a==b:
            continue
        for tnum in (-4,-3,-2,-1,1,2,3,4):
            t=Q(tnum,7)
            s0=(Q(1),t)
            for sign1,sign2 in ((1,1),(1,-1),(-1,1),(-1,-1)):
                aa=Q(a*sign1);bb=Q(b*sign2)
                d=aa*aa + bb*bb*t*t
                lam=(1+t*t)/d
                r1=(1-lam*aa*aa,t*(1-lam*bb*bb))
                eq(s0[0]*r1[0]+s0[1]*r1[1], Q(0))
                eq(r1[0]*r1[0]+r1[1]*r1[1] > 0, True)
                # Second sketch constraints impose s0 dot r2=r1 dot r2=0,
                # since the sketch spans R2; algebraically it has rank 2.
                eq(s0[0]*r1[1]-s0[1]*r1[0] !=0,True)

# Independent numerical quadrature, not an infinite mathematical certificate.
# Midpoint rule avoids the angular singular coordinate chart.
from math import cos,sin
for aa,bb in ((2,1),(3,1),(4,1),(7,5),(1,1)):
    n=40000
    accum=0.0
    for j in range(n):
        theta=2*pi*(j+0.5)/n
        c=cos(theta);s=sin(theta)
        d=aa*aa*c*c+bb*bb*s*s
        accum+=((aa*aa-bb*bb)*s*c/d)**2/n
    expected=(aa-bb)**2/(2*aa*bb)
    assert abs(accum-expected)<1e-9,(accum,expected)
    checks+=1

# Direct angular-frequency numerical check at kappa=3 and kappa=4.
for k in (3,4,6):
    n=40000
    count=0
    for j in range(n):
        theta=2*pi*(j+0.5)/n
        c=cos(theta);s=sin(theta)
        d=k*k*c*c+s*s
        if (k*k-1)*abs(c*s)>d:
            count+=1
    disc=k**4-6*k*k+1
    expected=2/pi*atan(sqrt(disc)/(k*k+1))
    assert abs(count/n-expected)<4.1/n,(k,count/n,expected)
    checks+=1

print('VERIFY_OK',checks)
