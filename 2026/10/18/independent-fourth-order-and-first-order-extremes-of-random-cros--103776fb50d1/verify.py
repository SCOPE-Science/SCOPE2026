#!/usr/bin/env python3
"""Reproducible supplementary checks for an explicit random-section theorem."""
import math, random, statistics

rng = random.Random(260924131)

def norms(x):
    n=len(x)
    rr=[]
    for i in range(n):
        for j in range(i+1,n):
            a,b=x[i],x[j]
            # Cross an actual signed edge by the central hyperplane.
            # Endpoint oriented with positive dot and the other negative.
            t=b/(a+b)
            v_i=t
            v_j=-(1-t)
            assert abs(a*v_i + b*v_j)<1e-13
            assert abs(abs(v_i)+abs(v_j)-1)<1e-13
            explicit=math.hypot(v_i,v_j)
            formula=math.hypot(a,b)/(a+b)
            assert abs(explicit-formula)<2e-15
            rr.append(explicit)
    return min(rr),2*max(rr)

for n in (2,3,4,8,13):
    for rep in range(200):
        a=[abs(rng.gauss(0,1)) for i in range(n)]
        r,d=norms(a)
        m,M=min(a),max(a)
        z=min(abs(a[i]-a[j])/(a[i]+a[j]) for i in range(n) for j in range(i+1,n))
        assert abs(r-math.sqrt(1+z*z)/math.sqrt(2))<1e-14
        assert abs(d-2*math.hypot(m,M)/(m+M))<1e-14

# Independent rectangle-grid quadrature for coefficient 4 int x f(x)^2 dx = 4/pi.
h=1/10000
j=h*sum((k+0.5)*h*(2/math.pi)*math.exp(-((k+0.5)*h)**2) for k in range(70000))
assert abs(4*j-4/math.pi)<1e-7

# Independent Monte Carlo comparison with two predicted limiting survival tails.
for n,reps in ((60,4000),(250,6000)):
    n2=n*n
    nz=0; nr=0; nd=0
    for rep in range(reps):
        a=sorted(abs(rng.gauss(0,1)) for i in range(n))
        z=min((a[i+1]-a[i])/(a[i+1]+a[i]) for i in range(n-1))
        r=math.sqrt(1+z*z)/math.sqrt(2)
        d=2*math.hypot(a[0],a[-1])/(a[0]+a[-1])
        nz += (n2*z>1.0)
        nr += ((n2*n2)*(r-1/math.sqrt(2))>0.5)
        nd += (n*math.sqrt(math.log(n))*(2-d)>1.0)
    assert abs(nz/reps - math.exp(-2/math.pi))<0.09
    assert abs(nr/reps - math.exp(-(2**(7/4))*math.sqrt(0.5)/math.pi))<0.09
    assert abs(nd/reps - math.exp(-1/math.sqrt(math.pi)))<0.15
print('CROSSPOLYTOPE_JOINT_EXTREMES_FINITE_CHECKS_OK')
