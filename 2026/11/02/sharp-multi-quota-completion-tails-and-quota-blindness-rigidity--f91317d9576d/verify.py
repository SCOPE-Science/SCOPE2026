"""Exact checks for multicolour reinforced-urn completion identities.
Run with Python 3 standard library: python verify.py
"""
from fractions import Fraction as Q
from math import comb, gamma
from itertools import product

def compositions(t, d):
    if d == 1:
        yield (t,)
    else:
        for x in range(t + 1):
            for sub in compositions(t - x, d - 1):
                yield (x,) + sub

def rising(a, k):
    ans = Q(1)
    for j in range(k):
        ans *= a + j
    return ans

def dm_prob(a, v):
    t = sum(v)
    ans = Q(1)
    for ai, xi in zip(a, v):
        ans *= rising(ai, xi)
        for j in range(1, xi + 1):
            ans /= j
    for j in range(1, t + 1):
        ans *= Q(j) / (sum(a) + j - 1)
    return ans

def direct(a, quota, t):
    assert len(a) == len(quota)
    d = len(a)
    F = sum((dm_prob(a, v) for v in compositions(t, d)
             if all(x >= r for x, r in zip(v, quota))), Q(0))
    marked = [Q(0) for _ in a]
    if t > 0:
        for v in compositions(t - 1, d):
            for i in range(d):
                if v[i] == quota[i] - 1 and all(v[j] >= quota[j] for j in range(d) if j != i):
                    marked[i] += dm_prob(a, v) * (a[i] + v[i]) / (sum(a) + t - 1)
    return F, marked

def cdf_unit(d, R, t):
    return Q(0) if t < R else Q(comb(t - R + d - 1, d - 1), comb(t + d - 1, d - 1))

checks = 0
for d in (2, 3, 4):
    for quota in product((1, 2, 3), repeat=d):
        R = sum(quota)
        a = tuple(Q(1) for _ in range(d))
        for t in range(R - 1, R + 7):
            F, marked = direct(a, quota, t)
            assert F == cdf_unit(d, R, t), ('cdf', d, quota, t, F)
            checks += 1
            prev = cdf_unit(d, R, t-1)
            for i in range(d):
                assert marked[i] == Q(quota[i], R) * (F - prev), ('terminal', d, quota, t, i)
                checks += 1
            assert sum(marked) == F - prev
            checks += 1

# Arbitrary unequal rational urns: last-arrival equation and CDF telescoping.
for a in ((Q(2),Q(3)),(Q(1),Q(3),Q(2)),(Q(1,2),Q(3,2),Q(5,2)),
          (Q(3,2),Q(7,4),Q(2,3),Q(1,3))):
    d = len(a)
    for quota in product((1, 2), repeat=d):
        R = sum(quota)
        for t in range(R, R + 6):
            F, marked = direct(a, quota, t)
            prev, _ = direct(a, quota, t-1)
            assert sum(marked) == F - prev
            checks += 1

# Equality of minimum-completion probabilities isolates symmetry of the masses.
for a in (Q(1),Q(1,2),Q(2),Q(4)):
    for d in (2, 3, 5):
        masses = tuple(a for _ in range(d))
        first = (3,) + (1,) * (d - 1)
        second = (2, 2) + (1,) * (d - 2)
        f1 = direct(masses, first, d+2)[0]
        f2 = direct(masses, second, d+2)[0]
        assert f1 / f2 == Q(2)*(a+2)/(Q(3)*(a+1))
        checks += 1

# Explicit power-law constant: compare computed beta-binomial missing counts to gamma limit.
for a, quota in [((Q(1),Q(2),Q(3)),(2,1,2)),((Q(2),Q(2),Q(4)),(1,3,2)),
                 ((Q(1,2),Q(3,2),Q(5,2)),(2,1,2))]:
    for i in range(len(a)):
        ai = float(a[i]); A = float(sum(a));
        ci = gamma(A)/gamma(A-ai)*sum(float(rising(a[i],k))/__import__('math').factorial(k)
                                             for k in range(quota[i]))
        for t in (1000, 3000):
            # beta-binomial marginal via exact rational, relatively expensive but small quotas
            p=Q(0)
            for k in range(quota[i]):
                p += Q(comb(t,k))*rising(a[i],k)*rising(sum(a)-a[i],t-k)/rising(sum(a),t)
            observed = float(p) * t**ai
            assert abs(observed/ci-1) < 0.035, (a,quota,i,t,observed,ci)
            checks += 1
# Independent path-propagation check: do not use Dirichlet-multinomial in this recursion.
for a in ((Q(1), Q(1)), (Q(1), Q(1), Q(1)), (Q(2), Q(1)),
          (Q(1, 2), Q(3, 2), Q(2))):
    d = len(a)
    for quota in product((1, 2), repeat=d):
        state = {(0,)*d: Q(1)}
        for t in range(1, sum(quota) + 5):
            newstate = {}
            marked = [Q(0) for _ in range(d)]
            for v, mass in state.items():
                for i in range(d):
                    nxt = tuple(v[j]+(j==i) for j in range(d))
                    p = mass * (a[i]+v[i]) / (sum(a)+t-1)
                    newstate[nxt] = newstate.get(nxt,Q(0))+p
                    if all(nxt[j]>=quota[j] for j in range(d)) and not all(v[j]>=quota[j] for j in range(d)):
                        marked[i] += p
            state = newstate
            F = sum((mass for v, mass in state.items() if all(v[i]>=quota[i] for i in range(d))),Q(0))
            dF, dMarked = direct(a, quota, t)
            assert F==dF and marked==dMarked, (a,quota,t)
            checks += d+1

print('PASS', checks, 'exact rational comparisons and asymptotic-constant spot checks')
