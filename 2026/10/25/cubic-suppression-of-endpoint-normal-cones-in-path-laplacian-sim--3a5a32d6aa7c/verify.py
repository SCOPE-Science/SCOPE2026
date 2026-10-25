"""Numerical checks for normal-cone angles of path Laplacian simplices.

Requires Python 3, NumPy and SciPy. All random seeds are fixed.
The finite computations below supplement, not establish, the limit theorems.
"""
import math
import numpy as np
from scipy.special import ndtri
from scipy.stats import norm


def path_laplacian(n):
    L = np.zeros((n, n), dtype=np.int64)
    for i in range(n - 1):
        L[i, i] += 1
        L[i + 1, i + 1] += 1
        L[i, i + 1] -= 1
        L[i + 1, i] -= 1
    return L


def direct_endpoint(n, repetitions, seed):
    rng = np.random.default_rng(seed)
    total = 0
    for start in range(0, repetitions, 4000):
        m = min(4000, repetitions - start)
        g = rng.standard_normal((m, n))
        scores = g @ path_laplacian(n)
        total += np.count_nonzero(np.argmax(scores, axis=1) == 0)
    p = total / repetitions
    return p, math.sqrt(p * (1-p) / repetitions)


def importance_endpoint(n, repetitions, seed):
    """Unbiased integral estimator, importance sampling the exceptional endpoint.

    Conditional on X_1=x, (g_1,g_2)=(x/2+Z/sqrt(2),-x/2+Z/sqrt(2)),
    with all other coordinates standard Gaussian and independent.
    """
    rng = np.random.default_rng(seed)
    U = ndtri(1.0 - 1.0/n)
    sigma = math.sqrt(6)
    total = total_sq = 0.0
    for start in range(0, repetitions, 4000):
        m = min(4000, repetitions - start)
        y = -np.log(rng.gamma(shape=3.0, scale=1.0, size=m))
        x = sigma*(U+y/U)
        g = rng.standard_normal((m, n))
        common = g[:, 0].copy() / math.sqrt(2)
        g[:, 0] = x/2 + common
        g[:, 1] = -x/2 + common
        interior = 2*g[:, 1:-1] - g[:, :-2] - g[:, 2:]
        last = g[:, -1] - g[:, -2]
        success = (interior.max(axis=1) < x) & (last < x)
        log_q = -3*y - np.exp(-y) - math.log(2.0)
        log_w = norm.logpdf(x, scale=math.sqrt(2)) + math.log(sigma/U) - log_q
        w = np.exp(log_w) * success
        total += w.sum()
        total_sq += np.dot(w, w)
    mean = total / repetitions
    err = math.sqrt(max(0., total_sq/repetitions-mean**2)/repetitions)
    return mean, err


def star_hub(n, repetitions, seed):
    rng = np.random.default_rng(seed)
    count = 0
    for start in range(0, repetitions, 2000):
        m = min(2000, repetitions-start)
        x = rng.standard_normal((m,n))
        center = x[:,0]
        leaves = x[:,1:]
        hub_score = (n-1)*center - leaves.sum(axis=1)
        leaf_best = leaves.max(axis=1)-center
        count += np.count_nonzero(hub_score > leaf_best)
    return count/repetitions


def main():
    # Symbolic-integer covariance check for all the graph-specified coordinates.
    for n in range(5, 90):
        L = path_laplacian(n)
        C = L@L
        assert (L==L.T).all() and (L.sum(axis=0)==0).all()
        assert C[0,0]==2 and C[-1,-1]==2
        assert np.all(np.diag(C)[1:-1]==6)
        for i in range(1,n-1):
            if i+1<n-1: assert C[i,i+1]==-4
            if i+2<n-1: assert C[i,i+2]==1
            for j in range(i+3,n-1): assert C[i,j]==0
        assert C[0,1]==-3 and C[0,2]==1
        assert np.all(C[0,3:]==0)
    print('COVARIANCE_PASS dimensions=5..89')

    for n in (24,60,100):
        direct,sd = direct_endpoint(n, 350000, 12345+n)
        weighted,wsd = importance_endpoint(n, 90000, 888+n)
        assert abs(direct-weighted) < 6*(sd+wsd)+0.00002
        print(f'FINITE_COMPARISON n={n} direct={direct:.9g} importance={weighted:.9g} '
              f'direct_se={sd:.2g} importance_se={wsd:.2g}')

    C=8*math.sqrt(3)*math.pi
    for n in (100,300,1000):
        weighted,wsd=importance_endpoint(n, 65000, 91231+n)
        leading=C*math.log(n)/n**3
        assert 0.25 < weighted/leading < 1.6
        print(f'RARE_EVENT_DIAGNOSTIC n={n} estimate={weighted:.9g} '
              f'leading={leading:.9g} ratio={weighted/leading:.4f} se={wsd:.2g}')

    for n in (100,1000):
        hub=star_hub(n, 30000, 4433+n)
        assert abs(hub-0.5)<0.035
        print(f'STAR_HUB_DIAGNOSTIC n={n} probability={hub:.6f}')
    print('CHECKS_PASS')

if __name__=='__main__':
    main()
