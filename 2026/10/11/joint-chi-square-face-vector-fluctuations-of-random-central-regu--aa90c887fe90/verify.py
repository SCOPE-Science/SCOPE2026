"""Numerical checks for random central sections of regular simplices."""
import math
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
from scipy.stats import chi2

rng = np.random.default_rng(231789)
sigma2 = 0.25 - 0.5/math.pi

def faces(n, k):
    return [math.comb(n, j+2) - (math.comb(k, j+2) if k >= j+2 else 0)
            - (math.comb(n-k, j+2) if n-k >= j+2 else 0)
            for j in range(n-2)]

def geometric_vertex_count(a):
    n = len(a)
    edges = []
    for i in range(n):
        for j in range(i+1,n):
            if a[i]*a[j] < 0:
                t = a[i]/(a[i]-a[j]); v = np.zeros(n)
                v[i] = 1-t; v[j] = t; edges.append(v)
    pts = np.array(edges)
    Q = null_space(np.stack((np.ones(n), a)))
    coords = pts@Q
    return len(ConvexHull(coords, qhull_options='Qx').vertices)

for n in range(4,9):
    for i in range(25):
        a = rng.standard_normal(n); a -= a.mean()
        k = int((a>0).sum())
        counts = faces(n,k)
        assert counts[0] == k*(n-k)
        assert geometric_vertex_count(a) == counts[0]
        dim = n-2
        assert sum((-1)**j * f for j,f in enumerate(counts)) == 1-(-1)**dim

for n in (16,64,256):
    m = 65000
    x = rng.standard_normal((m,n))
    k = np.count_nonzero(x>x.mean(axis=1)[:,None], axis=1)
    fv = k*(n-k)
    exact = n*(n-1)/4 + n*(n-1)/(2*math.pi)*math.asin(1/(n-1))
    assert abs(fv.mean()-exact) < 0.023*n
    loss = (n*n/4-fv)/n
    if n == 256:
        assert abs(loss.mean()-sigma2)<0.006
        assert abs(loss.var()-2*sigma2**2)<0.008
        assert abs(np.quantile(loss,0.9)-sigma2*chi2.ppf(.9,1))<0.035
        for j in (0,1,2,3):
            r = j+2
            b = math.comb(n,r)-math.comb(n//2,r)-math.comb((n+1)//2,r)
            lookup = np.array([math.comb(n,r) - (math.comb(t,r) if t>=r else 0) - (math.comb(n-t,r) if n-t>=r else 0) for t in range(n+1)],float)
            obs = (b - lookup[k])/n**(r-1)
            coef= 1/(2**j*math.factorial(j))
            assert abs(obs.mean()-coef*sigma2)<0.007

print('VERIFY_OK: direct section hulls, face Euler identities, finite means, joint-profile scaling, and non-Gaussian limit diagnostics')
