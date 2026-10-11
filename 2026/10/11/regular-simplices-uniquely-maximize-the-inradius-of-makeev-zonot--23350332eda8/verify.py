#!/usr/bin/env python3
import math
import numpy as np

def centered_simplex(d, seed):
    rng=np.random.default_rng(seed)
    # Standard centered simplex in R^{d+1}, then project to an orthonormal
    # basis of the zero-sum hyperplane and apply a deterministic nonsingular map.
    E=np.eye(d+1)-np.ones((d+1,d+1))/(d+1)
    Q,_=np.linalg.qr(E[:,:d])
    V=E@Q
    A=rng.normal(size=(d,d))
    A=A + (d+1)*np.eye(d)
    W=V@A.T
    W=W-W.mean(axis=0)
    diam=max(np.linalg.norm(W[i]-W[j]) for i in range(d+1) for j in range(i))
    return W/diam

def support(V,u):
    vals=V@u
    return np.maximum(vals,0).sum()

for d in range(2,8):
    V=centered_simplex(d,100+d)
    assert np.linalg.norm(V.sum(axis=0))<1e-12
    for i in range(d+1):
        for j in range(i+1,d+1):
            others=np.delete(V,[i,j],axis=0)
            _,_,vh=np.linalg.svd(others)
            u=vh[-1]
            u=u/np.linalg.norm(u)
            vals=V@u
            mask=[k for k in range(d+1) if k not in (i,j)]
            assert max(abs(vals[k]) for k in mask)<2e-11
            assert abs(vals[i]+vals[j])<2e-11
            h=support(V,u)
            edge=np.linalg.norm(V[i]-V[j])
            cert=0.5*abs(np.dot(u,V[i]-V[j]))
            assert abs(h-cert)<2e-11
            assert h<=0.5*edge+2e-11
            assert edge<=1+2e-12

# Regular simplex check in zero-sum coordinates.
for d in range(2,10):
    E=np.eye(d+1)-np.ones((d+1,d+1))/(d+1)
    # Scale so every edge has length 1.
    V=E/math.sqrt(2)
    edges=[np.linalg.norm(V[i]-V[j]) for i in range(d+1) for j in range(i)]
    assert max(abs(x-1) for x in edges)<2e-14

    # Unit directions in the ambient zero-sum hyperplane satisfy
    # sum_i (u·a_i)^2 = 1/2.
    rng=np.random.default_rng(900+d)
    for _ in range(200):
        u=rng.normal(size=d+1)
        u=u-u.mean()
        u=u/np.linalg.norm(u)
        vals=V@u
        assert abs(vals.sum())<2e-14
        assert abs(np.dot(vals,vals)-0.5)<2e-14
        # For zero-sum vals with l2^2=1/2, l1>=1.
        h=0.5*np.abs(vals).sum()
        assert h>=0.5-2e-14

    # Edge-difference direction attains support 1/2.
    u=V[0]-V[1]
    u=u/np.linalg.norm(u)
    assert abs(support(V,u)-0.5)<2e-14

print("VERIFY_OK")
print("pairwise_support_certificates = passed")
print("diameter_bound = passed")
print("regular_simplex_tight_case = passed")
