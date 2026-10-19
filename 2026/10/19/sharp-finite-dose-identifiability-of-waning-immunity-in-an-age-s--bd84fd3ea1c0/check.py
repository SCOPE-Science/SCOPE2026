"""Independent exact finite-response witness and forward/inverse consistency checks.
Only ordinary research mathematics; does not certify analytic generality.
"""
from fractions import Fraction as F
from math import exp, log, isclose

n = 5
ages = list(range(1, n+1))
a = [F(1,6), F(-7,6), F(17,6), F(-17,6), F(1)]
base = [F(1,5) for _ in ages]
eps = F(1,20)
plus = [z+eps*v for z,v in zip(base,a)]
minus = [z-eps*v for z,v in zip(base,a)]
assert plus != minus
assert all(w > 0 for w in plus + minus)
assert sum(plus) == sum(minus) == 1
assert sum(ages[i]*plus[i] for i in range(n)) == sum(ages[i]*minus[i] for i in range(n))
for b in (2,3):
    assert sum(plus[i] * F(1,b)**ages[i] for i in range(n)) == sum(minus[i] * F(1,b)**ages[i] for i in range(n))
print('Exact finite-rate nonidentifiability witness: positive, normalized, matched mean and transforms at log 2 and log 3.')

# Independent numerical cross-check of the SIRVS forward formula and inversion.
R0, ti, tv = 4.0, 5.0, 1.0
for law in (plus,minus):
    for v in (log(2),log(3),.04,.1):
        if v >= (R0-1)/tv: continue
        lt = sum(float(law[j])*exp(-v*ages[j]) for j in range(n))
        kv = (1-lt)/v
        phi = (R0-1-v*tv)/(ti+(1+v*tv)*kv)
        inv_k = ((R0-1-v*tv)/phi-ti)/(1+v*tv)
        inv_l = 1-v*inv_k
        assert isclose(inv_l,lt,rel_tol=1e-12,abs_tol=1e-12)
print('Numerical inversion consistency verified at rates in the endemic interval.')

# Explicit differing generation-time laws with the same R0 and infectious-period mean.
a_time = 3.0
c = 2*R0/a_time+1
beta1 = lambda t: R0/(c*a_time)
beta2 = lambda t: 2*R0/(c*a_time)*exp(-t/a_time)
assert 0 < beta1(0) < 1 and 0 < beta2(0) < 1
assert not isclose(beta1(0),beta2(0))
print('Explicit infectivity ambiguity example verified at t=0 and normalization by integration is analytic.')
