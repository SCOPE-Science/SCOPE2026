"""Exact finite-case checks for generation-wise thinning rearrangement.

The accompanying mathematical proof establishes the infinite-family theorem;
these tests check independent bounded examples and the exact moment identity.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import comb

CHECKS = 0


def check(statement, description):
    global CHECKS
    CHECKS += 1
    if not statement:
        raise AssertionError(description)


def convolution(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return out


def offspring_law(base, p):
    d = [Q(0)] * len(base)
    for k, mass in enumerate(base):
        for j in range(k + 1):
            d[j] += mass * comb(k, j) * p**j * (1-p)**(k-j)
    check(sum(d) == 1, 'offspring law normalization')
    return d


def output_law(base, parameters):
    cur = [Q(0), Q(1)]  # one initial infection
    for p in parameters:
        offspring = offspring_law(base, p)
        powers = [[Q(1)]]
        for _ in range(len(cur) - 1):
            powers.append(convolution(powers[-1], offspring))
        nxt = [Q(0)] * len(powers[-1])
        for z, w in enumerate(cur):
            for j, x in enumerate(powers[z]):
                nxt[j] += w * x
        cur = nxt
        check(sum(cur) == 1, 'population law normalization')
    return cur


def expectation(a):
    return sum(i*x for i, x in enumerate(a))


def variance(a):
    m = expectation(a)
    return sum((i-m)**2*x for i, x in enumerate(a))


def stop_loss(a, threshold):
    return sum(max(i-threshold, 0)*x for i, x in enumerate(a))


def dominates_convex(a, b, label):
    check(expectation(a) == expectation(b), label+' equal means')
    for t in range(max(len(a), len(b))):
        check(stop_loss(a, t) >= stop_loss(b, t), label+' stop loss '+str(t))


BASES = [
    [Q(0), Q(1)],
    [Q(0), Q(0), Q(1)],
    [Q(0), Q(0), Q(0), Q(1)],
    [Q(1,2), Q(0), Q(1,2)],
    [Q(0), Q(2,3), Q(0), Q(1,3)],
    [Q(1,3), Q(1,3), Q(1,3)],
]
PARAMS = [Q(1,4), Q(1,2), Q(3,4)]
for base in BASES:
    mean_k = sum(k*x for k, x in enumerate(base))
    factorial2 = sum(k*(k-1)*x for k, x in enumerate(base))
    laws = {v: output_law(base, v) for v in permutations(PARAMS)}
    high = laws[tuple(sorted(PARAMS))]
    low = laws[tuple(sorted(PARAMS, reverse=True))]
    for order, law in laws.items():
        dominates_convex(high, law, 'ascending over '+str(order))
        dominates_convex(law, low, 'descending under '+str(order))
        check(expectation(law) == mean_k**3 * Q(3,32), 'third generation mean product')
    for p, q in [(Q(1,4), Q(1,2)), (Q(1,4), Q(3,4)), (Q(1,2), Q(3,4))]:
        a = output_law(base, (p,q))
        b = output_law(base, (q,p))
        dominates_convex(a, b, 'two-level swap')
        check(variance(a)-variance(b) == mean_k*p*q*(q-p)*factorial2,
              'exact two-level variance commutator')
        if factorial2 > 0:
            check(a[0] > b[0], 'strict terminal extinction')
            check(variance(a) > variance(b), 'strict variance gap')
        else:
            check(a == b, 'nonbranching commutativity')

base = [Q(0), Q(0), Q(1)]
p, q = Q(1,4), Q(3,4)
a, b = output_law(base, (p,q)), output_law(base, (q,p))
check(a[0] == Q(2401,4096), 'exact front-loaded zero probability')
check(b[0] == Q(1849,4096), 'exact back-loaded zero probability')
check(variance(a)-variance(b) == Q(3,8), 'exact variance gap')
check(expectation(a) == Q(3,4), 'exact terminal mean')
print('PASS: %d exact-rational assertions'%CHECKS)
print('Binary potential contacts, two levels: mean=3/4, early-low extinction=2401/4096, late-low extinction=1849/4096, variance difference=3/8.')
