"""Independent numerical diagnostics for affine projection on uniform p-balls.
No finite simulation substitutes for the analytic asymptotic proof.
"""
import math
import numpy as np
from scipy.special import gammaln

def variance(p,d):
    return math.exp(gammaln(3/p)-gammaln(1/p)+gammaln(1+d/p)-gammaln(1+(d+2)/p))

def constant(p):
    return math.sqrt(2/math.pi)*math.exp((gammaln(1/p)-gammaln(3/p))/2-math.log(p)/p)

def experiment(p,d,seed=17,draws=50000):
    rng=np.random.default_rng(seed+d)
    sigma2=variance(p,d)
    # Gamma(shape=1/p,scale=1) independent coordinate magnitudes, plus Exp(1).
    # Draw in batches to avoid an unbounded allocation.
    totals=np.zeros(3)
    xs=[np.full(d,d**(-1/p)),np.r_[1.,np.zeros(d-1)],np.r_[np.full(d//2,(d//2)**(-1/p)),np.zeros(d-d//2)]]
    done=0
    while done<draws:
        k=min(2500,draws-done)
        y=rng.gamma(shape=1/p,scale=1,size=(k,d))
        signs=2*rng.integers(0,2,size=(k,d))-1
        numerator=signs*y**(1/p)
        scale=(y.sum(axis=1)+rng.exponential(size=k))**(1/p)
        xballs=numerator/scale[:,None]
        for j,x in enumerate(xs):
            totals[j]+=np.abs(1+xballs@x/sigma2).sum()
        done+=k
    estimates=totals/draws/math.sqrt(d)
    r=[np.linalg.norm(x)/d**(0.5-1/p) for x in xs]
    predicted=np.array(r)*constant(p)
    return estimates,predicted

if __name__=='__main__':
    for p in (3.,4.,6.):
        for d in (24,96,288):
            e,q=experiment(p,d,draws=18000)
            print(f'p={p:.0f} d={d}: observed {e.round(4)} predicted {q.round(4)}')
            assert all(np.isfinite(e)) and all(e>0)
            assert abs(e[0]-q[0])<0.15
    for d in range(1,9):
        assert math.isclose(variance(2.,d),1/(d+2),rel_tol=1e-12)
    print('PASS: finite sampling diagnostics and exact variance special cases')
