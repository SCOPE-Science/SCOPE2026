import math
import numpy as np

def orthogonal(rng,n):
    Q,_=np.linalg.qr(rng.normal(size=(n,n)))
    return Q

def build_C(sigmas,seed):
    rng=np.random.default_rng(seed)
    n=len(sigmas)
    U=orthogonal(rng,n)
    V=orthogonal(rng,n)
    return U@np.diag(sigmas)@V.T

def game_J(C):
    n=C.shape[0]
    Z=np.zeros_like(C)
    return np.block([[Z,C],[-C.T,Z]])

def iteration(C,eta,tau):
    J=game_J(C)
    I=np.eye(J.shape[0])
    # source field: (I-tau*J)Jz because J^T=-J
    return I-eta*((I-tau*J)@J)

def modal_factor(sigma,eta,tau):
    return math.sqrt((1-eta*tau*sigma*sigma)**2+(eta*sigma)**2)

# Full-matrix singular values agree with the modal formula for arbitrary singular-vector bases.
for sigmas,seed in [
    ([0.4,1.0,2.7],350088),
    ([1.0,1.3,4.2,7.0],350089),
    ([0.15,0.7,0.9,3.0,5.5],350090),
]:
    C=build_C(sigmas,seed)
    for tau in (0.03,0.2,0.7,2.0):
        for eta in (0.005,0.03,0.1):
            M=iteration(C,eta,tau)
            op=np.linalg.svd(M,compute_uv=False)[0]
            closed=max(modal_factor(s,eta,tau) for s in sigmas)
            assert abs(op-closed)<2e-12

# Sharp threshold: below contracts, equality has norm one, above expands.
for L in (0.7,2.0,8.0):
    for tau in (0.05,0.4,1.0,3.0):
        sigmas=[0.25*L,0.6*L,L]
        C=build_C(sigmas,350091)
        crit=2*tau/(1+(tau*L)**2)
        below=np.linalg.svd(iteration(C,0.999*crit,tau),compute_uv=False)[0]
        edge=np.linalg.svd(iteration(C,crit,tau),compute_uv=False)[0]
        above=np.linalg.svd(iteration(C,1.001*crit,tau),compute_uv=False)[0]
        assert below<1
        assert abs(edge-1)<3e-12
        assert above>1

# Dimensionless stability lens and reciprocal roots.
for s in (0.05,0.2,0.5,0.9,0.999):
    lo=(1-math.sqrt(1-s*s))/s
    hi=(1+math.sqrt(1-s*s))/s
    assert abs(lo*hi-1)<2e-12
    assert s*(1+lo*lo) >= 2*lo-2e-12
    assert s*(1+hi*hi) >= 2*hi-2e-12
    mid=math.sqrt(lo*hi)
    assert s*(1+mid*mid)<2*mid
    assert not (s*(1+(0.9*lo)**2)<2*(0.9*lo))
    assert not (s*(1+(1.1*hi)**2)<2*(1.1*hi))

# No stable adjustment exists at normalized step s >= 1.
for s in (1.0,1.1,2.0):
    vals=[2*u/(1+u*u) for u in np.logspace(-5,5,20001)]
    assert max(vals)<=1.0+2e-12
    assert not (s < max(vals)-1e-12)

# Exact threshold versus the later general quadratic sufficient bound.
for mu,L,tau in ((1.0,1.0,0.2),(1.0,3.0,0.7),(0.4,5.0,1.2)):
    exact=2*tau/(1+(tau*L)**2)
    sufficient=tau*mu*mu/((1+(tau*L)**2)*L*L)
    ratio=exact/sufficient
    assert abs(ratio-2*(L/mu)**2)<3e-12

print("verification passed")
