"""Reproduce finite-matrix consistency checks for the quantum-classical distance formulas.
Run: python verify.py (requires NumPy and SciPy). Finite tests do not prove the all-order theorem.
"""
import math
import numpy as np
from scipy.linalg import expm


def graph_laplacian(weights):
    return np.diag(weights.sum(axis=1)) - weights


def conditional_distance(laplacian, j, gamma, time):
    vals, vecs = np.linalg.eigh(laplacian)
    v = vecs[j, :]
    diff = vals[:, None] - vals[None, :]
    rho = vecs @ (np.outer(v, v) * np.exp((-1j * diff - gamma * diff * diff / 2) * time)) @ vecs.T
    classical = expm(-time * laplacian)[:, j]
    root = np.sqrt(np.maximum(classical, 0))
    spectral = np.linalg.eigvalsh(root[:, None] * rho * root[None, :])
    return 1 - float(np.sum(np.sqrt(np.maximum(0, spectral))) ** 2)


def formula_slope(weights, site, gamma):
    w = weights[:, site]
    return float(w.sum() + gamma * (w**2).sum() - 2 * math.sqrt(gamma * (w**3).sum()))


def analytic_terminal(a, b):
    n = a + b
    roots = 1/math.sqrt(n) + math.sqrt(b/(a*n)) + math.sqrt((a-1)/a)
    return 1 - roots*roots/n


def independently_pinched_distance(weights, site):
    laplacian = graph_laplacian(weights)
    vals, vecs = np.linalg.eigh(laplacian)
    n = len(vals)
    v = np.eye(n)[:, site]
    stationary = np.zeros((n,n), dtype=float)
    i = 0
    while i < n:
        k = i+1
        while k<n and abs(vals[k]-vals[i]) < 1e-8:
            k += 1
        proj = vecs[:, i:k] @ vecs[:, i:k].T
        sub = proj @ v
        stationary += np.outer(sub, sub)
        i = k
    assert abs(float(np.trace(stationary))-1)<2e-10
    roots = np.sqrt(np.maximum(0, np.linalg.eigvalsh(stationary)))
    return 1 - float(np.sum(roots)**2)/n


def main():
    matrix_cases = 0
    for a in range(1, 9):
        for b in range(1, 9):
            n=a+b
            weights=np.zeros((n,n), dtype=float)
            weights[:a,a:] = 1
            weights[a:,:a] = 1
            for site in range(n):
                expected = analytic_terminal(a,b) if site<a else analytic_terminal(b,a)
                actual=independently_pinched_distance(weights,site)
                assert abs(actual-expected)<1e-7,(a,b,site,expected,actual)
                matrix_cases+=1
    topology_cases=0
    for n in range(4, 201):
        values=[]
        for smaller in range(1,n//2+1):
            bigger=n-smaller
            a=analytic_terminal(smaller,bigger)
            b=analytic_terminal(bigger,smaller)
            maxv=max(a,b)
            if smaller==1:
                assert abs(maxv-a)<1e-11
            else:
                assert abs(maxv-b)<1e-11
            values.append(maxv)
            topology_cases+=1
        assert all(values[k]>values[k+1]+1e-12 for k in range(len(values)-1))
    rng=np.random.default_rng(20261010)
    small_time_checks=0
    for n in range(3, 8):
        for trial in range(3):
            weights=np.triu(rng.uniform(.25,1.3,(n,n)),1)
            weights += weights.T
            weights[0,-1] = weights[-1,0] = 0
            lap=graph_laplacian(weights)
            for gamma in (.25,1.,2.):
                for site in range(n):
                    slope=formula_slope(weights,site,gamma)
                    estimate=conditional_distance(lap,site,gamma,1e-5)/1e-5
                    assert abs(estimate-slope)<.035, (n,trial,gamma,site,slope,estimate)
                    small_time_checks+=1
    reversal_cases=0
    for a,b in ((2,3),(2,6),(3,7)):
        n=a+b
        weights=np.zeros((n,n),dtype=float)
        weights[:a,a:]=1
        weights[a:,:a]=1
        lap=graph_laplacian(weights)
        for gamma in (.15,.5,2.0,5.0):
            t0=2e-4
            early=conditional_distance(lap,0,gamma,t0)-conditional_distance(lap,a,gamma,t0)
            assert early > 0,(a,b,gamma,early)
            assert analytic_terminal(b,a) > analytic_terminal(a,b)
            reversal_cases+=1
    print('VERIFY_OK pinching=%d topology=%d weighted_short_time=%d reversal=%d' % (matrix_cases,topology_cases,small_time_checks,reversal_cases))

if __name__=='__main__':main()
