"""Reproduce analytic stationary identities and certified finite-truncation bounds.

The equilibrium model is the discrete-time Poisson-arrival, unit-service
wealth recursion. This verifies algebraic identities numerically; the
infinite-state assertions require the analytical proof.
"""
from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 100
D = Decimal
lam = D(2) - D(2).sqrt()
p0 = D(1) - lam
ex = lam.exp()
assert abs(lam + lam * lam / (2 * p0) - D(1)) < D('1e-96')
assert abs(p0 - (D(2).sqrt() - 1)) < D('1e-96')

# Exact differentiation of the probability generating function at one.
u = lam * lam / (2 * p0)
variance = D(1) + u*u + lam**3/(3*p0)
assert abs(variance - D(4)/3) < D('1e-95')

# Recursively extract the first 46 stationary coefficients from the
# transition equation, without iterating an artificially truncated chain.
K = 35
p = [p0, p0 * (ex - 1)]
for k in range(1, K):
    income = (p[0]+p[1])*lam**k / D(factorial(k))
    for j in range(2, k+1):
        income += p[j]*lam**(k-j+1)/D(factorial(k-j+1))
    p.append(ex*p[k] - income)

assert all(v > 0 for v in p)
for k in range(K):
    incoming = (p[0]+p[1])*lam**k/D(factorial(k))
    for j in range(2, k+2):
        incoming += p[j]*lam**(k-j+1)/D(factorial(k-j+1))
    assert abs(p[k] - (-lam).exp()*incoming) < D('1e-65')

# G = 1 - sum_{j>=1} P(X>=j)^2 when E[X]=1.
survival = D(1)
sum_survival_sq = D(0)
for j in range(1, K+1):
    survival -= p[j-1]
    sum_survival_sq += survival**2
upper_G = D(1) - sum_survival_sq
assert D(2)*(-lam).exp() > 1
P2 = p0 / (D(2)*(-lam).exp()-1)
# Markov: P(X>=j) <= E[2^X] * 2^{-j}.
# Summing squared bounds for j>=K+1:
tail_bound = P2*P2 / (D(3)*D(4)**K)
lower_G = upper_G - tail_bound
assert D('0.57992883311') < lower_G <= upper_G < D('0.57992883312')
assert upper_G < D(2)/3
assert lam**2 > D(1)/3  # exact Gini ordering also follows directly

# Cross-check two PGF evaluations, including the queue's normalization.
for z in (D('0.25'), D('0.75')):
    exact = p0*(1-z)/(1-z*(lam*(1-z)).exp())
    truncated = sum(pk*z**k for k,pk in enumerate(p))
    assert abs(exact-truncated) < D('1e-18')

print('lambda:', lam)
print('poverty:', p0)
print('variance:', variance)
print('Gini lower bound:', lower_G)
print('Gini upper bound:', upper_G)
print('Gini tail uncertainty:', tail_bound)
print('checks: PASS')
