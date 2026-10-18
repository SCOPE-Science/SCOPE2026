"""Numerical diagnostics for the exact first noninvertibility transition of sine-coupled path maps.

Analytic uniqueness, the cusp count, and Hölder sharpness require the proof in RESULT.md.
This script only checks finite instances at controlled precision.
"""
import numpy as np
from scipy.optimize import root


def path_matrix(n):
    return np.diag(2*np.ones(n)) - np.diag(np.ones(n-1), 1) - np.diag(np.ones(n-1), -1)


def branch_prediction(n, eps):
    indices = np.arange(1, n+1)
    return 2*np.sqrt(2*eps) * (-1.)**(indices-1)*np.sin(indices*np.pi/(n+1))


def run():
    count = 0
    for n in [2, 3, 4, 5, 7, 10, 15]:
        K = path_matrix(n)
        eig, U = np.linalg.eigh(K)
        lam = eig[-1]
        reference = 2+2*np.cos(np.pi/(n+1))
        assert abs(lam-reference) < 3e-13
        v = U[:,-1]
        beta = sum(v**4)/6
        assert abs(beta - 1/(4*(n+1))) < 1e-13
        assert eig[0] > 0
        for eps in [0.02, 0.004, 0.0005]:
            h = (1+eps)/lam
            predicted = branch_prediction(n, eps)
            fun=lambda u: u - h*K@np.sin(u)
            for sign in [-1, 1]:
                sol = root(fun, sign*predicted, tol=1e-12)
                assert np.linalg.norm(fun(sol.x))<2e-10, (n,eps,sign,np.linalg.norm(fun(sol.x)))
                assert np.linalg.norm(sol.x)>0.02*np.linalg.norm(predicted)
                err=np.linalg.norm(sol.x-sign*predicted)/np.linalg.norm(predicted)
                assert err < 0.12, (n,eps,sign,err)
                count+=1
        hc=1/lam
        for t in [0.03,0.01,0.003]:
            d=t*v
            image=d-hc*K@np.sin(d)
            assert np.linalg.norm(image)>0
            assert np.linalg.norm(image)<1.0*t**3
            count+=1
    # Exact two-edge invariant odd subspace: a-3h sin(a)=0,
    # with two nonzero solutions born at 3h=1.
    for eps in [.001, .01, .03]:
        h=(1+eps)/3
        a=float(np.sqrt(6*eps))
        f=lambda z:z-3*h*np.sin(z)
        assert f(a)>-0.1
        from scipy.optimize import brentq
        positive=brentq(f,np.sqrt(eps),min(np.pi,5*np.sqrt(eps)))
        assert 0<positive<np.pi
        assert abs(f(positive))<1e-12
        count+=1
    print(f'PASS: {count} numerical spectral, cusp, and critical-map diagnostics')

if __name__=='__main__':run()
