"""Reproducible numerical checks for intrinsic distance statistics of flat bands.

Requires numpy and scipy. This is numerical corroboration, not a proof.
"""
from math import pi, sqrt
import numpy as np
from scipy.integrate import quad


def phi(t, h):
    if t <= 0:
        return 0.0
    if t >= h:
        return 1.0
    return 2*t/h-(t/h)**2


def cylinder_cdf(c, h, r):
    if r <= 0:
        return 0.0
    return 2/c * quad(lambda a: phi(sqrt(max(0, r*r-a*a)), h),
                      0, min(r, c/2), epsabs=2e-12)[0]


def excess(c, h, r):
    if r <= c/2:
        return 0.0

    def integrand(a):
        b = c-a
        u = sqrt(max(0, r*r-a*a))
        v = sqrt(max(0, r*r-b*b))
        q = min(v, max(0, h-u))
        return (2*(h-u)*q-q*q)/(h*h)

    return 2/c * quad(integrand, max(0, c-r), c/2,
                      epsabs=2e-12, epsrel=2e-12, limit=100)[0]


def sample(c, h, n=400_000, seed=1729):
    """Sample quotient coordinates, then independently minimize deck-image paths."""
    rng = np.random.default_rng(seed)
    x = rng.random((n, 2))*c
    y = (rng.random((n, 2))-.5)*h
    dx = x[:, 1]-x[:, 0]
    a = np.minimum(np.abs(dx), c-np.abs(dx))
    # On odd nearest lifts, reflect the second vertical coordinate to
    # construct the equal-in-law cylinder coordinate used in the theorem.
    odd = np.abs(dx)>c/2
    coupled_y2 = np.where(odd, -y[:, 1], y[:, 1])
    dc = np.hypot(a, coupled_y2-y[:, 0])
    raw_cylinder = np.hypot(a, y[:, 1]-y[:, 0])
    # Minimize Euclidean lengths of straight covering-strip lifts, including
    # both twist parities. A wider image range is harmless and tests the
    # nearest-image reduction used in the proof.
    dm = np.full(n, np.inf)
    for k in range(-3, 4):
        dy = (-1 if k % 2 else 1)*y[:, 1]-y[:, 0]
        dm = np.minimum(dm, np.hypot(dx+k*c, dy))
    return dc, dm, raw_cylinder


def main():
    print('Distance-statistics checks on rectangular flat interval bundles')
    for c,h in [(1,1), (1,3), (3,.4), (2.3,1.8)]:
        r0=min(c/2,h)/2
        local=pi*r0*r0/(c*h)-4*r0**3/(3*c*h*h)
        numeric=cylinder_cdf(c,h,r0)
        assert abs(numeric-local)<3e-11
        assert excess(c,h,c/2)==0
        coeff=8/(3*h*sqrt(c))
        ratios=[]
        for e in [1e-3,1e-4,1e-5]:
            ratios.append(excess(c,h,c/2+e)/(coeff*e**1.5))
        assert abs(ratios[-1]-1)<.08, (c,h,ratios)
        print(f'c={c:g} h={h:g} local_err={numeric-local:.2e} '
              f'onset_coefficient={coeff:.10f} rescaled_ratios={ratios}')
    c,h=1.,1.
    dc,dm,rawdc=sample(c,h)
    assert np.all(dm<=dc+1e-14)
    for r in [.3,.5,.6,1.]:
        assert abs(np.mean(dc<=r)-np.mean(rawdc<=r))<.003

    for r in [.30,.50,.55,.60,.75,1.00]:
        observed=np.mean((dm<=r)&(dc>r))
        predicted=excess(c,h,r)
        # 6-sigma Monte Carlo tolerance, with a positive numerical margin
        tolerance=6*sqrt(max(predicted*(1-predicted),1e-8)/len(dc))+.0005
        assert abs(observed-predicted)<tolerance, (r, observed, predicted)
        print(f'r={r:.2f} predicted_excess={predicted:.8f} '
              f'sampled_excess={observed:.8f} tolerance={tolerance:.8f}')
    print('All deterministic identities and Monte Carlo comparisons passed.')


if __name__=='__main__':
    main()
