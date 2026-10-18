"""Independent numerical tests for co-observation law of coaxial spheroids.
Only uses elementary quadrature and independent random-normal sampling.
"""
import math
import numpy as np
from scipy.integrate import quad

def analytical(a,b,d):
    assert a>0 and b>0 and d>2*a
    if abs(a-b)<1.e-12*a:
        J=a
        I=2*a*a/d
    elif a>b:
        c=math.sqrt(a*a-b*b)
        J=a/2+b*b/(2*c)*math.asinh(c/b)
        I=b*b/c*math.atanh(2*c/d)
    else:
        c=math.sqrt(b*b-a*a)
        J=a/2+b*b/(2*c)*math.asin(c/b)
        I=b*b/c*math.atan(2*c/d)
    return I,J,I/(4*J-I)

def quadrature(a,b,d):
    h=lambda x: math.sqrt(b*b+(a*a-b*b)*x*x)
    x0=2*b/math.sqrt(d*d-4*(a*a-b*b))
    I=quad(lambda x:2*h(x)-d*x,0,x0,epsabs=1e-12)[0]
    J=quad(h,0,1,epsabs=1e-12)[0]
    return I,J,I/(4*J-I)

cases=[(1.,.13,2.1),(1.,.25,2.4),(1.,.6,2.4),(1.,.999,2.4),(1.,1.,2.4),(1.,1.01,2.4),(1.,1.6,2.4),(1.,5,2.4),(1.,30,2.4),(2.,.8,5.),(2.,3.5,4.001)]
for case in cases:
    v=analytical(*case);w=quadrature(*case)
    assert max(abs(x-y)/(1+abs(y)) for x,y in zip(v,w))<2e-11,(case,v,w)
for a,d in [(1,2.2),(1,3.7),(3,10)]:
    vals=[analytical(a,b,d)[2] for b in np.geomspace(.01*a,100*a,151)]
    assert all(q>p for p,q in zip(vals,vals[1:])),(a,d)
# Inverse calibration by bracketed bisection on the proved monotone profile.
for a,d,actual_b in [(1.,2.4,.28),(1.,2.4,1.),(1.,2.4,2.7),(2.,5.,.4)]:
    p=analytical(a,actual_b,d)[2]
    lo,hi=1e-6*a,1000*a
    for _ in range(90):
        mid=(lo+hi)/2
        if analytical(a,mid,d)[2]<p:lo=mid
        else:hi=mid
    assert abs((lo+hi)/2-actual_b)<1e-9*a,(a,d,actual_b,lo,hi)
for b in [.02,.04,.08]:
    p=analytical(1,b,2.4)[2]
    approx=.5*b*b*math.atanh(2/2.4)
    assert abs(p/approx-1)<.15
for b in [100,200,400]:
    p=analytical(1,b,2.4)[2]
    approx=2*2.4/(math.pi*b)
    assert abs((1-p)/approx-1)<.03

# sample unoriented random planes with correct hitting-region bias via uniform U and union-width weights
rng=np.random.default_rng(9832)
n=500000
u=rng.uniform(0,1,n)
for a,b,d in [(1,.45,2.4),(1,1.,2.4),(1,2.2,2.4)]:
    h=np.sqrt(b*b+(a*a-b*b)*u*u)
    over=np.maximum(0,2*h-d*u)
    # independent Monte Carlo ratio of integrated offset measures
    sampled=over.mean()/(4*h-over).mean()
    theory=analytical(a,b,d)[2]
    assert abs(sampled-theory)<.0015,(a,b,d,sampled,theory)
# Independent plane sampling: draw unit normals and offsets in a fixed outer slab,
# reject planes not meeting either solid, and directly count two profile disks.
ns=600000
for a,b,d in [(1,.45,2.4),(1,1.,2.4),(1,2.2,2.4)]:
    normals=rng.normal(size=(ns,3))
    normals/=np.linalg.norm(normals,axis=1)[:,None]
    uz=normals[:,2]
    t=rng.uniform(-(d/2+max(a,b)),d/2+max(a,b),ns)
    h=np.sqrt(a*a*uz*uz+b*b*(1-uz*uz))
    A=np.abs(t+d*uz/2)<h
    B=np.abs(t-d*uz/2)<h
    conditioned=A|B
    observed=np.count_nonzero(A&B)/np.count_nonzero(conditioned)
    theory=analytical(a,b,d)[2]
    assert abs(observed-theory)<.008,(a,b,d,observed,theory)
print('SPHEROID_PAIR_CROFTON_OK', 'quadrature_cases',len(cases),'monotonic_cases',3,'inversions',4,'simulation_trials',n*3+ns*3)
for b in [.2, .8,1.,2.,10.]:
    print('b',b,'P',round(analytical(1,b,2.4)[2],10))
