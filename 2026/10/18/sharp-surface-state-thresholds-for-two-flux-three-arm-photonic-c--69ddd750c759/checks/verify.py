#!/usr/bin/env python3
"""Independent finite-matrix checks for a terminated three-arm photonic lattice.

Requires Python >= 3.9 and NumPy. The infinite-volume statements are
proved analytically in RESULT.md; these finite checks are not that proof.
"""
import math
import numpy as np


def vectors(J1, J2, Jt1, Jt2, phi1, phi2):
    t = np.array([J1, Jt1*np.exp(-1j*phi1), Jt1*np.exp(1j*phi2)], dtype=complex)
    s = np.array([J2, Jt2, Jt2], dtype=complex)
    return t, s


def physical_t(N, t, s):
    T = np.zeros((N, 3*N), dtype=complex)
    for k in range(N):
        T[k, 3*k:3*k+3] = t
        if k:
            T[k, 3*(k-1):3*(k-1)+3] = s
    return T


def jacobi(N, u, v, q):
    J = np.diag([u] + [u+v]*(N-1)).astype(complex)
    for k in range(N-1):
        J[k,k+1] = q
        J[k+1,k] = np.conj(q)
    return J


def check(N, params, tol=1e-8):
    t, s = vectors(*params)
    u = float(np.vdot(t,t).real)
    v = float(np.vdot(s,s).real)
    q = np.dot(t,np.conj(s))
    c = abs(q)
    T = physical_t(N,t,s)
    J = jacobi(N,u,v,q)
    assert np.allclose(T @ T.conj().T,J,rtol=1e-11,atol=1e-11)
    vals = np.linalg.eigvalsh(T@T.conj().T)
    assert vals[0] > -tol
    if c > 1e-7:
        finite_detaches = v > c*(N+1)/N
        edge_below_bulk = vals[0] < u+v-2*c-tol
        if abs(v-c*(N+1)/N)>1e-5:
            assert finite_detaches == edge_below_bulk, (N,params,vals[0],u+v-2*c)
        if v>c+1e-6:
            mu = u-c*c/v
            r = -np.conj(q)/v
            assert abs(u+q*r-mu)<tol
            assert abs(u+v+np.conj(q)/r+q*r-mu)<tol
            assert mu >= -tol
            assert mu < u+v-2*c+tol
    else:
        assert abs(vals[0]-u)<tol
        assert np.allclose(vals[1:],u+v,atol=tol)
    # Direct Hermitian 4N by 4N, without relying on a spectral-square identity.
    if N<=8:
        H = np.block([[np.zeros((N,N),complex),T],
                      [T.conj().T,np.zeros((3*N,3*N),complex)]])
        spectrum = np.linalg.eigvalsh(H)
        predicted = np.sort(np.r_[ -np.sqrt(vals), np.zeros(2*N), np.sqrt(vals)])
        assert np.allclose(spectrum,predicted,rtol=1e-10,atol=tol)


def main():
    rng=np.random.default_rng(482311)
    count=0
    for N in range(2,17):
        for k in range(150):
            params=(*np.exp(rng.uniform(-1.2,1.2,4)),
                    *rng.uniform(-math.pi,math.pi,2))
            check(N,params)
            count+=1
    # Exact destructive-interference cases, and one parallel-coupling zero mode.
    for N in range(2,17):
        check(N,(1,1,1,1,2*math.pi/3,2*math.pi/3))
        check(N,(0.5,1,0.5,1,0,0))
        count+=2
    for N in range(2,17):
        angle=math.acos(1-3/(2*(N+1)))
        for phi in [max(1e-6,angle-0.02),angle+0.02]:
            check(N,(1,1,1,1,phi,phi))
            count+=1
    # A finite-size critical angle and a cubic band-edge detachment test.
    for p in [0.015,0.02,0.025,0.04]:
        c=1+2*math.cos(p)
        mu=3-c*c/3
        eb=math.sqrt(6-2*c)
        es=math.sqrt(mu)
        expected=p**3/(6*math.sqrt(2))
        assert abs((eb-es)/expected-1)<0.004
    print(f"PASS: {count} independent finite hopping matrices, finite-threshold checks,")
    print("      direct full-Hamiltonian eigenvalues for N<=8, special-flux cases,")
    print("      and cubic small-flux asymptotics.")

if __name__ == '__main__':
    main()
