"""Exact and numerical checks for a critical first-entry law in an affine interval map.

Requires Python 3 standard library only. Finite checks supplement, not replace,
the analytical proof of the asymptotic statements.
"""
from fractions import Fraction as Q
from math import exp, expm1, log

lam, b, c = Q(4, 5), Q(3, 4), Q(1, 4)
B, L = b-c, 1-b

for kappa in (Q(-2), Q(0), Q(1, 5)):
    for delta in (Q(1, 20), Q(1, 100)):
        s = 1+kappa*delta
        mu=s/lam
        a=b-lam*(c+delta)
        eta=(b-a)/lam
        assert eta == c+delta
        assert 0 < lam < 1 and 0 < c < b < 1
        assert (s <= 1 or (1-b)*mu <= 1-c)
        assert b-b*lam < a < b-c*lam
        assert (1-lam)*(c-mu*b) < (1-mu)*a
        gap = (1-s)*B+s*delta
        assert gap == b-(c+s*(b-eta)) and gap > 0

        def iterate(x):
            return lam*x+a if x < eta else s*(x-eta)+c

        for n in range(1, 13):
            threshold = gap * sum((s**(-j) for j in range(1,n)), Q(0))
            next_threshold = threshold+gap*s**(-n)
            for u in (Q(0), Q(1, 16), Q(1, 8), Q(3, 16)):
                x=b+u
                alive=True
                for j in range(n):
                    if x < b:
                        alive=False
                        break
                    x=iterate(x)
                assert alive == (u >= threshold), (kappa,delta,n,u)
            if next_threshold < L:
                width=next_threshold-threshold
                for q in (Q(0), Q(1, 4), Q(3, 4)):
                    x=b+threshold+q*width
                    for j in range(n):
                        assert x >= b
                        x=iterate(x)
                    assert x < b
                    assert (b-x)/gap == 1-q, (kappa,delta,n,q,(b-x)/gap)
    print('EXACT_SURVIVAL_AND_OVERSHOOT_OK', str(kappa))

b, c = float(b), float(c)
B, L = b-c, 1-b
for kappa in (-2., 0., .2):
    alpha=1-kappa*B
    T=log((1-kappa*B)/(1-kappa*(1-c)))/kappa if kappa else L
    H=lambda t: alpha*(-expm1(-kappa*t))/kappa if kappa else t
    assert abs(H(T)-L) < 1.e-13
    for delta in (.01,.002,.0005):
        s=1+kappa*delta
        gap=delta*(alpha+kappa*delta)
        for t in (.03,.08,.1):
            n=int(t/delta)
            h=gap*sum(s**(-j) for j in range(1,n+1))
            assert abs(h-H(n*delta)) < .2*delta, (kappa,delta,n,h,H(n*delta))
        # Pointwise discrete trajectory compared with the limiting linear flow.
        u=.2
        steps=int(.07/delta)
        z=u
        for j in range(steps):
            z=s*z-gap
        t=delta*steps
        ode=exp(kappa*t)*u-alpha*expm1(kappa*t)/kappa if kappa else u-t
        assert abs(z-ode) <= 1.0*delta, (kappa,delta,z,ode)
    print('CRITICAL_SCALING_CHECK_OK',kappa,'T=',T)
print('ALL_CHECKS_OK')
