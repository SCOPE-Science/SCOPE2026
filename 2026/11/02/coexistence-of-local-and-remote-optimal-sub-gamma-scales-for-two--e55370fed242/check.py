"""Reproducible arithmetic checks for two-point sub-gamma coexistence."""
from fractions import Fraction as Q
from math import factorial, exp

q = Q(1, 10000)
m = lambda p: (1 + 124*p)/(3*(1 + 24*p))
local_numerator = lambda p: 16576*p*p - 952*p + 1
assert local_numerator(q) > 0
assert local_numerator(0) > local_numerator(q)
assert Q(1, 3) <= m(q) < Q(1, 2)
assert all(Q(2, factorial(n+2)) <= Q(1,3)**n for n in range(0, 40))
assert all(Q(2, factorial(n+2)) < Q(1,3)**n for n in range(2, 40))
# The coefficient induction uses 1/(n+3)<1/3 for all n>=1.
assert sum((Q(2)**n)/factorial(n) for n in range(6)) > 7
assert sum((Q(10)**n)/factorial(n) for n in range(22)) > 22000
M_lower = Q(61985, 20048)
threshold = 1/(1-2*m(q))
assert M_lower > threshold
p=float(q)
M2 = ((1-p)*(exp(2)-3)+p*(exp(10)-11))/(2*(1+24*p))
psi2 = (1-1/M2)/2
assert psi2 > float(m(q))
# Numerical illustrations only; no search grid is used as a proof of existence.
print('arithmetic and finite-series checks passed')
print('p:', str(q), 'local numerator:', str(local_numerator(q)))
print('m(p):', str(m(q)), 'rational M(2) lower:', str(M_lower))
print('required M(2) threshold:', str(threshold))
print('illustrative Phi_p(2):', format(psi2, '.15f'))
