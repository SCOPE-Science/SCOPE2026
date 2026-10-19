"""Standalone numerical and exact-algebra checks for the Bayesian resource theorem.

The infinite-time assertions are proved analytically in RESULT.md.
Run: python verify.py
"""
from fractions import Fraction
from itertools import product
from math import isclose

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ndtr

STRATS = ('LL', 'LH', 'HL', 'HH')  # first action: replete; second: depleted
R, S, T, P = Fraction(1), Fraction(0), Fraction(3), Fraction(2)
assert T > R and P > S

def low_probability(strategy, prob_r):
    return prob_r * (strategy[0] == 'L') + (1 - prob_r) * (strategy[1] == 'L')

def payoff(i, j, prob_r):
    q = low_probability(j, prob_r)
    r = q * (R if i[0] == 'L' else T) + (1 - q) * (S if i[0] == 'L' else P)
    d = q * (T if i[1] == 'L' else R) + (1 - q) * (P if i[1] == 'L' else S)
    return prob_r * r + (1 - prob_r) * d

checks = 0
for prob_r in [Fraction(i, 29) for i in range(1, 29)]:
    for opponent in STRATS:
        d = (T - R) * low_probability(opponent, prob_r) + (P - S) * (1 - low_probability(opponent, prob_r))
        for other, factor in [('LL', prob_r), ('LH', Fraction(1)), ('HH', 1 - prob_r)]:
            assert payoff('HL', opponent, prob_r) - payoff(other, opponent, prob_r) == factor * d
            assert factor * d > 0
            checks += 1

sigma = 0.24
nc = 0.42

def omega(n):
    z = ndtr((nc - n) / sigma) - ndtr(-n / sigma)
    den = ndtr((1 - n) / sigma) - ndtr(-n / sigma)
    return z / den

def omega_prime(n):
    # Differentiating the Gaussian conditional expectation.
    dz = (np.exp(-n * n / (2 * sigma * sigma)) -
          np.exp(-(nc - n) ** 2 / (2 * sigma * sigma))) / (sigma * np.sqrt(2 * np.pi))
    dd = (np.exp(-n * n / (2 * sigma * sigma)) -
          np.exp(-(1 - n) ** 2 / (2 * sigma * sigma))) / (sigma * np.sqrt(2 * np.pi))
    # Derivatives of differences of Gaussian CDFs.
    z = ndtr((nc - n) / sigma) - ndtr(-n / sigma)
    den = ndtr((1 - n) / sigma) - ndtr(-n / sigma)
    return (dz * den - z * dd) / (den * den)

for n in np.linspace(0, 1, 51):
    assert omega_prime(float(n)) < 0
    h = 2e-6
    assert isclose(omega_prime(float(n)), (omega(n+h)-omega(n-h))/(2*h), rel_tol=3e-6, abs_tol=3e-7)

# At the extinction critical point, all-low resource feedback has a double zero.
theta = 1/omega(0.0) - 1
epsilon = 1.4
a = epsilon * (1 + theta) * (-omega_prime(0.0))
assert a > 0

def coupled_rhs(t, vec):
    z, n = np.asarray(vec[:4]), vec[4]
    p = 1 - omega(n)
    # For R=1,S=0,T=3,P=2, all fitnesses share the same
    # opponent-low component; only the displayed differences matter.
    fit = np.array([2*(1-p), 0.0, 2.0, 2*p])
    dz = z * (fit - z.dot(fit))
    x = z[0] + z[1]
    y = z[0] + z[2]
    q = p*x + (1-p)*y
    return np.r_[dz, epsilon*n*(1-n)*(-1 + (1+theta)*q)]

initial = np.array([0.13, 0.24, 0.42, 0.21, 0.4])
sol = solve_ivp(coupled_rhs, (0, 30000), initial,
                method='LSODA', rtol=2e-10, atol=2e-13,
                t_eval=[3000, 10000, 30000])
assert sol.success, sol.message
assert sol.y[2,-1] > 1 - 1e-9
for t, n in zip(sol.t, sol.y[4,:]):
    assert abs(t*n*a-1) < 0.12, (t,n,a)

print(f'PASS: {checks} exact payoff-advantage identities; 51 monotonic Gaussian derivative checks')
print('PASS: critical resource asymptotic at times', list(sol.t),
      'ratios', [float(t*n*a) for t,n in zip(sol.t, sol.y[4,:])])
