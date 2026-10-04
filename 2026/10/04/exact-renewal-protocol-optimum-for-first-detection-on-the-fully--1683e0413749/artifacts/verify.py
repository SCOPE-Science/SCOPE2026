#!/usr/bin/env python3
import cmath
import math


def bisect_root():
    lo = math.pi/2
    hi = math.pi - 1e-12
    def h(x):
        return math.tan(x/2)-x
    for _ in range(120):
        mid=(lo+hi)/2
        if h(mid)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def direct_check(N,m,J,tau):
    omega=N*J
    z=cmath.exp(1j*omega*tau)-1
    # b has amplitude 1/sqrt(m) on the first m sites.
    b=[(1/math.sqrt(m) if x<m else 0j) for x in range(N)]
    # U b = b + z <u,b> u; <u,b>=sqrt(m/N).
    add=z*math.sqrt(m)/N
    ub=[b[x]+add for x in range(N)]
    p=sum(abs(ub[x])**2 for x in range(m,N))
    expected=4*m*(N-m)/N**2 * math.sin(omega*tau/2)**2
    assert abs(p-expected)<2e-12
    # Failed amplitudes must be a common scalar times b.
    scalar=1+(m/N)*z
    for x in range(m):
        assert abs(ub[x]-scalar*b[x])<2e-12


def renewal_grid_check(kappa):
    # Deterministic set of positive finite-support laws in dimensionless X.
    grids=[
        ([0.2,1.1],[0.3,0.7]),
        ([0.0,2.3311223704144226],[0.4,0.6]),
        ([0.7,2.2,5.0],[0.2,0.5,0.3]),
        ([1.0,math.pi,9.0],[0.1,0.8,0.1]),
        ([2.3311223704144226],[1.0]),
    ]
    for xs,ps in grids:
        ex=sum(p*x for p,x in zip(ps,xs))
        ey=sum(p*(1-math.cos(x)) for p,x in zip(ps,xs))
        assert ey <= kappa*ex + 2e-12


def main():
    x=bisect_root()
    kappa=math.sin(x)
    assert abs(x-2.3311223704144226)<2e-14
    assert abs(kappa-(1-math.cos(x))/x)<2e-14
    assert 2/math.pi < kappa
    assert abs(1/(2*kappa)-0.6900250698446505)<2e-14
    for vals in [(2,1,1.0,0.37),(5,2,0.7,0.41),(8,3,1.3,0.19),(11,7,0.4,0.83)]:
        direct_check(*vals)
    renewal_grid_check(kappa)
    # Exact Poisson optimization in y=r/omega: y+1/y >= 2.
    for y in [0.1,0.5,1.0,2.0,10.0]:
        assert y+1/y >= 2-1e-15
    print('x_star=%.15f' % x)
    print('sin_x_star=%.15f' % kappa)
    print('renewal_to_best_poisson=%.15f' % (1/(2*kappa)))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
