"""Reproduce exact forward-Euler Dirac norm and metric-budget identities."""
from math import sqrt, isclose
import numpy as np


def assemble(B1, B2, gamma0, gamma1):
    n0, n1 = B1.shape
    assert B2.shape[0] == n1
    n2 = B2.shape[1]
    assert np.allclose(B1 @ B2, 0.0, atol=1e-12)
    D = np.zeros((n0 + n1 + n2, n0 + n1 + n2))
    D[:n0, n0:n0+n1] = gamma0 * B1
    D[n0:n0+n1, :n0] = gamma1 * B1.T
    D[n0:n0+n1, n0+n1:] = gamma0 * B2
    D[n0+n1:, n0:n0+n1] = gamma1 * B2.T
    return D


def ingredients(B1, B2, gamma0, gamma1, nu, r):
    s = max(np.linalg.norm(B1, 2), np.linalg.norm(B2, 2))
    p = s * sqrt(gamma0 * gamma1)
    C = s * (gamma0 * sqrt(r) + gamma1 / sqrt(r)) / 2
    D = s * abs(gamma0 * sqrt(r) - gamma1 / sqrt(r)) / 2
    assert isclose(C*C - D*D, p*p, rel_tol=1e-10, abs_tol=1e-10)
    return s,p,C,D


def direct_norm(B1, B2, gamma0, gamma1, nu, r, h):
    matrix = assemble(B1, B2, gamma0, gamma1)
    n0, n1 = B1.shape
    n2 = B2.shape[1]
    v = np.array([r]*n0 + [1]*n1 + [1/r]*n2)
    e = np.eye(len(v)) - h*(nu*np.eye(len(v))+matrix)
    return np.linalg.norm((np.sqrt(v)[:, None] * e)/np.sqrt(v)[None, :], 2)


def predicted(C, D, nu, h):
    return sqrt((1-nu*h)**2 + (h*D)**2) + h*C


def check_case(B1, B2, gamma0, gamma1, nu):
    s, p, _, _ = ingredients(B1, B2, gamma0, gamma1, nu, 1)
    U=max(gamma0,gamma1); V=min(gamma0,gamma1)
    for K in [1, 1.4, 3, 9, 81, 256, 1024]:
        r=max(K**-.5, min(gamma1/gamma0, K**.5))
        s,p,C,D=ingredients(B1,B2,gamma0,gamma1,nu,r)
        pred_C=s/2*(U*K**-.25+V*K**.25) if K<(U/V)**2 else p
        assert isclose(C,pred_C,rel_tol=1e-10,abs_tol=1e-10)
        for h in [.001,.03,.2,.43,1.1]:
            got=direct_norm(B1,B2,gamma0,gamma1,nu,r,h)
            assert isclose(got,predicted(C,D,nu,h),rel_tol=1e-10,abs_tol=1e-10), (K,r,h,got,predicted(C,D,nu,h))
        if nu>C:
            H=sqrt(nu*nu-p*p)
            Q=nu*nu+D*D
            hstar=(nu-C*D/H)/Q
            factor=(nu*C+D*H)/Q
            assert hstar>0 and factor<1
            assert isclose(predicted(C,D,nu,hstar),factor,rel_tol=1e-10,abs_tol=1e-10)
            for dh in [.01, .1, .3]:
                assert predicted(C,D,nu,hstar+dh)>factor+1e-12
                if hstar>dh:
                    assert predicted(C,D,nu,hstar-dh)>factor+1e-12
            hcrit=2*(nu-C)/(nu*nu-p*p)
            assert isclose(predicted(C,D,nu,hcrit),1,rel_tol=1e-10,abs_tol=1e-10)
            assert predicted(C,D,nu,hcrit/2)<1
            assert predicted(C,D,nu,hcrit*1.01)>1
        else:
            for h in [.00001,.01,.2,1.0]:
                assert predicted(C,D,nu,h)>=1-1e-12


B1=np.array([[-1.,0,1],[1,-1,0],[0,1,-1]])
B2=np.array([[1.],[1.],[1.]])
assert np.array_equal(B1 @ B2, np.zeros((3,1)))
assert isclose(max(np.linalg.norm(B1,2),np.linalg.norm(B2,2)),sqrt(3),rel_tol=1e-12)
check_case(B1,B2,4,.25,2)
check_case(B1,B2,1.3,.7,3)
check_case(B1,B2,.2,2,1.7)
check_case(B1,B2,1,1,2)

# A second chain with two disconnected filled triangular faces (different zero modes).
B1b=np.zeros((6,6)); B1b[:3,:3]=B1; B1b[3:,3:]=B1
B2b=np.zeros((6,2)); B2b[:3,0]=1; B2b[3:,1]=1
check_case(B1b,B2b,3.3,.18,2.1)

# Exact rational ratios and radicals for the stated witness.
assert isclose((4/sqrt(3))**4,256/9,rel_tol=1e-14)
assert isclose((25*sqrt(3)/24)**2-(7*sqrt(3)/24)**2,3,rel_tol=1e-14)
assert isclose((2-(25*sqrt(3)/24)*(7*sqrt(3)/24))/(4+(7*sqrt(3)/24)**2),209/817,rel_tol=1e-14)
assert isclose(predicted(25*sqrt(3)/24,7*sqrt(3)/24,2,209/817),456*sqrt(3)/817,rel_tol=1e-14)
assert direct_norm(B1,B2,4,.25,2,1,0.1)>1
assert direct_norm(B1,B2,4,.25,2,1/9,209/817)<1
assert direct_norm(B1,B2,4,.25,2,1/9,209/817)<direct_norm(B1,B2,4,.25,2,1/9,0.2)
print('PASS: exact triangle constants; full seven-dimensional singular norms; five chain/coupling scenarios; all budget/step and optimum checks')
