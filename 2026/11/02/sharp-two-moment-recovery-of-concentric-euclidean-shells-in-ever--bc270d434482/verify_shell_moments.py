"""Reproducible diagnostics for uniform-shell interpoint moments (standard library only)."""
from fractions import Fraction as F
import math, random

def radial(d,q,k):
    return F(d,d+2*k)*(1-q**(d+2*k))/(1-q**d)
def Q(d,q):
    mu2=radial(d,q,1); mu4=radial(d,q,2)
    return mu4/(2*mu2*mu2)+F(d+2,2*d)
def formula(d,q):
    return F((d+2)**2,2*d*(d+4))*(1-q**(d+4))*(1-q**d)/(1-q**(d+2))**2+F(d+2,2*d)

for d in range(2,13):
    for z in [F(0),F(1,10),F(1,3),F(1,2),F(3,4),F(9,10),F(99,100)]:
        assert Q(d,z)==formula(d,z)
    vals=[Q(d,F(j,200)) for j in range(200)]
    assert all(vals[j]>vals[j+1] for j in range(199)),d
    assert vals[0]==F((d+2)*(d+3),d*(d+4))
    assert vals[-1]>F(d+1,d)
print('EXACT_ALL_DIMENSION_MOMENT_IDENTITIES_AND_GRID_MONOTONICITY_PASSED')

# Independent pair sampling. Samples one radius with its correct conditional radial CDF,
# and two independent Gaussian-normalized directions.
def samplepoint(d,q,rng):
    rad=(q**d+(1-q**d)*rng.random())**(1/d)
    g=[rng.gauss(0,1) for _ in range(d)];norm=math.sqrt(sum(t*t for t in g))
    return [rad*t/norm for t in g]
for d,q in [(2,0.0),(2,0.45),(3,0.0),(3,0.6),(5,0.3),(8,0.8)]:
    rng=random.Random(12345+d+int(q*100))
    cnt=65000
    ss=ss2=0.0
    for _ in range(cnt):
        a=samplepoint(d,q,rng);b=samplepoint(d,q,rng)
        v=sum((x-y)**2 for x,y in zip(a,b));ss+=v;ss2+=v*v
    mu2=d/(d+2)*(1-q**(d+2))/(1-q**d)
    mu4=d/(d+4)*(1-q**(d+4))/(1-q**d)
    expected1=2*mu2;expected2=2*mu4+(2+4/d)*mu2**2
    assert abs(ss/cnt-expected1)<0.032,(d,q,ss/cnt,expected1)
    assert abs(ss2/cnt-expected2)<0.125,(d,q,ss2/cnt,expected2)
print('INDEPENDENT_UNIFORM_VOLUME_PAIR_SAMPLING_PASSED')

# Sharp endpoint coefficients, expressed in scaled dimensionless Q.
for d in [2,3,4,5,7,10]:
    ball=(d+2)*(d+3)/(d*(d+4));lower=1+1/d
    cb=(d+2)**2/(2*d*(d+4))
    for q in [0.01,0.015,0.02]:
        ratio=float(F((d+2)*(d+3),d*(d+4))-Q(d,F(str(q))))/(q**d)
        assert abs(ratio/cb-1)<0.012,(d,q,ratio,cb)
    for epsilon in [0.001,0.002]:
        q=1-epsilon
        ratio=float(Q(d,F(str(q)))-F(d+1,d))/(epsilon**2)
        assert abs(ratio-1/6)<0.004,(d,q,ratio)
print('SHARP_BALL_AND_THIN_SHELL_ENDPOINT_LAWS_PASSED')
print('ALL_CHECKS_PASSED')
