"""Supplemental finite checks for a Gaussian Robin-truncation theorem.
Uses only Python 3's standard library; not a substitute for the proof.
"""
import math
from statistics import NormalDist


def zeta_bound(s, N=200000):
    # Euler integral bounds on the omitted decreasing tail.
    partial = math.fsum(k**(-s) for k in range(1, N + 1))
    return partial + (N + 1)**(1-s)/(s-1), partial + N**(1-s)/(s-1)


def poisson_cdf(x, k):
    # Summing centered point masses avoids underflow at x=1000.
    j0 = int(x)
    p = math.exp(-x + j0*math.log(x) - math.lgamma(j0+1))
    cdf = p if j0 <= k else 0.0
    q = p
    for j in range(j0 - 1, -1, -1):
        q *= (j + 1)/x
        if j <= k:
            cdf += q
    q = p
    for j in range(j0 + 1, k + 1):
        q *= x/j
        cdf += q
    return cdf


def primes_count(n):
    p = []
    v = 2
    while len(p) < n:
        if all(v % z for z in p if z*z <= v):
            p.append(v)
        v += 1
    return p


def run():
    nd = NormalDist()
    zeta = [None] + [zeta_bound(r+1) for r in range(1, 7)]
    c = []
    H = []
    for r in range(1, 7):
        lo, hi = zeta[r]
        assert hi-lo < 1e-7
        cr = nd.inv_cdf(1 / ((lo+hi)/2))
        c.append(cr)
        H.append((4-cr*cr)/6)
    assert all(0 < t < 1 for t in H[:4])
    assert all(t < 0 for t in H[4:])
    assert c[3] < 2 < c[4]

    # Exact prime-factor products, then normalized by log log((primorial)^r).
    ps = primes_count(700)
    lnP, products = 0.0, [1.0]*6
    errors = []
    for k, p in enumerate(ps, 1):
        lnP += math.log(p)
        for r in range(1, 7):
            products[r-1] *= (1 - p**(-(r+1))) / (1 - 1/p)
        if k in (100, 400, 700):
            for r in range(1, 7):
                x = math.log(r*lnP)
                target = 1/((zeta[r][0]+zeta[r][1])/2)
                normalized = products[r-1]/(math.exp(0.5772156649015329)*math.log(p))
                errors.append(abs(normalized-target))
    assert errors and max(errors[-6:]) < .012

    checks = 0
    for r, cr in enumerate(c, 1):
        for x in (100.2, 275.7, 1000.3):
            y = x+cr*math.sqrt(x)
            f = y-math.floor(y)
            obs = poisson_cdf(x, math.floor(y))
            th = nd.cdf(cr)+nd.pdf(cr)/math.sqrt(x)*((4-cr*cr)/6-f)
            assert abs(obs-th) < .00075, (r,x,obs,th)
            checks += 1

    # The mesh of the shift phase tends to 0 along extremal primorials.
    def x_of_support(k, r):
        lnP = math.fsum(math.log(p) for p in ps[:k])
        return math.log(math.log(r*lnP))
    for r in (1, 4, 5):
        xa, xb = x_of_support(400, r), x_of_support(700, r)
        assert xb>xa>0
        yc = lambda x: x+c[r-1]*math.sqrt(x)
        assert yc(x_of_support(700,r))-yc(x_of_support(699,r)) < .004
    print('VERIFY_OK r=1..6 critical_transition=4_to_5 Poisson_Edgeworth_checks='+str(checks)
          +' extremal_product_samples='+str(len(errors))+' prime_support_max=700')

if __name__ == '__main__':
    run()
