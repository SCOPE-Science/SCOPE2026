"""Reproducible numerical checks for the fixed-size circumscribed-polygon tail theorem.

Run: python verify.py (requires numpy and scipy).
"""
import math
import numpy as np
from scipy.special import betainc, betaln


def constants(n, alpha):
    assert n >= 3 and alpha > 0
    q = 1 - n * (1 - betainc(alpha, (n-1)*alpha, 0.5))
    f = math.exp((2 - n*alpha)*math.log(2) - betaln(alpha, (n-1)*alpha))
    c = n * f / (math.pi * q)
    assert q > 0
    return q, c


def geometric_area(gaps):
    n = len(gaps)
    assert max(gaps) < 0.5 and abs(sum(gaps)-1) < 1e-12
    theta = 2 * math.pi * np.r_[0, np.cumsum(gaps)[:-1]]
    mid = theta + math.pi * gaps
    vertices = np.column_stack([np.cos(mid),np.sin(mid)]) / np.cos(math.pi*gaps)[:,None]
    x,y = vertices.T
    return 0.5*abs(np.dot(x,np.roll(y,-1))-np.dot(y,np.roll(x,-1)))


def checks():
    rg = np.random.default_rng(20261031)
    for n, alpha in ((3, .5),(3,1),(5,1),(6,2),(8, .75)):
        q, c = constants(n, alpha)
        print('parameters n=%d alpha=%.3f bounded_probability=%.10f tail_coefficient=%.10f' % (n,alpha,q,c))
        ys = rg.dirichlet([alpha]*n, size=1500)
        feasible = ys[np.max(ys,axis=1) < 0.5]
        assert len(feasible)>100
        for y in feasible[:min(300,len(feasible))]:
            a = geometric_area(y)
            b = float(np.tan(math.pi*y).sum())
            assert math.isclose(a,b,rel_tol=1e-11,abs_tol=1e-10), (a,b)
    # For a=1 the Dirichlet model is the circular-spacing model of iid uniform contact angles.
    for n in (3,5,7):
        q, _ = constants(n,1)
        assert math.isclose(q,1-n/2**(n-1),abs_tol=1e-12)
    # Density-controlled leading coefficient: conditional probability a single
    # gap approaches a half-circle, multiplied by the number of gaps.
    for n, alpha in ((3,.5),(3,1),(5,1),(5,2)):
        q,c = constants(n,alpha)
        b1,b2=alpha,(n-1)*alpha
        fhalf=math.exp((2-n*alpha)*math.log(2)-betaln(b1,b2))
        for d in (1e-3,1e-4,1e-5):
            # CDF difference for small neighborhoods, rather than sampling rare events.
            mass=betainc(b1,b2,0.5)-betainc(b1,b2,0.5-d)
            ratio=mass/(d*fhalf)
            assert abs(ratio-1)<0.015,(n,alpha,d,ratio)
        assert math.isclose(c,n*fhalf/(math.pi*q),rel_tol=1e-14)
    print('GEOMETRIC_SHOELACE_BETA_EDGE_AND_COEFFICIENT_CHECKS_PASSED')
    for n,alpha in ((3,1),(5,.5),(5,2)):
        yy=rg.dirichlet([alpha]*n,size=800_000)
        mask=np.max(yy,axis=1)<.5
        areas=np.tan(math.pi*yy[mask]).sum(axis=1)
        _,c=constants(n,alpha)
        # Coarse independent rare-event validation. Approximation error and
        # binomial counting fluctuations are appreciable at finite thresholds.
        for t in (30,70):
            empirical=t*np.count_nonzero(areas>t)/len(areas)
            print('n=%d alpha=%.2f t=%d t*tail=%.5f limiting=%.5f' % (n,alpha,t,empirical,c))
            assert 0.60*c<empirical<1.5*c
    print('ALL_CIRCUMSCRIBED_DIRICHLET_TAIL_CHECKS_PASSED')

if __name__=='__main__':
    checks()
