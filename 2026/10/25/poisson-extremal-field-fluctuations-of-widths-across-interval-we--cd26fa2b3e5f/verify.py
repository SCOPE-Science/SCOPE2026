"""Independent finite checks for interval-simplex directional widths.

Dependencies: Python 3, numpy, scipy.  Finite checks do not certify the limit law.
"""
import itertools
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr


def profile(k, s, t):
    if k == 0:
        return 1.0
    if k == 1:
        return 0.4 + 1.1 * (t-s)
    return 0.7 + 0.2 * math.sin(math.pi*s) + 0.4*t


def interval_weights(n, profile_index):
    return {(i,j):profile(profile_index,(i-1)/n,j/n)
            for i in range(1,n+1) for j in range(i,n+1)}


def support(x, wt):
    s=0.0
    for (i,j),v in wt.items():
        s += v*max(x[i-1:j])
    return s


def width_by_ranges(x, wt):
    return sum(v*(max(x[i-1:j])-min(x[i-1:j]))
               for (i,j),v in wt.items())


def exhaustive_vertex_support(x, wt):
    # Explicitly build all selections from the summand vertices.
    n=len(x)
    opts=[list(range(i-1,j)) for i,j in wt]
    weights=list(wt.values())
    ans=-float('inf')
    for sel in itertools.product(*opts):
        point=np.zeros(n)
        for h,v in enumerate(sel):
            point[v]+=weights[h]
        ans=max(ans,float(np.dot(x,point)))
    return ans


def expected_normal_maximum(k):
    if k == 1:
        return 0.0
    return quad(lambda x:1-ndtr(x)**k-(1-ndtr(x))**k,
                0,10,epsabs=1e-11)[0]


def truncated_poisson_integral(rng, cutoff=5):
    # Use a lower cutoff for PPP marks and integrate exactly the maximum of
    # retained marks, with cutoff substituted on uncovered intervals.
    m=rng.poisson(math.exp(cutoff))
    u=rng.uniform(0,1,m)
    marks=-cutoff+rng.exponential(size=m)
    perm=np.argsort(u)
    u=np.r_[0.0,u[perm],1.0]
    marks=marks[perm]
    gaps=np.diff(u)
    integral=-cutoff*np.dot(gaps,gaps)/2
    for i in range(m):
        peak=-float('inf')
        for j in range(i,m):
            peak=max(peak,marks[j])
            integral+=gaps[i]*gaps[j+1]*peak
    return integral


def run():
    rng=np.random.default_rng(20261018)
    support_cases=0
    for p in range(3):
        for n in range(2,8):
            wt=interval_weights(n,p)
            for r in range(8):
                g=rng.normal(size=n)
                a=width_by_ranges(g,wt)
                assert abs(a-support(g,wt)-support(-g,wt))<1e-10
                assert abs(a-width_by_ranges(g-g.mean(),wt))<1e-10
                support_cases+=1
        wt=interval_weights(4,p)
        for r in range(5):
            g=rng.normal(size=4)
            assert abs(support(g,wt)-exhaustive_vertex_support(g,wt))<1e-10
            support_cases+=1
    means={k:expected_normal_maximum(k) for k in range(1,10)}
    moment_cases=0
    for p in range(3):
        for n in (3,5,7,9):
            wt=interval_weights(n,p)
            exact=2*sum(v*means[j-i+1] for (i,j),v in wt.items())
            sims=np.array([width_by_ranges(rng.normal(size=n),wt)
                           for r in range(2000)])
            err=sims.std(ddof=1)/math.sqrt(len(sims))
            assert abs(sims.mean()-exact)<5*err+0.002
            moment_cases+=1
    # Diagnostic only: cutoff approximation converges slowly and is not a proof.
    poiss=np.array([truncated_poisson_integral(rng,5)
                    +truncated_poisson_integral(rng,5) for _ in range(100)])
    print('PPP cutoff=5 diagnostic:',round(float(poiss.mean()),5),
          'uncut theoretical mean=',round(float(np.euler_gamma-1.5),5))
    print('VERIFY_OK support_checks=',support_cases,'mean_checks=',moment_cases)

if __name__ == '__main__':
    run()
