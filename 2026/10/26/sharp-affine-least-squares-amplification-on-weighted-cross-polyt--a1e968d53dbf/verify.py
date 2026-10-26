#!/usr/bin/env python3
"""Exact quadratures and moment checks for affine projections on weighted cross-polytopes."""
from fractions import Fraction as Q
from math import comb
import sympy as sp
import mpmath as mp

checks = 0

def insist(ok, message):
    global checks
    if not ok:
        raise AssertionError(message)
    checks += 1


def formula_integer(m):
    c = Q((m+1)*(m+2), 2)
    return 1 + ((c-1)/(m+1)) * (1-1/c)**m


def polynomial_integral(m):
    """Integrate the independent polynomial expansion of the beta density."""
    c = Q((m+1)*(m+2), 2)
    lo = 1/c
    # Integrate m(cu-1)(1-u)^(m-1) from 1/c to 1 term by term.
    result = Q(0)
    for j in range(m):
        coeff = Q(m * (-1)**j * comb(m-1,j))
        result += coeff*(c*(1-lo**(j+2))/(j+2)-(1-lo**(j+1))/(j+1))
    return 1+result

for m in range(1,33):
    insist(polynomial_integral(m)==formula_integer(m), f'exact beta integral m={m}')
    # Beta(1,m) coordinate moments, integrated via factorial formula independently.
    for order in range(5):
        exact = Q(1)
        for k in range(1,order+1):
            exact *= Q(k,m+k)
        via_binomial = sum((Q(m*(-1)**j*comb(m-1,j), order+j+1) for j in range(m)),Q(0))
        insist(exact == via_binomial,f'moment m={m}, order={order}')

# Symbolically verify the positivity of a rigorous lower bound on the logarithmic derivative.
x=sp.symbols('x',positive=True)
a=x*(x+3)/((x+1)*(x+2))
log_deriv_except_log=1/x+1/(x+3)-1/(x+1)+x*sp.diff(sp.log(a),x)
lower_bound=sp.factor(log_deriv_except_log-2/(x*(x+3)))
insist(sp.simplify(lower_bound-(x*x+5*x+2)/(x*(x+2)*(x+3)))==0,'derivative lower bound')

# Independently evaluate the nonintegral beta integrals to 60 digits.
mp.mp.dps=65
for m in ['0.31','0.92','1.73','2.25','4.75','11.4','40.2']:
    mm=mp.mpf(m)
    c=(mm+1)*(mm+2)/2
    a=1-1/c
    f=(a**mm)*mp.quad(lambda v: (c-1)-c*a*(v**(1/mm)),[0,1])
    predicted=(c-1)/(mm+1)*(1-1/c)**mm
    insist(abs(f-predicted)<mp.mpf('1e-55'),f'noninteger beta integral m={m}')

# Check large-effective-dimension expansion, with a conservative bound.
for m in [100,250,500,1000]:
    mm=mp.mpf(m)
    c=(mm+1)*(mm+2)/2
    f=(c-1)/(mm+1)*(1-1/c)**mm
    err=abs(f-(mm/2+1/mm))
    insist(err < 5/mm**2, f'asymptotic m={m}')

print(f'PASS {checks} exact/symbolic/high-precision checks')
