"""Reproduce finite spectral checks and example SIS fixed points.
Scientific statement and proof are in RESULT.md; numerical checks are illustrative only.
Dependencies: Python 3.10+, NumPy, SciPy.
"""
import numpy as np
from scipy.optimize import root


def graph(m):
    assert isinstance(m, int) and m >= 4
    A = np.zeros((3 * m, 3 * m), dtype=np.float64)
    # Two disjoint m-cliques, and a middle m-path.
    for start in (0, 2*m):
        A[start:start+m, start:start+m] = np.ones((m,m)) - np.eye(m)
    for j in range(m-1):
        A[m+j, m+j+1] = A[m+j+1, m+j] = 1
    # Complete links from the path to the third clique.
    A[m:2*m, 2*m:3*m] = 1
    A[2*m:3*m, m:2*m] = 1
    # Exactly one bridge between the first clique and the path.
    A[0,m] = A[m,0] = 1
    return A


def infection_map(p, A, beta, delta):
    out = np.empty_like(p)
    for i in range(len(p)):
        out[i] = 1.0 - (1.0 - (1.0-delta)*p[i]) * np.prod(1.0 - beta*p[A[i] > 0.5])
    return out


def check(m, epsilon):
    A = graph(m)
    assert np.array_equal(A, A.T)
    assert np.all(np.diag(A) == 0)
    assert np.all(np.sum(A[:m,:m],axis=1) == m-1)
    assert np.all(np.sum(A[m:2*m, m:2*m],axis=1) >= 1)
    assert np.all(A[m:2*m,2*m:3*m] == 1)
    vals, vecs = np.linalg.eigh(A)
    lam, vec = vals[-1], abs(vecs[:,-1])
    assert np.min(vec) > 0
    a = lam-(m-1)
    XB = sum(vec[m:2*m]); XA = sum(vec[:m]); XC=sum(vec[2*m:])
    assert abs(a*XA-vec[m]) < 1e-10
    assert abs(a*XC-m*XB) < 1e-10
    assert lam >= m-1e-10
    assert lam <= 2*m-1+1e-10
    assert a >= (m+1)/2-1e-10
    assert XB/XA > m*m/8
    localA = m-1
    localB = 2*np.cos(np.pi/(m+1))
    assert localA > localB
    delta = .5
    beta_crit = delta/lam
    beta = beta_crit*(1+epsilon)
    assert beta < delta/localA and beta < delta/localB
    # Find the positive nonzero fixed point, not the zero root.
    candidate = None
    for scale in (.05, .2, .7):
        guess = scale*vec/vec.max()
        result = root(lambda p: infection_map(p,A,beta,delta)-p,guess,tol=1e-11)
        if np.max(abs(infection_map(result.x,A,beta,delta)-result.x)) < 1e-8 and np.min(result.x)>1e-11 and np.max(result.x)<1:
            candidate=result.x
            break
    assert candidate is not None, (m,epsilon)
    ratio = sum(candidate[m:2*m])/sum(candidate[:m])
    assert ratio > m*m/8
    print(f'm={m:2d}  lambda={lam:.9f}  local_lambda_A={localA:.6f}  local_lambda_B={localB:.6f}  '
          f'Perron_B/A={XB/XA:.6f}  endemic_B/A={ratio:.6f}  bound={m*m/8:.6f}  '
          f'max_residual={np.max(abs(infection_map(candidate,A,beta,delta)-candidate)):.2g}')


if __name__ == '__main__':
    for m in (4, 6, 10, 20, 40):
        for eps in (.02,.005):
            check(m,eps)
    print('PASS: ten numerical instances, exact graph identities and spectral bounds checked.')
