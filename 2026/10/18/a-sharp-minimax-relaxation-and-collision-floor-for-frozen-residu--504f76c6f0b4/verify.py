"""Reproduce exact multinomial moments and sharp finite-batch minimax formulas.

Requires only Python 3's standard library. Run: python verify.py
"""
from fractions import Fraction as F
from math import factorial
from itertools import product
from random import Random


def compositions(n, d):
    if d == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for rest in compositions(n - j, d - 1):
                yield (j,) + rest


def direct_moment(p, k, beta):
    d = len(p)
    result = F(0)
    for counts in compositions(k, d):
        probability = F(factorial(k), 1)
        for j in range(d):
            probability *= p[j] ** counts[j] / factorial(counts[j])
        ratio = sum(p[j] * (1 - beta * counts[j]) ** 2 for j in range(d))
        result += probability * ratio
    return result


def closed_moment(p, k, beta):
    s2 = sum(t*t for t in p)
    s3 = sum(t*t*t for t in p)
    return 1 - k*(2*beta-beta*beta)*s2 + k*(k-1)*beta*beta*s3


def endpoint_worst(d, k, beta):
    flat = 1 - F(2*k, d)*beta + F(k*(d+k-1), d*d)*beta*beta
    one = (1-k*beta)**2
    return max(flat, one)


def optimum(d, k):
    if k*(d-1) <= 2*d-1:
        return F(d, d+k-1), F(d-1, d+k-1), 'flat'
    return F(2*d, k*(d+1)-1), F((k*(d-1)+1)**2, (k*(d+1)-1)**2), 'balance'


checks = 0
# Independent multinomial enumeration on rational probability vectors.
for d in range(2, 5):
    for k in range(1, 8):
        for c in compositions(5, d):
            p = [F(t, 5) for t in c]
            for beta in [F(1, 5*k), F(3, 4*k), F(6, 5*k)]:
                lhs = direct_moment(p, k, beta)
                rhs = closed_moment(p, k, beta)
                assert lhs == rhs, (d, k, p, beta, lhs, rhs)
                assert lhs <= endpoint_worst(d, k, beta), (d, k, p, beta)
                checks += 2

# Exact lower witnesses, phase comparisons, and global scalar minimizers.
for d in range(2, 17):
    for k in range(1, 41):
        beta, value, phase = optimum(d, k)
        flat = [F(1, d)] * d
        one = [F(1)] + [F(0)] * (d-1)
        assert endpoint_worst(d, k, beta) == value
        assert max(closed_moment(flat, k, beta), closed_moment(one, k, beta)) == value
        # The maximum of two convex quadratics has its unique minimum here.
        for shift in [F(1, 100000*k), F(1, 1000*k), F(1, 10*k)]:
            for other in [beta-shift, beta+shift]:
                if other > 0:
                    assert endpoint_worst(d, k, other) > value, (d,k,beta,other)
                    checks += 1
        assert (phase == 'flat') == (k*(d-1) <= 2*d-1)
        checks += 3

# Dense simplex meshes provide redundant checks beyond the rational examples.
for d in range(2, 6):
    for k in [1, 2, 3, 4, 8, 13]:
        for t in range(1, 22):
            beta = F(t, 10*k)
            bound = endpoint_worst(d, k, beta)
            for c in compositions(8, d):
                p = [F(v, 8) for v in c]
                assert closed_moment(p, k, beta) <= bound
                checks += 1

# Actual Monte Carlo uses a separate binomial/multinomial sampling procedure.
rng = Random(721927)
d = 3
k = 6
beta, _, _ = optimum(d, k)
p = [0.61, 0.25, 0.14]
trials = 120000
s = 0.0
for _ in range(trials):
    counts = [0] * d
    for _ in range(k):
        u = rng.random()
        i = 0 if u < p[0] else 1 if u < p[0] + p[1] else 2
        counts[i] += 1
    s += sum(p[j]*(1-float(beta)*counts[j])**2 for j in range(d))
empirical = s / trials
target = float(closed_moment([F(61,100),F(25,100),F(14,100)], k, beta))
assert abs(empirical-target) < 0.012, (empirical, target)
checks += 1

# The limit differs from optimally relaxed uniform batch sampling.
for d in range(2, 13):
    for k in [50, 100, 1000]:
        b, r, _ = optimum(d, k)
        assert abs(float(r)-((d-1)/(d+1))**2) < 2.5/k
        assert F(d-1, d+k-1) < r if k > (2*d-1)/(d-1) else True
        checks += 2

print('ALL_CHECKS_PASSED', checks)
print('MONTE_CARLO', round(empirical,9), 'EXACT', round(target,9))
for d,k in [(2,2),(2,3),(2,4),(3,3),(4,8),(10,100)]:
    b,r,case=optimum(d,k)
    print('d=',d,'k=',k,'beta=',str(b),'worst=',str(r),'branch=',case)
