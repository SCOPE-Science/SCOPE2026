"""Auxiliary numerical and exact checks for weighted metric-cactus distance laws."""
from fractions import Fraction as F
import math
import numpy as np
from scipy.integrate import quad

def overlap(d,a,b):
    return max(0.0, min(a,d)-max(0.0,d-b))

def barbell_density(d):
    # Two cycles (lengths 2 and 3) connected by a length-1 bridge.
    # Probabilistic arclength density is 1/10 on first cycle, 1/5 on
    # second cycle, and 1/5 on bridge.
    if d < 0: return 0.0
    a,b,e=0.1,0.2,0.2
    q1,q2,l=1.0,1.5,1.0
    return (2*2*a*a*(d<q1) + 2*3*b*b*(d<q2)
            +2*e*e*max(l-d,0) +4*a*e*overlap(d,q1,l)
            +4*b*e*overlap(d,q2,l)+8*a*b*overlap(d-l,q1,q2))

assert 2*F(1,10)+3*F(1,5)+F(1,5)==1
expected_origin = 2*(2*F(1,100)+3*F(1,25)+F(1,25))
assert expected_origin==F(9,25)
assert abs(barbell_density(1e-9)-float(expected_origin))<1e-8
assert abs(barbell_density(1-1e-8)-barbell_density(1+1e-8)-float(F(1,25)))<1e-7
assert abs(barbell_density(1.5-1e-8)-barbell_density(1.5+1e-8)-float(F(6,25)))<1e-7
assert abs(sum(quad(barbell_density,lo,hi,epsabs=1e-11)[0] for lo,hi in [(0,1),(1,1.5),(1.5,2),(2,2.5),(2.5,3.5)])-1)<1e-10
print('EXACT_WEIGHTED_BARBELL_NORMALIZATION_AND_JUMPS_PASSED')

# Independent weighted-circle autocorrelation, calculated without using
# the circle-distance derivative formula's integrand simplification.
c,eps=2.0,0.5
w=lambda u: (1+eps*math.cos(math.pi*u))/c
for r in (0.07,0.2,0.55,0.82,0.999):
    numerical=2*quad(lambda s:w(s)*w((s+r)%c),0,c,epsabs=1e-12,limit=100)[0]
    closed=1+eps**2/2*math.cos(math.pi*r)
    assert abs(numerical-closed)<2e-10,(r,numerical,closed)
assert abs((1-eps**2/2)-F(7,8))<1e-15
assert abs((1+eps**2/2)-F(9,8))<1e-15
print('INDEPENDENT_NONUNIFORM_CIRCLE_AUTOCORRELATION_PASSED')

# Direct independent random-pair metric simulation of the barbell.
rng=np.random.default_rng(1782018)
n=500000
which=rng.choice(3,size=(2,n),p=[0.2,0.6,0.2])
pos=rng.random((2,n))*np.array([2.,3.,1.])[which]
D=np.zeros(n)
for i in range(3):
 for j in range(i,3):
    m=(which[0]==i)&(which[1]==j)
    if i==j:
        v=np.abs(pos[0,m]-pos[1,m]);D[m]=np.minimum(v,[2.,3.,1.][i]-v) if i<2 else v
    else:
        if i==0 and j==1: D[m]=np.minimum(pos[0,m],2-pos[0,m])+1+np.minimum(pos[1,m],3-pos[1,m])
        elif i==0 and j==2: D[m]=np.minimum(pos[0,m],2-pos[0,m])+pos[1,m]
        elif i==1 and j==2: D[m]=np.minimum(pos[0,m],3-pos[0,m])+(1-pos[1,m])
    if i!=j:
      m=(which[0]==j)&(which[1]==i)
      if i==0 and j==1: D[m]=np.minimum(pos[1,m],2-pos[1,m])+1+np.minimum(pos[0,m],3-pos[0,m])
      elif i==0 and j==2: D[m]=np.minimum(pos[1,m],2-pos[1,m])+pos[0,m]
      elif i==1 and j==2: D[m]=np.minimum(pos[1,m],3-pos[1,m])+(1-pos[0,m])

breaks=[0,1,1.5,2,2.5,3.5]
def cdf(x):
    return sum(quad(barbell_density,a,min(b,x),epsabs=1e-9)[0] for a,b in zip(breaks[:-1],breaks[1:]) if a<x)
for t in (0.15,0.45,0.9,1.1,1.4,1.7,2.15,2.75,3.2):
    empirical=np.mean(D<=t); theoretical=cdf(t)
    assert abs(empirical-theoretical)<0.004, (t,empirical,theoretical)
print('INDEPENDENT_RANDOM_METRIC_DISTANCE_CDF_PASSED')
print('ALL_CHECKS_PASSED')
