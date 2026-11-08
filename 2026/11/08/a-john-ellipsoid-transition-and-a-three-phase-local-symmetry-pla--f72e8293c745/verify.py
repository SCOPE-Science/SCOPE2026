"""Independent finite checks for an analytic theorem on rotational frusta.

Run with Python 3.10 or later; no third-party packages are required.
The checks are finite regression tests, not a proof for all parameters.
"""
from fractions import Fraction as Q
from math import sqrt, log
from random import Random


def exact_parameters(d, r):
    assert d >= 2 and Q(0) <= r <= Q(1)
    k = 1-r
    critical = Q(d-1, d+1)
    b = Q(1, 2) if r >= critical else 1/(k*(d+1))
    a2 = 1-2*k*b
    symmetry = 1/(2-r)
    mink_height = 1/(3-r)
    john_height = b
    local_symmetry = min(b/(1-b), (1-k*b)/(1+k*b))
    r_equal = Q(d-2, d)
    if r <= r_equal:
        claimed_local = 1/(k*(d+1)-1)
    elif r <= critical:
        claimed_local = Q(d, d+2)
    else:
        claimed_local = (1+r)/(3-r)
    assert claimed_local == local_symmetry, (d, r, claimed_local, local_symmetry)
    assert (b == Q(1, 2)) == (r >= critical)
    assert a2 > 0
    assert Q(0) < symmetry <= Q(1)
    assert Q(0) < local_symmetry <= symmetry
    assert b <= Q(1,2)
    assert (Q(1) if r == 1 else Q(0)) + a2 >= 0
    return b, a2, symmetry, mink_height, local_symmetry


def numeric_objective(d, r, b):
    k=1-r
    if b <= 0 or b>0.5 or 1-2*k*b<=0:
        return float('-inf')
    return log(b)+(d-1)/2*log(1-2*k*b)


def run():
    tests=0
    rng=Random(23117)
    for d in range(2,14):
        thresholds = {Q(0),Q(1),Q(d-2,d),Q(d-1,d+1)}
        thresholds.update(Q(j, 60) for j in range(61))
        for r in sorted(thresholds):
            b, a2, sym, s_m, loc=exact_parameters(d,r)
            k=1-r
            assert b-k*b*b >= 0
            assert 1-2*k*b == a2
            assert (k*b+sqrt(float(a2 + k*k*b*b))-1) < 1e-13
            assert b <= Q(1,2)
            assert s_m == sym/(1+sym)
            assert loc <= sym
            # The concave log-volume objective must not improve on a fine
            # independent grid of admissible axial semiaxes.
            best = numeric_objective(d,float(r),float(b))
            for j in range(1,1202):
                beta=j/2404
                value=numeric_objective(d,float(r),beta)
                assert value<=best+1e-11,(d,r,b,beta,value,best)
                tests+=1
            # Sample the boundary of the candidate ellipsoid in 2D
            # radial-axial coordinates. Every rotational copy is covered.
            a=sqrt(float(a2))
            beta=float(b)
            for _ in range(110):
                theta=rng.random()*6.283185307179586
                t=beta*(1+__import__('math').cos(theta))
                radial=a*abs(__import__('math').sin(theta))
                assert -1e-12<=t<=1+1e-12
                assert radial+float(k)*t<=1+1e-12
                tests+=1
    # Target the exact coincidence and phase boundaries, which can be
    # missed by a uniform discretization.
    for d in range(2,51):
        r_eq=Q(d-2,d)
        r_critical=Q(d-1,d+1)
        assert r_eq<r_critical
        for r in (r_eq,r_critical,Q(1)):
            b,a2,sym,sm,loc=exact_parameters(d,r)
            assert (b == sm) == (r==r_eq or r==1)
            tests+=1
    print('VERIFY_OK', 'checks', tests)


if __name__=='__main__':
    run()
