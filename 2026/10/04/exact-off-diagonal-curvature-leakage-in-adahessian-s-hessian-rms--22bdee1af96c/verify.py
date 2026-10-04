import itertools
import math
import random
import numpy as np

def all_rademacher(n):
    for bits in itertools.product((-1.0,1.0), repeat=n):
        yield np.array(bits)

def exact_single_probe_moments(H):
    vals=[]
    for z in all_rademacher(H.shape[0]):
        vals.append(z*(H@z))
    vals=np.asarray(vals)
    return vals.mean(axis=0),(vals*vals).mean(axis=0)

rng=np.random.default_rng(1234)

# Exhaustive exact one-probe identity.
for n in (2,3,4):
    for _ in range(10):
        A=rng.normal(size=(n,n))
        H=(A+A.T)/2.0
        mean,second=exact_single_probe_moments(H)
        assert np.max(np.abs(mean-np.diag(H))) < 2e-13
        assert np.max(np.abs(second-np.sum(H*H,axis=1))) < 2e-12

# Exact m-probe second moment by direct enumeration on a 2x2 matrix.
H=np.array([[2.0,-0.7],[-0.7,1.3]])
single=[]
for z in all_rademacher(2):
    single.append(z*(H@z))
single=np.asarray(single)
for m in (1,2,3):
    accum=[]
    for inds in itertools.product(range(len(single)), repeat=m):
        d=np.mean(single[list(inds)],axis=0)
        accum.append(d*d)
    exact=np.mean(np.asarray(accum),axis=0)
    target=np.diag(H)**2 + (np.sum(H*H,axis=1)-np.diag(H)**2)/m
    assert np.max(np.abs(exact-target)) < 3e-13

# Bias-corrected RMS-square expectation is independent of beta2.
H=np.array([[1.7,0.9,-0.4],[0.9,2.1,0.3],[-0.4,0.3,1.2]])
target=np.sum(H*H,axis=1)
for beta2 in (0.1,0.5,0.9,0.99):
    for t in (1,2,5,20):
        weights=np.array([(1-beta2)*beta2**(t-s)/(1-beta2**t) for s in range(1,t+1)])
        assert abs(weights.sum()-1.0) < 2e-14
        expected=weights.sum()*target
        assert np.max(np.abs(expected-target)) < 2e-13

# Monte Carlo replay of the RMS square for a fixed Hessian.
H=np.array([[2.0,1.1],[1.1,4.0]])
target=np.sum(H*H,axis=1)
beta2=0.8
t=8
N=120000
sum_state=np.zeros(2)
for rep in range(N):
    acc=np.zeros(2)
    for s in range(1,t+1):
        z=rng.choice((-1.0,1.0),size=2)
        d=z*(H@z)
        acc=beta2*acc+(1-beta2)*d*d
    corrected=acc/(1-beta2**t)
    sum_state+=corrected
emp=sum_state/N
assert np.max(np.abs(emp-target)) < 0.02

# Sharp two-dimensional condition-number factor.
for kappa in (1.0,2.0,5.0,10.0,100.0):
    closed=(kappa+1.0)/(2.0*math.sqrt(kappa))
    best=0.0
    for theta in np.linspace(0.0,math.pi/2.0,100001):
        c,s=math.cos(theta),math.sin(theta)
        Q=np.array([[c,-s],[s,c]])
        A=Q@np.diag([1.0,kappa])@Q.T
        ratio=np.linalg.norm(A[0,:])/A[0,0]
        best=max(best,ratio)
    assert abs(best-closed) < 3e-8

# Attaining orientation and m-probe closed form.
for kappa in (1.2,3.0,10.0,50.0):
    p=kappa/(kappa+1.0)
    mean=p+(1-p)*kappa
    second=p+(1-p)*kappa*kappa
    ratio2=second/(mean*mean)
    assert abs(ratio2-(kappa+1.0)**2/(4.0*kappa)) < 2e-14
    for m in (1,2,5,100):
        multi=math.sqrt(1.0+(ratio2-1.0)/m)
        formula=math.sqrt(1.0+(kappa-1.0)**2/(4.0*kappa*m))
        assert abs(multi-formula) < 2e-14

print("verification passed")
