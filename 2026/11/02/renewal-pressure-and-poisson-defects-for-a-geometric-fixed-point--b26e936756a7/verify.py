"""Finite numerical diagnostics for geometric-distance full-shift renewal equations.
Infinite-time and zero-temperature conclusions require the independent analytic proof.
"""
import math


def root_scaled(beta, theta):
    limit = 1 / (1 - theta)
    b = math.exp(-beta * limit)
    delta = [b * math.expm1(beta * theta**r/(1-theta)) for r in range(1,501)]
    def scaled_eq(k):
        p=b*k
        # k can be found without subtracting nearly equal exponentials.
        geom = (1 / k) * (p / math.expm1(p))
        return geom + sum(d * math.exp(-r*p) for r,d in enumerate(delta,1))-1
    lo, hi = .5, 2.0
    assert scaled_eq(lo)>0 and scaled_eq(hi)<0
    for _ in range(65):
        mid=(lo+hi)/2
        if scaled_eq(mid)>0: lo=mid
        else: hi=mid
    k=(lo+hi)/2
    return b,k,abs(scaled_eq(k))

for theta in (.25,.5,.75):
    for beta in (4,8,12,16):
        b,k,res=root_scaled(beta,theta)
        assert b>0 and 1<k<2 and res<1e-12
        first=(k-1)/math.exp(-beta)
        second=(k-1-math.exp(-beta))/math.exp(-beta*(1+theta))
        print('PRESSURE_ROOT_PASS',f'theta={theta}',f'beta={beta}',
              f'P_over_B={k:.13g}',f'first_scaled={first:.9g}',
              f'second_scaled={second:.9g}',f'residual={res:.2g}')
    for r in range(1,12):
        energy=1+sum(theta**(r-k) for k in range(1,r))
        assert abs(energy-(1-theta**r)/(1-theta))<1e-11
    print('EXCURSION_ENERGY_IDENTITY_PASS',f'theta={theta}')
print('ASYMPTOTIC_EXPANSIONS_AND_POISSON_LIMIT_REQUIRE_ANALYTIC_PROOF')
