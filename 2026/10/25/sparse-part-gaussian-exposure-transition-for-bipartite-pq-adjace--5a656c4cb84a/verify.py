"""Reproducible finite checks for the PQ adjacency-polytope directional crossover.
Requires Python 3, NumPy, SciPy. These are diagnostics, not asymptotic proofs.
"""
import math
import numpy as np
from scipy.special import ndtr
from scipy.integrate import quad

RNG = np.random.default_rng(20261018)
A = math.sqrt(2.0) - 1.0
B = A * A
C_STAR = A * (4.0 * math.pi) ** A


def b_from_log(log_m):
    r = math.sqrt(2.0 * log_m)
    return r - (math.log(log_m) + math.log(4.0 * math.pi)) / (2.0 * r)


def sparse_shift(log_n, delta):
    log_q = math.log(C_STAR) + A * delta + B * log_n + A * math.log(log_n)
    return math.sqrt(2*log_n) * (b_from_log(log_q) - A*b_from_log(log_n))


def fast_support(g, h, p):
    x = max(np.max(g[:p]) + np.max(h[p:]),
            np.max(g[p:]) + np.max(h[:p]),
            np.max(g+h))
    return float(x)


def brute_support(g, h, p):
    n=len(g)
    return max(float(g[i]+h[j]) for i in range(n) for j in range(n)
               if i==j or ((i<p)!=(j<p)))


def gumbel_cdf(t):
    return math.exp(-math.exp(-t))


def sum_cdf(s):
    # Exact law of G1+A^{-1}G2, independent standard Gumbels.
    f=lambda u: math.exp(-u-math.exp(-s)*u**(-1/A)) if u>0 else 0.0
    return quad(f,0.0,math.inf,epsabs=1e-11,epsrel=1e-11)[0]


def limiting_cdf(t,delta):
    return gumbel_cdf(t/math.sqrt(2))*sum_cdf(t-delta)**2


def main():
    support_checks=0
    for n in [4,5,8,12,25,50]:
        for p in range(2,n-1):
            for trial in range(7):
                g=RNG.normal(size=n)
                h=RNG.normal(size=n)
                exact=brute_support(g,h,p)
                fast=fast_support(g,h,p)
                assert abs(exact-fast)<1e-11
                # Translation into the affine direction subspace does not change width.
                centered_g=g-g.mean(); centered_h=h-h.mean()
                assert abs((fast_support(g,h,p)+fast_support(-g,-h,p))-
                   (fast_support(centered_g,centered_h,p)+fast_support(-centered_g,-centered_h,p)))<1e-10
                support_checks+=1

    # Asymptotic centering constant: exact formula at logarithmic N scales.
    shift_checks=0
    for delta in (-2.0,0.0,1.5):
        errs=[]
        for ln in (1e2,1e3,1e4,1e5,1e6):
            x=sparse_shift(ln,delta)
            assert math.isfinite(x)
            errs.append(abs(x-delta))
        assert errs[-1] < errs[1] and errs[-1] < 0.003, (delta,errs)
        shift_checks+=len(errs)

    # Compare two equivalent representations of the proposed limiting CDF.
    samples=RNG.gumbel(size=(220000,5))
    tlim=np.maximum(np.sqrt(2)*samples[:,0],
                    np.maximum(samples[:,1]+samples[:,2]/A,
                               samples[:,3]+samples[:,4]/A))
    cdf_checks=0
    for t in (0.0,3.0,6.0,9.0,12.0):
        f=limiting_cdf(t,0.)
        e=np.mean(tlim<=t)
        assert abs(e-f)<0.007,(t,e,f)
        cdf_checks+=1

    # Exposed type at finite N: exhaustive argmax versus the max-of-three reduction.
    angular_checks=0
    for n,p in ((10,7),(20,15),(100,85)):
        for _ in range(120):
            g=RNG.standard_normal(n);h=RNG.standard_normal(n)
            d=np.max(g+h)
            c1=np.max(g[:p])+np.max(h[p:])
            c2=np.max(g[p:])+np.max(h[:p])
            expected=int(d>max(c1,c2))
            val=fast_support(g,h,p)
            assert abs(val-max(d,c1,c2))<1e-11
            assert expected==int(d>val-1e-12)
            angular_checks+=1

    print('VERIFY_OK support=',support_checks,'asymptotic_shifts=',shift_checks,
          'cdf=',cdf_checks,'angular=',angular_checks)

if __name__=='__main__':
    main()
