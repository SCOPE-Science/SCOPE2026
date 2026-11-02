"""Finite checks for the logarithmic-colour lattice law. Standard library only."""
from math import comb, exp, floor, lgamma, log, sqrt, pi


def centre(n, a):
    lo, hi = 0.0, 1.0
    while hi * exp(2*a*hi) < n:
        hi *= 2
    for _ in range(90):
        mid = (lo+hi)/2
        if mid * exp(2*a*mid) < n:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def finite_law(n, a):
    vals = [lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)-a*k*k for k in range(n+1)]
    s = max(vals)
    mass = [exp(v-s) for v in vals]
    z = sum(mass)
    return [v/z for v in mass], s+log(z)


def phase_approx(n, a):
    x=centre(n, a)
    h=floor(x)
    th=x-h
    theta=sum(exp(-a*(j-th)**2) for j in range(-180, 181))
    law=[exp(-a*((k-h)-th)**2)/theta for k in range(n+1)]
    lz=a*x*x+x-0.5*log(2*pi*x)+log(theta)
    return law, lz, x


def exact_graph_hist(n):
    """Integer weights 3^number_of_true_R_edges_not_both_P, loops included."""
    h=[0]*(n+1)
    for P in range(1<<n):
        m=P.bit_count()
        for R in range(1<<(n*n)):
            count=0
            for i in range(n):
                for j in range(n):
                    if (R>>(i*n+j))&1 and not ((P>>i)&1 and (P>>j)&1):
                        count+=1
            h[m]+=3**count
    return h


for n in (1, 2, 3):
    hist=exact_graph_hist(n)
    # Divide by the universal factor 4^(n*n), then compare exactly.
    assert all(hist[m]*(2**(m*m)) == (4**(n*n))*comb(n,m)
               for m in range(n+1)), (n,hist)
    print('EXACT_RAW_NETWORK', n, hist)

for a in (log(2), 0.24, 2.0):
    previous = None
    for n in (100, 1000, 10000, 100000):
        p, true_lz=finite_law(n,a)
        q, approx_lz, x=phase_approx(n,a)
        tv=0.5*sum(abs(u-v) for u,v in zip(p,q))
        assert tv < 0.1
        assert abs(true_lz-approx_lz) < 0.8
        if previous is not None:
            assert tv < previous+0.02
        previous=tv
        print('FINITE_COMPARE', 'a=',round(a,5),'n=',n,
              'saddle=',round(x,6),'TV=',round(tv,6),
              'partition_log_error=',round(true_lz-approx_lz,6))

print('ALL_CHECKS_OK')
