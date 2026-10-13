"""Numerical and exact-rational checks for a sharp polar-direction score comparison.

Run with Python 3 and NumPy. These checks are diagnostic, not a proof.
"""
from fractions import Fraction
import numpy as np

rng = np.random.default_rng(260401)

def polar(x):
    u, _, vh = np.linalg.svd(x, full_matrices=False)
    return u @ vh

def score(g, b, p):
    return float(np.sum(g * p)**2 / np.trace(p @ b @ p.T))

# Exact rational sharpness algebra: for kappa=k, a=2k/(k+1),
# ||Bv||^2=k, hence a^2/||Bv||^2=4k/(k+1)^2.
for k in range(1, 71):
    q = Fraction(k, 1)
    a = 2*q/(1+q)
    ratio = a*a/q
    assert ratio == 4*q/(1+q)**2
    assert ratio <= 1

cases=0
for n in range(2, 8):
    for tall_extra in (0, 1, 3):
        m=n+tall_extra
        for _ in range(120):
            z=rng.normal(size=(n,n))
            lam=np.exp(rng.uniform(-3.,3.,size=n))
            rot=np.linalg.qr(z)[0]
            b=rot@np.diag(lam)@rot.T
            x=rng.normal(size=(m,n))
            g=x @ b
            p0=polar(g)
            p1=polar(x)
            s0=score(g,b,p0)
            s1=score(g,b,p1)
            kap=lam.max()/lam.min()
            bound=4*kap/(1+kap)**2
            assert s1/s0 >= bound-1e-10, (n,m,kap,s1/s0,bound)
            assert s1/s0 <= 1+1e-10, (n,m,s1/s0)
            # Verify actual optimal line search objective improvement.
            w=x.copy()
            eta=np.sum(g*p1)/np.trace(p1@b@p1.T)
            before=.5*np.trace(w@b@w.T)
            after=.5*np.trace((w-eta*p1)@b@(w-eta*p1).T)
            assert np.isclose(2*(before-after),s1,rtol=1e-9,atol=1e-9)
            cases+=1

# Strict, commuting equality and nearly rank-one sharpness.
for k in (1.1,2.,5.,10.,100.):
    b=np.diag([1.,k]); c=np.sqrt(k/(k+1)); s=np.sqrt(1/(k+1))
    v=np.array([[c,-s],[s,c]])
    lower=4*k/(1+k)**2
    ratios=[]
    for eps in (1e-2,1e-4,1e-6,1e-8):
        x=np.diag([1.,eps])@v.T
        g=x@b
        ratios.append(score(g,b,polar(x))/score(g,b,polar(g)))
    assert min(ratios)>=lower-1e-9
    assert abs(ratios[-1]-lower)<1e-6, (k,ratios[-1],lower)
    g=np.diag([2.,5.])@b
    assert abs(score(g,b,polar(g@np.linalg.inv(b)))/score(g,b,polar(g))-1)<1e-12

print(f'VERIFY_OK rational_sharpness={70} random_full_rank_cases={cases} sharp_sequences={5} line_search_cases={cases}')
