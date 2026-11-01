"""Reproducible finite checks of root-cap transition and lens coefficient.

Run with python3 verify.py. Uses only the standard library.
This checker is supplementary to the analytic proof.
"""
import itertools
import math


def root(n, i, j):
    return tuple((int(k == i) - int(k == j)) for k in range(n))


def dot2(a, b):
    # Twice the Euclidean scalar product of normalized roots.
    return sum(x * y for x, y in zip(a, b))


def sphere_c(d):
    return 2 * math.pi ** (d / 2) / math.gamma(d / 2)


def kappa(n):
    return math.pi ** (n / 2) / math.gamma(n / 2 + 1)


def beta_cdf_z(z, d):
    """I_z(1/2,(d-2)/2) for dimensions 3, 4, 5."""
    z = max(0.0, min(1.0, z))
    if d == 3:
        return 2 / math.pi * math.asin(math.sqrt(z))
    if d == 4:
        return math.sqrt(z)
    if d == 5:
        return 2 / math.pi * (math.asin(math.sqrt(z)) + math.sqrt(z * (1-z)))
    raise ValueError(d)


def lens(d, t, steps=20000):
    c = math.sqrt(3) / 2
    lower = t / c
    if t >= c:
        return 0.0
    dx = (1-lower) / steps
    total = 0
    for j in range(steps):
        s = lower + (j + 0.5) * dx
        z = 4*(c*s-t)**2 / (1-s*s)
        total += (1-s*s)**((d-3)/2)*beta_cdf_z(z, d)
    return (math.gamma(d/2)/(math.sqrt(math.pi)*math.gamma((d-1)/2)))*total*dx


def main():
    for d in range(3, 11):
        n=d+1
        roots = [root(n,i,j) for i in range(n) for j in range(n) if i != j]
        assert len(roots)==n*(n-1)
        hist={}
        for u,v in itertools.combinations(roots,2):
            z=dot2(u,v)
            hist[z]=hist.get(z,0)+1
        assert hist[1]==n*(n-1)*(n-2)
        assert max(z for z in hist if z!=2)==1
        assert set(hist).issubset({-2,-1,0,1})
        # If a triple is eligible for overlapping caps at t >= sqrt(2/3),
        # its three centers must have pairwise dot 1/2, so its sum has norm sqrt(6).
        eligible=0
        for u,v,w in itertools.combinations(roots,3):
            if dot2(u,v)==dot2(v,w)==dot2(u,w)==1:
                eligible+=1
                summ=[u[i]+v[i]+w[i] for i in range(n)]
                assert sum(x*x for x in summ)==12 # normalized squared norm 6
        assert eligible==2*n*math.comb(n-1,3)
    print('ROOT_GRAM_COUNTS_AND_TRIPLE_THRESHOLD_PASSED')
    c=math.sqrt(3)/2
    for d in (3,4,5):
        b=8*kappa(d-2)/(d*d*kappa(d))*(4/math.sqrt(3))**((d-2)/2)
        for eps in (0.008,0.003):
            measured=lens(d,c-eps)
            ratio=measured/(b*eps**(d/2))
            assert abs(ratio-1)<0.035, (d,eps,ratio)
        assert lens(d,c)==0
    print('INDEPENDENT_SPHERICAL_LENS_AND_ONSET_COEFFICIENT_PASSED')
    print('ALL_CHECKS_PASSED')


if __name__=='__main__':
    main()
