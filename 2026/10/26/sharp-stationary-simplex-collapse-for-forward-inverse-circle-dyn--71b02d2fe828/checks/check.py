"""Exact finite-truncation checks for a forward and inverse expanding-map kernel.
These checks are diagnostics, not a proof of the infinite stationary classification.
"""
from collections import defaultdict
from fractions import Fraction as F


def clean(v):
    return {x: mass for x, mass in v.items() if mass}


def plus(*pairs):
    z = defaultdict(F)
    for weight, measure in pairs:
        for x, val in measure.items():
            z[x] += weight * val
    return clean(z)


def forward(v, b):
    z = defaultdict(F)
    for x, mass in v.items():
        z[(b*x) % 1] += mass
    return clean(z)


def inverse(v, b):
    z = defaultdict(F)
    for x, mass in v.items():
        for k in range(b):
            z[(x+k)/b] += mass / b
    return clean(z)


def cycle(b, period):
    x = F(1, b**period-1) % 1
    xs = []
    y = x
    while y not in xs:
        xs.append(y)
        y = (b*y) % 1
    assert y == x
    return {t: F(1,len(xs)) for t in xs}


def truncated(rho, b, r, n):
    x = rho
    res = {}
    for j in range(n+1):
        res = plus((F(1),res), ((1-r)*r**j,x))
        x = inverse(x,b)
    return res


def verify():
    cases=0
    points=0
    for b in range(2,6):
        for period in (1,2,3):
            rho=cycle(b,period)
            assert forward(rho,b)==rho
            for r in (F(0), F(1,5), F(1,2), F(3,4)):
                for n in range(0,5):
                    nu=truncated(rho,b,r,n)
                    # (1+r)nu - Fnu - r Qnu is precisely the series tail boundary.
                    residual=plus((1+r,nu),(-1,forward(nu,b)),(-r,inverse(nu,b)))
                    qn=rho
                    for j in range(n):
                        qn=inverse(qn,b)
                    predicted=plus(((1-r)*r**(n+1),qn), (-(1-r)*r**(n+1),inverse(qn,b)))
                    assert residual==predicted, (b,period,r,n)
                    assert sum(nu.values()) == 1-r**(n+1)
                    # Exponential tail is an exact signed-mass error bound.
                    assert sum(abs(x) for x in residual.values()) <= 2*(1-r)*r**(n+1)
                    cases+=1
                    points+=len(nu)
    for b in range(2,11):
        q={F(0):F(1)}
        for j in range(5):
            assert len(q)==b**j
            assert set(q.values())=={F(1,b**j)}
            assert sum(q.values())==1
            assert sum(q.keys())==F(b**j-1,2)
            # First Fourier character cancels for every nontrivial inverse grid.
            if j:
                assert sum(1 for _ in q)==b**j
            q=inverse(q,b)
    print('EXACT_STATIONARY_TRUNCATION_AND_RESIDUAL_PASS',cases)
    print('EXACT_PREIMAGE_GRID_FORMULA_PASS',9*5)
    print('FULL_MEASURE_TRICHOTOMY_AND_WASSERSTEIN_BOUNDS_REQUIRE_ANALYTIC_PROOF')


if __name__=='__main__':
    verify()
