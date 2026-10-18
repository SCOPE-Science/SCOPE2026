"""Reproduce finite-population checks for a near-balanced Brownian exit race.

Uses only Python's standard library.  The exact image expansion is evaluated
in the short-time integration window; omitted image contributions are
exponentially small there.  Finite calculations illustrate, but do not prove,
the infinite-population theorem.
"""
import math


def exit_components(y, L, distance):
    """First-passage CDF and positive first-exit density in y=b/t, b=d_left^2/(4D)."""
    total_cdf, total_flux = 0.0, 0.0
    for k in range(4):
        a, b = distance + 2*k*L, (2*k+2)*L-distance
        total_cdf += math.erfc(a*math.sqrt(y))-math.erfc(b*math.sqrt(y))
        total_flux += a*math.exp(-a*a*y)-b*math.exp(-b*b*y)
    return total_cdf, total_flux/math.sqrt(math.pi*y)


def simpson(f, x0, x1, slices=12000):
    assert slices % 2 == 0
    h = (x1-x0)/slices
    accum = f(x0)+f(x1)
    for k in range(1, slices):
        accum += (4 if k%2 else 2)*f(x0+k*h)
    return accum*h/3


def finite_population(N, theta):
    logn = math.log(N)
    L=2.0+theta/logn
    assert L>1.0
    def p_integrand(y):
        fl,jl=exit_components(y,L,1.0)
        fr,_=exit_components(y,L,L-1.0)
        return N*jl*max(0.0,1-fl-fr)**(N-1)
    p=simpson(p_integrand,max(1.0,logn/5),logn+24)
    center=logn-.5*math.log(logn)-.5*math.log(math.pi)
    def cdf_at(y):
        yy=center+y
        fl,_=exit_components(yy,L,1.0)
        fr,_=exit_components(yy,L,L-1.0)
        return (1-fl-fr)**N
    return p,[cdf_at(y) for y in [-1,0,1]]


if __name__=='__main__':
    # Check image-series Laplace transforms against the exact Dirichlet forms.
    for L, d, D, s in [(2.4,1.0,0.8,0.6), (1.7,0.5,1.3,1.0), (3.0,1.7,0.35,0.8)]:
        kappa = math.sqrt(s/D)
        target = math.sinh((L-d)*kappa)/math.sinh(L*kappa)
        reset = math.sinh(d*kappa)/math.sinh(L*kappa)
        il = sum(math.exp(-(d+2*j*L)*kappa)-math.exp(-(2*L-d+2*j*L)*kappa) for j in range(25))
        ir = sum(math.exp(-(L-d+2*j*L)*kappa)-math.exp(-(L+d+2*j*L)*kappa) for j in range(25))
        assert abs(target-il)<1e-11 and abs(reset-ir)<1e-11
    print('Laplace-image consistency checks: 3 parameter sets PASS')
    for theta in [-1.0,0.0,1.0]:
        q = math.exp(-2.0*theta)
        p_limit = 1.0/(1.0+q)
        gumbel_limit=[math.exp(-(1+q)*math.exp(-y)) for y in [-1,0,1]]
        print(f'theta={theta:+.1f}: limiting target probability={p_limit:.9f}, Gumbel CDF={[round(v,7) for v in gumbel_limit]}')
        for N in [10**3,10**4,10**5,10**6]:
            p,cdf=finite_population(N,theta)
            print(f'  N={N:>7d} target={p:.9f} Gumbel CDF={[round(v,7) for v in cdf]}')
            assert math.isfinite(p) and 0<p<1
            assert all(0<=v<=1 for v in cdf)
            assert cdf[0]<cdf[1]<cdf[2]
            if theta==0.0:
                assert abs(p-0.5)<2e-7
    print('FINITE CHECKS PASS; no inference of infinite limits from numerics.')
