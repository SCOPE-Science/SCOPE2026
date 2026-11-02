"""Numerical consistency checks for the intrinsic radial law of a unit tetrahedron.

Run: python verify.py (requires numpy and scipy). Numerical tests are not
substitutes for the analytic proof in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad

h=math.sqrt(3)/2
R=2/math.sqrt(3)

def cdf(r):
    if r<=0: return 0.
    if r<=1: return math.pi*r*r/(2*math.sqrt(3))
    if r<R:
        return math.sqrt(3)*(r*r*(math.pi/6-math.acos(1/r))+math.sqrt(r*r-1))
    return 1.

def moment(k):
    return 2*math.sqrt(3)/(k+2)*quad(lambda t: math.cos(t)**(-k-2),0,math.pi/6,epsabs=2e-13)[0]

assert abs(cdf(1)-math.pi/(2*math.sqrt(3)))<1e-14
assert abs(cdf(R)-1)<1e-14
assert abs(moment(0)-1)<1e-13
assert abs(moment(2)-5/9)<1e-13
expected_mean=math.sqrt(3)/3*(2/3+math.log(3)/2)
assert abs(moment(1)-expected_mean)<1e-13

# Uniform triangular coordinates from two independent pseudo-random inputs.
# Each physical tetrahedral face has equal area.
rng=np.random.default_rng(2342809)
n=125000
B=np.array((0.,0.)); C=np.array((1.,0.)); D=np.array((.5,h))
A=np.array((0.,h)); L=np.array((-.5,0.)); Rbase=np.array((.5,0.))
images=np.array(((.5,-h),(1.5,h),(-.5,h)))
vals=[]
for face in range(4):
    u=rng.random(n); v=rng.random(n); s=np.sqrt(u)
    if face<3:
        # Equilateral triangles incident to source A, identical distances in
        # face coordinates; their physical position differs only by rotations.
        p=(1-s)[:,None]*A+s[:,None]*(1-v)[:,None]*L+s[:,None]*v[:,None]*Rbase
        dist=np.linalg.norm(p-A,axis=1)
    else:
        p=(1-s)[:,None]*B+s[:,None]*(1-v)[:,None]*C+s[:,None]*v[:,None]*D
        dist=np.sqrt(((p[:,None,:]-images[None,:,:])**2).sum(axis=2)).min(axis=1)
    vals.append(dist)
rs=np.concatenate(vals)
thresholds=[0.15,0.45,0.7,h,0.92,1.,1.02,1.06,1.10,1.13,1.15,R]
errors=[abs(np.mean(rs<=t)-cdf(t)) for t in thresholds]
print('cdf_max_error',max(errors))
print('mean_estimate',rs.mean(),'formula',expected_mean)
print('second_moment_estimate',np.mean(rs**2),'formula',5/9)
assert max(errors)<0.004
assert abs(rs.mean()-expected_mean)<0.004
assert abs(np.mean(rs**2)-5/9)<0.004

# Endpoint expansions checked with high precision to avoid catastrophic
# cancellation near the squared-root critical radius.
import mpmath as mp
mp.mp.dps=70
s3=mp.sqrt(3); rm=mp.mpf(2)/s3

def Fmp(r):
    if r<=1: return mp.pi*r*r/(2*s3)
    if r>=rm: return mp.mpf(1)
    return s3*(r*r*(mp.pi/6-mp.acos(1/r))+mp.sqrt(r*r-1))
for eps in ('1e-7','1e-9','1e-11'):
    eps=mp.mpf(eps)
    cusp=(Fmp(1+eps)-mp.pi*(1+eps)**2/(2*s3))/eps**mp.mpf('1.5')
    end=(1-Fmp(rm-eps))/eps**2
    assert abs(cusp+4*mp.sqrt(6)/3)<mp.mpf('0.02')
    assert abs(end-3)<mp.mpf('0.02')
print('critical_coefficient',mp.nstr(-4*mp.sqrt(6)/3,18))
print('endpoint_coefficient',3)
print('all_checks_passed')
