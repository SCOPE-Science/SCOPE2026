"""Reproducible numerical check of the explicit critical lens-diameter limit.

This check supplements but does not replace the proof in RESULT.md.
Requires NumPy and SciPy.
"""
import numpy as np
from scipy.integrate import quad
from scipy.spatial import ConvexHull
from scipy.spatial.distance import pdist


def poisson_cdf(lam, t):
    assert lam >= 0 and t > 0
    integral = quad(lambda th: max(0.,t-2*lam*abs(np.cos(th)))**2.5,
                    0.,2*np.pi,epsabs=2e-10)[0]
    return float(-np.expm1(-8*integral/(15*np.pi*np.pi)))


def uniform_lens(n, c, rng):
    kept=[]
    count=0
    while count<n:
        x=rng.uniform(-1,1,(int(1.2*n)+50,2))
        x=x[((x[:,0]-c)**2+x[:,1]**2<=1)&
            ((x[:,0]+c)**2+x[:,1]**2<=1)]
        kept.append(x)
        count+=len(x)
    return np.concatenate(kept)[:n]


def main():
    assert np.isclose(-np.log1p(-poisson_cdf(0,1)),16/(15*np.pi),rtol=1e-10)
    rng=np.random.default_rng(20261025)
    n=1500; s=n**(-.8); reps=350
    for lam in [0.,0.7]:
        values=[]
        for _ in range(reps):
            pts=uniform_lens(n,lam*s,rng)
            hull=pts[ConvexHull(pts).vertices]
            values.append((2-max(pdist(hull)))/s)
        values=np.array(values)
        tests=[1.0,1.6,2.2] if lam==0 else [1.,2.,3.]
        print('lambda:',lam,'mean:',round(values.mean(),5))
        for t in tests:
            empirical=np.mean(values<=t)
            target=poisson_cdf(lam,t)
            print('  t=',t,' empirical=',round(empirical,4),
                  ' asymptotic=',round(target,4))
            # Finite-n bias is not an error certificate. These deliberately
            # coarse bounds only catch gross normalization mistakes.
            assert abs(empirical-target)<.20
    print('Numerical illustrations completed.')


if __name__=='__main__':
    main()
