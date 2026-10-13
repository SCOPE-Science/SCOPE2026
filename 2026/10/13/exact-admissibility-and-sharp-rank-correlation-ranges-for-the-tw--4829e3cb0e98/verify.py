#!/usr/bin/env python3
"""Independent finite algebra and numerical checks for a two-mode polynomial copula.

This uses Python's standard library only. The continuum positivity argument
is in RESULT.md; finite checks are consistency tests, not a substitute.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random


def poly(*terms):
    return {i: F(v) for i, v in enumerate(terms) if v}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def mult(a, b):
    out = {}
    for (i, j), v in a.items():
        for (k, l), w in b.items():
            out[(i + k, j + l)] = out.get((i + k, j + l), F(0)) + v * w
    return out


def scale(a, r):
    return {k: v * r for k, v in a.items() if v * r}


def tensor(a, b):
    return {(i, j): v*w for i, v in a.items() for j, w in b.items() if v*w}


def d_uv(a):
    return {(i-1, j-1): F(i*j)*v for (i, j), v in a.items() if i and j}


def integrate(a):
    return sum((v/F((i+1)*(j+1)) for (i, j), v in a.items()), F(0))

U = poly(0, 1)
F1 = poly(0, 1, -1)
F2 = poly(0, 1, -3, 2)


def C(l1, l2):
    return add(add(tensor(U, U), scale(tensor(F1, F1), 3*l1)),
               scale(tensor(F2, F2), 5*l2))


def coefficients(l1, l2):
    cp = C(l1, l2)
    density = d_uv(cp)
    rho = 12 * integrate(cp) - 3
    tau = 4 * integrate(mult(cp, density)) - 1
    return rho, tau

# A quadratic polynomial in two parameters is determined by these six nodes.
nodes = [(F(0),F(0)), (F(1),F(0)), (F(-1),F(0)),
         (F(0),F(1)), (F(0),F(-1)), (F(1),F(1))]
for l1, l2 in nodes:
    rho, tau = coefficients(l1,l2)
    assert rho == l1, (l1,l2,rho)
    assert tau == F(2,3)*l1*(1+l2/F(5)), (l1,l2,tau)
print('PASS: six-point exact polynomial identification of Spearman and Kendall formulas.')

# Exact integration of Legendre factors and correct unit marginals for representative parameters.
x=poly(-1,2)  # 2u-1
p2=poly(1,-6,6)
assert sum((v/F(i+1) for i,v in x.items()), F(0))==0
assert sum((v/F(i+1) for i,v in p2.items()), F(0))==0
for l1,l2 in [(F(0),F(0)),(F(1,3),F(0)),(F(0),F(2,5)),(F(-1,5),F(1,10))]:
    dens=d_uv(C(l1,l2))
    assert integrate(dens)==F(1)
    assert dens==add(add({(0,0):F(1)},scale(tensor(x,x),3*l1)),scale(tensor(p2,p2),5*l2))
print('PASS: exact mixed derivative and unit marginal polynomials.')


def P2(t):
    return (3*t*t-1)/2


def c(a,b,x,y):
    return 1+a*x*y+b*P2(x)*P2(y)


def h(b):
    return (1+b) if b<=0.5 else sqrt(3*b*(2-b))

# Numerical probes for continuum theorem; perturbing above boundary should break positivity.
rng=Random(20261009)
checks=0
for k in range(0, 151):
    b=-1+3*k/150
    a=h(b)
    for j in range(110):
        x=rng.uniform(-1,1)
        y=rng.uniform(-1,1)
        assert c(a,b,x,y) >= -2e-12, (a,b,x,y,c(a,b,x,y))
        assert c(-a,b,x,y) >= -2e-12
        checks+=2
    if b<=0.5:
        assert c(a+0.003,b,1,-1) < 0
    elif b<2:
        w=sqrt((2-b)/(3*b))
        assert c(a+0.003,b,1,-w) < 0
    else:
        assert c(0.003,b,1,-0.0001)<0
    checks+=1
print(f'PASS: {checks} deterministic positivity/optimality probes across all parameter regimes.')

bstar=(sqrt(171)-11)/2
assert 0.5 < bstar < 2
assert abs(25-22*bstar-2*bstar**2)<1e-11
rhomax=sqrt(3)/3
taumax=2/9*h(bstar)*(1+bstar/25)
assert isclose(taumax,0.40059171855462555,abs_tol=1e-14)
assert isclose(rhomax,0.5773502691896257,abs_tol=1e-14)
print(f'PASS: exact-form critical point and endpoint scales; rho_max={rhomax:.15f}, tau_max={taumax:.15f}.')
print('VERIFICATION_OK')
