#!/usr/bin/env python3
"""Exact beta-integral and Irwin--Hall cross-checks for affine projectors."""
from fractions import Fraction as Q
from math import comb, factorial, sqrt, pi
import numpy as np


def diamond_formula(d):
    a = Q(2, (d + 1) * (d + 2))
    return 1 + Q(d + 2, 2) * (1 - a) ** (d + 1)


def diamond_expanded_integral(d):
    alpha = Q((d + 1) * (d + 2), 2)
    a = 1 / alpha
    # d * integral_{a}^{1} (alpha*t-1)(1-t)^{d-1}dt
    return 1 + d * sum(((-1)**k) * comb(d-1,k) *
                       (alpha * (1 - a**(k+2)) / Q(k+2)
                        - (1-a**(k+1)) / Q(k+1))
                       for k in range(d))


def cube_formula(d):
    b = Q(3*d-1,6)
    return 1 + Q(12, factorial(d+1)) * sum(
        (-1)**k * comb(d,k) * (b-k)**(d+1)
        for k in range(int(b)+1))


def cube_independent_tail_integral(d):
    # Irwin-Hall density of T=sum of d U[0,1], integrated against
    # (6*T-3*d-1)_+ using its piecewise polynomial density.
    a = Q(3*d+1,6)
    total = Q(0)
    for j in range(d):
        lo=max(a,Q(j)); hi=Q(j+1)
        if lo>=hi: continue
        # f_d(t)=1/(d-1)! sum_{k=0}^j (-1)^k*C(d,k)*(t-k)^(d-1)
        for k in range(j+1):
            s=(-1)**k * comb(d,k)
            # integral_lo^hi (6t-3d-1)(t-k)^(d-1)dt
            def ant(t):
                z=t-k
                return 6*z**(d+1)/Q(d+1)+(6*k-3*d-1)*z**d/Q(d)
            total += Q(s, factorial(d-1)) * (ant(hi)-ant(lo))
    return 1 + 2*total

count=0
for d in range(1,41):
    assert diamond_formula(d)==diamond_expanded_integral(d),('diamond',d)
    assert Q(2,(d+1)*(d+2)) == d * Q(factorial(2)*factorial(d-1), factorial(d+2)),('variance',d)
    count+=2
for d in range(1,19):
    assert cube_formula(d)==cube_independent_tail_integral(d),('cube',d)
    count+=1
assert diamond_formula(1)==cube_formula(1)==Q(5,3)
assert diamond_formula(2)==cube_formula(2)==Q(233,108)
assert diamond_formula(3)==Q(10561,4000)
assert cube_formula(3)==Q(415,162)
count+=4
# Two independent simulators: a Dirichlet-exponential sampler for crosspolytope
# and direct uniform cube sampling. Noncertifying sanity check.
rng=np.random.default_rng(41730)
for d in (1,2,3,4,7,12):
    nn=250_000
    E=rng.exponential(size=(nn,d+1))
    sigma=rng.choice([-1,1], size=nn)
    t=(E[:,0] / E.sum(axis=1))*sigma
    a=(d+1)*(d+2)/2
    obs=np.abs(1+a*t).mean()
    pred=float(diamond_formula(d))
    assert abs(obs-pred)<0.04,('diamond MC',d,obs,pred)
    U=rng.uniform(-1,1,size=(nn,d))
    obs=np.abs(1+3*U.sum(axis=1)).mean()
    pred=float(cube_formula(d))
    assert abs(obs-pred)<0.04,('cube MC',d,obs,pred)
    count+=2
print('PASS',count,'checks; exact arithmetic 102; numerical simulation 12')
print('d=3: crosspolytope',diamond_formula(3),'cube',cube_formula(3))
print('asymptotic: crosspolytope/d -> 1/2; cube/sqrt(d) ->',sqrt(6/pi))
