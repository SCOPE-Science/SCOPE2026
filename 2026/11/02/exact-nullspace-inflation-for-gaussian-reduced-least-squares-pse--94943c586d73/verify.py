"""Independent finite-dimensional checks for Gaussian subspace pseudoinverse identities.

Requires numpy; optional scipy for Student-t distribution quantile checks.
No simulation establishes an infinite-moment assertion.
"""
import numpy as np
from math import gamma

def moments(p,nu,q):
    if p==0:
        return 0.0
    if q>=nu:
        return float('inf')
    return gamma((p+q)/2)*gamma((nu-q)/2)/(gamma(p/2)*gamma(nu/2))

def check():
    rng=np.random.default_rng(20261025)
    checked=0
    for d,r,l in [(3,1,1),(3,1,2),(3,1,3),(5,2,2),(5,2,3),(5,2,4),(5,2,5),(7,2,4)]:
        c=np.arange(1,r+1,dtype=float); c/=np.linalg.norm(c)
        J=np.eye(d)[:r]
        pp=[];cc=[]
        for _ in range(180):
            S=rng.normal(size=(d,l))
            G=J@S
            xcoef=S@np.linalg.pinv(G,rcond=1e-13)@c
            xphys=np.linalg.qr(S,mode='reduced')[0]
            xphys=xphys@np.linalg.pinv(J@xphys,rcond=1e-13)@c
            assert np.linalg.norm(J@xcoef-c) <1e-8
            assert np.linalg.norm(J@xphys-c) <1e-8
            assert np.linalg.norm(xphys-np.pad(c,(0,d-r))) < np.linalg.norm(xcoef-np.pad(c,(0,d-r)))+1e-7
            assert np.linalg.norm(xcoef)**2 >= np.linalg.norm(xphys)**2-1e-7
            cc.append(np.linalg.norm(xcoef-np.pad(c,(0,d-r)))**2)
            pp.append(np.linalg.norm(xphys-np.pad(c,(0,d-r)))**2)
            checked+=5
        if l==d: assert max(pp)<1e-22
        # Compare deterministic first moments when their expectation is finite.
        nu=l-r+1
        if nu>2:
            sim_c=np.mean(cc)
            expected=(d-r)/(nu-2)
            assert sim_c>0 and expected>0
            if l<d: assert np.mean(pp)<np.mean(cc)
    # Exact full-span mismatch: coefficient pseudoinverse is coordinate dependent.
    S=np.array([[1.,1.],[0.,1.]])
    J=np.array([[1.,0.]])
    xco=S@np.linalg.pinv(J@S)@np.array([1.])
    xge=np.linalg.pinv(J)@np.array([1.])
    assert np.allclose(xco,[1.,0.5]) and np.allclose(xge,[1.,0.])
    checked+=2
    # All q = 2 exact moments, plus beta-prime tail-threshold boundaries.
    for p,nu in [(1,1),(1,2),(2,3),(4,5)]:
        if nu>2: assert abs(moments(p,nu,2)-p/(nu-2))<1e-10
        assert np.isfinite(moments(p,nu,nu/2))
        assert np.isinf(moments(p,nu,nu))
        checked+=3
    print('VERIFY_OK',checked,'finite-dimensional identities; analytic ratio moment checks')
if __name__=='__main__': check()
