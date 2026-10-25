"""Reproducible diagnostics for the shared-direction widths of rotated cubes."""
import itertools
import math
import numpy as np
from scipy.special import gammaln, ndtri
from scipy.stats import qmc


def sylvester(d):
    assert d >= 2 and (d & (d - 1)) == 0
    h = np.array([[1.0]])
    while len(h) < d:
        h = np.block([[h, h], [h, -h]])
    return h / math.sqrt(d)


def phi_s(s):
    s = np.clip(s, 0.0, 1.0)
    return np.sqrt(1.0-s) + np.sqrt(s)*np.arcsin(np.sqrt(s))


def mu(d):
    return d * math.exp(gammaln(d/2)-gammaln((d+1)/2)) / math.sqrt(math.pi)


def covariance_exact(r):
    d = len(r)
    return 2*np.sum(phi_s(r*r))/(d*math.pi)-mu(d)**2


def lower_bound(d):
    return 2*d*phi_s(1/d)/math.pi - mu(d)**2


def frame_defect(r):
    d = len(r)
    return np.sum((r*r-1/d)**2)


def mc_covariance(r, log2_samples=17):
    d=len(r)
    sampler=qmc.Sobol(d=d, scramble=True, seed=902711+d)
    x=ndtri(sampler.random_base2(log2_samples))
    x/=np.linalg.norm(x,axis=1)[:,None]
    a=np.abs(x).sum(axis=1)
    b=np.abs(x@r).sum(axis=1)
    m=mu(d)
    return float(np.mean((a-m)*(b-m)))


for d in (2,4,8,16):
    h=sylvester(d)
    assert np.allclose(h.T@h, np.eye(d), atol=1e-14)
    assert np.allclose(h*h,np.full((d,d),1/d))
    c=covariance_exact(h)
    assert abs(c-lower_bound(d))<5e-12
    assert c<0
    print('HADAMARD_SHARP_NEGATIVE_COVARIANCE_OK',d,round(c,12))

for d in (2,3,4,8):
    r=sylvester(d) if d!=3 else np.eye(3)-np.ones((3,3))*2/3
    c=covariance_exact(r)
    observed=mc_covariance(r,17 if d!=8 else 18)
    tolerance=0.0016
    assert abs(c-observed)<tolerance,(d,c,observed)
    print('INDEPENDENT_QUASIMONTE_CARLO_MIXED_MOMENT_OK',d,round(c,9),round(observed,9))

rng=np.random.default_rng(41857)
for d in (2,3,4,5,6,8):
    for i in range(140):
        a=rng.normal(size=(d,d))
        r,_=np.linalg.qr(a)
        gap=covariance_exact(r)-lower_bound(d)
        b=frame_defect(r)/(12*math.pi*d)
        assert gap + 3e-12 >= b,(d,i,gap,b)
    print('GLOBAL_STRONG_CONVEXITY_DEFECT_DIAGNOSTIC_OK',d)

for d in (2,3,4):
    r=sylvester(d) if d!=3 else np.eye(3)-2*np.ones((3,3))/3
    corners=np.array(list(itertools.product([-0.5,0.5],repeat=d)),float)
    for k in range(120):
        u=rng.normal(size=d); u/=np.linalg.norm(u)
        direct=(corners@u).max()-(corners@u).min()
        direct_rot=(corners@(r.T@u)).max()-(corners@(r.T@u)).min()
        assert abs(direct-np.abs(u).sum())<2e-14
        assert abs(direct_rot-np.abs(u@r).sum())<2e-14
    print('INDEPENDENT_CUBE_VERTEX_SUPPORT_WIDTH_IDENTITY_OK',d)

r3=np.eye(3)-np.ones((3,3))*2/3
assert -0.010<covariance_exact(r3)<-0.008
assert covariance_exact(np.eye(3))>0
print('THREE_DIMENSIONAL_OBLIQUE_ANTICORRELATION_WITNESS_OK')

import mpmath as mp
mp.mp.dps=65
for d in (128,256,512,1024,4096):
    D=mp.mpf(d)
    g=mp.sqrt(1-1/D)+mp.asin(1/mp.sqrt(D))/mp.sqrt(D)
    u=D*mp.gamma(D/2)/(mp.sqrt(mp.pi)*mp.gamma((D+1)/2))
    c=2*D*g/mp.pi-u*u
    assert abs(D*c+1/(6*mp.pi))<mp.mpf(0.3)/D
print('ASYMPTOTIC_NEGATIVE_COVARIANCE_COEFFICIENT_OK')
print('ALL_ROTATED_HYPERCUBE_WIDTH_COVARIANCE_CHECKS_OK')
