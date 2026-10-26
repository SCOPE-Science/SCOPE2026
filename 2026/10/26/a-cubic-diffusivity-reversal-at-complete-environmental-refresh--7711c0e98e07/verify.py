"""Exact symbolic check of four-step annealed path moments and cubic refresh expansion.

Requires SymPy >=1.12. Run: python verify.py
"""
from functools import lru_cache
from itertools import product
from collections import defaultdict
import sympy as sp

mu, q, d = sp.symbols('mu q d')
z = sp.symbols('z')

@lru_cache(None)
def site_weight(local_steps):
    f = sp.Poly(1, z)
    for direction in local_steps:
        f *= sp.Poly((1 + direction*z)/2, z)
    result = 0
    for (degree,), coefficient in f.terms():
        if degree == 0:
            moment = 1
        elif degree == 1:
            moment = mu
        elif degree == 2:
            moment = q
        else:
            raise AssertionError('More than two departures from one site')
        result += coefficient * moment
    return sp.expand(result)


def annealed_probability(path):
    departures = defaultdict(list)
    location = 0
    for step in path:
        departures[location].append(step)
        location += step
    result = 1
    for directions in departures.values():
        result *= site_weight(tuple(directions))
    return sp.expand(result)

mean, second = {}, {}
for n in range(1, 5):
    mean[n] = 0
    second[n] = 0
    total = 0
    for path in product((-1, 1), repeat=n):
        probability = annealed_probability(path)
        location = sum(path)
        mean[n] += location * probability
        second[n] += location**2 * probability
        total += probability
    assert sp.simplify(total - 1) == 0
    mean[n] = sp.factor(mean[n])
    second[n] = sp.factor(second[n])

w = q - mu**2
expected_mean = {
    1: mu,
    2: 2*mu,
    3: 3*mu - mu*w/2,
    4: 4*mu - mu*w,
}
expected_second = {
    1: 1,
    2: 2 + 2*mu**2,
    3: 3 + 6*mu**2,
    4: 4 + 12*mu**2 - 2*mu**2*w - w**2/2,
}
for n in range(1, 5):
    assert sp.simplify(mean[n] - expected_mean[n]) == 0
    assert sp.simplify(second[n] - expected_second[n]) == 0

p = 1-d
# Terms for n >= 5 have order d^4 or smaller in the speed and diffusivity.
v = sp.series(p**2*sum(mean[n]*d**(n-1) for n in range(1,5)),d,0,4).removeO()
assert sp.simplify(sp.expand(v).coeff(d, 0) - mu) == 0
assert sp.simplify(sp.expand(v).coeff(d, 1)) == 0
assert sp.simplify(sp.expand(v).coeff(d, 2) + mu*w/2) == 0
assert sp.simplify(sp.expand(v).coeff(d, 3)) == 0

D = sp.series(p**2*sum(
    (second[n]-2*n*mean[n]*v+n*n*v*v)*d**(n-1)
    for n in range(1,5)
),d,0,4).removeO().expand()
assert sp.simplify(D.coeff(d,0)-(1-mu**2)) == 0
assert sp.simplify(D.coeff(d,1)) == 0
assert sp.simplify(D.coeff(d,2)-3*mu**2*w) == 0
assert sp.simplify(D.coeff(d,3)+w**2/2) == 0
print('PASS: four-step path probabilities, moments, and cubic Taylor coefficients')

# Fully deterministic, two-cycle fair-arrow environment. Derive its
# displacement second-moment generating function from the first opposing arrow.
r = sp.symbols('r')
F = (1+r/2)**2 / ((1-r/2)**2*(1-r**2))
first_part = (1+r/2)/(1-r/2)**3
second_part = 3*r**2*(1+r/2)/(4*(1-r/2)**3*(1-r**2))
assert sp.simplify(F-first_part-second_part) == 0
for n in range(1,5):
    coef = sp.series(F,r,0,n).removeO().expand().coeff(r,n-1)
    assert sp.simplify(coef - second[n].subs({mu:0,q:1})) == 0
D_arrow = (1-r)**2*F
assert sp.simplify(D_arrow - (1-r)*(2+r)**2/((1+r)*(2-r)**2)) == 0
assert sp.simplify((1-D_arrow) - 2*r**3/((2-r)**2*(1+r))) == 0
assert sp.simplify(sp.series(D_arrow,r,0,4).removeO()-(1-r**3/2)) == 0
print('PASS: exact fair-arrow generating function and all-refresh diffusivity')
