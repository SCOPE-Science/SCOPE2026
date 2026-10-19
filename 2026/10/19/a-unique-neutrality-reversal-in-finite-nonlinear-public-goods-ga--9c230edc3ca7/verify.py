"""Reproducible independent checks for finite public-goods fixation reversal.

Uses only the Python 3 standard library. All finite payoff comparisons are
exact rational calculations; numerical roots illustrate, but do not prove,
the all-parameter or asymptotic theorems.
"""
from fractions import Fraction as F
from math import comb, exp, isclose

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1


def exact_payoff_gap(N, n, X, r1, rn, cost=1):
    r1, rn, cost = F(r1), F(rn), F(cost)
    def r(k):
        return r1 + F(k - 1, n - 1) * (rn - r1)
    value = F(0)
    for k in range(n):
        if 0 <= k <= X - 1 and 0 <= n - 1 - k <= N - X:
            pc = F(comb(X - 1, k) * comb(N - X, n - 1 - k), comb(N - 1, n - 1))
            value += pc * cost * (F(k + 1, n) * r(k + 1) - 1)
        if 0 <= k <= X and 0 <= n - 1 - k <= N - X - 1:
            pd = F(comb(X, k) * comb(N - X - 1, n - 1 - k), comb(N - 1, n - 1))
            if k:
                value -= pd * cost * F(k, n) * r(k)
    return value


def closed_payoff_gap(N, n, X, r1, rn, cost=1):
    K = F(n * (N - 1), N - n)
    return F(cost) * (F(r1) / K - 1 + F(2 * (X - 1), N - 2) * F(rn - r1) / K)


def prefixes(N, n, r1, rn, cost=1):
    result = [F(0)]
    for X in range(1, N):
        result.append(result[-1] + closed_payoff_gap(N, n, X, r1, rn, cost))
    return result


def rho(prefix, w):
    return 1 / sum(exp(-w * float(a)) for a in prefix)


def bisect(func, lo, hi, iterations=100):
    assert func(lo) * func(hi) < 0
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if func(mid) * func(lo) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# Independently evaluate the hypergeometric payoffs in each state.
for N in range(4, 12):
    for n in range(3, N):
        for r1, rn in ((1, 3), (4, 7), (9, 4), (11, 5), (2, 2)):
            for X in range(1, N):
                check(exact_payoff_gap(N, n, X, r1, rn) == closed_payoff_gap(N, n, X, r1, rn))
            P = prefixes(N, n, r1, rn)
            K = F(n * (N - 1), N - n)
            check(P[-1] == F(N - 1) * (F(rn) / K - 1))
            check(sum(P) == F(N * (N - 1), 2) * ((F(r1 + 2 * rn) / (3 * K)) - 1))

# An independently solved one-step fixation recurrence for Fermi imitation:
# boundary rho_0=0, rho_N=1; forward increments are proportional to
# exp(-w*prefix). Compare against the closed expression.
for r1, rn in ((4, 7), (9, 4), (6, 6)):
    N, n, w = 6, 3, .75
    P = prefixes(N, n, r1, rn)
    closed = rho(P, w)
    # Recurrence: h_(X+1)-h_X=e^(-w delta_X) (h_X-h_(X-1)).
    increments = [exp(-w * float(z)) for z in P]
    h = [0.0]
    for z in increments:
        h.append(h[-1] + z / sum(increments))
    check(isclose(h[1], closed, rel_tol=1e-13))
    check(isclose(h[-1], 1., rel_tol=1e-13))
    for X in range(1, N):
        factor = exp(-w * float(closed_payoff_gap(N, n, X, r1, rn)))
        check(isclose(h[X + 1] - h[X], factor * (h[X] - h[X - 1]), rel_tol=1e-12))

# Two explicit strict reversal examples with unique roots.
for r1, rn, target in ((4, 7, 5.592288595787397), (9, 4, 1.1554760747212847)):
    N, n = 6, 3
    P = prefixes(N, n, r1, rn)
    check(sum(P) > 0)
    check(min(P) < 0)
    f = lambda w: sum(exp(-w * float(p)) for p in P) - N
    root = bisect(f, 1e-7, 15.)
    check(isclose(root, target, abs_tol=1e-10))
    check(rho(P, root / 2) > F(1, N))
    check(rho(P, root * 2) < F(1, N))
    print('example:', r1, rn, 'crossing:', format(root, '.12f'),
          'rho at half / twice crossover:', round(rho(P, root / 2), 12),
          round(rho(P, root * 2), 12))

# The convergence-to-integral scaling is checked at several finite N;
# this is a numerical illustration only (proof uses uniform Riemann sums).
def midpoint_integral(tau, n, r1, rn, cost=1, steps=20000):
    s = 0.
    for j in range(steps):
        t = (j + .5) / steps
        G = cost * (t * (r1 / n - 1) + t * t * (rn - r1) / n)
        s += exp(-tau * G)
    return s / steps

for r1, rn in ((2, 5), (10, 2)):
    n = 3
    tau = bisect(lambda t: midpoint_integral(t, n, r1, rn) - 1., .0001, 100.)
    target = midpoint_integral(tau, n, r1, rn)
    check(abs(target - 1.) < 1e-10)
    for N in (1000, 5000):
        P = prefixes(N, n, r1, rn)
        finite = sum(exp(-tau * float(z) / N) for z in P) / N
        check(abs(finite - 1.) < .075)
    print('limiting example:', r1, rn, 'scaled crossing:', format(tau, '.10f'))

print('PASS:', checks, 'assertions; exact payoff comparisons and illustrative numerical roots')
