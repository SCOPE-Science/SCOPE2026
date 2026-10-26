"""Independent finite-dimensional checks for the first singularity of a cycle-gradient map.
Run with Python 3 and numpy/scipy (see requirements.txt). Tests support, but do not replace, the all-n proof.
"""
import math
import numpy as np
from scipy.optimize import root, brentq


def cycle_data(n):
    K = np.zeros((n,n))
    for j in range(n):
        K[j,j] += 2
        K[j,(j+1)%n] -= 1
        K[j,(j-1)%n] -= 1
    lam = 4.0 if n%2==0 else 2+2*math.cos(math.pi/n)
    if n%2==0:
        w = np.array([(-1.)**j for j in range(n)])/math.sqrt(n)
        z = np.full(n,math.pi)
        c = 1/(6*n)
    else:
        k=(n-1)//2
        w=np.array([math.sin(2*math.pi*k*j/n) for j in range(n)])*math.sqrt(2/n)
        z=np.full(n, math.pi)
        z[0]=0.0
        c=1/(4*n)
    w /= np.linalg.norm(w)
    return K,lam,w,z,c


def checks(n):
    K,lam,w,z,c=cycle_data(n)
    D=np.diag(np.cos(z))
    h=1/lam
    J=np.eye(n)+h*K@D
    assert abs(w.sum())<1e-11
    assert abs(np.sum(z)/(2*math.pi)-round(np.sum(z)/(2*math.pi)))<1e-10
    assert np.linalg.norm(K@w-lam*w)<1e-11
    assert np.linalg.norm(D@w+w)<1e-11
    assert np.linalg.norm(J@w)<1e-11
    assert np.linalg.norm(J.T@w)<1e-11
    assert abs(sum(w**4)/6-c)<1e-11
    # Basis of sum-zero space and its w-orthogonal complement.
    _,_,vt=np.linalg.svd(np.vstack([np.ones(n),w]),full_matrices=True)
    Q=vt[2:].T
    assert Q.shape == (n,n-2)
    assert np.linalg.matrix_rank(Q.T@J@Q,tol=1e-8)==n-2
    # For several small supercritical steps, use the actual transverse implicit equations.
    for mu in [0.015,0.005]:
        hh=(1+mu)/lam
        def out(t,avec):
            u=t*w+Q@avec
            return u+hh*K@(np.cos(z)*np.sin(u))
        def solve_y(t):
            rr=root(lambda y: Q.T@out(t,y),np.zeros(n-2),tol=1e-11)
            assert rr.success or np.linalg.norm(Q.T@out(t,rr.x))<1e-11
            return rr.x
        def g(t):
            return float(w@out(t,solve_y(t)))
        tguess=math.sqrt(mu/c)
        positive=brentq(g,tguess*0.55,tguess*1.5,xtol=1e-12)
        negative=brentq(g,-tguess*1.5,-tguess*0.55,xtol=1e-12)
        assert abs(positive+negative)<1e-8
        assert abs(positive/tguess-1)<0.25
        for t in [negative,0.,positive]:
            assert np.linalg.norm(out(t,solve_y(t)))<1e-9
    return n,lam,c

if __name__=='__main__':
    for n in range(3,16):
        print('CHECK',*checks(n))
    print('VERIFY_OK')
