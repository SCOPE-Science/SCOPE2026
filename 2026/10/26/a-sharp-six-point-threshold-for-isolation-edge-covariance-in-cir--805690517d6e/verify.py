"""Reproduce finite exact identities and representative simulations for a circular geometric graph.
Run with Python 3 standard library: python verify.py
"""
from fractions import Fraction as F
from math import comb, sqrt
from random import Random


def conditional_edge_probability(r):
    r = F(r)
    assert 0 < r < F(1, 2)
    ell = 1 - 2*r
    if r >= ell:
        return F(1)
    return 1 - (1-r/ell)**2


def covariance_conditioning(n, r):
    r = F(r)
    ell = 1 - 2*r
    chance_iso = ell**(n-1)
    expected_edges_cond_iso = F(comb(n-1, 2))*conditional_edge_probability(r)
    expected_edges = F(n*(n-1))*r
    return n*chance_iso*(expected_edges_cond_iso-expected_edges)


def covariance_piecewise(n, r):
    r = F(r)
    ell = 1 - 2*r
    if 3*r < 1:
        return F(n*(n-1), 2)*r*ell**(n-3)*(-4+(3*n+10)*r-8*n*r*r)
    return F(n*(n-1), 2)*ell**(n-1)*(n-2-2*n*r)


def sign_classification(n, r):
    r = float(r)
    if n <= 5:
        return -1
    root_low = (3*n+10 - sqrt(9*n*n-68*n+100))/(16*n)
    root_high = (n-2)/(2*n)
    return 1 if root_low < r < root_high else -1


def run_checks():
    count = 0
    for n in range(2, 51):
        for i in range(1, 60):
            r = F(i, 120)
            a = covariance_conditioning(n, r)
            b = covariance_piecewise(n, r)
            assert a == b, (n, r, a, b)
            count += 1
            # Floating-point sign comparisons away from roots.
            root_low = (3*n+10-sqrt(max(0,9*n*n-68*n+100)))/(16*n) if n >= 6 else -1
            root_high = (n-2)/(2*n) if n >= 6 else -1
            if n < 6 or min(abs(float(r)-root_low),abs(float(r)-root_high)) > 1e-9:
                assert (1 if a > 0 else -1) == sign_classification(n, r)
                count += 1
    # Boundary and exact exceptional six-vertex roots.
    assert covariance_conditioning(6, F(1,4)) == 0
    assert covariance_conditioning(6, F(1,3)) == 0
    assert covariance_conditioning(5, F(1,3)) < 0
    assert covariance_conditioning(7, F(1,3)) > 0
    count += 4
    # A direct numerical experiment with independently sampled point configurations.
    rng = Random(20261023)
    samples = 120000
    simulations = []
    for n,r in [(5,F(3,10)),(6,F(1,5)),(6,F(7,25)),(6,F(17,50)),(7,F(3,10)),(7,F(2,5))]:
        rr = float(r)
        si=se=sie=0
        for _ in range(samples):
            points = [rng.random() for j in range(n)]
            degrees = [0]*n
            e=0
            for u in range(n):
                for v in range(u+1,n):
                    d=abs(points[u]-points[v])
                    if min(d,1-d) < rr:
                        e += 1
                        degrees[u] += 1
                        degrees[v] += 1
            iso = sum(d==0 for d in degrees)
            si+=iso;se+=e;sie+=iso*e
        empirical = sie/samples-si*se/(samples*samples)
        exact = float(covariance_piecewise(n,r))
        assert abs(empirical-exact) < 0.075, (n,r,empirical,exact)
        simulations.append((n,str(r),round(empirical,5),round(exact,5)))
        count += 1
    print('PASS',count,'exact algebra/sign and numerical corroboration checks')
    for sample in simulations:
        print('n,r,empirical,exact',*sample)
    print('Simulation is a consistency check, not a proof. Infinite-family sign claims follow from conditional expectation and quadratic signs.')


if __name__ == '__main__':
    run_checks()
