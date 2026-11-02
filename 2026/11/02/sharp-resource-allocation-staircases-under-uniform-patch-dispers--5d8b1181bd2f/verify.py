"""Exact and numerical checks for complete-mixing patch-budget allocation."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
import numpy as np
import sympy as sp


def solution(efficiency, theta, budget=1.0):
    c = np.asarray(efficiency, dtype=float)
    n = len(c)
    assert n >= 2 and np.all(c > 0) and np.all(c[:-1] >= c[1:])
    assert 0 <= theta <= 1 and budget > 0
    d = np.zeros(n)
    if theta < (n-1)/n-1e-12:
        d[0] = budget
        return d
    if abs(theta - (n-1)/n) <= 1e-12:
        d[0] = budget
        return d
    delta = n-(n-1)/theta
    u = np.sqrt(c)
    for m in range(1,n+1):
        z = (m-delta)/np.sum(1/u[:m])
        if (m == n or z >= u[m] - 1e-12) and u[m-1] >= z -1e-12:
            vals = 1/u[:m] - z/(u[:m]**2)
            d[:m] = budget*vals/vals.sum()
            return d
    raise RuntimeError('no active-set certificate')


def rho(efficiency, theta, budget):
    n = len(efficiency)
    P = np.full((n,n), theta/(n-1), dtype=float)
    np.fill_diagonal(P,1-theta)
    x = np.asarray(efficiency)*np.asarray(budget)
    S = np.sqrt(x)[:,None]*P*np.sqrt(x)[None,:]
    return np.linalg.eigvalsh(S)[-1]


# Exact threshold inequalities: c=(16,9,4,1), theta=1.
u = [Q(4),Q(3),Q(2),Q(1)]
delta = Q(1)
z = (3-delta)/sum(1/t for t in u[:3])
q = [1/t-z/t**2 for t in u[:3]]
assert z == Q(24,13)
assert [v/sum(q) for v in q] == [Q(21,47),Q(20,47),Q(6,47)]
assert 1-u[1]/u[0] == Q(1,4)
assert sum(1-u[2]/t for t in u[:2]) == Q(5,6)
assert sum(1-u[3]/t for t in u[:3]) == Q(23,12)
assert Q(3)/(4-Q(1,4)) == Q(4,5)
assert Q(3)/(4-Q(5,6)) == Q(18,19)
P=sp.ones(4,4)/3-sp.eye(4)/3
D=sp.diag(Q(16)*Q(21,47),Q(9)*Q(20,47),Q(4)*Q(6,47),Q(1)*0)
assert (P*D).charpoly().as_expr().subs(sp.Symbol('lambda'),sp.Rational(96,47)) == 0
assert max(complex(z0).real for z0 in (P*D).eigenvals().keys()) == 96/47

# Parametric active set and strict improvement relative to perturbations.
rng = np.random.default_rng(20261026)
num=0
for n in range(2,9):
    for t in [0,0.01,0.2,(n-1)/n,((n-1)/n+1)/2,0.99,1]:
        for _ in range(15):
            c=np.sort(np.exp(rng.uniform(-2,2,n)))[::-1]
            b=solution(c,t)
            val=rho(c,t,b)
            assert abs(b.sum()-1) < 1e-10 and b.min()>=-1e-12
            for _ in range(25):
                trial=rng.dirichlet(np.ones(n))
                assert rho(c,t,trial) <= val+1e-8, (n,t,c,b,trial)
                num+=1
print('PASS: exact thresholds, exact 4-patch eigenvalue,',num,'random competitor comparisons')
